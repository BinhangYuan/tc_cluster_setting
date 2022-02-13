## Reduce

#### 4 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 314 ms      | 148 ms      | 616 ms      | 265 ms      |
| delay 1ms  bandwidth 5Gbps  | 406 ms      | 251 ms      | 801 ms      | 463 ms      |
| delay 5ms  bandwidth 2Gbps  | 1177 ms     | 717 ms      | 2275 ms     | 1168 ms     |
| delay 10ms  bandwidth 1Gbps | 2331 ms     | 1457 ms     | 4511 ms     | 2361 ms     |

#### 8 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 313 ms      | 149 ms      | 637 ms      | 283 ms      |
| delay 1ms  bandwidth 5Gbps  | 427 ms      | 254 ms      | 843 ms      | 473 ms      |
| delay 5ms  bandwidth 2Gbps  | 1176 ms     | 744 ms      | 2307 ms     | 1190 ms     |
| delay 10ms  bandwidth 1Gbps | 2314 ms     | 1525 ms     | 4329 ms     | 2426 ms     |

#### 16 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 320 ms      | 171 ms      | 647 ms      | 282 ms      |
| delay 1ms  bandwidth 5Gbps  | 438 ms      | 273 ms      | 873 ms      | 502 ms      |
| delay 5ms  bandwidth 2Gbps  | 1185 ms     | 822 ms      | 2337 ms     | 1251 ms     |
| delay 10ms  bandwidth 1Gbps | 2287 ms     | 1617 ms     | 4525 ms     | 2557 ms     |


#### 32 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 327 ms      | 173 ms      | 659 ms      | 300 ms      |
| delay 1ms  bandwidth 5Gbps  | 425 ms      | 316 ms      | 872 ms      | 601 ms      |
| delay 5ms  bandwidth 2Gbps  | 1196 ms     | 905 ms      | 2338 ms     | 1397 ms     |
| delay 10ms  bandwidth 1Gbps | 2318 ms     | 1709 ms     | 4448 ms     | 2815 ms     |