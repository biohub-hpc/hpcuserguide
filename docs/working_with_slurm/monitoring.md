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