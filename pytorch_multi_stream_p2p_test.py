import random
import torch
import argparse
import time
from nccl_backend import *


def test_multi_stream_send_recv(args, device, communicator:NCCLCommunicator):
    torch_odd_stream = torch.cuda.Stream(device=device, priority=-1)
    torch_even_stream = torch.cuda.Stream(device=device, priority=-1)
    if args.rank == 0:
        start_send_events = [torch.cuda.Event(blocking=False) for _ in range(args.iter)]
        for i in range(args.iter):
            send_tensor = torch.full((args.dim,), i, dtype=torch.int, device=device)
            if i % 2 == 0:
                with torch.cuda.stream(torch_even_stream):
                    cupy_even_stream = cupy.cuda.ExternalStream(torch_even_stream.cuda_stream)
                    torch_even_stream.wait_event(start_send_events[i])
                    communicator.send(send_tensor, dst=1, stream=cupy_even_stream)
            else:
                with torch.cuda.stream(torch_odd_stream):
                    cupy_odd_stream = cupy.cuda.ExternalStream(torch_odd_stream.cuda_stream)
                    torch_odd_stream.wait_event(start_send_events[i])
                    communicator.send(send_tensor, dst=1, stream=cupy_odd_stream)
        for i in range(args.iter//2):
            rand_val = random.randint(0, 1)
            if rand_val == 0:
                torch_even_stream.record_event(start_send_events[i*2])
                print("Record event: {}".format(i * 2))
                torch_odd_stream.record_event(start_send_events[i*2 + 1])
                print("Record event: {}".format(i * 2 + 1))
            else:
                torch_odd_stream.record_event(start_send_events[i*2 + 1])
                print("Record event: {}".format(i * 2 + 1))
                torch_even_stream.record_event(start_send_events[i*2])
                print("Record event: {}".format(i * 2))
    elif args.rank == 1:
        for i in range(args.iter):
            if i % 2 == 0:
                with torch.cuda.stream(torch_even_stream):
                    recv_tensor = torch.zeros((args.dim,), dtype=torch.int, device=device)
                    cupy_even_stream = cupy.cuda.ExternalStream(torch_even_stream.cuda_stream)
                    communicator.recv(recv_tensor, src=0, stream=cupy_even_stream)
                    print("====In even stream====")
                    print("Iter {} recv tensor: {} ".format(i, recv_tensor))
            else:
                with torch.cuda.stream(torch_odd_stream):
                    recv_tensor = torch.zeros((args.dim,), dtype=torch.int, device=device)
                    cupy_odd_stream = cupy.cuda.ExternalStream(torch_odd_stream.cuda_stream)
                    communicator.recv(recv_tensor, src=0, stream=cupy_odd_stream)
                    print("----In odd stream----")
                    print("Iter {} recv tensor: {} ".format(i, recv_tensor))


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
    parser.add_argument('--dim', type=int, default=32, metavar='R',
                        help='size of the tensor to be sent.') # this is an approximated size of a macro-bench
    parser.add_argument('--use-cuda', default=False, type=lambda x: (str(x).lower() == 'true'),
                        help='if this is set to True, will use cuda to train')
    parser.add_argument('--cuda-id', type=int, default=0, metavar='N',
                        help='cuda index, if the instance has multiple GPUs.')
    parser.add_argument('--iter', type=int, default=10, metavar='R',
                        help='number of iterations for benchmark.')
    args = parser.parse_args()

    assert (args.use_cuda and torch.cuda.is_available())
    device = torch.device('cuda', args.cuda_id)

    assert (args.dist_backend == 'cupy_nccl')
    communicator = NCCLCommunicator(rank=args.rank, intra_gpu_rank=args.cuda_id,
                                    world_size=args.world_size, master_ip=args.dist_url)
    test_multi_stream_send_recv(args, device, communicator)


if __name__ == '__main__':
    main()
