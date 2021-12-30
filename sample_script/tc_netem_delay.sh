DELAY_MS=10
sudo tc qdisc add dev ens3 root netem delay ${DELAY_MS}ms