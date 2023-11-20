# Slurm: Job Submission

Before diving into a job submission, let's stop for a moment to consider what
happens when a job is submitted to Slurm. A simplifed diagram of the basic
steps is:

```kroki-actdiag
actdiag {
  submit -> accept -> parseargs -> schedule -> assign -> run -> writeoutput -> exit -> writejobrecord -> reviewoutput

  lane user {
     label = "User"
     submit [label = "Submit Job\nsbatch, srun, salloc"];
     reviewoutput [label = "slurm-JOBID.out"];
  }
  lane slurmctld {
     label = "Slurm Controller"
     accept [label = "Accept job submission"];
     parseargs [label = "Parse job options"];
     schedule [label = "Schedule job for\nexecution"];
     assign [label = "Assign job to\nresources"];
     writejobrecord [label = "Write job record\nto accounting db"];
  }
  lane slurmd {
     label = "Slurm Node Daemon(s)";
     run [label = "Run job script on\nnodes(s)"];
     writeoutput [label = "Write stdio/stderr\nto output file"];
     exit [label = "Return script exit\ncode"];
  }
}
```

# Interactive Jobs

There are many occasions when it's desirable to have a node or nodes for interactive use
with a specific hardware configuration. For instance, manually editing a 256GB
file in vim might work better on a node with a fast connection to the storage
and > 256 GB of memory, rather than a login node that is shared and may have
memory usage restrictions. Or you may want to start a series of
graphical applications and display them on your workstation (local, NoMachine or OnDemand desktop) while still
having fast access to the underlying storage. In these cases a straightforward
interactive shell obtained with {{{srun}}} or {{{salloc}}} is a good solution. Some examples:

```
# Simple srun session
[john.hanks@login01 ~]$ srun --pty bash -l
[john.hanks@cpu-c-001 ~]$ exit
logout
[john.hanks@login01 ~]$ 

# Same thing, but using salloc
[john.hanks@login01 ~]$ salloc
salloc: Granted job allocation 40494
salloc: Waiting for resource configuration
salloc: Nodes cpu-c-001 are ready for job
[john.hanks@cpu-c-001 ~]$ exit
exit
salloc: Relinquishing job allocation 40494
salloc: Job allocation 40494 has been revoked.
[john.hanks@login01 ~]$ 

# Using srun for a session with a specific type of GPU
[john.hanks@login01 ~]$ srun --pty --gpus=a100:1 --partition=gpu bash -l
[john.hanks@gpu-a-003 ~]$ exit
logout
[john.hanks@login01 ~]$ 

# salloc with a generic gpu request.
[john.hanks@login01 ~]$ salloc --gpus=1 --partition=gpu
salloc: Granted job allocation 40496
salloc: Waiting for resource configuration
salloc: Nodes gpu-sm01-08 are ready for job
[john.hanks@gpu-sm01-08 ~]$ exit
exit
salloc: Relinquishing job allocation 40496

# This is better done by getting a NoMachine desktop on a workstation node, but
# shown here just to show it works. Run an X app on a node with the display
# forwarded to the submitting host. Requires X Forwarding having been set up
# correctly, which may involve ssh options if trying to tunnel this back to a
# desktop/laptop client.
[john.hanks@login01 ~]$ srun --pty --partition=gpu --gpus=1 --x11 glxgears
3713 frames in 5.0 seconds = 742.472 FPS
2071 frames in 5.0 seconds = 413.784 FPS
746 frames in 5.0 seconds = 149.094 FPS
793 frames in 5.0 seconds = 158.556 FPS

```

