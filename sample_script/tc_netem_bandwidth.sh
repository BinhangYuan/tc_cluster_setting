RATE_GBIT=1
LIMIT_PKTS=$(echo "$RATE_GBIT * 1500 * 10 * 1.5" | bc -q)
sudo tc qdisc replace dev ens3 root netem rate ${RATE_GBIT}Gbit limit ${LIMIT_PKTS}