source ./ip_dict.sh

scp -i ../pems/binhang_ds3_aws_"${ip_region_dict[$vpn_server_ip]}".pem ubuntu@"$vpn_server_ip":~/*.ovpn ../openvpn_configs
echo "Copied openVPN client configs to local machine."

for ip in "${!ip_region_dict[@]}"; do
  if [ $ip != $vpn_server_ip ]
  then
    region=${ip_region_dict[$ip]}
    echo "IP $ip in region $region"
    scp -i ../pems/binhang_ds3_aws_"$region".pem ../openvpn_configs/"$region"_0.ovpn ubuntu@"$ip":~/
  fi
done

