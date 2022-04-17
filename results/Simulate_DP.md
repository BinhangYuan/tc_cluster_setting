# Simulate DP 

### AllReduce

- Run synchronization of 256 MB / 1 GB. 

|                             | 256 MB  |         |          | 1024 MB |         |          |
|-----------------------------|---------|---------|----------|---------|---------|----------|
| Network setting             | 4 nodes | 8 nodes | 16 nodes | 4 nodes | 8 nodes | 16 nodes |
| AWS default                 | 0.37 s  | 0.45 s  | 0.53 s   | 1.42 s  | 1.95 s  | 2.07 s   |  
| delay 1ms  bandwidth 5Gbps  | 0.71 s  | 0.87 s  | 1.52 s   | 3.15 s  | 3.81 s  | 4.88 s   | 
| delay 5ms  bandwidth 2Gbps  | 1.77 s  | 2.50 s  | 4.72 s   | 7.23 s  | 8.23 s  | 8.82 s   | 
| delay 10ms  bandwidth 1Gbps | 4.06 s  | 5.14 s  | 8.22 s   | 16.87 s | 17.21 s | 18.56 s  | 
| delay 50ms  bandwidth 1Gbps | 7.57 s  | 8.27 s  | 28.63 s  | 29.83 s | 33.46 s | 36.26 s  |  


### Centralized PS (based on NCCL reduce + broadcast)

- Run synchronization of 256 MB / 1 GB.

|                             | 256 MB  |         |          | 1024 MB |         |          |
|-----------------------------|---------|---------|----------|---------|---------|----------|
| Network setting             | 4 nodes | 8 nodes | 16 nodes | 4 nodes | 8 nodes | 16 nodes |
| AWS default                 | 0.57 s  | 0.59 s  | 0.62 s   | 1.97 s  | 2.09 s  | 2.38 s   | 
| delay 1ms  bandwidth 5Gbps  | 1.09 s  | 1.10 s  | 1.28 s   | 3.88 s  | 4.28 s  | 4.52 s   |
| delay 5ms  bandwidth 2Gbps  | 2.86 s  | 3.29 s  | 2.99 s   | 10.14 s | 10.66 s | 11.75 s  | 
| delay 10ms  bandwidth 1Gbps | 5.55 s  | 5.87 s  | 7.41 s   | 14.10 s | 21.26 s | 23.41 s  | 
| delay 50ms  bandwidth 1Gbps | 6.65 s  | 7.73 s  | 10.87 s  | 20.56 s | 23.52 s | 28.67 s  |

### Sharded PS (based on NCCL all_to_all + all_gather)

- Run synchronization of 256 MB / 1 GB. 

|                             | 256 MB  |         |          | 1024 MB |         |          |
|-----------------------------|---------|---------|----------|---------|---------|----------|
| Network setting             | 4 nodes | 8 nodes | 16 nodes | 4 nodes | 8 nodes | 16 nodes |
| AWS default                 | 0.42 s  | 0.53 s  | 0.60 s   | 1.63 s  | 3.12 s  | 2.33 s   | 
| delay 1ms  bandwidth 5Gbps  | 0.80 s  | 0.87 s  | 1.00 s   | 2.92 s  | 3.40 s  | 4.24 s   | 
| delay 5ms  bandwidth 2Gbps  | 2.35 s  | 2.60 s  | 2.88 s   | 7.58 s  | 9.52 s  | 10.11 s  |
| delay 10ms  bandwidth 1Gbps | 4.23 s  | 5.16 s  | 6.39 s   | 16.18 s | 20.17 s | 22.64 s  |  
| delay 50ms  bandwidth 1Gbps | 4.77 s  | 6.07 s  | 7.27 s   | 18.48 s | 21.69 s | 26.76 s  | 

