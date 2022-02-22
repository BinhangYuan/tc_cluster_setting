import argparse
import cupy
import numpy as np
import torch


def main():
    parser = argparse.ArgumentParser(description='Test Cross region NCCL init')
    parser.add_argument('--rank', type=int, default=0, metavar='R',
                        help='rank for distributed PyTorch')
    parser.add_argument('--cuda-id', nargs='+', default=[1], metavar='S',
                        help='Magic cuda-id')
    args = parser.parse_args()

    if args.rank == 0:
        comm_id = cupy.cuda.nccl.get_unique_id()
        print(comm_id)
        # cuda_id_str = np.array(comm_id).tobytes()
        # print(cuda_id_str)
        nccl_comm = cupy.cuda.nccl.NcclCommunicator(2, comm_id, 0)
        print("Initialize NCCL succeed! - Rank 0")
    elif args.rank == 1:
        comm_id = args.cuda_id
        nccl_comm = cupy.cuda.nccl.NcclCommunicator(2, comm_id, 1)
        print("Initialize NCCL succeed! - Rank 1")

    tensor = torch.ones(1024, dtype=torch.float32, device='cuda:0')
    nccl_comm.allReduce(tensor.data_ptr(), tensor.data_ptr(), torch.numel(tensor), cupy.cuda.nccl.NCCL_FLOAT32,
                        cupy.cuda.nccl.NCCL_SUM, cupy.cuda.Stream.null)
    print(tensor)


if __name__ == '__main__':
    main()
