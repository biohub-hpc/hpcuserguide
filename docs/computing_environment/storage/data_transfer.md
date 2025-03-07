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

1. Understanding File Transfer Protocols

    SCP ([Secure Copy Protocol](https://en.wikipedia.org/wiki/Secure_copy_protocol)): A secure way to transfer files between local and remote systems. It uses SSH (Secure Shell) for data transfer and authentication.
    SFTP (Secure File Transfer Protocol): An extension of SSH, it allows for secure file transfer and access to the file system.
    rsync: A fast and versatile command-line tool for copying files and directories locally and remotely. It can synchronize files between two locations while minimizing data transfer by only sending differences.

2. Preparing Your Data

    Organize Your Files: Before transferring, organize your files and directories in a structured manner. This makes it easier to locate and manage data on the HPC system.
    Compress Large Files: Compress large files or directories to reduce transfer time. Tools like tar, gzip, or zip can be used for compression.

3. Connecting to the HPC System

    Obtain Access Credentials: Ensure you have the necessary credentials (username, password, or SSH keys) provided by your HPC administrator.
    Establish an SSH Connection: Use an SSH client (e.g., ssh command in Unix/Linux, PuTTY for Windows) to connect to the HPC system. Example command:
    
    ```bash
    ssh username@hpc-system-address
    ```

4. Transferring Files

    Using SFTP:


    ```command
    sftp username@hpc-system-address
    
        Once connected, use put to upload files:
    
        sh
    
        put /path/to/local/file /path/to/remote/directory
    ```

