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
      
      export NCCL_SOCKET_IFNAME=wg0
      export GLOO_SOCKET_IFNAME=wg0
      export NCCL_SOCKET_NTHREADS=4
      export NCCL_NSOCKS_PERTHREAD=4

- Iperf3 commands:

      iperf3 -s
      iperf3 -c server-IP -t 8 -P 32

### Oregon (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | NCCL-B(swan)-dumped | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------------|---------------|---------------|
| Oregon          | Virginia        | 67 ms  | 790 Mbps  | 761 Mbps            | 4.56 Gbps     | 1.16 Gbps     |
| Oregon          | Ohio            | 49 ms  | 1.10 Gbps | 650 Mbps            | 4.52 Gbps     | 1.34 Gbps     |
| Oregon          | Tokyo           | 96 ms  | 523 Mbps  | 284 Mbps            | 3.71 Gbps     | 641 Mbps      |
| Oregon          | Seoul           | 124 ms | 460 Mbps  | 238 Mbps            | 2.82 Gbps     | 488 Mbps      |
| Oregon          | Singapore       | 163 ms | 341 Mbps  | 171 Mbps            | 2.05 Gbps     | 384 Mbps      | 
| Oregon          | Sydney          | 139 ms | 360 Mbps  | 218 Mbps            | 2.50 Gbps     | 430 Mbps      |
| Oregon          | London          | 136 ms | 420 Mbps  | 228 Mbps            | 2.64 Gbps     | 475 Mbps      |
| Oregon          | Frankfurt       | 143 ms | 404 Mbps  | 177 Mbps            | 2.40 Gbps     | 458 Mbps      |
| Oregon          | Ireland         | 124 ms | 482 Mbps  | 300 Mbps            | 2.85 Gbps     | 424 Mbps      |


### Virginia (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| Virginia        | Oregon          | 67 ms  | 1.15 Gbps |               |               |
| Virginia        | Ohio            | 11 ms  | 1.12 Gbps |               |               |
| Virginia        | Tokyo           | 143 ms | 524 Mbps  |               |               |
| Virginia        | Seoul           | 172 ms | 500 Mbps  |               |               |
| Virginia        | Singapore       | 230 ms | 364 Mbps  |               |               |
| Virginia        | Sydney          | 197 ms | 383 Mbps  |               |               | 
| Virginia        | London          | 76 ms  | 1.16 Gbps |               |               | 
| Virginia        | Frankfurt       | 90 ms  | 1.02 Gbps |               |               |
| Virginia        | Ireland         | 67 ms  | 1.05 Gbps |               |               |


### Ohio (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| Ohio            | Oregon          | 48 ms  | 1.07 Gbps |               |               |
| Ohio            | Virginia        | 11 ms  | 1.13 Gbps |               |               |
| Ohio            | Tokyo           | 130 ms | 694 Mbps  |               |               |
| Ohio            | Seoul           | 159 ms | 529 Mbps  |               |               |
| Ohio            | Singapore       | 197 ms | 452 Mbps  |               |               | 
| Ohio            | Sydney          | 185 ms | 484 Mbps  |               |               |
| Ohio            | London          | 86 ms  | 1.05 Gbps |               |               |
| Ohio            | Frankfurt       | 99 ms  | 799 Mbps  |               |               |
| Ohio            | Ireland         | 77 ms  | 1.14 Gbps |               |               |

### Tokyo (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| Tokyo           | Oregon          | 97 ms  | 861 Mbps  |               |               |
| Tokyo           | Virginia        | 143 ms | 535 Mbps  |               |               |
| Tokyo           | Ohio            | 130 ms | 696 Mbps  |               |               |
| Tokyo           | Seoul           | 34 ms  | 1.10 Gbps |               |               |
| Tokyo           | Singapore       | 73 ms  | 1.01 Gbps |               |               | 
| Tokyo           | Sydney          | 100 ms | 761 Mbps  |               |               |
| Tokyo           | London          | 210 ms | 366 Mbps  |               |               |
| Tokyo           | Frankfurt       | 223 ms | 360 Mbps  |               |               |
| Tokyo           | Ireland         | 199 ms | 465 Mbps  |               |               |


### Seoul (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| Seoul           | Oregon          | 124 ms | 719 Mbps  |               |               |
| Seoul           | Virginia        | 172 ms | 511 Mbps  |               |               |
| Seoul           | Ohio            | 159 ms | 518 Mbps  |               |               |
| Seoul           | Tokyo           | 33 ms  | 1.11 Gbps |               |               |
| Seoul           | Singapore       | 74 ms  | 1.14 Gbps |               |               | 
| Seoul           | Sydney          | 148 ms | 580 Mbps  |               |               |
| Seoul           | London          | 238 ms | 342 Mbps  |               |               |
| Seoul           | Frankfurt       | 235 ms | 358 Mbps  |               |               |
| Seoul           | Ireland         | 228 ms | 335 Mbps  |               |               |

### Singapore (NCCL recv / Iperf3 server)

| Region 1 (recv)    | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|--------------------|-----------------|--------|-----------|---------------|---------------|
| Singapore          | Oregon          | 163 ms | 510 Mbps  |               |               |
| Singapore          | Virginia        | 230 ms | 358 Mbps  |               |               |
| Singapore          | Ohio            | 197 ms | 447 Mbps  |               |               |
| Singapore          | Tokyo           | 73 ms  | 1.05 Gbps |               |               |
| Singapore          | Seoul           | 74 ms  | 1.11 Gbps |               |               | 
| Singapore          | Sydney          | 92 ms  | 816 Mbps  |               |               |
| Singapore          | London          | 169 ms | 500 Mbps  |               |               |
| Singapore          | Frankfurt       | 155 ms | 535 Mbps  |               |               |
| Singapore          | Ireland         | 179 ms | 492 Mbps  |               |               |

### Sydney (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B   | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|----------|---------------|---------------|
| Sydney          | Oregon          | 139 ms | 537 Mbps |               |               |
| Sydney          | Virginia        | 197 ms | 463 Mbps |               |               |
| Sydney          | Ohio            | 186 ms | 490 Mbps |               |               |
| Sydney          | Tokyo           | 114 ms | 807 Mbps |               |               |
| Sydney          | Seoul           | 140 ms | 567 Mbps |               |               | 
| Sydney          | Singapore       | 94 ms  | 990 Mbps |               |               |
| Sydney          | London          | 262 ms | 326 Mbps |               |               |
| Sydney          | Frankfurt       | 265 ms | 328 Mbps |               |               |
| Sydney          | Ireland         | 254 ms | 344 Mbps |               |               |

### London (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| London          | Oregon          | 134 ms | 698 Mbps  |               |               |
| London          | Virginia        | 76 ms  | 761 Mbps  |               |               |
| London          | Ohio            | 86 ms  | 1.02 Gbps |               |               |
| London          | Tokyo           | 210 ms | 441 Mbps  |               |               |
| London          | Seoul           | 238 ms | 339 Mbps  |               |               | 
| London          | Singapore       | 169 ms | 506 Mbps  |               |               |
| London          | Sydney          | 263 ms | 343 Mbps  |               |               |
| London          | Frankfurt       | 14 ms  | 1.14 Gbps |               |               |
| London          | Ireland         | 12 ms  | 1.09 Gbps |               |               |


### Frankfurt (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| Frankfurt       | Oregon          | 147 ms | 339 Mbps  |               |               |
| Frankfurt       | Virginia        | 89 ms  | 521 Mbps  |               |               |
| Frankfurt       | Ohio            | 99 ms  | 474 Mbps  |               |               |
| Frankfurt       | Tokyo           | 223 ms | 212 Mbps  |               |               |
| Frankfurt       | Seoul           | 235 ms | 226 Mbps  |               |               | 
| Frankfurt       | Singapore       | 155 ms | 333 Mbps  |               |               |
| Frankfurt       | Sydney          | 265 ms | 204 Mbps  |               |               |
| Frankfurt       | London          | 14 ms  | 1.06 Gbps |               |               |
| Frankfurt       | Ireland         | 24 ms  | 1.08 Gbps |               |               |

### Ireland (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay  | NCCL-B    | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|--------|-----------|---------------|---------------|
| Ireland         | Oregon          | 122 ms | 726 Mbps  |               |               |
| Ireland         | Virginia        | 66 ms  | 794 Mbps  |               |               |
| Ireland         | Ohio            | 77 ms  | 447 Mbps  |               |               |
| Ireland         | Tokyo           | 199 ms | 460 Mbps  |               |               |
| Ireland         | Seoul           | 228 ms | 353 Mbps  |               |               | 
| Ireland         | Singapore       | 179 ms | 482 Mbps  |               |               |
| Ireland         | Sydney          | 255 ms | 339 Mbps  |               |               |
| Ireland         | London          | 11 ms  | 1.08 Gbps |               |               |
| Ireland         | Frankfurt       | 25 ms  | 1.10 Gbps |               |               |