# Interactive Jobs

There are many occasions when it's desirable to have a node or nodes for interactive use
with a specific hardware configuration. For instance, manually editing a 256GB
file in vim might work better on a node with a fast connection to the storage
and > 256 GB of memory, rather than a login node that is shared and may have
memory usage restrictions. Or you may want to start a series of
graphical applications and display them on your workstation (local, NoMachine or OnDemand desktop) while still
having fast access to the underlying storage. In these cases a straightforward
interactive shell obtained with `srun` or `salloc` is a good solution. Some examples:

## Examples using salloc

### Interactive job on any available node

```console
[john.hanks@login-01 ~]$ salloc
salloc: Granted job allocation 40494
salloc: Waiting for resource configuration
salloc: Nodes cpu-c-1 are ready for job
[john.hanks@cpu-c-1 ~]$ exit
```

### Allocate 1 GPU on interactive partition

The `--gpus` option can be used to request number of GPUs.

```console
[john.hanks@login-01 ~]$ salloc --gpus=1 --partition=interactive
salloc: Granted job allocation 40496
salloc: Waiting for resource configuration
salloc: Nodes gpu-sm01-08 are ready for job
```

## Examples using srun

### 1 Node with 1 task on the `cpu` partition

```console
[shahzeb.siddiqui@login-01 ~]$ srun -N 1 -n 1 -p cpu hostname
cpu-b-6
```

### 1 Node with 4 task on the `cpu` partition
```
[shahzeb.siddiqui@login-01 ~]$ srun -N 1 -n 4 -p cpu hostname
cpu-b-3
cpu-b-3
cpu-b-3
cpu-b-3
```

### 4 node with 4 task on the `cpu` partition

```console
[shahzeb.siddiqui@login-01 ~]$ srun -N 4 -n 4 -p cpu hostname
cpu-b-3
cpu-b-2
cpu-b-4
cpu-b-5
```

In example below, we request 8 tasks on 4 nodes. Notice that **5/8 tasks** were allocated to `cpu-b-2`

```console
[shahzeb.siddiqui@login-01 ~]$ srun -N 4 -n 8 -p cpu hostname
cpu-b-2
cpu-b-4
cpu-b-3
cpu-b-5
cpu-b-2
cpu-b-2
cpu-b-2
cpu-b-2
```

If you want to control number of tasks to run on each node, you will need to use `--ntasks-per-node` option. For instance, if we
want to evenly distribute 8 tasks across 4 nodes, we need to use `--ntasks-per-node=2` which will assign 2 tasks to each node as shown
below

```console
[shahzeb.siddiqui@login-01 ~]$ srun -N 4 -n 8 --ntasks-per-node=2 -p cpu hostname
cpu-b-2
cpu-b-4
cpu-b-3
cpu-b-5
cpu-b-2
cpu-b-4
cpu-b-5
cpu-b-3
```

###Running jobs on specific nodes

The `--nodelist` option or short option `-w` can be used to specify the nodes to run the job on. This may be useful if you want
to reproduce results on same node or request a specific hardware configuration that is only available on certain nodes.

```console
[shahzeb.siddiqui@login-01 ~]$ srun -w cpu-a-1 -p cpu hostname
cpu-a-1
```

You can specify multiple nodes using the bracket notation which you typically see in output of `sinfo`. In example below
we run jobs on `cpu-a-1` and `cpu-a-2`

```console
[shahzeb.siddiqui@login-01 ~]$ srun -w cpu-a-[1-2] -p cpu hostname
cpu-a-1
cpu-a-2
```

You can specify multiple nodes via comma separated list of nodes as shown below

```console
[shahzeb.siddiqui@login-01 ~]$ srun -w cpu-a-[1-2],cpu-b-4 -p cpu hostname
cpu-a-1
cpu-a-2
cpu-b-4
```

You can specify nodes in a file and use `--nodefile` option with path to file. For example we create a file called `nodelist.txt` 
with list of nodes and run the job on those nodes as shown below

```console
[shahzeb.siddiqui@login-01 ~]$ cat nodelist.txt
cpu-a-1
cpu-a-2
cpu-b-4

[shahzeb.siddiqui@login-01 ~]$ srun --nodefile=nodelist.txt -p cpu hostname
cpu-b-4
cpu-a-1
cpu-a-2
```

### Using srun for a session with a specific type of GPU

Shown below we request access to 1 NVIDIA H100 gpu, which can be useful if you want to request a specific GPU. 

```console
[shahzeb.siddiqui@login-01 ~]$ srun --pty --gpus=h100:1 --partition=gpu bash -l
[shahzeb.siddiqui@gpu-f-3 ~]$ nvidia-smi
Mon Feb  3 14:43:29 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 565.57.01              Driver Version: 565.57.01      CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          On  |   00000000:9D:00.0 Off |                    0 |
| N/A   36C    P0             70W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

###  Using srun with GPU with X11 forwarding

This is better done by getting a NoMachine desktop on a workstation node, but
shown here just to show it works. Run an X app on a node with the display
forwarded to the submitting host. Requires X Forwarding having been set up
correctly, which may involve ssh options if trying to tunnel this back to a
desktop/laptop client.


```console
[john.hanks@login-01 ~]$ srun --pty --partition=gpu --gpus=1 --x11 glxgears
3713 frames in 5.0 seconds = 742.472 FPS
2071 frames in 5.0 seconds = 413.784 FPS
746 frames in 5.0 seconds = 149.094 FPS
793 frames in 5.0 seconds = 158.556 FPS
```

