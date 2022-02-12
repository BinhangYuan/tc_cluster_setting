cd ~/tc_cluster_setting
source activate pytorch_p38

export NCCL_SOCKET_IFNAME=ens3
export GLOO_SOCKET_IFNAME=ens3

WORLD_SIZE=$1
RANK=$2
DIM=$3

timestamp=$(date +%Y_%m_%d_%H_%M)

# The private IP of Rank-0 node should be manually updated in each run.
python pytorch_collective_test.py --dist-url tcp://172.31.45.33:9000 --dist-backend gloo --use-cuda False --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM">>  "./logs/${timestamp}_gloo_default.log"

python pytorch_collective_test.py --dist-url tcp://172.31.45.33:9000 --dist-backend cupy_nccl --use-cuda True --world-size "$WORLD_SIZE" --rank "$RANK" --dim-mb "$DIM" >>  "./logs/${timestamp}_cupyNccl_default.log"