sudo /sbin/tc qdisc add dev wg0 root handle 1:0 htb default 10
sudo /sbin/tc class add dev wg0 parent 1:0 classid 1:10 htb rate 400mbps prio 0
sudo /sbin/iptables -A OUTPUT -t mangle -p udp -j MARK --set-mark 10
sudo tc filter add dev wg0 parent 1:0 prio 0 protocol ip handle 10 fw flowid 1:10