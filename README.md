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

- A cluster of 2 AWS p3.2xlarge instances;
- The results are from the recv side (TC can only control recv side.)
- The data size is determined by the bytes of a practical macro-batch (for GPT-3 XL).
  - macro-batch size: 4, 8;
  - sequence length: 2048;
  - model size: 2048.

| Network setting              | Gloo-64 MB | NCCL-64 MB | Gloo-128 MB | NCCL-128 MB |
|------------------------------|------------|------------|-------------|-------------|
| default (0.1ms delay 10Gbps) |            |            |             |             |
| delay 1ms                    |            |            |             |             |
| delay 5ms                    |            |            |             |             |
| delay 10ms                   |            |            |             |             |
| bandwidth 5Gbps              |            |            |             |             |
| bandwidth 2Gbps              |            |            |             |             |
| bandwidth 1Gbps              |            |            |             |             |
| delay 1ms  bandwidth 5Gbps   |            |            |             |             |
| delay 5ms  bandwidth 2Gbps   |            |            |             |             |
| delay 10ms  bandwidth 1Gbps  |            |            |             |             |
