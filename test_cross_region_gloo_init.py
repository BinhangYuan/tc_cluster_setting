import argparse
import torch
import torch.distributed as dist
from datetime import timedelta


def main():
    parser = argparse.ArgumentParser(description='Test Cross region NCCL init')
    parser.add_argument('--ip', type=str, default='127.0.0.1', metavar='S',
                        help='master ip for distributed PyTorch')
    parser.add_argument('--rank', type=int, default=0, metavar='R',
                        help='rank for distributed PyTorch')
    args = parser.parse_args()

    store = dist.TCPStore(args.ip, 1234, 2, args.rank == 0, timedelta(seconds=60))
    print("TCP store initialized.")
    dist.init_process_group(backend='gloo', store=store, rank=args.rank, world_size=2)
    print("Process group initialized.")

    tensor = torch.ones(1024, dtype=torch.float32, device='cpu')
    dist.all_reduce(tensor)
    print(tensor)


if __name__ == '__main__':
    main()
