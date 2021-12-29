DELAY_MS=40
RATE_GBIT=1
LIMIT_PKTS=$(echo "$RATE_GBIT * 1500 * $DELAY_MS * 1.5" | bc -q)
sudo tc qdisc replace dev ens3 root netem delay ${DELAY_MS}ms rate ${RATE_GBIT}Gbit limit ${LIMIT_PKTS}