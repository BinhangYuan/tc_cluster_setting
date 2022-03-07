source ./ip_dict.sh

for ip in "${!ip_region_dict[@]}"; do
  region=${ip_region_dict[$ip]}
  echo "IP $ip in region $region"
  if [ $ip == $vpn_server_ip ]
  then
    scp -i ../pems/binhang_ds3_aws_"$region".pem  ../wireguard/"$ip"_gen.conf ubuntu@"$ip":~/wg0.conf
  else
    scp -i ../pems/binhang_ds3_aws_"$region".pem  ../wireguard/"$ip"_gen.conf ubuntu@"$ip":~/wg0.conf
  fi &
done