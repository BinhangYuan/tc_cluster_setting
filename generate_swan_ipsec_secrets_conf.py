ip_region_dict = {}
ip_priviate_dict = {}
ip_region_dict['52.40.103.92']='oregon'
ip_priviate_dict['52.40.103.92']='172.31.47.46'
#ip_region_dict['44.200.95.108']='virginia'
ip_region_dict['18.218.126.1']='ohio'
ip_priviate_dict["18.218.126.1"]='172.31.30.93'
#ip_region_dict['54.199.156.57']='tokyo'
ip_region_dict['13.212.8.228']='singapore'
ip_priviate_dict['13.212.8.228']='172.31.28.41'
#ip_region_dict['13.236.153.216']='sydney'
#ip_region_dict['35.182.88.213']='central'
#ip_region_dict['3.67.175.232']='frankfurt'
#ip_region_dict['34.247.57.152']='ireland'
ip_region_dict['35.178.239.43']='london'
ip_priviate_dict['35.178.239.43']='172.31.2.37'

shared_key = "\"NOU9h8KOiStPeTp1Uj9StrAjE/ScGzPuB77a98EK1/QcDh1q9EaxTzV/+wCQA/ptZl6R5AUnOgIM3asDGEMWng==\""

for public_ip in ip_priviate_dict.keys():
    with open("./swan/"+public_ip+"_ipsec.secrets", 'w') as secret_f:
        secret_f.write("# This file holds shared secrets or RSA private keys for authentication.\n")
        secret_f.write("# RSA private key for this host, authenticating it to any other host")
        secret_f.write("# which knows the public part.\n")
        for other_public_ip in ip_priviate_dict.keys():
            if other_public_ip != public_ip:
                secret_f.write(public_ip+" "+other_public_ip+" : PSK "+shared_key+"\n")

    with open("./swan/"+public_ip+"_ipsec.conf", 'w') as conf_f:
        conf_f.write("# basic configuration\n")
        conf_f.write("config setup\n")
        conf_f.write("\tcharondebug=\"all\"\n")
        conf_f.write("\tuniqueids=yes\n")
        conf_f.write("\tstrictcrlpolicy=no\n")

        conf_f.write("# connection to different region below:\n")
        for other_public_ip in ip_priviate_dict.keys():
            if other_public_ip != public_ip:
                conf_f.write("conn "+ip_region_dict[public_ip]+"-to-"+ip_region_dict[other_public_ip]+"\n")
                conf_f.write("\tauthby=secret\n")
                conf_f.write("\tleft=%defaultroute\n")
                conf_f.write("\tleftid="+public_ip+"\n")
                conf_f.write("\tleftsubnet="+ip_priviate_dict[public_ip]+"/32\n")
                conf_f.write("\tright="+other_public_ip+"\n")
                conf_f.write("\trightsubnet="+ip_priviate_dict[other_public_ip]+'/32\n')
                conf_f.write("\tike=aes128gcm8-sha256-modp1024\n")
                conf_f.write("\tesp=aes256-sha2_256\n")
                conf_f.write("\tkeyingtries=0\n")
                conf_f.write("\tikelifetime=1h\n")
                conf_f.write("\tlifetime=8h\n")
                conf_f.write("\tdpddelay=30\n")
                conf_f.write("\tdpdtimeout=120\n")
                conf_f.write("\tdpdaction=restart\n")
                conf_f.write("\tauto=start\n")
                conf_f.write("\treplay_window = -1\n")
                conf_f.write("\n")


