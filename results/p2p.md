# Point to Point

## TC results

- A cluster of 2 AWS p3.2xlarge instances;
- The results are from the recv side (TC can only control recv side.)
- The data size is determined by the bytes of a practical macro-batch (for GPT-3 XL).

| Network setting             | Gloo-64 MB | NCCL-64 MB | Gloo-128 MB | NCCL-128 MB |
|-----------------------------|------------|------------|-------------|-------------|
| AWS default                 | 107 ms     | 55 ms      | 216 ms      | 112 ms      |
| delay 1ms                   | 110 ms     | 59 ms      | 222 ms      | 115 ms      |
| delay 5ms                   | 274 ms     | 80 ms      | 512 ms      | 134 ms      |
| delay 10ms                  | 532 ms     | 113 ms     | 972 ms      | 171 ms      |
| bandwidth 5Gbps             | 110 ms     | 109 ms     | 218 ms      | 217 ms      |
| bandwidth 2Gbps             | 271 ms     | 270 ms     | 542 ms      | 541 ms      |
| bandwidth 1Gbps             | 541 ms     | 541 ms     | 1082 ms     | 1082 ms     |
| delay 1ms  bandwidth 5Gbps  | 115 ms     | 110 ms     | 224 ms      | 220 ms      |
| delay 5ms  bandwidth 2Gbps  | 311 ms     | 275 ms     | 581 ms      | 542 ms      |
| delay 10ms  bandwidth 1Gbps | 620 ms     | 543 ms     | 1160 ms     | 1083 ms     |


## Real cross region by Swan VPN 

- 10 regions:
  - us-west-2 (Oregon)
  - us-east-1 (Virginia) 
  - us-east-2 (Ohio)
  - ap-northeast-1 (Tokyo)
  - ap-northeast-2 (Seoul)
  - ap-southeast-1 (Singapore)
  - ap-southeast-2 (Sydney)
  - eu-west-2 (London)
  - eu-central-1 (Frankfurt)
  - eu-west-1 (Ireland)

- Delay is tested by ping (connected private IP)

      ping -c 3 IP
- NCCL time is by transferring 64 MB data multiple times
- NCCL bandwidth is based on the above 
      
      export NCCL_SOCKET_NTHREADS=1      
      export NCCL_NSOCKS_PERTHREAD=8
pk
- Iperf3 commands:

      iperf3 -s
      iperf3 -c server-IP -t 8 -P 32

### Oregon (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B  | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|---------|---------------|---------------|
| Oregon          | Virginia        | 67 ms  | 761 Mbps | 4.56 Gbps     | 1.16 Gbps     |
| Oregon          | Ohio            | 49 ms  | 650 Mbps | 4.52 Gbps     | 1.34 Gbps     |
| Oregon          | Tokyo           | 96 ms  | 284 Mbps | 3.71 Gbps     | 641 Mbps      |
| Oregon          | Seoul           | 124 ms | 238 Mbps | 2.82 Gbps     | 488 Mbps      |
| Oregon          | Singapore       | 163 ms | 171 Mbps | 2.05 Gbps     | 384 Mbps      | 
| Oregon          | Sydney          | 139 ms | 218 Mbps | 2.50 Gbps     | 430 Mbps      |
| Oregon          | London          | 136 ms | 228 Mbps | 2.64 Gbps     | 475 Mbps      |
| Oregon          | Frankfurt       | 143 ms | 177 Mbps | 2.40 Gbps     | 458 Mbps      |
| Oregon          | Ireland         | 124 ms | 300 Mbps | 2.85 Gbps     | 424 Mbps      |


### Virginia (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Virginia        | Oregon          | 67 ms  |        |               |               |
| Virginia        | Ohio            | 11 ms  |        |               |               |
| Virginia        | Tokyo           | 143 ms |        |               |               |
| Virginia        | Seoul           | 172 ms |        |               |               |
| Virginia        | Singapore       | 230 ms |        |               |               |
| Virginia        | Sydney          | 197 ms |        |               |               | 
| Virginia        | London          | 76 ms  |        |               |               | 
| Virginia        | Frankfurt       | 90 ms  |        |               |               |
| Virginia        | Ireland         | 67 ms  |        |               |               |


### Ohio (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Ohio            | Oregon          | 48 ms  |        |               |               |
| Ohio            | Virginia        | 11 ms  |        |               |               |
| Ohio            | Tokyo           | 130 ms |        |               |               |
| Ohio            | Seoul           | 159 ms |        |               |               |
| Ohio            | Singapore       | 197 ms |        |               |               | 
| Ohio            | Sydney          | 185 ms |        |               |               |
| Ohio            | London          | 86 ms  |        |               |               |
| Ohio            | Frankfurt       | 99 ms  |        |               |               |
| Ohio            | Ireland         | 77 ms  |        |               |               |

### Tokyo (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Tokyo           | Oregon          | 97 ms  |        |               |               |
| Tokyo           | Virginia        | 143 ms |        |               |               |
| Tokyo           | Ohio            | 130 ms |        |               |               |
| Tokyo           | Seoul           | 34 ms  |        |               |               |
| Tokyo           | Singapore       | 73 ms  |        |               |               | 
| Tokyo           | Sydney          | 100 ms |        |               |               |
| Tokyo           | London          | 210 ms |        |               |               |
| Tokyo           | Frankfurt       | 223 ms |        |               |               |
| Tokyo           | Ireland         | 199 ms |        |               |               |


### Seoul (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Seoul           | Oregon          | 124 ms |        |               |               |
| Seoul           | Virginia        | 172 ms |        |               |               |
| Seoul           | Ohio            | 159 ms |        |               |               |
| Seoul           | Tokyo           | 33 ms  |        |               |               |
| Seoul           | Singapore       | 74 ms  |        |               |               | 
| Seoul           | Sydney          | 148 ms |        |               |               |
| Seoul           | London          | 238 ms |        |               |               |
| Seoul           | Frankfurt       | 235 ms |        |               |               |
| Seoul           | Ireland         | 228 ms |        |               |               |

### Singapore (NCCL recv / Iperf3 server)

| Region 1 (recv)    | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|--------------------|-----------------|--------|--------|---------------|---------------|
| Singapore          | Oregon          | 163 ms |        |               |               |
| Singapore          | Virginia        | 230 ms |        |               |               |
| Singapore          | Ohio            | 197 ms |        |               |               |
| Singapore          | Tokyo           | 73 ms  |        |               |               |
| Singapore          | Seoul           | 74 ms  |        |               |               | 
| Singapore          | Sydney          | 92 ms  |        |               |               |
| Singapore          | London          | 169 ms |        |               |               |
| Singapore          | Frankfurt       | 155 ms |        |               |               |
| Singapore          | Ireland         | 179 ms |        |               |               |

### Sydney (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Sydney          | Oregon          | 139 ms |        |               |               |
| Sydney          | Virginia        | 197 ms |        |               |               |
| Sydney          | Ohio            | 186 ms |        |               |               |
| Sydney          | Tokyo           | 114 ms |        |               |               |
| Sydney          | Seoul           | 140 ms |        |               |               | 
| Sydney          | Singapore       | 94 ms  |        |               |               |
| Sydney          | London          | 262 ms |        |               |               |
| Sydney          | Frankfurt       | 265 ms |        |               |               |
| Sydney          | Ireland         | 254 ms |        |               |               |

### London (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| London          | Oregon          | 134 ms |        |               |               |
| London          | Virginia        | 76 ms  |        |               |               |
| London          | Ohio            | 86 ms  |        |               |               |
| London          | Tokyo           | 210 ms |        |               |               |
| London          | Seoul           | 238 ms |        |               |               | 
| London          | Singapore       | 169 ms |        |               |               |
| London          | Sydney          | 263 ms |        |               |               |
| London          | Frankfurt       | 14 ms  |        |               |               |
| London          | Ireland         | 12 ms  |        |               |               |


### Frankfurt (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Frankfurt       | Oregon          | 147 ms |        |               |               |
| Frankfurt       | Virginia        | 89 ms  |        |               |               |
| Frankfurt       | Ohio            | 99 ms  |        |               |               |
| Frankfurt       | Tokyo           | 223 ms |        |               |               |
| Frankfurt       | Seoul           | 235 ms |        |               |               | 
| Frankfurt       | Singapore       | 155 ms |        |               |               |
| Frankfurt       | Sydney          | 265 ms |        |               |               |
| Frankfurt       | London          | 14 ms  |        |               |               |
| Frankfurt       | Ireland         | 24 ms  |        |               |               |

### Ireland (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|--------|---------------|---------------|
| Ireland         | Oregon          | 122 ms |        |               |               |
| Ireland         | Virginia        | 66 ms  |        |               |               |
| Ireland         | Ohio            | 77 ms  |        |               |               |
| Ireland         | Tokyo           | 199 ms |        |               |               |
| Ireland         | Seoul           | 228 ms |        |               |               | 
| Ireland         | Singapore       | 179 ms |        |               |               |
| Ireland         | Sydney          | 255 ms |        |               |               |
| Ireland         | London          | 11 ms  |        |               |               |
| Ireland         | Frankfurt       | 25 ms  |        |               |               |