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


def test_allreduce(args, device, communicator:NCCLCommunicator):
    print("<==== Test AllReduce ====>")
    dim = data_size_mb2dim(args.dim_mb)
    tensor = torch.arange(dim, dtype=torch.float32, device=device)
    if args.use_cuda:
        torch.cuda.synchronize()

    start_time = time.time()
    communicator.all_reduce(tensor)

    if args.use_cuda:
        torch.cuda.synchronize()
    end_time = time.time()
    total_time = end_time - start_time
    print('AllReduce of tensor <', args.dim_mb, "> MB takes ", total_time, "seconds.")
    return total_time


def test_broadcast(args, device, communicator:NCCLCommunicator):
    print("<==== Test Broadcast ====>")
    dim = data_size_mb2dim(args.dim_mb)
    if args.rank == 0:
        tensor = torch.arange(dim, dtype=torch.float32, device=device)
    else:
        tensor = torch.zeros(dim, dtype=torch.float32, device=device)

    if args.use_cuda:
        torch.cuda.synchronize()

    start_time = time.time()
    communicator.broadcast(tensor, src=0)

    if args.use_cuda:
        torch.cuda.synchronize()
    end_time = time.time()
    total_time = end_time - start_time
    print('Broadcast of tensor <', args.dim_mb, "> MB takes ", total_time, "seconds.")
    return total_time


def test_reduce(args, device, communicator: NCCLCommunicator):
    print("<==== Test Reduce ====>")
    dim = data_size_mb2dim(args.dim_mb)
    if args.rank == 0:
        tensor = torch.zeros(dim, dtype=torch.float32, device=device)
    else:
        tensor = torch.arange(dim, dtype=torch.float32, device=device)

    if args.use_cuda:
        torch.cuda.synchronize()

    start_time = time.time()
    communicator.reduce(tensor, dst=0)

    if args.use_cuda:
        torch.cuda.synchronize()
    end_time = time.time()
    total_time = end_time - start_time
    print('Reduce of tensor <', args.dim_mb, "> MB takes ", total_time, "seconds.")
    return total_time


def main():
    parser = argparse.ArgumentParser(description='Test PyTorch Distributed')
    parser.add_argument('--dist-backend', type=str, default='gloo', metavar='S',
                        help='PyTorch backend type')
    parser.add_argument('--dist-url', type=str, default='tcp://127.0.0.1:9000', metavar='S',
                        help='master ip for distributed PyTorch')
    parser.add_argument('--world-size', type=int, default=2, metavar='D',
                        help='world size (default: 2)')
    parser.add_argument('--rank', type=int, default=0, metavar='R',
                        help='rank for distributed PyTorch')
    parser.add_argument('--dim-mb', type=int, default=128, metavar='R',
                        help='size of the tensor to be sent. (in MB)')
    parser.add_argument('--use-cuda', default=False, type=lambda x: (str(x).lower() == 'true'),
                        help='if this is set to True, will use cuda to train')
    parser.add_argument('--cuda-id', type=int, default=0, metavar='N',
                        help='cuda index, if the instance has multiple GPUs.')
    parser.add_argument('--iter', type=int, default=10, metavar='R',
                        help='number of iterations for benchmark.')
    args = parser.parse_args()

    if args.use_cuda:
        assert (torch.cuda.is_available())
        device = torch.device('cuda', args.cuda_id)
    else:
        device = torch.device('cpu')
    if args.dist_backend == 'cupy_nccl':
        communicator = NCCLCommunicator(rank=args.rank, intra_gpu_rank=args.cuda_id,
                                        world_size=args.world_size, master_ip=args.dist_url)
    else:
        dist.init_process_group(backend=args.dist_backend, init_method=args.dist_url,
                                rank=args.rank, world_size=args.world_size)
        communicator = dist

    allreduce_time = 0
    for i in range(args.iter + 1):
        dist.barrier()
        if i == 0:
            test_allreduce(args, device, communicator)
        else:
            allreduce_time += test_allreduce(args, device, communicator)
        time.sleep(1)
    allreduce_time /= args.iter

    broadcast_time = 0
    for i in range(args.iter + 1):
        dist.barrier()
        if i == 0:
            test_broadcast(args, device, communicator)
        else:
            broadcast_time += test_broadcast(args, device, communicator)
        time.sleep(1)
    broadcast_time /= args.iter

    reduce_time = 0
    for i in range(args.iter + 1):
        dist.barrier()
        if i == 0:
            test_reduce(args, device, communicator)
        else:
            reduce_time += test_reduce(args, device, communicator)
        time.sleep(1)
    reduce_time /= args.iter

    print("<=====Averaged local AllReduce time: ", allreduce_time * 1000, "ms.=====>")
    print("<=====Averaged local Broadcast time: ", broadcast_time * 1000, "ms.=====>")
    print("<=====Averaged local Reduce time: ", reduce_time * 1000, "ms.=====>")

    max_allreduce_time = collect_run_time(args, allreduce_time)
    max_broadcast_time = collect_run_time(args, broadcast_time)
    max_reduce_time = collect_run_time(args, reduce_time)

    if args.rank == 0:
        print("Backend: ", args.dist_backend)
        print("<=====Averaged global AllReduce time: ", max_allreduce_time * 1000, "ms.=====>")
        print("<=====Averaged global Broadcast time: ", max_broadcast_time * 1000, "ms.=====>")
        print("<=====Averaged global Reduce time: ", max_reduce_time * 1000, "ms.=====>")


if __name__ == '__main__':
    main()
