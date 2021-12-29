# TC configure for PyTorch Benchmark

## Setup:

- Use AWS Deep Learning Base AMI, and install PyTorch:

       pip3 install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
- Clone this repository:
       
      git clone https://github.com/BinhangYuan/tc_cluster_setting.git

- set the github cache (Optional) 

      git config credential.helper 'cache --timeout=30000'

## Benchmark:

- Run this for benchmark:
     
      python3 pytorch_send_recv_test.py --dist-url tcp://XXX.XXX.XXX.XXX:9000 --world-size 2 --rank 0/1

## Results (AWS p3.2xlarge):
### default network:
- gloo backend delay: