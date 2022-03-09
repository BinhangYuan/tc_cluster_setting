source ./ip_dict.sh

#ip='13.211.228.136'
for ip in "${!ip_region_dict[@]}"; do
  region=${ip_region_dict[$ip]}
  echo "IP $ip in region $region"
  scp -i ../pems/binhang_ds3_aws_"$region".pem ubuntu@"$ip":~/tc_cluster_setting/nccl_run_logs/*.log  ../nccl_run_logs/ &
done

wait