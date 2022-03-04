# TC configure for PyTorch Benchmark

## Setup:

- If use my AWS GPT@Home-Dev AMI, no further setup; 

- If use AWS deep learning base AMI:

      pip3 install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
      pip3 install cupy-cuda110==8.6.0


- Set the GitHub (Optional) 

      git clone https://github.com/BinhangYuan/tc_cluster_setting.git
      git config credential.helper 'cache --timeout=30000'

- Set network interface (updated below):

      export NCCL_SOCKET_IFNAME=ens3
      export GLOO_SOCKET_IFNAME=ens3
      export NCCL_SOCKET_IFNAME=tun0


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






