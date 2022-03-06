vpn_server_ip='34.220.155.244'

ip_region_dict = {}
ip_priviate_dict = {}
ip_region_dict['34.220.155.244']='oregon'
ip_priviate_dict['34.220.155.244']='172.31.47.46'
ip_region_dict['18.206.81.198']='virginia'
ip_priviate_dict['18.206.81.198']='172.31.81.36'
ip_region_dict['3.142.239.129']='ohio'
ip_priviate_dict["3.142.239.129"]='172.31.30.93'
#ip_region_dict['54.199.156.57']='tokyo'
ip_region_dict['54.169.216.236']='singapore'
ip_priviate_dict['54.169.216.236']='172.31.28.41'
#ip_region_dict['13.236.153.216']='sydney'
#ip_region_dict['35.182.88.213']='central'
#ip_region_dict['3.67.175.232']='frankfurt'
ip_region_dict['3.248.222.64']='ireland'
ip_priviate_dict['3.248.222.64']='172.31.25.5'

ip_keys= {}

for public_ip in ip_region_dict.keys():
    if public_ip == vpn_server_ip:
        file_prefix = "wireguard/s_"
    else:
        file_prefix = "wireguard/c_"
    with open(file_prefix + public_ip + '_public.key') as public_key_f:
        current_public_key = public_key_f.read()
    with open(file_prefix + public_ip + '_private.key') as private_key_f:
        current_private_key = private_key_f.read()
    ip_keys[public_ip] = {
        'public_key': current_public_key[:-1],
        'private_key': current_private_key[:-1]
    }

print(ip_keys)

# generate server conf first:
with open("./wireguard/s_" + vpn_server_ip + "_gen.conf", 'w') as conf_f:
    conf_f.write("[Interface]\n")
    conf_f.write("Address = 192.168.100.10\n")
    conf_f.write("PrivateKey = " + ip_keys[vpn_server_ip]['private_key'] + "\n")
    conf_f.write("ListenPort = 51820\n\n")
    last_no = 11
    for public_ip in ip_region_dict:
        if public_ip != vpn_server_ip:
            ip_priviate_dict[public_ip] = "192.168.100."+str(last_no) # limits to 256 so far
            last_no += 1
            assert last_no < 256
            conf_f.write("[Peer]\n")
            conf_f.write("PublicKey = " + ip_keys[public_ip]['public_key'] + "\n" )
            conf_f.write("AllowedIPs = " + ip_priviate_dict[public_ip] +"\n")
            conf_f.write("Endpoint = " + public_ip + ":51820\n\n")

# generate client conf then:
for public_ip in ip_region_dict.keys():
    if public_ip != vpn_server_ip:
        with open("./wireguard/c_" + public_ip + "_gen.conf", 'w') as conf_f:
            conf_f.write("[Interface]\n")
            conf_f.write("Address = " + ip_priviate_dict[public_ip] + "\n")
            conf_f.write("PrivateKey = " + ip_keys[public_ip]['private_key'] + "\n")
            conf_f.write("ListenPort = 51820\n\n")

            conf_f.write("[Peer]\n")
            conf_f.write("PublicKey = " + ip_keys[vpn_server_ip]['public_key'] + "\n")
            conf_f.write("Endpoint = " + vpn_server_ip + ":51820\n")
            conf_f.write("AllowedIPs = 192.168.100.0/24\n")

