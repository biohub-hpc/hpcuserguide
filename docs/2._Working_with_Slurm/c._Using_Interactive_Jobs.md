# Interactive Jobs

There are many occasions when it's desirable to have a node or nodes for interactive use
with a specific hardware configuration. For instance, manually editing a 256GB
file in vim might work better on a node with a fast connection to the storage
and > 256 GB of memory, rather than a login node that is shared and may have
memory usage restrictions. Or you may want to start a series of
graphical applications and display them on your workstation (local, NoMachine or OnDemand desktop) while still
having fast access to the underlying storage. In these cases a straightforward
interactive shell obtained with `srun` or `salloc` is a good solution. Some examples:

```
# Simple srun session
[john.hanks@login-01 ~]$ srun --pty bash -l
[john.hanks@cpu-c-1 ~]$ exit
logout
[john.hanks@login-01 ~]$ 

# Same thing, but using salloc
[john.hanks@login-01 ~]$ salloc
salloc: Granted job allocation 40494
salloc: Waiting for resource configuration
salloc: Nodes cpu-c-1 are ready for job
[john.hanks@cpu-c-1 ~]$ exit
exit
salloc: Relinquishing job allocation 40494
salloc: Job allocation 40494 has been revoked.
[john.hanks@login-01 ~]$ 

# Using srun for a session with a specific type of GPU
[john.hanks@login-01 ~]$ srun --pty --gpus=a100:1 --partition=gpu bash -l
[john.hanks@gpu-a-3 ~]$ exit
logout
[john.hanks@login-01 ~]$ 

# salloc with a generic gpu request.
[john.hanks@login-01 ~]$ salloc --gpus=1 --partition=interactive
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
[john.hanks@login-01 ~]$ srun --pty --partition=gpu --gpus=1 --x11 glxgears
3713 frames in 5.0 seconds = 742.472 FPS
2071 frames in 5.0 seconds = 413.784 FPS
746 frames in 5.0 seconds = 149.094 FPS
793 frames in 5.0 seconds = 158.556 FPS

```

