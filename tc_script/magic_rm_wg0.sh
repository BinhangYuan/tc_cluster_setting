sudo /sbin/tc qdisc del dev wg0 root
sudo /sbin/iptables -D OUTPUT -t mangle -p udp -j MARK --set-mark 10