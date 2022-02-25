# TC configure for PyTorch Benchmark

## Setup:

- Use my AWS GPT@Home-Dev AMI


- Set the GitHub cache (Optional) 

      git config credential.helper 'cache --timeout=30000'

- Set network interface (updated below):

      export NCCL_SOCKET_IFNAME=ens3
      export GLOO_SOCKET_IFNAME=ens3

- Set NCCL FLAGs:

      export NCCL_DEBUG=INFO
      export NCCL_COMM_ID=XX.XX.XX.XX:30000

## Benchmark:

- Run this for benchmark:
     
      python3 pytorch_send_recv_test.py --dist-url tcp://XXX.XXX.XXX.XXX:9000 --world-size 2 --rank 0/1

## Results 

- [Point to Point](./results/p2p.md)

- [AllReduce](./results/allreduce.md)

- [Broadcast](./results/broadcast.md)

- [Reduce](./results/reduce.md)






