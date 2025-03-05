# Lustre 

## Introduction to Lustre

Lustre is a high-performance, distributed parallel file system widely used in High Performance Computing (HPC) environments.
It is designed to handle large-scale data storage and I/O operations, making it ideal for scientific simulations, data analysis, 
and other compute-intensive workloads. Lustre scales efficiently to support thousands of nodes, petabytes of storage, 
and high I/O throughput (hundreds of GB/s).

### Key Components
- **Metadata Servers (MDS)**: Manage file metadata (e.g., filenames, permissions).
- **Metadata Targets (MDT)**: Store the metadata.
- **Object Storage Servers (OSS)**: Handle file data storage.
- **Object Storage Targets (OST)**: Physical storage devices where file data resides.
- **Clients**: Compute nodes that access the file system.

### Benefits for HPC Users
- High scalability for large datasets.
- Parallel I/O for faster data access.
- Flexible striping to optimize performance.

## Getting Started with Lustre

### Accessing Lustre

Lustre file systems is typically mounted at `/hpc/projects` that is used as project space for users to store their data. The project space 
is shared among all users in a group and is accessible from all compute nodes in the cluster.


### Basic Commands

Lustre provides the `lfs` utility for managing and querying the file system. Common commands include:

- `lfs df`: Display Lustre file system usage.
- `lfs quota`: View quota information
- `lfs setstripe`: Set file striping parameters.
- `lfs getstripe`: Get file striping information.

Run `lfs --list-commands` for a full list of available commands and please refer to the man pages (`man lfs`) for detailed 
usage information.

## Managing Quotas

Quotas limit the amount of storage a user, group, or project can consume. Lustre supports three types of quotas:

- **User Quotas**: Limits storage usage for individual users.
- **Group Quotas**: Limits storage usage for groups of users.
- **Project Quotas**: Limits storage usage for specific projects.

### Checking User Quota

To view your quota, use the `lfs quota` command. The syntax may vary depending on the project or group quota you want to check.

```bash
lfs quota -u $USER /hpc/projects/<myproject>
```

### Checking Group Quota

To view your group quota, you will use the `-g` flag with the group name and specify the path to project.

```bash
lfs quota -g <mygroup> /hpc/projects/<myproject>
```

### Checking Project Quota

Project quotas are tied to a project ID. We typically assign each project a unique ID that is used to manage the quota. The 
`-p` flag is used to specify the project ID. 

```bash
lfs quota -p <project_id> /hpc/projects/<myproject>
```

## Finding Project ID

Project IDs are assigned by system adminstrators and are used to manage project quotas. To find your project ID, you
will need to use `lfs project` command to list project IDs for a directory.

The command will be the following

```bash
lfs project -d /hpc/projects/<myproject>
```

Shown below is an example output

```bash
[shahzeb.siddiqui@login-01 ~]$ lfs project -d /hpc/projects/group.royer
200020 P /hpc/projects/group.royer
```

You can use this project ID to get the project quota information. Shown below is a sample output showing 
lustre quota in human-readable format using `-h` flag.

```bash
[shahzeb.siddiqui@login-01 ~]$ lfs quota -h -p 200020 /hpc/projects/group.royer
Disk quotas for prj 200020 (pid 200020):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
/hpc/projects/group.royer
                 322.5T    327T    327T       - 18005642       0       0       -
```

### Disk Space Usage

The `lfs df` command can be used to see disk usage for Lustre file system. This will show the disk usage across
all available OSTs and MDTs since the data is distributed across multiple storage devices. Shown below is an example output

```bash
[shahzeb.siddiqui@login-01 ~]$ lfs df -h /hpc/projects/group.royer
UUID                       bytes        Used   Available Use% Mounted on
exa1-MDT0000_UUID           1.8T      210.5G        1.6T  12% /hpc/projects/group.royer[MDT:0]
exa1-MDT0001_UUID           1.8T      218.6G        1.6T  13% /hpc/projects/group.royer[MDT:1]
exa1-MDT0002_UUID           1.8T      184.8G        1.6T  11% /hpc/projects/group.royer[MDT:2]
exa1-MDT0003_UUID           1.8T      194.3G        1.6T  11% /hpc/projects/group.royer[MDT:3]
exa1-OST0000_UUID           3.7T        2.3T        1.4T  63% /hpc/projects/group.royer[OST:0]
exa1-OST0001_UUID           3.7T        2.1T        1.5T  59% /hpc/projects/group.royer[OST:1]
exa1-OST0002_UUID           3.7T        2.2T        1.5T  61% /hpc/projects/group.royer[OST:2]
exa1-OST0003_UUID           3.7T        2.2T        1.4T  62% /hpc/projects/group.royer[OST:3]
exa1-OST0004_UUID           3.7T        2.4T        1.2T  67% /hpc/projects/group.royer[OST:4]
exa1-OST0005_UUID           3.7T        2.5T        1.1T  70% /hpc/projects/group.royer[OST:5]
exa1-OST0006_UUID           3.7T        2.5T        1.2T  69% /hpc/projects/group.royer[OST:6]
exa1-OST0007_UUID           3.7T        2.5T        1.2T  69% /hpc/projects/group.royer[OST:7]
exa1-OST0008_UUID          60.2T       46.9T       12.6T  79% /hpc/projects/group.royer[OST:8]
exa1-OST0009_UUID          60.2T       46.6T       13.0T  79% /hpc/projects/group.royer[OST:9]
exa1-OST000a_UUID          60.2T       47.5T       12.1T  80% /hpc/projects/group.royer[OST:10]
exa1-OST000b_UUID          60.2T       46.7T       12.9T  79% /hpc/projects/group.royer[OST:11]
exa1-OST000c_UUID          60.2T       47.6T       12.0T  80% /hpc/projects/group.royer[OST:12]
exa1-OST000d_UUID          60.2T       47.0T       12.6T  79% /hpc/projects/group.royer[OST:13]
exa1-OST000e_UUID          60.2T       47.2T       12.4T  80% /hpc/projects/group.royer[OST:14]
exa1-OST000f_UUID          60.2T       48.9T       10.7T  83% /hpc/projects/group.royer[OST:15]
exa1-OST0010_UUID         551.6T      436.7T       87.1T  84% /hpc/projects/group.royer[OST:16]
exa1-OST0011_UUID         551.6T      438.6T       85.2T  84% /hpc/projects/group.royer[OST:17]
exa1-OST0012_UUID         551.6T      438.2T       85.6T  84% /hpc/projects/group.royer[OST:18]
exa1-OST0013_UUID         551.6T      437.2T       86.5T  84% /hpc/projects/group.royer[OST:19]
exa1-OST0014_UUID         551.6T      438.3T       85.5T  84% /hpc/projects/group.royer[OST:20]
exa1-OST0015_UUID         551.6T      441.1T       82.6T  85% /hpc/projects/group.royer[OST:21]
exa1-OST0016_UUID         551.6T      439.5T       84.3T  84% /hpc/projects/group.royer[OST:22]
exa1-OST0017_UUID         551.6T      442.9T       80.9T  85% /hpc/projects/group.royer[OST:23]
exa1-OST0018_UUID         551.6T      437.8T       86.0T  84% /hpc/projects/group.royer[OST:24]
exa1-OST0019_UUID         551.6T      438.0T       85.8T  84% /hpc/projects/group.royer[OST:25]

filesystem_summary:         5.9P        4.7P      958.2T  84% /hpc/projects/group.royer
```

### Optimizing Lustre Usage

#### Striping Files
Striping distributes file data across multiple OSTs for better performance. Use `lfs setstripe` to configure striping parameters. 
Shown below is an exaple of striping a file with 4 stripes and a stripe size of 1MB.

```bash
lfs setstripe -c 4 -S 1M /hpc/projects/group.royer/myfile.txt
``` 

You can use `lfs getstripe` to verify the striping configuration.

```bash
lfs getstripe /hpc/projects/group.royer/myfile.txt
```

You can retrieve stripe information for a directory by using the `-d` flag.

```bash
lfs getstripe -d /hpc/projects/group.royer
```

Shown below is an example output

```console
[shahzeb.siddiqui@login-01 ~]$ lfs getstripe -d /hpc/projects/group.royer
stripe_count:  1 stripe_size:   1048576 pattern:       raid0 stripe_offset: -1 pool:          ddn_hdd
```

####  Best Practices

- Large Files: Lustre excels with large files; avoid many small files.
- Parallel I/O: Use tools like MPI-IO for parallel access.
- Avoid Overloading Metadata: Minimize operations like ls -l on directories with many files.

## Additional Resources

- Lustre Official Site: lustre.org
- `man lfs`: Detailed command documentation on your cluster.
