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
- Iperf3 commands:

      iperf3 -s
      iperf3 -c server-IP -t 10 -P 24

### Oregon (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send)    | Delay  | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|--------------------|--------|--------|--------|---------------|---------------|
| Oregon          | Virginia           | 67 ms  |        |        |               |               |
| Oregon          | Ohio               | 49 ms  |        |        |               |               |
| Oregon          | Tokyo              | 96 ms  |        |        |               |               |
| Oregon          | Seoul              | 124 ms |        |        |               |               |
| Oregon          | Singapore          | 168 ms |        |        |               |               | 
| Oregon          | Sydney             | 139 ms |        |        |               |               |
| Oregon          | London             | 136 ms |        |        |               |               |
| Oregon          | Frankfurt          | 143 ms |        |        |               |               |
| Oregon          | Ireland            | 124 ms |        |        |               |               |


### Virginia (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Virginia        | Oregon          |       |        |        |               |               |
| Virginia        | Ohio            |       |        |        |               |               |
| Virginia        | Tokyo           |       |        |        |               |               |
| Virginia        | Seoul           |       |        |        |               |               |
| Virginia        | Singapore       |       |        |        |               |               | 
| Virginia        | Sydney          |       |        |        |               |               |
| Virginia        | London          |       |        |        |               |               |
| Virginia        | Frankfurt       |       |        |        |               |               |
| Virginia        | Ireland         |       |        |        |               |               |


### Ohio (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Ohio            | Oregon          |       |        |        |               |               |
| Ohio            | Virginia        |       |        |        |               |               |
| Ohio            | Tokyo           |       |        |        |               |               |
| Ohio            | Seoul           |       |        |        |               |               |
| Ohio            | Singapore       |       |        |        |               |               | 
| Ohio            | Sydney          |       |        |        |               |               |
| Ohio            | London          |       |        |        |               |               |
| Ohio            | Frankfurt       |       |        |        |               |               |
| Ohio            | Ireland         |       |        |        |               |               |

### Tokyo (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Tokyo           | Oregon          |       |        |        |               |               |
| Tokyo           | Virginia        |       |        |        |               |               |
| Tokyo           | Ohio            |       |        |        |               |               |
| Tokyo           | Seoul           |       |        |        |               |               |
| Tokyo           | Singapore       |       |        |        |               |               | 
| Tokyo           | Sydney          |       |        |        |               |               |
| Tokyo           | London          |       |        |        |               |               |
| Tokyo           | Frankfurt       |       |        |        |               |               |
| Tokyo           | Ireland         |       |        |        |               |               |


### Seoul (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Seoul           | Oregon          |       |        |        |               |               |
| Seoul           | Virginia        |       |        |        |               |               |
| Seoul           | Ohio            |       |        |        |               |               |
| Seoul           | Tokyo           |       |        |        |               |               |
| Seoul           | Singapore       |       |        |        |               |               | 
| Seoul           | Sydney          |       |        |        |               |               |
| Seoul           | London          |       |        |        |               |               |
| Seoul           | Frankfurt       |       |        |        |               |               |
| Seoul           | Ireland         |       |        |        |               |               |

### Singapore (NCCL recv / Iperf3 server)

| Region 1 (recv)    | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|--------------------|-----------------|-------|--------|--------|---------------|---------------|
| Singapore          | Oregon          |       |        |        |               |               |
| Singapore          | Virginia        |       |        |        |               |               |
| Singapore          | Ohio            |       |        |        |               |               |
| Singapore          | Tokyo           |       |        |        |               |               |
| Singapore          | Seoul           |       |        |        |               |               | 
| Singapore          | Sydney          |       |        |        |               |               |
| Singapore          | London          |       |        |        |               |               |
| Singapore          | Frankfurt       |       |        |        |               |               |
| Singapore          | Ireland         |       |        |        |               |               |

### Sydney (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Sydney          | Oregon          |       |        |        |               |               |
| Sydney          | Virginia        |       |        |        |               |               |
| Sydney          | Ohio            |       |        |        |               |               |
| Sydney          | Tokyo           |       |        |        |               |               |
| Sydney          | Seoul           |       |        |        |               |               | 
| Sydney          | Singapore       |       |        |        |               |               |
| Sydney          | London          |       |        |        |               |               |
| Sydney          | Frankfurt       |       |        |        |               |               |
| Sydney          | Ireland         |       |        |        |               |               |

### London (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| London          | Oregon          |       |        |        |               |               |
| London          | Virginia        |       |        |        |               |               |
| London          | Ohio            |       |        |        |               |               |
| London          | Tokyo           |       |        |        |               |               |
| London          | Seoul           |       |        |        |               |               | 
| London          | Singapore       |       |        |        |               |               |
| London          | Sydney          |       |        |        |               |               |
| London          | Frankfurt       |       |        |        |               |               |
| London          | Ireland         |       |        |        |               |               |


### Frankfurt (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Frankfurt       | Oregon          |       |        |        |               |               |
| Frankfurt       | Virginia        |       |        |        |               |               |
| Frankfurt       | Ohio            |       |        |        |               |               |
| Frankfurt       | Tokyo           |       |        |        |               |               |
| Frankfurt       | Seoul           |       |        |        |               |               | 
| Frankfurt       | Singapore       |       |        |        |               |               |
| Frankfurt       | Sydney          |       |        |        |               |               |
| Frankfurt       | London          |       |        |        |               |               |
| Frankfurt       | Ireland         |       |        |        |               |               |

### Ireland (NCCL recv / Iperf3 server)

| Region 1 (recv) | Region 2 (send) | Delay | NCCL-T | NCCL-B | Iperf3 pub IP | Iperf3 (swan) |
|-----------------|-----------------|-------|--------|--------|---------------|---------------|
| Ireland         | Oregon          |       |        |        |               |               |
| Ireland         | Virginia        |       |        |        |               |               |
| Ireland         | Ohio            |       |        |        |               |               |
| Ireland         | Tokyo           |       |        |        |               |               |
| Ireland         | Seoul           |       |        |        |               |               | 
| Ireland         | Singapore       |       |        |        |               |               |
| Ireland         | Sydney          |       |        |        |               |               |
| Ireland         | London          |       |        |        |               |               |
| Ireland         | Frankfurt       |       |        |        |               |               |