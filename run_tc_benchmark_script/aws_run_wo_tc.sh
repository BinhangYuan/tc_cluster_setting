source ./ip_list.sh

world_size=${#ips[@]}
dim=1024

for rank in "${!ips[@]}"
do
  echo "Issue command in Rank-$rank node: ${ips[$rank]}"
  ssh -i ../pems/binhang_ds3_aws_oregon.pem ubuntu@"${ips[rank]}" "bash -s" < ./local_python_script_wo_tc.sh "$master_ip" "$world_size" "$rank" "$dim" &
done