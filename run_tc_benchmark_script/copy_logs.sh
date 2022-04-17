source ./ip_list.sh

scp -i ../pems/binhang_ds3_aws_oregon.pem ubuntu@"${ips[0]}":/home/ubuntu/tc_cluster_setting/logs/* ../logs