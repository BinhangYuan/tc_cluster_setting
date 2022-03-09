sudo su
cp ./wg0.conf /etc/wireguard/wg0.conf
#shut down previous interface.
# wg-quick down wg0
wg-quick up wg0
#su ubuntu