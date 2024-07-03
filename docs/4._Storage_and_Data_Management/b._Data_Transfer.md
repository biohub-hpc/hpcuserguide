---
title: Data Transfer 
description: Data transfer procedures, and tools for the Bruno HPC System
published: true
date: 2024-06-27T16:00:54.471Z
tags: 
editor: markdown
dateCreated: 2024-06-27T16:00:54.471Z
---

# Data Transfer

Transferring data to a High-Performance Computing (HPC) system involves several steps to ensure that your data is securely and efficiently moved to the computing environment where you can perform complex computations. 


## Transfer protocols

A number of different methods allows for transferring data in and out of the HPC resources at the Biohub Network. 
Terminal SSH-based commands such as `sftp`, or `rsync`, are highly recommended. 
GUI SSH-based 
These will provide the best performance for data transfers to and from the Biohub campuses.

!!! warning "A note about the `scp` tool"

    The `scp` command has been deemed insecure. Its use is now deprecated. `rsync` or `sftp` should be used instead.
    [More information on its deprecation](https://lwn.net/Articles/835962/).

### SSH Based Protocols

#### SFTP 

SFTP clients are interactive file transfer programs, similar to FTP, which perform all operations over an encrypted transport.

A variety of graphical SFTP clients are available for different OSes:

| Application | Platform 
| -------- | -------- |
| [WinSCP](https://winscp.net/eng/index.php)     | Windows     |
| [Filezilla](https://filezilla-project.org/)     | Cross-Platform     |
| [Fetch](https://fetchsoftworks.com/)     | Mac     |
| [CyberDuck](https://cyberduck.io)     | Mac     |
| [muCommander](https://www.mucommander.com/)     | Cross-Platform     |


#### Rsync 

Using rsync:

sh

    rsync -avz /path/to/local/file username@hpc-system-address:/path/to/remote/directory

        For directories, you can use the same command format.



|  |  |
| -------- | -------- |
| Hostname | login.bruno.czbiohub.org |
| Port | 22 |
| Username | firstname.lastname |
| Password | your okta password |



1. Understanding File Transfer Protocols

    SCP (Secure Copy Protocol): A secure way to transfer files between local and remote systems. It uses SSH (Secure Shell) for data transfer and authentication.
    SFTP (Secure File Transfer Protocol): An extension of SSH, it allows for secure file transfer and access to the file system.
    rsync: A fast and versatile command-line tool for copying files and directories locally and remotely. It can synchronize files between two locations while minimizing data transfer by only sending differences.

2. Preparing Your Data

    Organize Your Files: Before transferring, organize your files and directories in a structured manner. This makes it easier to locate and manage data on the HPC system.
    Compress Large Files: Compress large files or directories to reduce transfer time. Tools like tar, gzip, or zip can be used for compression.

3. Connecting to the HPC System

    Obtain Access Credentials: Ensure you have the necessary credentials (username, password, or SSH keys) provided by your HPC administrator.
    Establish an SSH Connection: Use an SSH client (e.g., ssh command in Unix/Linux, PuTTY for Windows) to connect to the HPC system. Example command:

    sh

    ssh username@hpc-system-address

4. Transferring Files


Using SFTP:

sh

sftp username@hpc-system-address

    Once connected, use put to upload files:

    sh

    put /path/to/local/file /path/to/remote/directory



5. Verifying Transfer

    Check File Integrity: After transfer, log in to the HPC system and verify that the files have been transferred correctly by checking file sizes and contents.

6. Automating Transfers

    Batch Scripts: Create scripts to automate repetitive transfer tasks using shell scripting. This can be particularly useful for regular data uploads.
    Cron Jobs: Schedule regular file transfers using cron jobs (Unix/Linux) to automate the process.

By following these steps, you can efficiently and securely transfer your data to an HPC system, allowing you to leverage powerful computing resources for your computational tasks.
