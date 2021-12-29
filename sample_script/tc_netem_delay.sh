DELAY_MS=40
sudo tc qdisc add dev ens3 root netem delay ${DELAY_MS}ms