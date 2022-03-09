source ./ip_dict.sh

for rank0_ip in "${!ip_private_dict[@]}"; do
  for rank1_ip in "${!ip_private_dict[@]}"; do
    if [ "$rank0_ip" -ne  "$rank1_ip" ]
    then
        echo "${ip_region_dict[$rank0_ip]} recv, ${ip_region_dict[$rank0_ip]} send."
        ssh -i ../pems/binhang_ds3_aws_"${ip_region_dict[$rank0_ip]}".pem ubuntu@"$rank0_ip" "bash -s" < ./aws_instance_run_send_recv.sh \
        "${ip_private_dict[rank0_ip]}" 0 "${ip_region_dict[$rank0_ip]}_r_${ip_region_dict[$rank0_ip]}_s" &
        ssh -i ../pems/binhang_ds3_aws_"${ip_region_dict[$rank1_ip]}".pem ubuntu@"$rank1_ip" "bash -s" < ./aws_instance_run_send_recv.sh \
        "${ip_private_dict[rank0_ip]}" 1 &
        wait
    fi
  done
done