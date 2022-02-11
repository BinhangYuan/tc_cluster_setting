cd ~/tc_cluster_setting
source activate pytorch_p38

RANK=$1
WORLD_SIZE=$2

timestamp=$(date +%Y_%m_%d_%H_%M)

# The private IP of Rank-0 node should be manually updated in each run.
python pytorch_collective_test.py --dist-url tcp://172.31.41.25:9000 --dist-backend gloo --world-size "$WORLD_SIZE" --rank "$RANK" >>  "./log/${timestamp}.log"

