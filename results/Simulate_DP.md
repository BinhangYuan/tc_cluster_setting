# Simulate DP 

- Run 16 iterations, each iteration needs to sync 64 MB.  

### AllReduce

| Network setting             | 4 nodes | 8 nodes | 16 nodes |  
|-----------------------------|---------|---------|----------|
| AWS default                 | 1.42 s  | s       | s        | 
| delay 1ms  bandwidth 5Gbps  | 2.95 s  | s       | s        | 
| delay 5ms  bandwidth 2Gbps  | 9.69 s  | s       | s        | 
| delay 10ms  bandwidth 1Gbps | 16.87 s | s       | s        | 
| delay 50ms  bandwidth 1Gbps | 31.43 s | s       | s        | 

### Centralized PS (based on NCCL Reduce-Broadcast)

| Network setting             | 4 nodes | 8 nodes | 16 nodes |  
|-----------------------------|---------|---------|----------|
| AWS default                 | 2.01 s  | s       | s        | 
| delay 1ms  bandwidth 5Gbps  | 4.27 s  | s       | s        | 
| delay 5ms  bandwidth 2Gbps  | 10.33 s | s       | s        | 
| delay 10ms  bandwidth 1Gbps | 19.79 s | s       | s        | 
| delay 50ms  bandwidth 1Gbps | 21.77 s | s       | s        | 


### Sharded PS

| Network setting             | 4 nodes | 8 nodes | 16 nodes |  
|-----------------------------|---------|---------|----------|
| AWS default                 | 2.24 s  | s       | s        | 
| delay 1ms  bandwidth 5Gbps  | 4.18 s  | s       | s        | 
| delay 5ms  bandwidth 2Gbps  | 10.13 s | s       | s        | 
| delay 10ms  bandwidth 1Gbps | 19.95 s | s       | s        | 
| delay 50ms  bandwidth 1Gbps | 21.84 s | s       | s        | 
