source ./ip_list.sh

world_size=${#ips[@]}

delay_ms=$1
rate_gbit=$2
dim=1024

for rank in "${!ips[@]}"
do
  echo "Issue command in Rank-$rank node: ${ips[$rank]}"
  ssh -i ../pems/binhang_ds3_aws_oregon.pem ubuntu@"${ips[rank]}" "bash -s" < ./local_python_script_w_tc.sh "$delay_ms" "$rate_gbit" "$master_ip" "$world_size" "$rank" "$dim" &
done