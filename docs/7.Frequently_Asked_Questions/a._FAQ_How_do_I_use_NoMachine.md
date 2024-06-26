---
title: How do I use NoMachine?
description: 
published: true
date: 2024-06-26T16:00:54.471Z
tags: 
editor: markdown
dateCreated: 2024-06-26T16:00:54.471Z
---

# How do I use NoMachine?

## NoMachine Client
The first step to using NoMachine is to get and install the NoMachine
Enterprise Desktop Client, which can be downloaded at [NoMachine Enterprise
Client](https://www.nomachine.com/product&p=NoMachine%20Enterprise%20Client).

!!! warning "Network restrictions"
    The NoMachine servers are only visible from on-site, with a VPN connection
    or via some advanced SSH tunneling.

The long term goal is to have our NoMachine nodes integrated into OnDemand, but
at the current time that is a work in progress. 

## Reserving a Node

Login nodes are open to any connection, but the `gpu-sm[01-02]-[01-20]` nodes
will require that you have a running job on the node before you are allowed to
log in to the node desktop.  To claim the node as your own, submit a job like:

```
[john.hanks@login01 ~]$ srun --exclusive --partition=gpu --gpus=a40:1 --time=8:00:00 --pty bash -l
[john.hanks@gpu-sm01-10 ~]$
```
You can then attach to the assigned node. For longer sessions, using `sbatch`
to wrap the `sleep` command will use a batch job which is not subject to the
job being lost if, for instance, the session with the `srun` were dropped or
network connection to your laptop lost. That `sbatch` would look like:

```
[john.hanks@gpu-sm01-10 ~]$ sbatch --job-name=NOMACHINE --partition=gpu --gpus=a40:1 --time=8:00:00 --exclusive  --wrap "sleep 8h"
Submitted batch job 40547
[john.hanks@gpu-sm01-10 ~]$ squeue -j 40547
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             40547       gpu NOMACHIN john.han  R       0:09      1 gpu-sm01-01
```

And the assigned node is now yours for the duration of the job.

!!! warning "Use `--exclusive`"
    Be sure to include the `--exclusive` flag, or other people will be able to
    run jobs on the node if any CPUs are available.

## Connecting to the Node

Begin by setting up an SSH tunnel to the node. Following the job submission
examples above, our node is `gpu-sm01-10` so we need to tunnel to that node via
a cluster login node, to the NX service on port 4000. In a terminal connect
with

```
   # Off-site and not on VPN, jump through login-01 or login-02
   $ ssh -J login-01 -L 24000:localhost:4000 YOUR.LOGIN@gpu-sm01-10

   # On-site or on VPN, jump through login01 or login02
   $ ssh -J login01 -L 24000:localhost:4000 YOUR.LOGIN@gpu-sm01-10
```

The `ssh` commands show here will prompt as needed to log you in and tunnel
port 24000 on your local laptop/workstation to the compute node's port 4000
where the NoMachine service is listening.

Once the tunnel is connected, create a connection in the NoMachine client with the settings:

* Host: localhost
* Port: 24000
* Protocol: NX

Note: 24000 is an arbitrary value, to connect to multiple nodes just change
that to any value between 4096 and 65535. If there is an error due to a
collision just pick another port. 

## Future

Watch the #hpc-community Slack channel for updates as we make progress on
putting a better interface around NoMachine desktop access.
