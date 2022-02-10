# TC configure for PyTorch Benchmark

## Setup:

- Use AWS Deep Learning Base AMI, and install PyTorch:

       pip3 install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
       pip3 install cupy-cuda110==8.6.0

- Clone this repository:
       
      git clone https://github.com/BinhangYuan/tc_cluster_setting.git

- Set the github cache (Optional) 

      git config credential.helper 'cache --timeout=30000'

- Set network interface:

      export NCCL_SOCKET_IFNAME=ens3
      export GLOO_SOCKET_IFNAME=ens3

## Benchmark:

- Run this for benchmark:
     
      python3 pytorch_send_recv_test.py --dist-url tcp://XXX.XXX.XXX.XXX:9000 --world-size 2 --rank 0/1

## Results 

- [Point to Point](./results/p2p.md)

- [AllReduce](./results/allreduce.md)

- [Broadcast](./results/broadcast.md)

- [Reduce](./results/reduce.md)






