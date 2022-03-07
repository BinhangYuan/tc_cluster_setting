# TC configure for PyTorch Benchmark

## Setup:

- If use my AWS GPT@Home-Dev AMI, no further setup; 
      
     source activate pytorch_p38

- If use AWS deep learning base AMI:

      pip3 install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
      pip3 install cupy-cuda110==8.6.0


- Set the GitHub (Optional) 

      git clone https://github.com/BinhangYuan/tc_cluster_setting.git
      git config credential.helper 'cache --timeout=30000'

- <del>Set wireguard VPN (deprecated, use Swan VPN instead):

  - Install wireguard if necessary:
      
        sudo apt install wireguard

  - Generate public/private key (in root mode of each instance):
        
        wg genkey | tee private.key | wg pubkey > public.key
  
  - Sync up the configuration (in run_vpn_benchmark_script), update ip in ip_dict.sh/generate_wireguard_p2p_conf.py first: 
        
        bash wg_download_keys.sh
        python generate_wireguard_conf
        bash wg_upload_conf.sh
  
  - Start vpn (in root mode of each instance)

        bash wg_start_vpn.sh

- Set up swan ipsec VPN
  - Install strongswan if necessary:
      
        sudo apt install strongswan
  - Sync secret/conf file, update ip in generate_swan_ipsec_secrets_conf.py
        
        python generate_swan_ipsec_secrets_conf.py
        bash swan_upload_conf.sh
  
  - Start vpn (in root mode of each instance)
        
         bash swan_start_vpn.sh
    or
         bash aws_cluster_run_cmd.sh swan_start_vpn.sh


- Set network interface (updated below):

      export NCCL_SOCKET_IFNAME=ens3
      export GLOO_SOCKET_IFNAME=ens3
  or    

<del>export NCCL_SOCKET_IFNAME=wg0<del> 

<del>export GLOO_SOCKET_IFNAME=wg0<del>


- Set NCCL FLAGs:

      export NCCL_SOCKET_NTHREADS=1
      export NCCL_NSOCKS_PERTHREAD=8/16
      export NCCL_DEBUG=INFO
      export NCCL_COMM_ID=XX.XX.XX.XX:30000


## Benchmark:

- Run this for benchmark:

      python pytorch_send_recv_test.py --iter 5 --dist-url tcp://10.8.0.1:9000 --world-size 2 --dist-backend cupy_nccl --use-cuda True --rank 0/1

## Results 

- [Point to Point](./results/p2p.md)

- [AllReduce](./results/allreduce.md)

- [Broadcast](./results/broadcast.md)

- [Reduce](./results/reduce.md)






