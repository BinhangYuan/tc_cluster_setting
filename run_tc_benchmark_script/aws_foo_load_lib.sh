source ./ip_list.sh

for ip in "${ips[@]}"
do
  echo "Issue command in $ip"
  ssh -i ../pems/binhang_ds3_aws_oregon.pem ubuntu@"$ip" "bash -s" < ./foo_load_lib.sh &
done
