# TC configure for PyTorch Benchmark

## Setup:

- Use AWS Deep Learning Base AMI, and install PyTorch:

       pip3 install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
       pip3 install cupy-cuda110==8.6.0

- Clone this repository:
       
      git clone https://github.com/BinhangYuan/tc_cluster_setting.git

- set the github cache (Optional) 

      git config credential.helper 'cache --timeout=30000'

## Benchmark:

- Run this for benchmark:
     
      python3 pytorch_send_recv_test.py --dist-url tcp://XXX.XXX.XXX.XXX:9000 --world-size 2 --rank 0/1

## Results (AWS p3.2xlarge):
### Default network (AWS spec: up to 10 Gbps):
- PyTorch-gloo backend delay: 0.1 ms; bandwidth: 4.5 Gbps
- PyTorch-nccl backend delay: 0.05 ms; bandwidth: 8.9 Gbps

### Use tc netem to setup delay to 1 ms:
- PyTorch-gloo backend delay: 1.2 ms; bandwidth: 4.5 Gbps
- PyTorch-nccl backend delay: <span style="color:red">0.05 ms </span>; bandwidth: 8.9 Gbps

### Use tc netem to setup delay to 10 ms:
- PyTorch-gloo backend delay: 10.2 ms; bandwidth: <span style="color:red">1.05 Gbps </span>
- PyTorch-nccl backend delay: <span style="color:red">0.05 ms </span>; bandwidth: <span style="color:red"> 6.5 Gbps </span>

### Use tc netem to setup bandwidth to 1 Gbps:
- PyTorch-gloo backend delay: 0.15 ms; bandwidth: 0.93 Gbps
- PyTorch-nccl backend delay: 0.08 ms; bandwidth: 0.93 Gbps

### Use tc tbf to setup bandwidth to 1 Gbps:
- PyTorch-gloo backend delay: 0.1 ms; bandwidth: <span style="color:red">4.5</span> Gbps
- PyTorch-nccl backend delay: 0.05 ms; bandwidth: <span style="color:red">8.9</span> Gbps