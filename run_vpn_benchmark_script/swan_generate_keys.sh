region=$1
sudo cp "$region"_0.ovpn /etc/openvpn/client.conf
sudo openvpn --client --config /etc/openvpn/client.conf