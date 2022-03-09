ip_region_dict = {}
ip_private_dict = {}

ip_region_dict['52.11.170.18']='oregon'
ip_private_dict['52.11.170.18']='172.31.32.123'

ip_region_dict['18.210.23.239']='virginia'
ip_private_dict['18.210.23.239']='172.31.84.109'

ip_region_dict['18.224.107.171']='ohio'
ip_private_dict["18.224.107.171"]='172.31.18.48'

ip_region_dict['18.182.10.97']='tokyo'
ip_private_dict['18.182.10.97']='172.31.21.127'

ip_region_dict['3.35.137.147']='seoul'
ip_private_dict['3.35.137.147']='172.31.5.28'

ip_region_dict['54.169.227.37']='singapore'
ip_private_dict['54.169.227.37']='172.31.19.162'

ip_region_dict['13.211.228.136']='sydney'
ip_private_dict['13.211.228.136']='172.31.1.165'

ip_region_dict['18.168.255.66']='london'
ip_private_dict['18.168.255.66']='172.31.16.34'

ip_region_dict['52.59.207.74']='frankfurt'
ip_private_dict['52.59.207.74']='172.31.29.106'

ip_region_dict['3.249.65.157']='ireland'
ip_private_dict['3.249.65.157']='172.31.31.5'

ip_keys= {}

last_no = 10
for public_ip in ip_region_dict.keys():
    file_prefix = "wireguard/"
    ip_private_dict[public_ip] = "192.168.100." + str(last_no)  # limits to 256 so far
    last_no += 1
    assert last_no < 256
    with open(file_prefix + public_ip + '_public.key') as public_key_f:
        current_public_key = public_key_f.read()
    with open(file_prefix + public_ip + '_private.key') as private_key_f:
        current_private_key = private_key_f.read()
    ip_keys[public_ip] = {
        'public_key': current_public_key[:-1],
        'private_key': current_private_key[:-1]
    }

for ip in ip_keys.keys():
    print(ip, ip_keys[ip])

for ip in ip_private_dict.keys():
    print(ip_region_dict[ip], ip, ip_private_dict[ip])

for self_ip in ip_region_dict.keys():
    with open("./wireguard/" + self_ip + "_gen.conf", 'w') as conf_f:
        conf_f.write("[Interface]\n")
        conf_f.write("Address = " + ip_private_dict[self_ip] + "\n")
        conf_f.write("PrivateKey = " + ip_keys[self_ip]['private_key'] + "\n")
        conf_f.write("ListenPort = 51820\n\n")
        
        for other_ip in ip_region_dict:
            if other_ip != self_ip:
                conf_f.write("[Peer]\n")
                conf_f.write("PublicKey = " + ip_keys[other_ip]['public_key'] + "\n")
                conf_f.write("AllowedIPs = " + ip_private_dict[other_ip] + "\n")
                conf_f.write("Endpoint = " + other_ip + ":51820\n\n")

