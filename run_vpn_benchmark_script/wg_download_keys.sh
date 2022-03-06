source ./ip_dict.sh

for ip in "${!ip_region_dict[@]}"; do
  region=${ip_region_dict[$ip]}
  echo "IP $ip in region $region"
  if [ $ip == $vpn_server_ip ]
  then
    scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/public.key  ../wireguard/s_"$ip"_public.key
    scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/private.key ../wireguard/s_"$ip"_private.key
  else
    scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/public.key  ../wireguard/c_"$ip"_public.key
    scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/private.key ../wireguard/c_"$ip"_private.key
  fi
done

