# Navigating the Cluster

In this section, we will briefly cover how to navigate the HPC cluster. We recommend you have some prior knowledge of Linux commands as it
will be necessary for you to navigate the system. You can view the [Linux Command Line Basics](https://www.tutorialspoint.com/unix/unix-getting-started.htm) 
tutorial.

## System Overview

When you connect to the cluster, you will be routed to the login nodes. The login nodes are shared amongst all users as an entry point to the cluster.
The login nodes are `login-01` and `login-02`. You can tell the hostname of node by running `hostname -f` 

```console
[shahzeb.siddiqui@login-01 ~]$ hostname
login-01
```

On Bruno, the login node is a 128 core AMD EPYC 7713 processor, you can view the CPU information of any machine by running 
`lscpu` command.

```console
[shahzeb.siddiqui@login-01 ~]$ lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              128
On-line CPU(s) list: 0-127
Thread(s) per core:  1
Core(s) per socket:  64
Socket(s):           2
NUMA node(s):        2
Vendor ID:           AuthenticAMD
CPU family:          25
Model:               1
Model name:          AMD EPYC 7713 64-Core Processor
Stepping:            1
CPU MHz:             3051.804
CPU max MHz:         3720.7029
CPU min MHz:         1500.0000
BogoMIPS:            4000.12
Virtualization:      AMD-V
L1d cache:           32K
L1i cache:           32K
L2 cache:            512K
L3 cache:            32768K
NUMA node0 CPU(s):   0-63
NUMA node1 CPU(s):   64-127
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 pcid sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 invpcid_single hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr wbnoinvd amd_ppin brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
```

To see all available users on the system, you can run `who` which will show you all the users logged in.

```console
[shahzeb.siddiqui@login-01 ~]$ who
deepika.sundarraman pts/3        2025-03-06 14:33 (192.168.103.94)
yttria.aniseia pts/9        2025-03-07 11:12 (192.168.104.75)
svc.msbot.swe pts/11       2025-02-05 10:29 (::1)
julia.peukes pts/12       2025-02-19 20:22 (100.64.2.104)
ryan.mcclure pts/27       2025-03-07 05:59 (10.30.30.35)
rowan.cassius pts/30       2025-03-07 09:01 (98.113.94.119)
gibraan.rahman pts/36       2025-03-07 10:02 (47.231.130.21)
peter.wu pts/57       2025-03-07 12:09 (99.57.139.222)
svc.seqbot pts/68       2025-03-01 09:07 (::1)
svc.seqbot pts/70       2025-03-01 09:08 (::1)
dari.kimanius pts/74       2025-03-07 10:12 (10.50.30.56)
frank.mccarthy pts/86       2025-02-27 10:35 (171.65.160.102)
abigail.glascock pts/45       2025-03-07 08:19 (98.114.12.188)
yttria.aniseia pts/47       2025-03-07 11:12 (:pts/9:S.0)
deepika.sundarraman pts/23       2025-02-09 12:33 (192.168.103.94)
deepika.sundarraman pts/20       2025-02-16 15:36 (192.168.103.94)
sarah.lin pts/41       2025-03-07 07:31 (171.65.2.4)
marcus.forst pts/80       2025-02-28 13:04 (171.65.93.16)
aaron.daniel pts/43       2025-03-07 07:33 (66.85.230.143)
deepika.sundarraman pts/79       2025-02-26 13:54 (192.168.103.94)
krishnakant.saboo pts/122      2025-03-07 10:52 (169.230.248.195)
sarah.lin pts/127      2025-03-07 09:16 (171.65.2.4)
svc.msbot.swe pts/135      2025-02-26 13:10 (::1)
josh.elias pts/110      2025-03-04 17:21 (171.65.160.236)
svc.msbot.swe pts/171      2025-02-26 16:12 (::1)
frank.mccarthy pts/173      2025-03-04 10:55 (171.66.11.53)
george.crowley pts/149      2025-03-07 10:06 (171.65.92.197)
carlos.gonzalez pts/151      2025-02-28 15:54 (:pts/144:S.0)
deepika.sundarraman pts/165      2025-02-21 11:41 (192.168.103.94)
josh.elias pts/169      2025-03-05 14:25 (171.65.160.236)
doug.henze pts/170      2025-03-05 14:25 (171.65.93.28)
mathias.voges pts/176      2025-03-07 12:13 (192.168.105.68)
deepika.sundarraman pts/152      2025-02-24 10:51 (192.168.103.94)
sevahn.vorperian pts/163      2025-03-07 10:09 (98.51.6.165)
root     pts/180      2025-03-05 11:30 (100.64.15.254)
sevahn.vorperian pts/142      2025-03-07 09:26 (98.51.6.165)
luca.zanella pts/197      2025-03-07 11:01 (156.145.235.24)
deepika.sundarraman pts/189      2025-03-05 11:06 (192.168.103.94)
eric.waltari pts/128      2025-03-07 09:17 (192.168.102.150)
deepika.sundarraman pts/195      2025-03-03 10:42 (192.168.103.94)
kyle.harrington pts/205      2025-03-03 13:44 (96.231.246.206)
shahzeb.siddiqui pts/129      2025-03-07 12:27 (216.15.94.168)
krishnakant.saboo pts/221      2025-03-07 11:13 (169.230.248.195)
jonathan.schwartz pts/230      2025-03-07 11:19 (10.50.30.49)
ram.ayyala pts/232      2025-03-07 11:31 (104.172.241.71)
shailee.jain pts/234      2025-03-07 11:34 (64.54.15.154)
bruno.moretti pts/240      2025-03-07 12:27 (10.20.180.71)
ariana.peck pts/210      2025-03-07 12:16 (204.102.230.199)
yttria.aniseia pts/212      2025-03-07 11:13 (192.168.104.75)
sarah.lin pts/238      2025-03-07 12:21 (171.65.2.4)
```

## File System

We have several filesystems including NFS, VAST, and Lustre. To see all filesystems, you can view output of the following commands 

```console
mount -l

cat /proc/mounts
```

The `df -hT` command can be useful to see all filesystems and their disk usage. The `-T` option will show you the filesystem type.
You may pass arguments with path to filesystem mount to see usage. For example to see usage for $HOME and $MYDATA you can run

```console
[shahzeb.siddiqui@login-01 ~]$ df -hT $HOME $MYDATA
Filesystem                                           Type  Size  Used Avail Use% Mounted on
storage-home:/nvmepool/exports/home/shahzeb.siddiqui nfs    32G   22G   11G  67% /home/shahzeb.siddiqui
vast-sf.mammoth.infiniband:/mydata/shahzeb.siddiqui  nfs   273T   53T  221T  20% /hpc/mydata/shahzeb.siddiqui
```

## Software

The software stack is installed in `/hpc/apps` and is accessible via `module` command which dynamically modifies your 
environment to include the software you need. 

To see all available modules you can run 

```console
[shahzeb.siddiqui@login-01 ~]$ module av

----------------------------------------------------------------------------------------------------------------------------- /hpc/modules/modulefiles/Core -----------------------------------------------------------------------------------------------------------------------------
   StdEnv    proot/current    slurm/current (S)    slurm/default (S,L,D)

------------------------------------------------------------------------------------------------------------------------- /hpc/modules/modulefiles/Applications -------------------------------------------------------------------------------------------------------------------------
   BEAGLE/2023.06.06                  awscli/v2                               cuda/11.7.1_515.65.01                            emacs/29.2                                 julia/1.10.0         (D)    nvhpc-sdk/24.3                      relion/ver5.0-12cf15de-CU86
   BEAST/1.10.4                       axel/2.17.14                            cuda/11.8.0_520.61.05                            eman/2.99.47_sphire1.4_sparx_huge          lightning/2.3.1             nvhpc/2024_2411                     relion/ver5.0-12cf15de-CU90   (D)
   BEAST2/2.7.4                       beagle/2023.06.06                       cuda/12.0.0_525.60.13                            fastga/latest                              mafft/7.520                 ollama/0.2.8                        resmap/1.1.4
   FASTGA/latest                      beast/1.10.4                            cuda/12.0.1_525.85.12                            fastga/1.0                        (D)      mamba/23.1.0-3-pypy3        ollama/0.3.6                        rstudio/2024.04.1+748
   FASTGA/1.0                  (D)    beast2/2.7.4                            cuda/12.1.1_530.30.02                            fastp/0.24.0                               mamba/23.1.0-3       (D)    ollama/0.5.7                 (D)    rsync/default
   FastANI/1.34-gcc-12.4              bioformats2raw/0.9.4                    cuda/12.2.0_535.54.03                            ffmpeg/7.0                                 matlab/R2024b               omnitrace/1.11.1                    rsync/3.2.7                   (D)
   FragPipe/20.0                      bowtie2/2.1.0                           cuda/12.2.1_535.86.10                            fm-index/1.0                               maxquant/2.0.3.1            openmpi/4.1.6                (D)    ruse/2.0
   FragPipe/21.1                      bowtie2/2.5.3                    (D)    cuda/12.3.2_545.23.08                            fpart/1.6.1                                meme/5.5.5                  openmpi/5.0.3                       rust/1.77.2
   FragPipe/22.0_python3.9            btop/1.3.0                              cuda/12.4.0_550.54.14                            fragpipe/20.0                              minimap2/2.26               oracle-java/jdk-17.0.1              samtools/1.18
   FragPipe/22.0               (D)    caddy/2.4.6                             cuda/12.5.1_555.42.06                            fragpipe/21.1                              mongodb/7.0.8               oracle-java/jdk-17.0.6       (D)    samtools/1.19                 (D)
   IGV/2.17.4                         caddy/2.6.4                      (D)    cuda/12.6.1_560.35.03                     (D)    fragpipe/22.0_python3.9                    mongosh/2.2.3               oracle-java/jdk-19.0.1              schrodinger/2021.04
   MrBayes/git-d5aa8ed                cellprofiler/4.2.1                      cuda/12.6.3_560.35.05                            fragpipe/22.0                     (D)      motioncor2/1.6.4            oracle-java/jdk-20                  spaceranger/2.1.0
   R/4.1                              cellranger-arc/2.0.2                    cuda/12.8.0_570.86.10                            gcc/11.3                          (L,D)    motioncor3/1.1.1            papi/7.1.0                          spectronaut/19.5.241126.62635
   R/4.2                              cellranger-atac/2.1.0                   cudnn/8.7.0.84_cuda10                            gcc/12.4                                   mpifileutils/0.11.1         pixi/0.25.0                         spid/master
   R/4.3                       (D)    cellranger/7.0.1                 (D)    cudnn/8.8.1.3_cuda11                             gcc/13.3                                   mrbayes/git-d5aa8ed         pixi/0.39.5                  (D)    squashfs-tools/4.6.1
   R/4.4                              cellranger/9.0.0                        cudnn/8.8.1.3_cuda12                             gcc/14.2                                   msrsync/20170730            promtail/3.3.2                      star/default
   STAR/default                       chimerax/1.7.1                          cudnn/8.9.7.29_cuda11                            gsl/2.8-gcc-12.4                           mustem-gpu/5.3              pycharm/community-2022.2            star/2.7.10b
   STAR/2.7.10b                       chimerax/1.8                     (D)    cudnn/8.9.7.29_cuda12                            gurobi/11.0.2                              mzmine/4.4.3                r/4.1                               star/2.7.11b                  (D)
   STAR/2.7.11b                (D)    cistem/b21db55                          cudnn/9.0.0.3_cuda12                      (D)    hdf5/1.14.4                                nano/7.2                    r/4.2                               stui/0.3.6
   alphafold/2.1.0                    cistem/1.0.0                     (D)    curl/8.12.1                                      hpcx/2.19                                  napari/test                 r/4.3                        (D)    turm/0.6.0
   alphafold/2.2.0                    cmake/3.28.2                            demuxlet/current                                 httm/0.38.0                                neovim/0.10.0               r/4.4                               uv/0.2.23
   alphafold/2.3.2                    cryosparc/4.4.0-motioncor2-1.6.4        demuxlet/default                                 hwloc/2.10.0                               nextflow/current     (D)    raxml-ng-mpi/1.2.1                  uv/0.4.9                      (D)
   alphafold/3.0.0             (D)    cryosparc/4.4.1-motioncor2-1.6.4 (D)    demuxlet/f5044eb                          (D)    igv/2.17.4                                 nextflow/22.02.1            raxml-ng/1.2.1                      versitygw/1.0.7
   alphafold/3.0.1-23-g792e61e        cryosparc/4.5.1-motioncor2-1.6.4        diann/1.8.1                                      imod/4.11.25                               nextflow/23.10.1            rclone/1.65.2                       zed/0.146.5
   anaconda/latest                    cryosparc/4.6.0-motioncor2-1.6.4        diann/2.0.1                               (D)    iqtree/2.2.2.6                             nextflow/24.10.2            rclone/1.67.0                (D)
   anaconda/2021_09_16         (D)    ctffind/4.1.14                          dragon/0.10                                      julia/default                              nextpyp/0.5                 relion-turbo/ver5.0-git-CU80
   anaconda/2022.05                   cuda/10.2.89_440.33.01                  duc/1.4.4                                        julia/1.7.3                                ninja/1.12.1                relion-turbo/ver5.0-git-CU86
   anaconda/2023.03                   cuda/11.6.2_510.47.03                   dynamo/1.1.546_MCR-24.1.0_GLNXA64_withMCR        julia/1.8.5                                nsight/2024.1.1.59          relion-turbo/ver5.0-git-CU90 (D)
   aria2/1.37.0                       cuda/11.7.0_515.43.04                   elfindo/0.9.5                                    julia/1.9.4                                nvhpc-sdk/23.11      (D)    relion/ver5.0-12cf15de-CU80

---------------------------------------------------------------------------------------------------------------------------- /hpc/modules/modulefiles/Groups ----------------------------------------------------------------------------------------------------------------------------
   comp_micro/default    czii/default    data.science/default    jacobo_group/default    royerlab/default

  Where:
   S:  Module is Sticky, requires --force to unload or purge
   L:  Module is loaded
   D:  Default Module

If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```

To load any software such as R you can run the following

```console
[shahzeb.siddiqui@login-01 ~]$ module load R
[shahzeb.siddiqui@login-01 ~]$ which R
/hpc/apps/r/4.3/bin/R
[shahzeb.siddiqui@login-01 ~]$ R --version
R version 4.3.2 (2023-10-31) -- "Eye Holes"
Copyright (C) 2023 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under the terms of the
GNU General Public License versions 2 or 3.
For more information about these matters see
https://www.gnu.org/licenses/.
```

For more details on how to use module please refer to our [Lmod](../environment/lmod.md) documentation. You can 
see a [List of Available Software](../software/software_modules.md).

## Monitoring System Load

To see active load on the system you can run `top` command which will show you real-time usage of the system with list of processes.

The `htop` command is a more interactive version of `top` and provides a better view of the system load.

### Monitoring Process Usage

To list all your user process you can run

```console
ps -u $USER
```

The output will contain Process ID (PID) along with the command that is running. Shown below is an example output

```console
[shahzeb.siddiqui@login-01 ~]$ ps -u $USER
    PID TTY          TIME CMD
1479962 ?        00:00:00 systemd
1480047 ?        00:00:00 (sd-pam)
1480111 ?        00:00:00 pulseaudio
1480175 ?        00:00:00 sshd
1480323 pts/129  00:00:00 bash
1480465 ?        00:00:00 dbus-daemon
1480476 ?        00:00:00 gvfsd
1480490 ?        00:00:00 gvfsd-fuse
2818212 pts/129  00:00:00 ps
```

You can get detailed process list with resource usage. The `-o` option can be used to specify the columns you want to see.

For example the command below will list process sorted by CPU usage and display the top 10 processes

```console
[shahzeb.siddiqui@login-01 ~]$ ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu | head -n10
    PID USER     %CPU %MEM CMD
2590601 jonatha+  115  0.0 /home/jonathan.schwartz/.cursor-server/cli/servers/Stable-7b3e0d45d4f952938dbd8e1e29c1b17003198480/server/node --dns-result-order=ipv4first /home/jonathan.schwartz/.cursor-server/cli/servers/Stable-7b3e0d45d4f952938dbd8e1e29c1b17003198480/server/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
2854051 root     90.0  0.0 /bin/bash /usr/sbin/nhc
1220968 yang-jo+ 70.7  0.0 /home/yang-joon.kim/.cursor-server/cli/servers/Stable-906121b8c0bdf041c14a15dac228e66ab5505260/server/node --dns-result-order=ipv4first /home/yang-joon.kim/.cursor-server/cli/servers/Stable-906121b8c0bdf041c14a15dac228e66ab5505260/server/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
2821931 yang-jo+ 55.8  0.1 /home/yang-joon.kim/.cursor-server/cli/servers/Stable-906121b8c0bdf041c14a15dac228e66ab5505260/server/node /home/yang-joon.kim/.cursor-server/extensions/ms-python.vscode-pylance-2024.8.1/dist/server.bundle.js --cancellationReceive=file:60670bd8eb467785420634dacf82ed6eb328e233f1 --node-ipc --clientProcessId=1220968
2248533 duo.peng 35.0  0.3 /home/duo.peng/.cursor-server/cli/servers/Stable-be4f0962469499f009005e66867c8402202ff0b0/server/node /home/duo.peng/.cursor-server/extensions/ms-python.vscode-pylance-2024.8.1/dist/server.bundle.js --cancellationReceive=file:f82e098e6937b20ffd273562081a41091b865b61ae --node-ipc --clientProcessId=4105312
1088193 kevin.z+ 12.8  0.3 /home/kevin.zhao/.vscode-server/cli/servers/Stable-e54c774e0add60467559eb0d1e229c6452cf8447/server/node /home/kevin.zhao/.vscode-server/extensions/ms-python.vscode-pylance-2025.3.1/dist/server.bundle.js --cancellationReceive=file:b00959797d1af888d3322291e890980b2b40055e6e --node-ipc --clientProcessId=2126576
  81171 saugat.+ 11.1  0.1 /home/saugat.kandel/.vscode-server/cli/servers/Stable-e54c774e0add60467559eb0d1e229c6452cf8447/server/node /home/saugat.kandel/.vscode-server/extensions/ms-python.vscode-pylance-2025.3.1/dist/server.bundle.js --cancellationReceive=file:37874b9c9d579ad24523c21c94bc34a966a38e165d --node-ipc --clientProcessId=76397
1113387 jonatha+ 10.3  0.3 /home/jonathan.schwartz/.cursor-server/cli/servers/Stable-7b3e0d45d4f952938dbd8e1e29c1b17003198480/server/node /home/jonathan.schwartz/.cursor-server/extensions/ms-python.vscode-pylance-2024.8.1/dist/server.bundle.js --cancellationReceive=file:efb53943cd30e5072f95682822ca21a2e13573ca14 --node-ipc --clientProcessId=2590601
2384230 josh.hu+  9.5  0.2 /home/josh.hutchings/.vscode-server/cli/servers/Stable-e54c774e0add60467559eb0d1e229c6452cf8447/server/node /home/josh.hutchings/.vscode-server/cli/servers/Stable-e54c774e0add60467559eb0d1e229c6452cf8447/server/out/bootstrap-fork --type=fileWat
```

You can find process by name, for instance if you want to see all `python` process you can run

```console
ps -C python
```

A better utility is `pgrep` which can be used to find process by name

```console
[shahzeb.siddiqui@login-01 ~]$ pgrep -l python
6149 python3
6170 python3
26790 python
402799 python3.12
672130 python
1076597 python
1108375 python
1419294 python
1618506 python
1914689 python3.10
2244105 python3.10
2284274 python
2430319 python
3294387 python
3294635 python
3553462 python3.10
```

To kill a process you simply run

```console
kill <PID>
```