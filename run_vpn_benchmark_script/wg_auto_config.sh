bash aws_cluster_run_cmd.sh wg_generate_keys.sh

bash wg_download_keys.sh

cd ..
python generate_wireguard_p2p_conf.py
cd ./run_vpn_benchmark

bash wg_upload_conf.sh

bash aws_cluster_run_cmd.sh wg_start_vpn.sh

bash aws_cluster_run_cmd.sh ../tc_script/magic_add_wg0.sh