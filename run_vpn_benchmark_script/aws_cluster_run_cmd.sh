source ./ip_dict.sh
script=$1

for ip in "${!ip_region_dict[@]}"; do
    region=${ip_region_dict[$ip]}
    echo "execute CMD in IP $ip - region $region"
    ssh -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip" "bash -s" < ./"$script" &
done

wait
