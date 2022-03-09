cd ~/tc_cluster_setting
source activate pytorch_p38

ip=$1
rank=$3

export NCCL_SOCKET_IFNAME=wg0
export GLOO_SOCKET_IFNAME=wg0
export NCCL_SOCKET_NTHREADS=4
export NCCL_NSOCKS_PERTHREAD=4

if [ "$rank" -eq 0 ]
then
  python pytorch_send_recv_test.py --iter 20 --dist-url tcp://"$ip":9000 --world-size 2 --dist-backend cupy_nccl --use-cuda True --rank 0
else
  python pytorch_send_recv_test.py --iter 20 --dist-url tcp://"$ip":9000 --world-size 2 --dist-backend cupy_nccl --use-cuda True --rank 1 >> "./foo.log"
fi