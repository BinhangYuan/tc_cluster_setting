source ./ip_dict.sh

for ip in "${!ip_region_dict[@]}"; do
  region=${ip_region_dict[$ip]}
  echo "IP $ip in region $region"
  scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/public.key  ../wireguard/"$ip"_public.key &
  scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/private.key ../wireguard/"$ip"_private.key &
done

wait

