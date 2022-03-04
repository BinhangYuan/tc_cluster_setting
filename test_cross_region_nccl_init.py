import argparse
import cupy
import numpy as np
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

    if args.rank == 0:
        store = dist.TCPStore(args.ip, 1234, 2, True, timedelta(seconds=60))
        comm_id = cupy.cuda.nccl.get_unique_id()
        print(comm_id)
        comm_id_str = np.array(comm_id).tobytes()
        print("Rank 0 generate comm_id:", comm_id_str)
        store.set('comm_id', comm_id_str)
        nccl_comm = cupy.cuda.nccl.NcclCommunicator(2, comm_id, 0)
        print("Initialize NCCL succeed! - Rank 0")
    elif args.rank == 1:
        # comm_id = args.cuda_id
        store = dist.TCPStore(args.ip, 1234, 2, False, timedelta(seconds=60))
        comm_id_str = store.get('comm_id')
        print("Rank 1 get comm_id:", comm_id_str)
        comm_id = tuple(np.frombuffer(comm_id_str, dtype=int))
        nccl_comm = cupy.cuda.nccl.NcclCommunicator(2, comm_id, 1)
        print("Initialize NCCL succeed! - Rank 1")

    tensor = torch.ones(1024, dtype=torch.float32, device='cuda:0')
    nccl_comm.allReduce(tensor.data_ptr(), tensor.data_ptr(), torch.numel(tensor), cupy.cuda.nccl.NCCL_FLOAT32,
                        cupy.cuda.nccl.NCCL_SUM, cupy.cuda.Stream.null.ptr)
    print(tensor)


if __name__ == '__main__':
    main()
