cd ~/tc_cluster_setting
source activate pytorch_p38

WORLD_SIZE=$1
RANK=$2

timestamp=$(date +%Y_%m_%d_%H_%M)

# The private IP of Rank-0 node should be manually updated in each run.
python pytorch_collective_test.py --dist-url tcp://172.31.45.33:9000 --dist-backend gloo --world-size "$WORLD_SIZE" --rank "$RANK" >>  "./logs/${timestamp}_gloo_default.log"

python pytorch_collective_test.py --dist-url tcp://172.31.45.33:9000 --dist-backend cupy_nccl --world-size "$WORLD_SIZE" --rank "$RANK" >>  "./logs/${timestamp}_cupyNccl_default.log"