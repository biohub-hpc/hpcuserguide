# Running Jobs on GPUs

## Example Code

For this example, we will use this simple code to print out the GPUs available to each MPI rank which will help us understand how to use GPUs in a distributed environment.

```c
// gpus_for_tasks.cpp
#include <iostream>
#include <string>
#include <cuda_runtime.h>
#include <mpi.h>

int main(int argc, char **argv) {
  int deviceCount = 0;
  int rank, nprocs;

  MPI_Init (&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &nprocs);

  cudaGetDeviceCount(&deviceCount);

  printf("Rank %d out of %d processes: I see %d GPU(s).\n", rank, nprocs, deviceCount);

  int dev, len = 15;
  char gpu_id[15];
  cudaDeviceProp deviceProp;

  for (dev = 0; dev < deviceCount; ++dev) {
    cudaSetDevice(dev);
    cudaGetDeviceProperties(&deviceProp, dev);
    cudaDeviceGetPCIBusId(gpu_id, len, dev);
    printf("%d for rank %d: %s\n", dev, rank, gpu_id);
  }

  MPI_Finalize ();

  return 0;
}
```

To compile this code you will need to load `openmpi` so you can get MPI wrappers into your user environment. You can run the following to compile this code

```bash
mpicxx -o gpus_for_tasks gpus_for_tasks.cpp -lcudart
```

## 1 node, 1 task, 1 GPU

```bash
#!/bin/bash
#SBATCH -p gpu
#SBATCH -t 1:00:00
#SBATCH -n 1
#SBATCH -c 32
#SBATCH --gpus-per-task=1

export SLURM_CPU_BIND="cores"
srun --mpi=pmix ./gpus_for_tasks
```

This example script will run the code on a single node with 1 task and 1 GPU. The `--gpus-per-task=1` will ensure that each task gets a single GPU, therefore only 1 GPU will
be allocated. There will be 32 cores allocated to the task which can be used for threading.

Output: 

```console
[shahzeb.siddiqui@login-02 jobs]$ cat slurm-18029160.out
Rank 0 out of 1 processes: I see 1 GPU(s).
0 for rank 0: 0000:C3:00.0
```

We can confirm from output of `scontrol show job <job_id>` that this job ran as we expected. The `NumCPUs` and `NumTasks` are 32 and 1 with `CPUs/Task=32` which is 
what we requested from slurm. 

```console
[shahzeb.siddiqui@login-02 jobs]$ scontrol show job 18029160 | grep NumCPUs
   NumNodes=1 NumCPUs=32 NumTasks=1 CPUs/Task=32 ReqB:S:C:T=0:0:*:*
```

## 1 node, 4 tasks, 4 GPUs, all GPUs visible to all tasks

```bash
#!/bin/bash
#SBATCH -p gpu
#SBATCH -t 1:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH -c 32
#SBATCH --gpus-per-task=1
#SBATCH --gpu-bind=none

export SLURM_CPU_BIND="cores"
srun --mpi=pmix ./gpus_for_tasks
```

Output:

```console
[shahzeb.siddiqui@login-02 jobs]$ cat slurm-18029175.out
Rank 0 out of 4 processes: I see 4 GPU(s).
0 for rank 0: 0000:19:00.0
1 for rank 0: 0000:2A:00.0
2 for rank 0: 0000:3B:00.0
3 for rank 0: 0000:5D:00.0
Rank 1 out of 4 processes: I see 4 GPU(s).
0 for rank 1: 0000:19:00.0
1 for rank 1: 0000:2A:00.0
2 for rank 1: 0000:3B:00.0
3 for rank 1: 0000:5D:00.0
Rank 3 out of 4 processes: I see 4 GPU(s).
0 for rank 3: 0000:19:00.0
1 for rank 3: 0000:2A:00.0
2 for rank 3: 0000:3B:00.0
3 for rank 3: 0000:5D:00.0
Rank 2 out of 4 processes: I see 4 GPU(s).
0 for rank 2: 0000:19:00.0
1 for rank 2: 0000:2A:00.0
2 for rank 2: 0000:3B:00.0
3 for rank 2: 0000:5D:00.0
```

As you can see from the output, we have 4 tasks running on a single node and each task can see all 4 GPUs. We can see 
that a total of 128 CPUs were allocated with 4 tasks with `CPUs/Task=32` which was honored by slurm when we used `-c 32` 

```console
[shahzeb.siddiqui@login-02 jobs]$ scontrol show job 18029175 | grep NumCPUs
   NumNodes=1 NumCPUs=128 NumTasks=4 CPUs/Task=32 ReqB:S:C:T=0:0:*:*
```

## Topology

You can run `salloc` into a node and run `nvidia-smi topo -m` to see the GPU topology. This may be helpful
to see the node topology and how GPUs are connected to each other, which can help you understand which 
GPUs 

In example below we allocate a single node with 4 GPUs and run `nvidia-smi topo -m` to see the topology. We can see breakdown
of GPU affinity and NUMA affinity.

```console
[shahzeb.siddiqui@login-02 jobs]$ salloc -p gpu -G 4 -N 1
salloc: Pending job allocation 18029528
salloc: job 18029528 queued and waiting for resources
salloc: job 18029528 has been allocated resources
salloc: Granted job allocation 18029528
salloc: Nodes gpu-d-2 are ready for job

[shahzeb.siddiqui@gpu-d-2 jobs]$ nvidia-smi topo -m
	GPU0	GPU1	GPU2	GPU3	NIC0	NIC1	NIC2	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	NV4	NV4	NV4	NODE	NODE	NODE	0	0		N/A
GPU1	NV4	 X 	NV4	NV4	NODE	NODE	NODE	0	0		N/A
GPU2	NV4	NV4	 X 	NV4	NODE	NODE	NODE		1		N/A
GPU3	NV4	NV4	NV4	 X 	NODE	NODE	NODE		1		N/A
NIC0	NODE	NODE	NODE	NODE	 X 	PIX	PHB
NIC1	NODE	NODE	NODE	NODE	PIX	 X 	PHB
NIC2	NODE	NODE	NODE	NODE	PHB	PHB	 X

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
```

To see the numa affinity you can run `numactl -H` which will show the node and cpu affinity. We can see that CPUs 0-63 are on NUMA node 0 and CPUs 64-127 are on NUMA node 1. 

```console
[shahzeb.siddiqui@gpu-d-2 jobs]$ numactl -H
available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
node 0 size: 1019859 MB
node 0 free: 50829 MB
node 1 cpus: 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
node 1 size: 1028108 MB
node 1 free: 637513 MB
node distances:
node   0   1
  0:  10  32
  1:  32  10
```


Here is a simple program you use to see the CPU ID which we can show how the CPU affinity works. 

```c
#define _GNU_SOURCE  // Required for sched_getcpu()
#include <stdio.h>
#include <unistd.h>
#include <sched.h>

int main() {
    int cpu_id = sched_getcpu();  // Get current CPU ID
    printf("Process is running on CPU: %d\n", cpu_id);
    return 0;
}
```

You can compile this code by running the following

```console
gcc -o cpu_id cpu_id.c
```

If you run this code several times you will notice the CPU ID will be different, where this program will run on different CPUs.

```console
[shahzeb.siddiqui@login-01 jobs]$ ./cpu_id
Process is running on CPU: 97
[shahzeb.siddiqui@login-01 jobs]$ ./cpu_id
Process is running on CPU: 100
[shahzeb.siddiqui@login-01 jobs]$ ./cpu_id
Process is running on CPU: 0
[shahzeb.siddiqui@login-01 jobs]$ ./cpu_id
Process is running on CPU: 79
```

If you want to bind this to a particular CPU you can use `numactl --physcpubind` option. Note in output below the CPU ID will match the option specified by `--physcpubind`

```console
[shahzeb.siddiqui@login-01 jobs]$ numactl --physcpubind=5 ./cpu_id
Process is running on CPU: 5
[shahzeb.siddiqui@login-01 jobs]$ numactl --physcpubind=8 ./cpu_id
Process is running on CPU: 8
```

Now you can also bind to a particular numa node, recall from example above that we had 2 NUMA nodes with the following settings

- Numa Node 0: CPUs 0-63
- Numa Node 1: CPUs 64-127

If we want to bind to NUMA node 0 we can use the `--cpunodebind` option and specify the node id. Now you will see the CPU ID will be in range from 0-63

```console
[shahzeb.siddiqui@login-01 jobs]$ numactl --cpunodebind=0 ./cpu_id
Process is running on CPU: 6
[shahzeb.siddiqui@login-01 jobs]$ numactl --cpunodebind=0 ./cpu_id
Process is running on CPU: 53
[shahzeb.siddiqui@login-01 jobs]$ numactl --cpunodebind=0 ./cpu_id
Process is running on CPU: 47
```

Likewise, if we want to bind to NUMA node 1 we can use the `--cpunodebind` option and specify the node id. Now you will see the CPU ID will be in range from 64-127

```console
[shahzeb.siddiqui@login-01 jobs]$ numactl --cpunodebind=1 ./cpu_id
Process is running on CPU: 90
[shahzeb.siddiqui@login-01 jobs]$ numactl --cpunodebind=1 ./cpu_id
Process is running on CPU: 113
[shahzeb.siddiqui@login-01 jobs]$ numactl --cpunodebind=1 ./cpu_id
Process is running on CPU: 94
```

We can run this same program with `srun` and you can see the CPU ID that will be set. We will use `--cpu-bind=verbose` and you will notice that Slurm will apply a mask when setting
the CPUs.

```console
[shahzeb.siddiqui@login-01 jobs]$ srun -n4 -p cpu --cpu-bind=verbose ./cpu_id
srun: job 18030922 queued and waiting for resources
srun: job 18030922 has been allocated resources
cpu-bind=MASK - cpu-b-4, task  0  0 [1282813]: mask 0x800000000000000000000000000 set
cpu-bind=MASK - cpu-b-4, task  1  1 [1282814]: mask 0x20000000000000000000000000000000 set
cpu-bind=MASK - cpu-b-4, task  2  2 [1282815]: mask 0x40000000000000000000000000000000 set
cpu-bind=MASK - cpu-b-4, task  3  3 [1282816]: mask 0x80000000000000000000000000000000 set
Process is running on CPU: 125
Process is running on CPU: 126
Process is running on CPU: 127
Process is running on CPU: 107
```