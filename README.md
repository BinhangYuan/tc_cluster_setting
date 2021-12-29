# TC configure for PyTorch Benchmark

## Setup:

- Use AWS Deep Learning Base AMI, and install PyTorch:

      pip3 install torch==1.9.0+cu111
- Clone this repository:
       
      git clone https://github.com/BinhangYuan/tc_cluster_setting.git

## Benchmark:

- Run this for benchmark:
     
      python pytorch_send_recv_test.py --dist-url tcp://XXX.XXX.XXX.XXX:9000 --world-size 2 --rank 0/1