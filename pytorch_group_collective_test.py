import torch
import argparse
import time
import torch.distributed as dist
from nccl_backend import NCCLCommunicator


def data_size_mb2dim(mb:int):
    return mb // 4 * 1024 * 1024


def collect_run_time(args, local_run_time: float):
    run_time = torch.zeros(1, dtype=torch.float32, device='cpu')
    run_time[0] = local_run_time
    if args.rank == 0:
        run_times = [torch.zeros(1, dtype=torch.float32, device='cpu') for _ in range(args.world_size)]
    else:
        run_times = None
    dist.gather(run_time, run_times, dst=0)
    if args.rank == 0:
        return torch.max(torch.cat(run_times)).item()
    else:
        return None


def test_paradigm_allreduce(args, device, communicator: NCCLCommunicator):
    print("<==== Test AllReduce ====>")
    dim = data_size_mb2dim(args.dim_mb) // args.world_size
    tensors = []
    for _ in range(args.world_size):
        tensors.append(torch.arange(dim, dtype=torch.float32, device=device))

    dist.barrier()
    start_time = time.time()
    for i in range(args.world_size):
        communicator.all_reduce(tensors[i])
    torch.cuda.synchronize()
    dist.barrier()
    end_time = time.time()

    total_time = end_time - start_time
    print(args.iter, '-allReduce of tensor <', args.dim_mb, "> MB takes ", total_time, "seconds.")
    return total_time


def test_paradigm_central_ps(args, device, communicator: NCCLCommunicator):
    print("<==== Test Central PS ====>")
    dim = data_size_mb2dim(args.dim_mb) // args.world_size
    tensors = []
    for _ in range(args.world_size):
        tensors.append(torch.arange(dim, dtype=torch.float32, device=device))

    dist.barrier()
    start_time = time.time()
    for i in range(args.world_size):
        communicator.reduce(tensors[i], dst=0)
    for i in range(args.world_size):
        communicator.broadcast(tensors[i], src=0)
    torch.cuda.synchronize()
    dist.barrier()
    end_time = time.time()
    total_time = end_time - start_time
    print(args.iter, '-central PS of tensor <', args.dim_mb, "> MB takes ", total_time, "seconds.")
    return total_time


def test_paradigm_sharded_ps(args, device, communicator: NCCLCommunicator):
    print("<==== Test Sharded PS ====>")
    dim = data_size_mb2dim(args.dim_mb) // args.world_size
    input_tensors = []
    output_tensors = []
    for _ in range(args.world_size):
        input_tensors.append(torch.arange(dim, dtype=torch.float32, device=device))
        output_tensors.append(torch.zeros(dim, dtype=torch.float32, device=device))
    dist.barrier()
    start_time = time.time()
    communicator.all_to_all(input_tensors, output_tensors)
    for i in range(1, args.world_size):
        output_tensors[0].add_(output_tensors[i])
    communicator.all_gather(output_tensors[0], input_tensors)
    torch.cuda.synchronize()
    dist.barrier()
    end_time = time.time()

    total_time = end_time - start_time
    print(args.iter, '-sharded PS of tensor <', args.dim_mb, "> MB takes ", total_time, "seconds.")
    return total_time


def main():
    parser = argparse.ArgumentParser(description='Test PyTorch Distributed')
    parser.add_argument('--dist-backend', type=str, default='gloo', metavar='S',
                        help='PyTorch backend type')
    parser.add_argument('--dist-url', type=str, default='tcp://127.0.0.1:9000', metavar='S',
                        help='master ip for distributed PyTorch')
    parser.add_argument('--world-size', type=int, default=4, metavar='D',
                        help='world size (default: 2)')
    parser.add_argument('--rank', type=int, default=0, metavar='R',
                        help='rank for distributed PyTorch')
    parser.add_argument('--dim-mb', type=int, default=1024, metavar='R',
                        help='size of the tensor to be synced. (in MB)')
    parser.add_argument('--use-cuda', default=True, type=lambda x: (str(x).lower() == 'true'),
                        help='if this is set to True, will use cuda to train')
    parser.add_argument('--cuda-id', type=int, default=0, metavar='N',
                        help='cuda index, if the instance has multiple GPUs.')
    parser.add_argument('--iter', type=int, default=16, metavar='R',
                        help='number of iterations for benchmark.')
    args = parser.parse_args()

    assert (torch.cuda.is_available())
    device = torch.device('cuda', args.cuda_id)

    communicator = NCCLCommunicator(rank=args.rank, intra_gpu_rank=args.cuda_id,
                                    world_size=args.world_size, master_ip=args.dist_url)

    assert args.iter % args.world_size == 0
    # warm up run.
    print("Warm up run, does not count in timing")
    test_paradigm_allreduce(args, device, communicator)
    test_paradigm_central_ps(args, device, communicator)
    test_paradigm_sharded_ps(args, device, communicator)

    allreduce_time = 0
    central_ps_time = 0
    sharded_ps_time = 0

    n = 5
    for i in range(n):
        allreduce_time += test_paradigm_allreduce(args, device, communicator)
        central_ps_time += test_paradigm_central_ps(args, device, communicator)
        sharded_ps_time += test_paradigm_sharded_ps(args, device, communicator)

    allreduce_time = allreduce_time / n
    central_ps_time = central_ps_time / n
    sharded_ps_time = sharded_ps_time / n

    print("<=====Averaged local AllReduce time: ", allreduce_time, "s.=====>")
    print("<=====Averaged local Central PS time: ", central_ps_time, "s.=====>")
    print("<=====Averaged local Sharded PS time: ", sharded_ps_time, "s.=====>")

    max_allreduce_time = collect_run_time(args, allreduce_time)
    max_central_ps_time = collect_run_time(args, central_ps_time)
    max_shard_ps_time = collect_run_time(args, sharded_ps_time)

    if args.rank == 0:
        print("Backend: ", args.dist_backend)
        print("<=====Averaged global AllReduce time: ", max_allreduce_time, "s.=====>")
        print("<=====Averaged global Central PS time: ", max_central_ps_time, "s.=====>")
        print("<=====Averaged global Sharded PS time: ", max_shard_ps_time, "s.=====>")


if __name__ == '__main__':
    main()
