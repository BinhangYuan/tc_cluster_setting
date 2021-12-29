RATE_GBIT=1
sudo tc qdisc add dev ens3 root tbf rate ${RATE_GBIT}gbit burst 100gbit latency 4000ms