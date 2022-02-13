## AllReduce

#### 4 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB | 
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 327 ms      | 175 ms      | 657 ms      | 363 ms      |
| delay 1ms  bandwidth 5Gbps  | 485 ms      | 329 ms      | 959 ms      | 655 ms      |
| delay 5ms  bandwidth 2Gbps  | 1517 ms     | 835 ms      | 2989 ms     | 1650 ms     |
| delay 10ms  bandwidth 1Gbps | 2993 ms     | 1669 ms     | 5909 ms     | 3298 ms     |

#### 8 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 382 ms      | 208 ms      | 765 ms      | 443 ms      |
| delay 1ms  bandwidth 5Gbps  | 537 ms      | 383 ms      | 1111 ms     | 763 ms      |
| delay 5ms  bandwidth 2Gbps  | 1814 ms     | 970 ms      | 3562 ms     | 1921 ms     |
| delay 10ms  bandwidth 1Gbps | 3582 ms     | 1940 ms     | 6999 ms     | 3841 ms     |

#### 16 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 412 ms      | 252 ms      | 819 ms      | 474 ms      |
| delay 1ms  bandwidth 5Gbps  | 612 ms      | 410 ms      | 1239 ms     | 817 ms      |
| delay 5ms  bandwidth 2Gbps  | 1950 ms     | 1038 ms     | 3861 ms     | 2057 ms     |
| delay 10ms  bandwidth 1Gbps | 3873 ms     | 2076 ms     | 7636 ms     | 4114 ms     |


#### 32 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 428 ms      | 252 ms      | 849 ms      | 523 ms      |
| delay 1ms  bandwidth 5Gbps  | 629 ms      | 434 ms      | 1299 ms     | 844 ms      |
| delay 5ms  bandwidth 2Gbps  | 1992 ms     | 1071 ms     | 4029 ms     | 2124 ms     |
| delay 10ms  bandwidth 1Gbps | 3940 ms     | 2141 ms     | 7816 ms     | 4251 ms     |