# Container

We currently support [apptainer](https://apptainer.org/docs/user/latest/index.html) which is a container platform 
that allows one to run complex applications in a containerized environment on HPC systems. Apptainer comes a simple and 
effective security model where user can run applications in a container without needing to be a root user. This
is typically a problem with running Docker on HPC systems.

## Using Apptainer

The `apptainer` command comes with many options, shown below is the help message for `apptainer`. You will want to familiarize
yourself with the options and refer to the documentation for more information

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer --help

Linux container platform optimized for High Performance Computing (HPC) and
Enterprise Performance Computing (EPC)

Usage:
  apptainer [global options...]

Description:
  Apptainer containers provide an application virtualization layer enabling
  mobility of compute via both application and environment portability. With
  Apptainer one is capable of building a root file system that runs on any
  other Linux system where Apptainer is installed.

Options:
      --build-config    use configuration needed for building containers
  -c, --config string   specify a configuration file (for root or
                        unprivileged installation only) (default
                        "/etc/apptainer/apptainer.conf")
  -d, --debug           print debugging information (highest verbosity)
  -h, --help            help for apptainer
      --nocolor         print without color output (default False)
  -q, --quiet           suppress normal output
  -s, --silent          only print errors
  -v, --verbose         print additional information
      --version         version for apptainer

Available Commands:
  build       Build an Apptainer image
  cache       Manage the local cache
  capability  Manage Linux capabilities for users and groups
  checkpoint  Manage container checkpoint state (experimental)
  completion  Generate the autocompletion script for the specified shell
  config      Manage various apptainer configuration (root user only)
  delete      Deletes requested image from the library
  exec        Run a command within a container
  help        Help about any command
  inspect     Show metadata for an image
  instance    Manage containers running as services
  key         Manage OpenPGP keys
  keyserver   Manage apptainer keyservers
  oci         Manage OCI containers
  overlay     Manage an EXT3 writable overlay image
  plugin      Manage Apptainer plugins
  pull        Pull an image from a URI
  push        Upload image to the provided URI
  registry    Manage authentication to OCI/Docker registries
  remote      Manage apptainer remote endpoints
  run         Run the user-defined default command within a container
  run-help    Show the user-defined help for an image
  search      Search a Container Library for images
  shell       Run a shell within a container
  sif         Manipulate Singularity Image Format (SIF) images
  sign        Add digital signature(s) to an image
  test        Run the user-defined tests within a container
  verify      Verify digital signature(s) within an image
  version     Show the version for Apptainer

Examples:
  $ apptainer help <command> [<subcommand>]
  $ apptainer help build
  $ apptainer help instance start


For additional help or support, please visit https://apptainer.org/help/
```

## Running a Container 

To run a container you can use the `apptainer run` command. This command will run the container and spawn a shell within the container. 
Shown below is an example running apline container. Take note that once the image is downloaded, you are in an interactive shell **Apptainer>** 

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer run docker://alpine
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Copying blob f18232174bc9 done   |
Copying config aded1e1a5b done   |
Writing manifest to image destination
2025/02/20 06:48:22  info unpack layer: sha256:f18232174bc91741fdf3da96d85011092101a032a93a388b79e99e69c2d5c870
INFO:    Creating SIF file...
Apptainer>
```

You can run commands inside the container, for instance the command below will show the OS version of the container

```console
Apptainer> cat /etc/os-release
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.21.3
PRETTY_NAME="Alpine Linux v3.21"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
```

To exit the container, you can type `exit` or `Ctrl-D` to exit the container.

You can also pass arguments to the container which will execute the commands and exit. For example to run ``echo "hello"`` in the container you can do

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer run docker://alpine echo "hello"
INFO:    Using cached SIF image
hello
```

It's worth noting that you will be same user inside the container as you are outside the container. 
```console
[shahzeb.siddiqui@login-01 ~]$ whoami
shahzeb.siddiqui

[shahzeb.siddiqui@login-01 ~]$ apptainer run docker://alpine whoami
INFO:    Using cached SIF image
shahzeb.siddiqui
```

## Mounting Filesystems

Apptainer will mount $HOME directory in the container by default so you can access files directly. However, its worth 
noting that not all filesystems will be mounted from the host, which will need to be mounted manually. Shown below we
run `df` and `echo $HOME` which confirms that the $HOME directory is mounted in the container.

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer run docker://alpine
INFO:    Using cached SIF image
Apptainer> echo $HOME
/home/shahzeb.siddiqui
Apptainer> df -hT $HOME
Filesystem           Type            Size      Used Available Use% Mounted on
storage-home:/nvmepool/exports/home/shahzeb.siddiqui
                     nfs            32.0G     10.4G     21.6G  32% /home/shahzeb.siddiqui
```

To mount additional directories into the container, you can use the `--bind` option. For example to mount $MYDATA into the container
at `/tmp/mydata` you can run the following. We can confirm with the `df` command the directory is mounted in the container. We can
also access the files directly in the container. 


```console
[shahzeb.siddiqui@login-01 ~]$ apptainer run --bind $MYDATA:/tmp/mydata docker://alpine
INFO:    Using cached SIF image

Apptainer> df -hT /tmp/mydata/
Filesystem           Type            Size      Used Available Use% Mounted on
vast-sf.mammoth.infiniband:/mydata/shahzeb.siddiqui
                     nfs           272.8T     50.4T    222.4T  18% /tmp/mydata
                     
Apptainer> ls -l /tmp/mydata/
total 0
drwxr-xr-x    2 shahzeb.siddiqui shahzeb.siddiqui.grp      4096 Jan 28 13:07 hpc
drwxr-xr-x    2 shahzeb.siddiqui shahzeb.siddiqui.grp      4096 Jan 27 09:04 modulefiles
drwxr-xr-x    2 shahzeb.siddiqui shahzeb.siddiqui.grp      4096 Jan 31 15:33 shpc                     
```

## Interacting with images

You can interact with images, in several ways. 

For instance, if you want to pull an image locally, apptainer will download the image and convert it to SIF format (`.sif`) file which you can use
later to build or run container interactively.

In example below we pull a container image, apptainer will download image and store it in current directory.

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer pull  docker://ghcr.io/apptainer/lolcow
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Copying blob 5ca731fc36c2 done   |
Copying blob 16ec32c2132b done   |
Copying config fd0daa4d89 done   |
Writing manifest to image destination
2025/02/20 07:14:20  info unpack layer: sha256:16ec32c2132b43494832a05f2b02f7a822479f8250c173d0ab27b3de78b2f058
2025/02/20 07:14:20  info unpack layer: sha256:5ca731fc36c28789c5ddc3216563e8bfca2ab3ea10347e07554ebba1c953242e
INFO:    Creating SIF file...
```

We can confirm this file was stored in the current directory

```console
[shahzeb.siddiqui@login-01 ~]$ ls lolcow_latest.sif
lolcow_latest.sif
```

We can run the sif image directly, which is equivalent to running the container with `apptainer run` 

```console
[shahzeb.siddiqui@login-01 ~]$ ./lolcow_latest.sif
 ______________________________
< Thu Feb 20 07:17:50 PST 2025 >
 ------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

You can get an interactive shell  you can run the `apptainer shell` command given the image.

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer shell lolcow_latest.sif
Apptainer>
```

You can get an interactive shell from a remote image where apptainer will pull the image and give you an interactive shell. This
can be useful to inspect the image before running it. 

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer shell docker://python
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Copying blob d49ecfcc3fa9 done   |
Copying blob 35af2a7690f2 done   |
Copying blob 32b550be6cb6 done   |
Copying blob a492eee5e559 done   |
Copying blob 42c54e83066f done   |
Copying blob 7576b00d9bb1 done   |
Copying blob b2eee27aad58 done   |
Copying config 7398721493 done   |
Writing manifest to image destination
2025/02/20 07:30:30  info unpack layer: sha256:a492eee5e55976c7d3feecce4c564aaf6f14fb07fdc5019d06f4154eddc93fde
2025/02/20 07:30:32  info unpack layer: sha256:32b550be6cb62359a0f3a96bc0dc289f8b45d097eaad275887f163c6780b4108
2025/02/20 07:30:32  info unpack layer: sha256:35af2a7690f2b43e7237d1fae8e3f2350dfb25f3249e9cf65121866f9c56c772
2025/02/20 07:30:33  info unpack layer: sha256:7576b00d9bb10cc967bb5bdeeb3d5fa078ac8800e112aa03ed15ec199662d4f7
2025/02/20 07:30:38  info unpack layer: sha256:42c54e83066f3058aa6bf96f9730d368917d4fa5d15bb0235dc7768af82e706f
2025/02/20 07:30:38  info unpack layer: sha256:d49ecfcc3fa9333d07fc0b338de14afb43714291da4ac5f54fe6bcc4b7081d57
2025/02/20 07:30:38  info unpack layer: sha256:b2eee27aad58d8e13b37b4380b94f7525782f4aa3a0cbcc5ef7e984c6493b7b3
INFO:    Creating SIF file...
Apptainer>
```

## Cleaning up cache

Once you start using `apptainer`, you will run into quota issue in your $HOME directory if you start downloading images. To cleanup your 
cache, you can list your cache using `apptainer cache list` which will show total space used by container files and oci blobs. 

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer cache list
There are 17 container file(s) using 10.90 GiB and 176 oci blob file(s) using 11.97 GiB of space
Total space used: 22.88 GiB
```

To see a detailed list you can run `apptainer cache list --verbose` which will show you the list of files and blobs. The 
apptainer cache is located in `~/.apptainer/cache` directory as shown below. We can see that the cache is taking up 23G of space, using the
`du` command

```console
[shahzeb.siddiqui@login-01 ~]$ du -sh  ~/.apptainer/cache/
23G	/home/shahzeb.siddiqui/.apptainer/cache/

[shahzeb.siddiqui@login-01 ~]$ ls ~/.apptainer/cache/
blob  library  net  oci-tmp  oras  shub
```

To clean the cache you can run `apptainer cache clean`, press `y` to confirm the deletion.

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer cache clean
This will delete everything in your cache (containers from all sources and OCI blobs).
Hint: You can see exactly what would be deleted by canceling and using the --dry-run option.
Do you want to continue? [y/N] y
INFO:    Removing blob cache entry: blobs
INFO:    Removing blob cache entry: index.json
INFO:    Removing blob cache entry: oci-layout
INFO:    No cached files to remove at /home/shahzeb.siddiqui/.apptainer/cache/library
INFO:    Removing oci-tmp cache entry: 00e361db49c070bfc80f455b3b7e783d257919ecb8dfe1ef5a1968eac62c2604
INFO:    Removing oci-tmp cache entry: 096246eb1714cda9110e2f61f41e6624338f3c0d16c89b8219ba6b3607d96e29
INFO:    Removing oci-tmp cache entry: 0fa1d0405cacc24a7d4f45af968ff154709fb873368e38032b80ffbb4c8037db
INFO:    Removing oci-tmp cache entry: 1123a1808db091c023d54d09234fb20a712c70d0716306c7047b4de1ecc467bc
INFO:    Removing oci-tmp cache entry: 64a87d8d0bf2ae37aa71d1a11c156e72565f1697c6d28c2d887625c7d7555938
INFO:    Removing oci-tmp cache entry: 71a648707cf2dfcc3d062a2765dc0e603ac24b1c84c5e26d4c364e4eaaac104b
INFO:    Removing oci-tmp cache entry: a214cd6ee7d01432425d5f151326f9855aed0b7590bbfbf5f1b5395cf41ba3cc
INFO:    Removing oci-tmp cache entry: a7bbd60f2b76dd04450697e73a80512a162c2654bf4e9cb74b9a042a9a69009d
INFO:    Removing oci-tmp cache entry: a98a1f658fd61f889887693e7b4d2e1c726a6633ec2d3e1d63f81c86104d0621
INFO:    Removing oci-tmp cache entry: b0358a1f13c01c1ca1fa9c30c7584ec2e57968145b3c07cebc10c1d1f24d45cd
INFO:    Removing oci-tmp cache entry: b365e222c78bde12c678af91c2a7a6793cd48458e9bba4daf46cf8e785693d8b
INFO:    Removing oci-tmp cache entry: b40121acccd4c8ee538f8aee9802f5cf5f428412655030fc5aec0ea8ed98e545
INFO:    Removing oci-tmp cache entry: c380dadb737cc258013e68b1dfd4f641e33c83f5a1ce8104861372dec6eb696a
INFO:    Removing oci-tmp cache entry: cad21926724ff9eb35f711b9a5ff27e1c96c58cef892cb0b8d9bf84d7f54e74e
INFO:    Removing oci-tmp cache entry: d7babcb0490097c125efc7475206e452079afe12db4d5831fabc6b03f7854db0
INFO:    Removing oci-tmp cache entry: e1f7f5ebce0e1ece861cb00f9b6c9d9433fd807212384c117f2a44012e43a72d
INFO:    Removing oci-tmp cache entry: fd6eb4659806524b923e4b144f70d6d425d293d17bc3a0fb699ab9fd994e0f25
INFO:    No cached files to remove at /home/shahzeb.siddiqui/.apptainer/cache/shub
INFO:    No cached files to remove at /home/shahzeb.siddiqui/.apptainer/cache/oras
INFO:    No cached files to remove at /home/shahzeb.siddiqui/.apptainer/cache/net
```

Upon completion, you can confirm the cache is empty by running `apptainer cache list` and `du` command. 
This will help recover space in your $HOME directory.

```console
[shahzeb.siddiqui@login-01 ~]$ apptainer cache list
There are 0 container file(s) using 0.00 KiB and 0 oci blob file(s) using 0.00 KiB of space
Total space used: 0.00 KiB

[shahzeb.siddiqui@login-01 ~]$ du -sh ~/.apptainer/cache/
97K	/home/shahzeb.siddiqui/.apptainer/cache/
```

## Running a pytorch container with GPU support

In this example, we will show how to run a batch job using a pytorch container with GPU support. To get started we will 
pull the pytorch container locally by running 

```console
apptainer pull docker://pytorch/pytorch:latest
```

Once this is complete you should see a `pytorch_latest.sif` file in your current directory

```console
[shahzeb.siddiqui@login-01 pytorch]$ ls -l pytorch_latest.sif
-rwxr-xr-x 1 shahzeb.siddiqui shahzeb.siddiqui.grp 3651129344 Feb 20 08:30 pytorch_latest.sif
```

For this example, we have a python script `list_gpus.py` that will list the available GPUs using the `pytorch` program

```python
import torch
print('PyTorch Version:', torch.__version__)
print('Available GPUs:', torch.cuda.device_count())
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f'GPU {i}:', torch.cuda.get_device_name(i))
else:
    print('No GPU detected!')
```
 
Shown below is the slurm job script, we will request with 1GPU and run `nvidia-smi` inside the container. Note we will
use `apptainer exec --nv`, the `--nv` flag enables NVIDIA GPU support inside the container. Please refer to
https://apptainer.org/docs/user/latest/gpu.html# for more information on running containers with GPU support. 

The next command `apptainer exec --nv ./pytorch_latest.sif python list_gpus.py` will run the python script inside the container.

```bash
[shahzeb.siddiqui@login-01 pytorch]$ cat pytorch.slurm
#!/bin/bash
#SBATCH --job-name=pytorch_container_test
#SBATCH --partition=gpu              # Change to your GPU partition
#SBATCH --gres=gpu:1                 # Request 1 GPU
#SBATCH --cpus-per-task=4            # Request 4 CPU cores
#SBATCH --mem=16G                    # Request 16GB RAM
#SBATCH --time=00:30:00              # Set max runtime to 30 min
#SBATCH --output=pytorch_test.log    # Output log file

echo "Starting PyTorch Container on GPU..."
echo "Checking NVIDIA GPUs inside the container:"

# Run NVIDIA SMI inside the container
apptainer exec --nv ./pytorch_latest.sif nvidia-smi

# Run Python inside the container to list available GPUs
apptainer exec --nv ./pytorch_latest.sif python list_gpus.py
```

We can run the script using `sbatch` command

```console
[shahzeb.siddiqui@login-01 pytorch]$ sbatch pytorch.slurm
Submitted batch job 18095244
```

Shown below is the expected output

```console
[shahzeb.siddiqui@login-01 pytorch]$ cat pytorch_test.log
Starting PyTorch Container on GPU...
Checking NVIDIA GPUs inside the container:
Thu Feb 20 08:40:29 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.86.15              Driver Version: 570.86.15      CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  |   00000000:C1:00.0 Off |                    0 |
| N/A   26C    P0             59W /  500W |       1MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
PyTorch Version: 2.2.1
Available GPUs: 1
GPU 0: NVIDIA A100-SXM4-80GB
```

If you were going to run the container without `--nv` option, the container will have no way of seeing the GPU even though you
have requested GPU in slurm. To demonstrate this example, we will get an interactive node using `salloc` with 1 GPU as follows

```console
[shahzeb.siddiqui@login-01 pytorch]$ salloc -G 1 -p gpu -n4
salloc: Pending job allocation 18095275
salloc: job 18095275 queued and waiting for resources
salloc: job 18095275 has been allocated resources
salloc: Granted job allocation 18095275
salloc: Nodes gpu-f-3 are ready for job
```

We can confirm that there is a 1 GPU available on the node based on our slurm request

```console
[shahzeb.siddiqui@gpu-f-3 pytorch]$ nvidia-smi -L
GPU 0: NVIDIA H100 80GB HBM3 (UUID: GPU-414db5f5-1dd5-0661-eb11-8508d143f4ba)


Now if we execute the container without `--nv` option, the container will not see the GPU, and `nvidia-smi` program will fail 

```console
[shahzeb.siddiqui@gpu-f-3 pytorch]$ apptainer exec  ./pytorch_latest.sif nvidia-smi -L
FATAL:   "nvidia-smi": executable file not found in $PATH
```

If we run the python script, we see that no GPUs were detected

```console
[shahzeb.siddiqui@gpu-f-3 pytorch]$ apptainer exec  ./pytorch_latest.sif python list_gpus.py
PyTorch Version: 2.2.1
Available GPUs: 0
No GPU detected!
```

Now rerunning the same example with `--nv` option will show the GPUs and the script will work as expected.

```console
[shahzeb.siddiqui@gpu-f-3 pytorch]$ apptainer exec --nv  ./pytorch_latest.sif nvidia-smi -L
GPU 0: NVIDIA H100 80GB HBM3 (UUID: GPU-414db5f5-1dd5-0661-eb11-8508d143f4ba)


[shahzeb.siddiqui@gpu-f-3 pytorch]$ apptainer exec --nv  ./pytorch_latest.sif python list_gpus.py
PyTorch Version: 2.2.1
Available GPUs: 1
GPU 0: NVIDIA H100 80GB HBM3
```