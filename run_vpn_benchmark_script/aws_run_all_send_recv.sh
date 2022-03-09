source ./ip_dict.sh

for rank0_ip in "${!ip_private_dict[@]}"; do
  for rank1_ip in "${!ip_private_dict[@]}"; do
    if [ "$rank0_ip" -ne  "$rank1_ip" ]
    then
        ssh -i ../pems/binhang_ds3_aws_"${ip_region_dict[$rank0_ip]}".pem ubuntu@"$ip" "bash -s" < ./aws_instance_run_send_recv.sh &
        ssh -i ../pems/binhang_ds3_aws_"${ip_region_dict[$rank1_ip]}".pem ubuntu@"$ip" "bash -s" < ./aws_instance_run_send_recv.sh &
        wait
    fi
  done
done