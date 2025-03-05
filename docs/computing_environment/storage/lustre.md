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
 
Lustre file systems is typically mounted at `/hpc/projects`, `/hpc/instruments`, `/hpc/references`, `/hpc/scratch` that is used as project space for users to store their data. The project space 
is shared among all users in a group and is accessible from all compute nodes in the cluster.


### Basic Commands

Lustre provides the `lfs` utility for managing and querying the file system. Common commands include:

- `lfs df`: Display Lustre file system usage.
- `lfs quota`: View quota information
- `lfs getstripe`: Get file striping information.

Run `lfs --list-commands` for a full list of available commands and please refer to the man pages (`man lfs`) for detailed 
usage information.

## Managing Quotas

Quotas limit the amount of storage a user, group, or project can consume. Lustre supports three types of quotas:

- **User Quotas**: Limits storage usage for individual users.
- **Group Quotas**: Limits storage usage for groups of users.
- **Project Quotas**: Limits storage usage for specific projects.

!!! note

    We currently use Project Quotas to manage storage usage on Lustre file systems. We dont set user or group quotas.


### Checking Project Quota

Project IDs are assigned by system adminstrators and are used to manage project quotas. To find your project ID, you
will need to use `lfs project` command to list project IDs for a directory.

To retrieve project ID you can run the following:

```bash
lfs project -d /hpc/projects/<myproject>
```

Shown below is an example output, the project ID is *200020*.

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

### Optimizing Lustre Usage

Lustre provides a means to stripe data across multiple Object Storage Targets (OSTs) to improve performance. This can be 
configured using `lfs setstripe`. The system administrators have configured the stripe pattern at the top-level directory; however
users are free to configure striping at subdirectories or individual files. The `lfs setstripe` command can be used to configure
stripping. Please take a look at https://wiki.lustre.org/Configuring_Lustre_File_Striping for some example usage of stripping.


The `lfs getstripe` can be used to retrieve stripe information. Shown below is an example to retrieve stripe information for file.

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
