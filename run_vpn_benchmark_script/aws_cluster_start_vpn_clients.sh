source ./ip_dict.sh

for ip in "${!ip_region_dict[@]}"; do
  if [ $ip != $vpn_server_ip ]
  then
    region=${ip_region_dict[$ip]}
    echo "IP $ip in region $region"
    ssh -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip" "bash -s" < ./aws_instance_start_vpn_client.sh "$region" &
  fi
done
