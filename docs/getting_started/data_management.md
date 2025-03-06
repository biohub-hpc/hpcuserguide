# Data Management

It's important to keep track of the data that is being used on the cluster. 
This is to ensure that the data is not lost and can be easily accessed by other users.

## Rsync 

The `rsync` command is a powerful tool for copying files between two locations. 
It can be used to copy files from one directory to another on the same machine or between two different machines.
Please refer to man pages `man rsync` for detailed summary of the command.

Shown below are some practical examples you can use on day-day work

## Basic Sync with Progress

The command below will sync files from `source` to `destination` directory. The `-a` option is used to archive files and directories, 
`-v` is used to show progress and `-h` is used to show human readable format. The `--progress` option is used to show progress 
of the transfer.

```console
rsync -avh --progress <source> <destination>
```

The `--progress` can be useful to ensure data integrity and to see the progress of the transfer.

## Sync Files with Deletion

If you are periodically syncing files and want to delete files that are not present in the source directory, you can use the `--delete` option.
This would make sure the files are mirrored properly and files on destination are deleted.

This can be done using the following

```console
rsync -avh --delete <source> <destination>
```

## Dry Run with verbose output 

The `--dry-run` option is used to perform a trial run without making any changes. This can be useful to see what files will be copied. 
The `--itemize-changes` option is used to show a change summary for all updates which will help you understand what files will be copied.

```console
rsync -avh --dry-run --itemize-changes <source> <destination>
```

## Selective Sync with Include/Exclude Patterns

You can use the `--include` and `--exclude` options to include or exclude files based on patterns.

```console
[shahzeb.siddiqui@login-02 shahzeb.siddiqui]$ rsync -avh --progress --include='*.csv' --exclude='*' files/ new_files/
sending incremental file list
created directory new_files
./
1.csv
              0 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=4/6)
2.csv
              0 100%    0.00kB/s    0:00:00 (xfr#2, to-chk=3/6)
3.csv
              0 100%    0.00kB/s    0:00:00 (xfr#3, to-chk=2/6)
4.csv
              0 100%    0.00kB/s    0:00:00 (xfr#4, to-chk=1/6)
5.csv
              0 100%    0.00kB/s    0:00:00 (xfr#5, to-chk=0/6)

sent 364 bytes  received 146 bytes  1.02K bytes/sec
total size is 0  speedup is 0.00
```

### Extending this with CRON

Once you get familiar with `rsync` you may want to consider automating the process using `cron` such as doing automatic backup or
data transfer between two locations.

A simple example of `cron` job to run `rsync` every day at 03:00AM where all files of `.h5` extension are copied to $MYDATA

```console
0 3 * * * rsync -avh --progress --include='*.h5' --exclude='*' /home/shahzeb.siddiqui/large_files/ /hpc/mydata/shahzeb.siddiqui/backups/ >> /hpc/mydata/shahzeb.siddiqui/logs/rsync_backup.log 2>&1
```

Once the files are copied, you may want to delete the files from $HOME if you need to clear up some space.


## Finding Files

The Linux `find` command is a powerful tool for finding files that you will want to take some time to learn how to use by reading the
man pages `man find` or refer to help `find --help`.

Shown below are some practical examples you can use on day-day work

### Finding All Large Files ( > 1GB)

The command below will find all files that are greater than 1GB in size in $HOME directory. 

```console
find $HOME -type f -size +1G
```

### Finding All Files Modified in the Last 7 Days

The command below will find all files exactly 7 days ago using the `-mtime` option.
```console
find $HOME -type f -mtime 7
```

### Find all recently modified files (Last 24 hrs)

One common thing is to find all recently modified files. The argument `-mtime -1` will find all files modified in the last 24 hours, where 
the negative sign `-` is used to indicate the last 24 hours.

```console
find $HOME -type f -mtime -1
```

### Find empty files

You can find all empty files using the `-empty` option.

```console
find $HOME -type f -empty
```

You can extend this and delete all empty files by using the `-delete` option.

```console
find $HOME -type f -empty -delete
```

### Find Files by Extension (e.g. .log files)

Let's say you want to find all log files, you can use the `-name` option to search for files with `.log` extension.

```console
find /var/log -type f -name "*.log"
```

Shown below is an example output

```console
$ find /var/log -type f -name "*.log"
/var/log/fsck_apfs_error.log
/var/log/alf.log
/var/log/fsck_hfs.log
/var/log/com.apple.xpc.launchd/launchd.log
/var/log/shutdown_monitor.log
/var/log/system.log
/var/log/wifi.log
/var/log/acroUpdaterTools.log
/var/log/install.log
/var/log/fsck_apfs.log
```

### Find Files Owned by a Specific User

Let's say you want to find all files by specific user, this can be useful in a project space `/hpc/projects` where multiple users
write to same directory. You can use the `-user` option to specify name of user you want to search. 

```console
find /hpc/projects/<project_name> -type f -user <username>
```

### Find all files with specific permission (e.g Executables)

You can find all executables files or binaries using the `-perm` option. The example below will find all files with permission `755`.

```console
find /usr/bin -type f -perm 755
```

### Find and Delete Old Files (e.g., Older Than 30 Days)

The command below will delete all temporary files in the past 30 days

```console
find /tmp -type f -mtime +30 -exec rm -f {} \;
```

### Find Files by Size Range (e.g., Between 100MB - 1GB)

You can narrow search field to find files between a specific size range using the `-size` option. 

```console
find /data -type f -size +100M -size -1G
```

The `+100M` will find files greater than 100MB and `-1G` will find files less than 1GB.

### Execute commands on found files

You can use the `-exec` option to specify a command to run on the found files. For example, you can use the `ls -l` 
command to list all files found.

Shown below we will show all files modified in the last 7 days, and list them using `ls -lh` command.

```console
find $HOME -type f -mtime -7 -exec ls -lh {} \;
```
