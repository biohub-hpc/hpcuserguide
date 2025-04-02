# Understanding Job Priority

## What is Job Priority in Slurm?

In Slurm, job priority determines the order in which pending jobs are scheduled to run on the cluster. 
When you submit a job, it doesn’t start immediately if resources 
(like CPUs, GPUs, or memory) are already in use. Instead, it enters a queue,
and Slurm’s scheduler decides when it runs based on its priority. Higher-priority jobs 
get scheduled before lower-priority ones, assuming the required resources are available. 
Understanding your job’s priority can help you predict when it might start and adjust your
submission strategy if needed.

Priority isn’t just about who submitted first—it’s a calculated score influenced by 
multiple factors set by the system administrator. These factors include how long your 
job has been waiting, your usage history, the partition you’re submitting to, and more.
Our cluster uses a **backfill scheduler**, a variation of first-in, first-out (FIFO) 
scheduling. This means jobs generally run in submission order, but lower-priority 
jobs can “backfill” and start earlier if they won’t delay higher-priority ones. 
Knowing your job’s priority helps you understand its place in this dynamic queue.

Slurm calculates priority using a weighted formula, combining elements like:

**Age**: How long your job has been pending.
**Fair-share**: Your usage compared to others (to ensure equitable resource access).
**Partition**: The priority tier of the partition you submit to (e.g., `interactive` vs. `cpu`).
**Job Size**: The resources your job requests (e.g., number of nodes or CPUs).
**QoS**: Quality of Service settings, if applied.
You can check your job’s priority with tools likes `sprio` and `squeue`, as shown later in this guide. 
The system administrator configures these weights and partition priorities in 
`/etc/slurm/slurm.conf`, so they may differ across clusters.

## sprio: Viewing Job Priority

The `sprio` command can be used to view the priority of a job.

Let's first see the liust of priority weights which can be shown using the `-w` option.


```console
[shahzeb.siddiqui@login-01 ~]$ sprio -w
          JOBID PARTITION   PRIORITY       SITE        AGE  FAIRSHARE    JOBSIZE  PARTITION        QOS
        Weights                               1      10000      10000      10000     100000     200000
```

The system adminstrator will typically set these priority weights in `/etc/slurm/slurm.conf`. Each partition
has a priority and priority tier. Jobs submitted to partition in higher priority tier will be evalued
by scheduler before pending jobs in partition with lower priority tier.

You can run `scontrol show partition` to see partition configuration. You will see a value
`PriorityTier` and `PriorityJobFactor` for each partition. Higher the value, means the 
partition has higher priority which contributes to the overall job priority.

```console
[shahzeb.siddiqui@login-01 ~]$ scontrol show partition
PartitionName=cpu
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=YES QoS=N/A
   DefaultTime=1-00:00:00 DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=180-00:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
   NodeSets=cpu
   Nodes=cpu-a-[1-2],cpu-b-[1-6],cpu-e-1,cpu-f-[1-2],cpu-g-[1-2]
   PriorityJobFactor=1000 PriorityTier=1000 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=REQUEUE
   State=UP TotalCPUs=1472 TotalNodes=13 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerCPU=8000 MaxMemPerNode=UNLIMITED
   TRES=cpu=1472,mem=24552361M,node=13,billing=1472

PartitionName=gpu
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=1-00:00:00 DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=180-00:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
   NodeSets=gpu
   Nodes=gpu-a-[1-4],gpu-b-[1-6],gpu-c-1,gpu-d-[1-2],gpu-f-[1-6],gpu-g-[1-2],gpu-h-[1-8]
   PriorityJobFactor=1000 PriorityTier=1000 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=REQUEUE
   State=UP TotalCPUs=3104 TotalNodes=29 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerCPU=8000 MaxMemPerNode=UNLIMITED
   TRES=cpu=3104,mem=47992314M,node=29,billing=3104,gres/gpu=176

PartitionName=interactive
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=interactive
   DefaultTime=1-00:00:00 DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=180-00:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
   NodeSets=interactive
   Nodes=cpu-c-[1-4],gpu-e-[1-8],gpu-sm01-[01-20],gpu-sm02-[01-20]
   PriorityJobFactor=2000 PriorityTier=2000 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=UNLIMITED PreemptMode=REQUEUE
   State=UP TotalCPUs=864 TotalNodes=52 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerCPU=15000 MaxMemPerNode=UNLIMITED
   TRES=cpu=864,mem=14480000M,node=52,billing=864,gres/gpu=48

PartitionName=dtn
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=dtn
   DefaultTime=1-00:00:00 DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=180-00:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=32 MaxCPUsPerSocket=UNLIMITED
   NodeSets=dtn
   Nodes=login-[01-02]
   PriorityJobFactor=20000 PriorityTier=20000 RootOnly=NO ReqResv=NO OverSubscribe=FORCE:4
   OverTimeLimit=NONE PreemptMode=REQUEUE
   State=UP TotalCPUs=512 TotalNodes=2 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerCPU=4000 MaxMemPerNode=UNLIMITED
   TRES=cpu=512,mem=2063728M,node=2,billing=512

PartitionName=preempted
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=1-00:00:00 DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=30 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=2-00:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
   NodeSets=cpu,gpu,interactive
   Nodes=cpu-a-[1-2],cpu-b-[1-6],cpu-c-[1-4],cpu-e-1,cpu-f-[1-2],cpu-g-[1-2],gpu-a-[1-4],gpu-b-[1-6],gpu-c-1,gpu-d-[1-2],gpu-e-[1-8],gpu-f-[1-6],gpu-g-[1-2],gpu-h-[1-8],gpu-sm01-[01-20],gpu-sm02-[01-20]
   PriorityJobFactor=1 PriorityTier=1 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=REQUEUE
   State=UP TotalCPUs=5440 TotalNodes=94 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerCPU=8000 MaxMemPerNode=UNLIMITED
   TRES=cpu=5440,mem=87024675M,node=94,billing=5440,gres/gpu=224

PartitionName=preview
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=1-00:00:00 DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=180-00:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
   NodeSets=preview
   Nodes=cpu-vm-[1-2]
   PriorityJobFactor=1 PriorityTier=1 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=REQUEUE
   State=UP TotalCPUs=16 TotalNodes=2 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerCPU=8000 MaxMemPerNode=UNLIMITED
   TRES=cpu=16,mem=250G,node=2,billing=16
```

To see job priority by partition you can use `-p` option and specify the partition name.
Shown below is job priority for each job in column name `PRIORITY`. 

```
[shahzeb.siddiqui@login-01 ~]$ sprio -p cpu
          JOBID PARTITION   PRIORITY       SITE        AGE  FAIRSHARE    JOBSIZE  PARTITION        QOS
       18598418 cpu             5120          0          0         12        109       5000          0
       18611663 cpu             5252          0        132         12        109       5000          0
       18622601 cpu             5679          0          0        615         64       5000          0
       18622778 cpu             5681          0          2        615         64       5000          0
```

You can see a normalized priority value using the `-n` option which shows value between `0-1`

```console
[shahzeb.siddiqui@login-01 ~]$ sprio -p cpu -n
          JOBID PARTITION PRIORITY   AGE        FAIRSHARE  JOBSIZE    PARTITION  QOS
       18598418 cpu       0.00000119 0.0000000  0.0011834  0.0108683  0.0500000  0.0000000
       18611663 cpu       0.00000122 0.0131705  0.0011834  0.0108683  0.0500000  0.0000000
       18622601 cpu       0.00000132 0.0000000  0.0615385  0.0064239  0.0500000  0.0000000
       18622778 cpu       0.00000132 0.0002001  0.0615385  0.0064239  0.0500000  0.0000000
```


If you want to view job priority for pending jobs, you can specify via `squeue` using the 
the `-t pd` for all pending jobs with `-p <partition>` name for the desired partition. The `-o`
for output field can be used with `%p` to show priority.

Shown below is an example output for pending jobs in `interactive` partition.

```console
[shahzeb.siddiqui@login-01 ~]$ squeue -p interactive -t pd -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %p"
             JOBID PARTITION     NAME     USER ST       TIME  NODES PRIORITY
          17640995 interacti "seqbotv svc.seqb PD       0:00      1 0.00004910537974
          18372817 interacti ghw-enga gibraan. PD       0:00      1 0.00000255298801
          18372816 interacti ghw-scan gibraan. PD       0:00      1 0.00000255298801
          18576234 interacti OD_noVNC   yue.yu PD       0:00      1 0.00000239559449
          18576042 interacti OD_noVNC   yue.yu PD       0:00      1 0.00000239559449
```


