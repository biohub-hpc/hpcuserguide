# Job Management

## OnDemand

[OnDemand](https://ondemand.czbiohub.org) includes a jobs app which can be used
to manage and submit jobs.

## A Graphical View

SLURM includes a graphical tool which can be used to check the state of many
things associated with the scheduler. To use it you will need to be on a
NoMachine or OnDemand compute node desktop session or have support for
forwarding X applications to your local client. If forwarding to a local
client, each operating system has a different set of requirements:

### Linux

Just add -Y to your ssh command when connecting to the login nodes.

### Mac OS X

Since Mavericks you need to install
[XQuartz](http://xquartz.macosforge.org/landing/). Once XQuartz is available,
adding -Y to your ssh command should enable forwarding.

### Windows

There are many free and commercial options, one of which is
[MobaXterm](https://mobaxterm.mobatek.net/). 

 With that support enabled, simply start the viewer with

```bash
sview &
```

The sview window should appear, with the job tab open by default as shown here.
```bash
# TODO: Add screenshot of sview once we have something interesting to see.
```

## Command Line 

!!! note
    Most Slurm commands will accept `--json` or `--yaml` to produce JSON or
    YAML formatted output for use in scripts that can parse JSON or YAML data.

### `scontrol`

`scontrol` is the Swiss Army Knife of SLURM commands and can access and display
information about all aspects of the scheduler, nodes, jobs and partitions and
control them as well. Complete usage information is beyond the scope of this
wiki, please see the [`scontrol` man page](http://slurm.schedmd.com/scontrol.html)
for complete details. Some examples of `scontrol` commands/options that are
useful are given below as a handy reference.

```bash
# Place hold on job JOBID
[user@host]$ scontrol hold JOBID

# Release hold on job JOBID
[user@host]$ scontrol release JOBID

# List job details
[user@host]$ scontrol show jobid=JOBID
```

You can see list of all available nodes and their status via 

```console
scontrol show nodes
```

To see output of a specific node, you can run

```console
[shahzeb.siddiqui@login-01 ~]$ scontrol show nodes login-01
NodeName=login-01 Arch=x86_64 CoresPerSocket=64
   CPUAlloc=0 CPUEfctv=256 CPUTot=256 CPULoad=1.36
   AvailableFeatures=login,dtn,external,amd,milan
   ActiveFeatures=login,dtn,external,amd,milan
   Gres=(null)
   NodeAddr=login-01 NodeHostName=login-01 Version=24.05.4
   OS=Linux 4.18.0-553.33.1.el8_10.x86_64 #1 SMP Thu Dec 19 14:28:01 UTC 2024
   RealMemory=1031864 AllocMem=0 FreeMem=87011 Sockets=2 Boards=1
   State=IDLE ThreadsPerCore=2 TmpDisk=1000000 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=dtn
   BootTime=2025-01-29T09:38:23 SlurmdStartTime=2025-01-29T09:49:10
   LastBusyTime=2025-02-03T15:20:44 ResumeAfterTime=None
   CfgTRES=cpu=256,mem=1031864M,billing=256
   AllocTRES=
   CurrentWatts=0 AveWatts=0
```

Note you can see multiple nodes using bracket notation so if you want to see both login nodes you can run

```console
scontrol show nodes login-[01-02]
```

### squeue

`squeue` can be used to get information about jobs and queues in a way that can
be further manipulated with scripts or other tools or just in a human readable
format. The [`squeue` man page](http://slurm.schedmd.com/squeue.html) has more
information, some usage examples are shown below.

To list all jobs:

```bash
squeue
```
If you want to view your jobs you can run either of the following commands:

```bash
squeue -u $USER

squeue --me
```

To see all pending jobs for current user:

```bash
squeue --me -t PENDING
```

To see all running jobs for current user:

```bash
squeue --me -t RUNNING
```

To get more detailed information about a job:

```bash
squeue -j JOBID

# Extra detail for job JOBID
squeue -l -j JOBID
```

View multiple jobs at once:
```bash
squeue -j JOBID1,JOBID2,JOBID3
```

To see all jobs pending on `cpu` partition

```bash
squeue -p cpu -t PENDING
```

To see all nodes allocated to user jobs you can run

```bash
squeue -u $USER -o "%N"
```

### sacct

The `sacct` command is used to view accounting information about jobs which can be really useful for viewing historical data.

You can view the job history for current user by running `sacct`. Shown below is an example output

```console
[shahzeb.siddiqui@login-01 ~]$ sacct
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
17883019     interacti+    preview    default          1  COMPLETED      0:0
17883019.in+ interacti+               default          1  COMPLETED      0:0
17883019.ex+     extern               default          1  COMPLETED      0:0
17885870     interacti+    preview    default          1  COMPLETED      0:0
```
    

You can format columns as you wish using the ```--format``` option. 
For example, we can format columns based on **User** **JobName** **State** and **Submit** as follows

```console
[shahzeb.siddiqui@login-01 ~]$  sacct --format=User,JobName,State,Submit
     User    JobName      State              Submit
--------- ---------- ---------- -------------------
shahzeb.+ interacti+  COMPLETED 2025-02-03T13:11:15
          interacti+  COMPLETED 2025-02-03T13:11:15
              extern  COMPLETED 2025-02-03T13:11:15
shahzeb.+ interacti+  COMPLETED 2025-02-03T13:37:31
          interacti+  COMPLETED 2025-02-03T13:37:31
              extern  COMPLETED 2025-02-03T13:37:31
```

We can retrieve historical data for any given user. For example if you want
to filter jobs by Start Time `2025-01-20` and End Time `2025-01-21` for current user 
you can do the following

```console
[shahzeb.siddiqui@login-01 ~]$ sacct -u $USER -S 2025-01-20 -E 2025-01-21
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
[shahzeb.siddiqui@login-01 ~]$ sacct -u $USER -S 2025-01-20 -E 2025-01-22
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
17604621     interacti+        gpu    default          1  COMPLETED      0:0
17604621.in+ interacti+               default          1  COMPLETED      0:0
17604621.ex+     extern               default          1  COMPLETED      0:0
17604622     interacti+        gpu    default          1  COMPLETED      0:0
17604622.in+ interacti+               default          1  COMPLETED      0:0
17604622.ex+     extern               default          1  COMPLETED      0:0
17604623     interacti+        gpu    default          0     FAILED      1:0
17604624     interacti+        gpu    default          0 CANCELLED+      0:0
17604625     interacti+        gpu    default          1  COMPLETED      0:0
17604625.in+ interacti+               default          1  COMPLETED      0:0
17604625.ex+     extern               default          1  COMPLETED      0:0
17604626     interacti+        gpu    default          0 CANCELLED+      0:0
```

To query by job states, use the option `-s` (or long option `--state`) plus 
the abbreviated state name code. For complete list of job states and their
codes, see the [JOB STATE CODES](https://slurm.schedmd.com/sacct.html#lbAG) section
in the sacct manual. In the example below we query for all failed jobs. The start 
and end window to your query, indicated by the `--start` and `--end` options, are
required arguments.

Shown below are the failed jobs for current user between start time `2025-01-01` and current time.

```console
[shahzeb.siddiqui@login-01 ~]$ sacct -X --format=User,JobName,State -s f --start=2025-01-01 --end=now
     User    JobName      State
--------- ---------- ----------
shahzeb.+ interacti+     FAILED
shahzeb.+ nvidia-smi     FAILED
shahzeb.+ nvidia-sm+     FAILED
shahzeb.+ nvidia-sm+     FAILED
shahzeb.+       bash     FAILED
shahzeb.+ nvidia-smi     FAILED
shahzeb.+ nvidia-smi     FAILED
shahzeb.+ nvidia-smi     FAILED
shahzeb.+ nvidia-smi     FAILED
shahzeb.+     h100:1     FAILED
shahzeb.+ nvidia-smi     FAILED
```


To filter output by JobID, you can specify the `-j` option with a list
of comma-separated job IDs

```console
[shahzeb.siddiqui@login-01 ~]$ sacct -j 17604623,17757942
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
17604623     interacti+        gpu    default          0     FAILED      1:0
17757942     nvidia-smi        gpu    default          1     FAILED      2:0
17757942.ex+     extern               default          1  COMPLETED      0:0
17757942.0   nvidia-smi               default          1     FAILED      2:0
```

### sinfo

The `sinfo` is a slurm command used to display information about nodes and partitions in the cluster. The command below can be used
to show all available partitions and their status

```console
[shahzeb.siddiqui@login-01 ~]$ sinfo
PARTITION   AVAIL  TIMELIMIT  NODES  STATE NODELIST
cpu*           up 180-00:00:      2  down* cpu-f-[1-2]
cpu*           up 180-00:00:      5    mix cpu-b-[2-3,5-6],cpu-g-1
cpu*           up 180-00:00:      1  alloc cpu-b-1
cpu*           up 180-00:00:      5   idle cpu-a-[1-2],cpu-b-4,cpu-e-1,cpu-g-2
gpu            up 180-00:00:     14    mix gpu-a-[1-3],gpu-b-[1-3],gpu-d-[1-2],gpu-f-[1,3],gpu-g-[1-2],gpu-h-[1,8]
gpu            up 180-00:00:      2  alloc gpu-a-4,gpu-b-4
gpu            up 180-00:00:     12   idle gpu-b-[5-6],gpu-c-1,gpu-f-[2,4-6],gpu-h-[2-6]
interactive    up 180-00:00:      6  drng@ gpu-sm01-[09,11,13-15,18]
interactive    up 180-00:00:      1   drng gpu-sm01-08
interactive    up 180-00:00:      5    mix cpu-c-[1-3],gpu-sm01-[01,20]
interactive    up 180-00:00:     17  alloc gpu-e-[2-4,7],gpu-sm01-[02-03,07,10,12,16,19],gpu-sm02-[01-03,11,14,20]
interactive    up 180-00:00:     23   idle cpu-c-4,gpu-e-[1,5-6,8],gpu-sm01-[04-06,17],gpu-sm02-[04-10,12-13,15-19]
dtn            up 180-00:00:      2   idle login-[01-02]
preempted      up 2-00:00:00      6  drng@ gpu-sm01-[09,11,13-15,18]
preempted      up 2-00:00:00      2  down* cpu-f-[1-2]
preempted      up 2-00:00:00      1   drng gpu-sm01-08
preempted      up 2-00:00:00     24    mix cpu-b-[2-3,5-6],cpu-c-[1-3],cpu-g-1,gpu-a-[1-3],gpu-b-[1-3],gpu-d-[1-2],gpu-f-[1,3],gpu-g-[1-2],gpu-h-[1,8],gpu-sm01-[01,20]
preempted      up 2-00:00:00     20  alloc cpu-b-1,gpu-a-4,gpu-b-4,gpu-e-[2-4,7],gpu-sm01-[02-03,07,10,12,16,19],gpu-sm02-[01-03,11,14,20]
preempted      up 2-00:00:00     40   idle cpu-a-[1-2],cpu-b-4,cpu-c-4,cpu-e-1,cpu-g-2,gpu-b-[5-6],gpu-c-1,gpu-e-[1,5-6,8],gpu-f-[2,4-6],gpu-h-[2-6],gpu-sm01-[04-06,17],gpu-sm02-[04-10,12-13,15-19]
preview        up 180-00:00:      1    mix cpu-vm-1
preview        up 180-00:00:      1   idle cpu-vm-2
```

If you want to filter by a partition name, you can run

```console
[shahzeb.siddiqui@login-01 ~]$ sinfo -p cpu
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
cpu*         up 180-00:00:      2  down* cpu-f-[1-2]
cpu*         up 180-00:00:      5    mix cpu-b-[2-3,5-6],cpu-g-1
cpu*         up 180-00:00:      1  alloc cpu-b-1
cpu*         up 180-00:00:      5   idle cpu-a-[1-2],cpu-b-4,cpu-e-1,cpu-g-2
```

To see all idle nodes by partition name `cpu` you can run the following, the **STATE** field indicates the state of the node that are idle

```console
[shahzeb.siddiqui@login-01 ~]$ sinfo -p cpu -t idle
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
cpu*         up 180-00:00:      5   idle cpu-a-[1-2],cpu-b-4,cpu-e-1,cpu-g-2
```

If job doesnt run on a particular node, you may see node in **DOWN** which can be seen if you run

```console
[shahzeb.siddiqui@login-01 ~]$ sinfo -t down
PARTITION   AVAIL  TIMELIMIT  NODES  STATE NODELIST
cpu*           up 180-00:00:      2  down* cpu-f-[1-2]
gpu            up 180-00:00:      0    n/a
interactive    up 180-00:00:      0    n/a
dtn            up 180-00:00:      0    n/a
preempted      up 2-00:00:00      2  down* cpu-f-[1-2]
preview        up 180-00:00:      0    n/a
```

You can use the `sinfo -o` option to filter the output by specific columns. The command below will show nodes by state along with CPU count
and Memory. 

Shown below is summary of few of the options

- `%P` → Partition Name
- `%D` → Number of Nodes
- `%N` → Node List
- `%t` → Node State
- `%C` → CPU Count
- `%m` → Total Memory

```console
[shahzeb.siddiqui@login-01 ~]$ sinfo -o "%P %D %N %t %C %m"
PARTITION NODES NODELIST STATE CPUS(A/I/O/T) MEMORY
cpu* 2 cpu-f-[1-2] down* 0/0/64/64 750000
cpu* 5 cpu-b-[2-3,5-6],cpu-g-1 mix 314/326/0/640 1024000+
cpu* 1 cpu-b-1 alloc 128/0/0/128 1024000
cpu* 5 cpu-a-[1-2],cpu-b-4,cpu-e-1,cpu-g-2 idle 0/640/0/640 1024000+
gpu 12 gpu-a-[1-2],gpu-b-[1-3],gpu-d-1,gpu-f-[1,3],gpu-g-[1-2],gpu-h-[1,8] mix 519/665/0/1184 500000+
gpu 2 gpu-a-4,gpu-b-4 alloc 192/0/0/192 500000+
gpu 14 gpu-a-3,gpu-b-[5-6],gpu-c-1,gpu-d-2,gpu-f-[2,4-6],gpu-h-[2-6] idle 0/1600/0/1600 500000+
interactive 6 gpu-sm01-[09,11,13-15,18] drng@ 96/0/0/96 250000
interactive 1 gpu-sm01-08 drng 16/0/0/16 250000
interactive 5 cpu-c-[1-3],gpu-sm01-[01,20] mix 50/54/0/104 120000+
interactive 17 gpu-e-[2-4,7],gpu-sm01-[02-03,07,10,12,16,19],gpu-sm02-[01-03,11,14,20] alloc 272/0/0/272 250000+
interactive 23 cpu-c-4,gpu-e-[1,5-6,8],gpu-sm01-[04-06,17],gpu-sm02-[04-10,12-13,15-19] idle 0/376/0/376 120000+
dtn 2 login-[01-02] idle 0/512/0/512 1031864
preempted 6 gpu-sm01-[09,11,13-15,18] drng@ 96/0/0/96 250000
preempted 2 cpu-f-[1-2] down* 0/0/64/64 750000
preempted 1 gpu-sm01-08 drng 16/0/0/16 250000
preempted 22 cpu-b-[2-3,5-6],cpu-c-[1-3],cpu-g-1,gpu-a-[1-2],gpu-b-[1-3],gpu-d-1,gpu-f-[1,3],gpu-g-[1-2],gpu-h-[1,8],gpu-sm01-[01,20] mix 883/1045/0/1928 120000+
preempted 20 cpu-b-1,gpu-a-4,gpu-b-4,gpu-e-[2-4,7],gpu-sm01-[02-03,07,10,12,16,19],gpu-sm02-[01-03,11,14,20] alloc 592/0/0/592 250000+
preempted 42 cpu-a-[1-2],cpu-b-4,cpu-c-4,cpu-e-1,cpu-g-2,gpu-a-3,gpu-b-[5-6],gpu-c-1,gpu-d-2,gpu-e-[1,5-6,8],gpu-f-[2,4-6],gpu-h-[2-6],gpu-sm01-[04-06,17],gpu-sm02-[04-10,12-13,15-19] idle 0/2616/0/2616 120000+
preview 1 cpu-vm-1 mix 1/7/0/8 128000
preview 1 cpu-vm-2 idle 0/8/0/8 128000
```
