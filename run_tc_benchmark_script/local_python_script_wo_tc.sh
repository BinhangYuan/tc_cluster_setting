cd ~/tc_cluster_setting
source activate pytorch_p38

export NCCL_SOCKET_IFNAME=ens3
export GLOO_SOCKET_IFNAME=ens3

MASTER_IP=$1
WORLD_SIZE=$2
RANK=$3
DIM=$4

timestamp=$(date +%Y_%m_%d_%H_%M)

# The private IP of Rank-0 node should be manually updated in each run.
#python pytorch_collective_test.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend gloo --use-cuda False --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM">>  "./logs/${timestamp}_gloo_default.log"
#python pytorch_collective_test.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_cupyNccl_default.log"
# python pytorch_group_collective_test.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_group_cupyNccl_default.log"
python pytorch_debug_allreduce_opt.py --dist-url tcp://"$MASTER_IP":9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_shardedPS_cupyNccl_default.log"
echo "Done with the benchmark."