RATE_GBIT=$1
echo "TC(tbf) set up bandwidth to $1 gbit."
sudo tc qdisc add dev ens3 root tbf rate ${RATE_GBIT}gbit burst 100gbit latency 4000ms