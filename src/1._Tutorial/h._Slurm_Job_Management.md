# Job Management

## OnDemand

[OnDemand](https://ondemand.czbiohub.org) includes a jobs app which can be used to manage and submit jobs.

## A Graphical View

SLURM includes a graphical tool which can be used to check the state of many things associated with the scheduler. To use it you will need to be on a NoMachine or OnDemand compute node desktop session or have support for forwarding X applications to your local client. If forwarding to a local client, each operating system has a different set of requirements:

- Linux: Just add -Y to your ssh command when connecting to the login nodes.
- Mac OS X: Since Mavericks you need to install
  [XQuartz](http://xquartz.macosforge.org/landing/). Once XQuartz is available,
  adding -Y to your ssh command should enable forwarding.
- Windows: There are many free and commercial options, one of which is
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
information, some usage examples are shown below:

```bash
# List all jobs
[user@host]$ squeue

# List my jobs
[user@host]$ squeue -u $USER

# Details for job JOBID
[user@host]$ squeue -j JOBID

# Extra detail for job JOBID
[user@host]$ squeue -l -j JOBID

```
