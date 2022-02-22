import torch
import numpy as np
import cupy
import torch.distributed as dist
from typing import List


def _type_torch_to_cupy(torch_type: torch.dtype):
    # print(torch_type)
    mappings = {
        torch.uint8: cupy.cuda.nccl.NCCL_UINT8,
        torch.int32: cupy.cuda.nccl.NCCL_INT32,
        torch.int: cupy.cuda.nccl.NCCL_INT,
        torch.float16: cupy.cuda.nccl.NCCL_FLOAT16,
        torch.float32: cupy.cuda.nccl.NCCL_FLOAT32,
        torch.float64: cupy.cuda.nccl.NCCL_FLOAT64,
        torch.float: cupy.cuda.nccl.NCCL_FLOAT
    }
    return mappings[torch_type]


class NCCLCommunicator:
    def __init__(self,
                 rank: int,
                 intra_gpu_rank: int,
                 world_size: int,
                 master_ip: str):
        self.rank = rank
        self.intra_gpu_rank = intra_gpu_rank
        cupy.cuda.Device(self.intra_gpu_rank).use()
        self.world_size = world_size
        dist.init_process_group(backend='gloo', init_method=master_ip, world_size=world_size, rank=rank)
        self.store = dist.distributed_c10d._get_default_store()

        if self.rank == 0:
            cuda_id = cupy.cuda.nccl.get_unique_id()
            # print(cuda_id)
            cuda_id_str = np.array(cuda_id).tobytes()
            self.store.set('master-unique-id', cuda_id_str)
            # print("Master put key ", cuda_id_str)
        else:
            cuda_id_str = self.store.get('master-unique-id')
            # print("Slave get key", cuda_id_str)
        comm_id = tuple(np.frombuffer(cuda_id_str, dtype=int))
        # comm_id = cupy.cuda.nccl.get_unique_id()
        # print(comm_id)
        self.comm = cupy.cuda.nccl.NcclCommunicator(self.world_size, comm_id, self.rank)

    @staticmethod
    def barrier():
        dist.barrier()

    def send(self,
             tensor: torch.Tensor,
             dst: int,
             stream=cupy.cuda.Stream.null):
        cupy.cuda.nccl.groupStart()
        self.comm.send(
            tensor.data_ptr(),
            torch.numel(tensor),
            _type_torch_to_cupy(tensor.dtype),
            dst,
            stream.ptr
        )
        cupy.cuda.nccl.groupEnd()

    def recv(self,
             tensor: torch.Tensor,
             src: int,
             stream=cupy.cuda.Stream.null):
        cupy.cuda.nccl.groupStart()
        self.comm.recv(
            tensor.data_ptr(),
            torch.numel(tensor),
            _type_torch_to_cupy(tensor.dtype),
            src,
            stream.ptr
        )
        cupy.cuda.nccl.groupEnd()

    def broadcast(self,
                  tensor: torch.Tensor,
                  src: int,
                  stream=cupy.cuda.Stream.null):
        self.comm.bcast(
            tensor.data_ptr(),
            torch.numel(tensor),
            _type_torch_to_cupy(tensor.dtype),
            src,
            stream.ptr
        )

    def reduce(self,
               tensor: torch.Tensor,
               dst: int,
               stream=cupy.cuda.Stream.null,
               op=cupy.cuda.nccl.NCCL_SUM):
        self.comm.reduce(
            tensor.data_ptr(),  # force it to be in-place.
            tensor.data_ptr(),
            torch.numel(tensor),
            _type_torch_to_cupy(tensor.dtype),
            op,
            dst,
            stream.ptr
        )

    def all_reduce(self,
                  tensor: torch.Tensor,
                  stream=cupy.cuda.Stream.null,
                  op=cupy.cuda.nccl.NCCL_SUM):
        self.comm.allReduce(
            tensor.data_ptr(),
            tensor.data_ptr(),
            torch.numel(tensor),
            _type_torch_to_cupy(tensor.dtype),
            op,
            stream.ptr
        )

    def scatter(self,
                tensor: torch.Tensor,
                scatter_list: List[torch.Tensor],
                src: int,
                stream=cupy.cuda.Stream.null):
        cupy.cuda.nccl.groupStart()
        if self.rank == src:
            for i in range(self.world_size):
                if i != src:
                    self.send(
                        scatter_list[i],
                        i,
                        stream
                    )
                else:
                    tensor.copy_(scatter_list[i])
        else:
            self.recv(
                tensor,
                src,
                stream
            )
        cupy.cuda.nccl.groupEnd()

    def gather(self,
               tensor: torch.Tensor,
               gather_list: List[torch.Tensor],
               dst: int,
               stream=cupy.cuda.Stream.null):
        cupy.cuda.nccl.groupStart()
        if self.rank == dst:
            for i in range(self.world_size):
                if i != dst:
                    self.recv(
                        gather_list[i],
                        i,
                        stream
                    )
                else:
                    gather_list[i].copy_(tensor)
        else:
            self.send(
                tensor,
                dst,
                stream
            )
        cupy.cuda.nccl.groupEnd()