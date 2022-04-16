cd ~/tc_cluster_setting
source activate pytorch_p38

export NCCL_SOCKET_IFNAME=ens3
export GLOO_SOCKET_IFNAME=ens3

DELAY_MS=$1
RATE_GBIT=$2
MASTER_IP=$3
WORLD_SIZE=$4
RANK=$5
DIM=$6

timestamp=$(date +%Y_%m_%d_%H_%M)

sh ./tc_script/tc_netem_delay_bandwdith.sh $DELAY_MS $RATE_GBIT #>>  "./logs/${timestamp}_tc.log"

#python pytorch_collective_test.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend gloo --use-cuda False --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_gloo_d${DELAY_MS}b${RATE_GBIT}.log"
#python pytorch_collective_test.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_cupy_nccl_d${DELAY_MS}b${RATE_GBIT}.log"
python pytorch_group_collective_test.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_group_cupyNCCL_d${DELAY_MS}b${RATE_GBIT}.log"
sh ./tc_script/tc_clear.sh
echo "Done with the benchmark."