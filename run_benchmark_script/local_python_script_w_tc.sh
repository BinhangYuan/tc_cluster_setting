cd ~/tc_cluster_setting
source activate pytorch_p38

export NCCL_SOCKET_IFNAME=ens3
export GLOO_SOCKET_IFNAME=ens3

DELAY_MS=$1
RATE_GBIT=$2
WORLD_SIZE=$3
RANK=$4
DIM=$5

timestamp=$(date +%Y_%m_%d_%H_%M)

sh ./tc_script/tc_netem_delay_bandwdith.sh $DELAY_MS $RATE_GBIT >>  "./logs/${timestamp}_tc.log"

# The private IP of Rank-0 node should be manually updated in each run.
python pytorch_collective_test.py --dist-url tcp://172.31.43.110:9000 --dist-backend gloo --use-cuda False --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_gloo_d${DELAY_MS}b${RATE_GBIT}.log"

python pytorch_collective_test.py --dist-url tcp://172.31.43.110:9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_cupy_nccl_d${DELAY_MS}b${RATE_GBIT}.log"

sh ./tc_script/tc_clear.sh