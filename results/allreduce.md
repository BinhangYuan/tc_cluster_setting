## AllReduce

#### 4 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-----|-----|
| AWS default                 | 327 ms      | 175 ms      |  ms |  ms |
| delay 1ms  bandwidth 5Gbps  | 485 ms      | 329 ms      |  ms |  ms |
| delay 5ms  bandwidth 2Gbps  | 1517 ms     | 835 ms      |  ms |  ms |
| delay 10ms  bandwidth 1Gbps | 2993 ms     | 1669 ms     |  ms |  ms |

#### 8 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-----|-----|
| AWS default                 | ms          | ms          |  ms |  ms |
| delay 1ms  bandwidth 5Gbps  | ms          | ms          |  ms |  ms |
| delay 5ms  bandwidth 2Gbps  | ms          | ms          |  ms |  ms |
| delay 10ms  bandwidth 1Gbps | ms          | ms          |  ms |  ms |

#### 16 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-----|-----|
| AWS default                 | ms          | ms          |  ms |  ms |
| delay 1ms  bandwidth 5Gbps  | ms          | ms          |  ms |  ms |
| delay 5ms  bandwidth 2Gbps  | ms          | ms          |  ms |  ms |
| delay 10ms  bandwidth 1Gbps | ms          | ms          |  ms |  ms |


#### 32 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-----|-----|
| AWS default                 | ms          | ms          |  ms |  ms |
| delay 1ms  bandwidth 5Gbps  | ms          | ms          |  ms |  ms |
| delay 5ms  bandwidth 2Gbps  | ms          | ms          |  ms |  ms |
| delay 10ms  bandwidth 1Gbps | ms          | ms          |  ms |  ms |