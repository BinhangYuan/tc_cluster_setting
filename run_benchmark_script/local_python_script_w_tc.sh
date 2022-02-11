cd ~/tc_cluster_setting
source activate pytorch_p38

DELAY_MS=$1
RATE_GBIT=$2
RANK=$3
WORLD_SIZE=$4

timestamp=$(date +%Y_%m_%d_%H_%M)

sh ./tc_script/tc_netem_delay_bandwdith.sh $DELAY_MS $RATE_GBIT >>  "./log/${timestamp}.log"

# The private IP of Rank-0 node should be manually updated in each run.
python pytorch_collective_test.py --dist-url tcp://172.31.41.25:9000 --dist-backend gloo --world-size "$WORLD_SIZE" --rank "$RANK" >>  "./log/${timestamp}.log"

sh ./tc_script/tc_clear.sh