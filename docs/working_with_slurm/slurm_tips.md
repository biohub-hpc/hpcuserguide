# Slurm Tips

This document provides tips and tricks for using Slurm effectively.

## Setting Time Limit

By default, we have a default time set for all jobs, we recommend you specify the time limit `sbatch -t` to best align with your workload. The default time
is 24hrs and this may not make sense if your job is expected to run for a few minutes. Slurm can schedule your job faster if you specify a more realistic timelimit.

As you can see a sleep job for 60sec with no timelimit will take the default timelimit of `TimeLimit=1-00:00:00` which is 24hrs. 

```console
[shahzeb.siddiqui@login-02 ~]$ sbatch -N 1 -p cpu --wrap="sleep 60"
Submitted batch job 18643594
[shahzeb.siddiqui@login-02 ~]$ scontrol show job 18643594 | grep TimeLimit
   RunTime=00:01:00 TimeLimit=1-00:00:00 TimeMin=N/A
```   

You can certainly improve this by specifying a timelimit of 5min and Slurm will honor your request

```console
[shahzeb.siddiqui@login-02 ~]$ sbatch -N 1 -p cpu -t 5 --wrap="sleep 60"
Submitted batch job 18643601
[shahzeb.siddiqui@login-02 ~]$ scontrol show job 18643601 | grep TimeLimit
   RunTime=00:00:09 TimeLimit=00:05:00 TimeMin=N/A
```

## Dont want to wait in queue, find idle node

Sometimes you might want to find any idle node to run your job. You can use `sinfo` command to find idle nodes. Shown below is a summarized list of all
idle nodes across the partitions. The column `Nodes(A/I/O/T)` shows the number of nodes in the partition and the `I` refers to the number of idle nodes. You can
quickly determine that the `gpu` partition has 4 idle nodes with nodes `gpu-b-5,gpu-h-[2-3,5]`, however the nodes `gpu-h-[2-3,5]` are reserved so you cant use them

```console
[shahzeb.siddiqui@login-02 ~]$ sinfo -t idle
PARTITION   AVAIL  TIMELIMIT  NODES  STATE NODELIST
cpu*           up 180-00:00:      0    n/a
gpu            up 180-00:00:      3   resv gpu-h-[2-3,5]
gpu            up 180-00:00:      1   idle gpu-b-5
interactive    up 180-00:00:      1  drain gpu-sm02-16
interactive    up 180-00:00:      9   idle gpu-e-7,gpu-sm01-[05-06,10,13-16],gpu-sm02-18
dtn            up 180-00:00:      1  drain login-01
dtn            up 180-00:00:      1   idle login-02
preempted      up 2-00:00:00      1  drain gpu-sm02-16
preempted      up 2-00:00:00      3   resv gpu-h-[2-3,5]
preempted      up 2-00:00:00     10   idle gpu-b-5,gpu-e-7,gpu-sm01-[05-06,10,13-16],gpu-sm02-18
preview        up 180-00:00:      2   idle cpu-vm-[1-2]
```

## Want to check number of GPUs for set of nodes

You can check the node configuration using `scontrol show node` command, let's say you want to know the total number of GPUs on
each node you can run the following command. The `gres/gpu` field shows the number of GPUs on each node. Then you can add them 
together to get the total number of GPUs

```console
[shahzeb.siddiqui@login-02 ~]$ scontrol show node gpu-b-5,gpu-h-[2-3,5] | grep "gres/gpu"
   CfgTRES=cpu=64,mem=500000M,billing=64,gres/gpu=4
   CfgTRES=cpu=128,mem=2063837M,billing=128,gres/gpu=8
   CfgTRES=cpu=128,mem=2063837M,billing=128,gres/gpu=8
   CfgTRES=cpu=128,mem=2063837M,billing=128,gres/gpu=8
```