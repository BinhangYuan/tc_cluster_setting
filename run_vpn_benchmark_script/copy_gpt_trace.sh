source ./ip_dict.sh

# Current valid prefix includes:
# gpt3_gpipe_b64_1_l2048_m768_w3_p3_d1,
# gpt3_gpipe_b64_1_l2048_m768_w12_p3_d4
# gpt3_gpipe_b64_1_l2048_m768_w48_p3_d16
# gpt3_gpipe_b64_1_l2048_m2048_w12_p12_d1
# gpt3_gpipe_b64_1_l2048_m2048_w48_p12_d4


profix="gpt3_gpipe_b64_1_l2048_m2048_w12_p12_d1"
postfix="real"
world_size=12

if [ -d "../trace_json/${profix}" ]
then
  rm -rf ../trace_json/"$profix"
fi

mkdir ../trace_json/"$profix"


for ip in "${!ip_region_dict[@]}"; do
  region=${ip_region_dict[$ip]}
  scp -i ../pems/binhang_ds3_aws_"$region".pem  ubuntu@"$ip":~/GPT-home-private/trace_json/"$profix"_*_"$postfix".json ../trace_json/"$profix" &
done
