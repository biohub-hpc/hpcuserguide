Troubleshooting Slurm Jobs
==========================

There are a number of common issues that can arise when working with Slurm. This guide will help you
identify and resolve some of the most common issues.

## Unable to allocate resources

You might run into problem with slurm job submission where its unable to allocate resources, which could be
due to a number of reasons such as node, task, memory allocation. For instance if you try allocating 3 nodes 
on `dtn` partition you will get an error 

```console
[shahzeb.siddiqui@login-02 ~]$ srun -N 3 -p dtn hostname
srun: error: Unable to allocate resources: Node count specification invalid
```

Slurm is unable to process your request because we have 2 nodes available in `dtn` partition and you are requesting 3 nodes.

```console
[shahzeb.siddiqui@login-02 ~]$ sinfo -p dtn -o "%P %D"
PARTITION NODES
dtn 2
```

Similarly, if you request more tasks available than total processor count, you will get an error. For example, if you request
**129** tasks on a single node such as `cpu-a-1` you will get an error, however if you request **128** tasks it will be successful.
We can see any node configuration using `scontrol show node <NODE>` command. The field `CPUTotal` in output of `scontrol show node`
will show total CPU count.

```console
[shahzeb.siddiqui@login-02 ~]$ sbatch -N 1 -n 129 -p cpu -w cpu-a-1 --wrap="hostname"
sbatch: error: Batch job submission failed: Requested node configuration is not available

[shahzeb.siddiqui@login-02 ~]$ sbatch -N 1 -n 128 -p cpu -w cpu-a-1 --wrap="hostname"
Submitted batch job 17895320

[shahzeb.siddiqui@login-02 ~]$ scontrol show node cpu-a-1
NodeName=cpu-a-1 Arch=x86_64 CoresPerSocket=64
   CPUAlloc=0 CPUEfctv=128 CPUTot=128 CPULoad=0.02
   AvailableFeatures=cpu,compute,largemem,amd_7h12
   ActiveFeatures=cpu,compute,largemem,amd_7h12
   Gres=(null)
   NodeAddr=cpu-a-1 NodeHostName=cpu-a-1 Version=24.05.4
   OS=Linux 4.18.0-553.33.1.el8_10.x86_64 #1 SMP Thu Dec 19 14:28:01 UTC 2024
   RealMemory=4096000 AllocMem=0 FreeMem=4028252 Sockets=2 Boards=1
   State=IDLE ThreadsPerCore=1 TmpDisk=10000000 Weight=200 Owner=N/A MCS_label=N/A
   Partitions=cpu,preempted
   BootTime=2024-12-28T19:22:18 SlurmdStartTime=2025-01-23T12:56:46
   LastBusyTime=2025-02-03T18:07:58 ResumeAfterTime=None
   CfgTRES=cpu=128,mem=4000G,billing=128
   AllocTRES=
   CurrentWatts=0 AveWatts=0
```

## Where is the slurm configuration

The slurm configuration can be found in `/etc/slurm/` directory. The main configuration files that may be of relevance are

- **/etc/slurm/nodes.conf**: Node Configuration

- **/etc/slurm/gres.conf**: Generic Resource Configuration

## Where is my output and error files, I can't find them

When you submit a job, slurm will create output and error files in the directory where you submitted the job. The output 
and error files are named `slurm-JOBID.out` and `slurm-JOBID.err` respectively. However, if you specify a custom filename 
using `--output` and `--error` options, the output and error files will be named accordingly. If you are not sure please
run `scontrol show job <JOBID>` to get the output and error file paths.

Shown below is an example output when using custom filenames with options `#SBATCH --output=simple.out` and `#SBATCH --error=simple.err`

```console
[shahzeb.siddiqui@login-02 ~]$ scontrol show job 17895323 | grep -E "StdOut|StdErr"
   StdErr=/home/shahzeb.siddiqui/simple.err
   StdOut=/home/shahzeb.siddiqui/simple.out
```

## Find available nodes in a partition

If you want to find state of available nodes at any given time for a specific partition, you should use the `sinfo` command. The `sinfo -s` 
will summarize the output and show a single entry per partition for list of Available, Idle, Other and Total nodes. This is captured in 
field `NODES(A/I/O/T)` in output of `sinfo -s` command.

```console
[shahzeb.siddiqui@login-02 ~]$ sinfo -s -p cpu,gpu
PARTITION AVAIL  TIMELIMIT   NODES(A/I/O/T) NODELIST
cpu*         up 180-00:00:         6/5/2/13 cpu-a-[1-2],cpu-b-[1-6],cpu-e-1,cpu-f-[1-2],cpu-g-[1-2]
gpu          up 180-00:00:       14/14/0/28 gpu-a-[1-4],gpu-b-[1-6],gpu-c-1,gpu-d-[1-2],gpu-f-[1-6],gpu-g-[1-2],gpu-h-[1-6,8]
```

## Why is my job not starting?

The job might not start due to a number of reasons such as resources not available, job priority, job dependencies, etc... If you know the 
jobID you should examine the column `NODELIST(REASON)`. For example in output below we see the job is pending because of `QOSMaxCpuPerUserLimit`.
According to slurm the [job reason codes](https://slurm.schedmd.com/job_reason_codes.html) the job code is the following

- **QOSMaxCpuPerUserLimit**: The job exceeds the maximum number of CPUs per user for the specified QOS.

```console
[shahzeb.siddiqui@login-02 ~]$ squeue -j 17513984
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          17513984 interacti OD_NoMac miguel.c PD       0:00      1 (QOSMaxCpuPerUserLimit)
```

Currently, this user has a total of 32 CPUs allocated on `interactive` partition.

```console
[shahzeb.siddiqui@login-02 ~]$ sacct -X -u miguel.cid-rosas -s running
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
17513978       OD_noVNC interacti+    default         16    RUNNING      0:0
17513983     OD_NoMach+ interacti+    default         16    RUNNING      0:0
```

The partition name `interactive` has a qos limit of 32 CPUs per user, which can be seen by running

```console
[shahzeb.siddiqui@login-02 ~]$ sacctmgr show qos -P interactive format=Name,MaxCPUsPerUser
Name|MaxCPUsPU
interactive|32
```

## See job start time for pending job

If you want to know when a job may start, you can look at the **START_TIME** field, this can be retrieved using the `--start` option. The job
start time may vary depending on the resources available and the job priority. Shown below is an example output, where job *17640995* is 
set to start at `2025-02-04T08:30:00`.

```console
[shahzeb.siddiqui@login-02 ~]$ squeue -j 17640995 --start
             JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES           NODELIST(REASON)
          17640995 interacti "seqbotv svc.seqb PD 2025-02-04T08:30:00      1 (null)               (BeginTime)
```

You can retrieve current date and time using `date` command to get sense of when job may start, for instance this job
will possibly start in 5 mins from now at around 8:30am .

```console
[shahzeb.siddiqui@login-02 ~]$ date +"%Y-%m-%dT%H:%M:%S"
2025-02-04T08:25:11
```