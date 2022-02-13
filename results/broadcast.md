## Broadcast

#### 4 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 437 ms      | 144 ms      | 877 ms      | 258 ms      |
| delay 1ms  bandwidth 5Gbps  | 674 ms      | 243 ms      | 1334 ms     | 507 ms      |
| delay 5ms  bandwidth 2Gbps  | 1694 ms     | 710 ms      | 3322 ms     | 1284 ms     |
| delay 10ms  bandwidth 1Gbps | 3395 ms     | 1441 ms     | 6623 ms     | 2346 ms     |

#### 8 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 762 ms      | 147 ms      | 1344 ms     | 282 ms      |
| delay 1ms  bandwidth 5Gbps  | 1321 ms     | 264 ms      | 2628 ms     | 566 ms      |
| delay 5ms  bandwidth 2Gbps  | 3319 ms     | 744 ms      | 6567 ms     | 1187 ms     |
| delay 10ms  bandwidth 1Gbps | 6663 ms     | 1520 ms     | 13133 ms    | 2387 ms     |

#### 16 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 983 ms      | 181 ms      | 2179 ms     | 327 ms      |
| delay 1ms  bandwidth 5Gbps  | 2172 ms     | 277 ms      | 4331 ms     | 502 ms      |
| delay 5ms  bandwidth 2Gbps  | 5469 ms     | 831 ms      | 10868 ms    | 1333 ms     |
| delay 10ms  bandwidth 1Gbps | 10897 ms    | 1651 ms     | 21724 ms    | 2552 ms     |


#### 32 node:
| Network setting             | Gloo-128 MB | NCCL-128 MB | Gloo-256 MB | NCCL-256 MB |
|-----------------------------|-------------|-------------|-------------|-------------|
| AWS default                 | 1717 ms     | 172 ms      | 2761 ms     | 304 ms      |
| delay 1ms  bandwidth 5Gbps  | 3227 ms     | 309 ms      | 6487 ms     | 571 ms      |
| delay 5ms  bandwidth 2Gbps  | 8158 ms     | 957 ms      | 16204 ms    | 1475 ms     |
| delay 10ms  bandwidth 1Gbps | 16394 ms    | 1824 ms     | 32447 ms    | 2788 ms     |