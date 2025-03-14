# File Permissions and Ownership in HPC

Managing file permissions and ownership is critical for securing data and enabling collaboration on a 
High-Performance Computing (HPC) system. This guide covers basic tools like `chown`, `chmod`, `umask`, as well as 
advanced access control with `setfacl` and `getfacl`.

## Changing Ownership with `chown`

The `chown` command changes the ownership of files or directories. The command syntax is 

```
chown [user][:group] file
```

Some example usage of chown can be shown below

To change the file owner to `alice` you can run the following command:

```console
$ chown alice myfile.txt
```

If you want to change the owner and group to `alice:research` you can run the following command:

```console
$ chown alice:research myfile.txt
```

To change the ownership recursively you can use the `-R` option:

```console
$ chown -R alice:research /path/to/dir
```

## Setting Permissions with `chmod`

The chmod ("change mode") command is used to change the permission flags on
existing files. It can be applied recursively using the `-R` option. It can be
invoked with either octal values representing the permission flags, or with
symbolic representations of the flags. The octal values have the following
meaning:

| Octal Digit | Binary Representation (rwx) | Permission                                  |
|-------------|-----------------------------|---------------------------------------------|
| 0           | 000                         | none                                        |
| 1           | 001                         | execute only                                |
| 2           | 010                         | write only                                  |
| 3           | 011                         | write and execute                           |
| 4           | 100                         | read only                                   |
| 5           | 101                         | read and execute                            |
| 6           | 110                         | read and write                              |
| 7           | 111                         | read, write, and execute (full permissions) |

Here is an example of chmod using octal values:

```console
$ umask
0077
$ touch foo
$ ls -l foo
-rw------- 1 elvis elvis 0 Nov 19 14:49 foo
$ chmod 755 foo
$ ls -l foo
-rwxr-xr-x 1 elvis elvis 0 Nov 19 14:49 foo
```

Here is the format of the chmod command when using symbolic values:

```
chmod [-R] [classes][operator][modes] file ...
```

The *classes* determine to which combination of user/group/other the operation
will apply, the *operator* specifies whether permissions are being added or
removed, and the *modes* specify the permissions to be added or removed.
Classes are formed by combining one or more of the following letters:

| Letter | Class | Description                                                            |
|--------|-------|------------------------------------------------------------------------|
| u      | user  | Owner of the file                                                      |
| g      | group | Users who are members of the file's group                              |
| o      | other | Users who are not the owner of the file or members of the file's group |
| a      | all   | All of the above (equivalent to "ugo")                                 |

The following *operators* are supported:

| Operator | Description                                                             |
|----------|-------------------------------------------------------------------------|
| +        | Add the specified modes to the specified classes.                       |
| -        | Remove the specified modes from the specified classes.                  |
| =        | The specified modes are made the exact modes for the specified classes. |

The modes specify which permissions are to be added to or removed from the
specified classes. There are three primary values which correspond to the basic
permissions, and two less frequently-used values that are useful in specific
circumstances:

| Mode | Name              | Description                                 |
|------|-------------------|---------------------------------------------|
| r    | read              | Read a file or list a directory's contents. |
| w    | write             | Write to a file or directory.               |
| x    | execute           | Execute a file or traverse a directory.     |
| X    | "special" execute | This is a slightly more restrictive version of "x".  It applies execute permissions to directories in all cases, and to files **only if** at least one execute permission bit is already set.  It is typically used with the "+" operator and the `-R` option, to give group and/or other access to a large directory tree, without setting execute permissions on normal (non-executable) files (e.g., text files).  For example, `chmod -R go+rx bigdir` would set read and execute permissions on every file (including text files) and directory in the bigdir directory, recursively, for group and other.  The command `chmod -R go+rX bigdir` would set read and execute permissions on every directory, and would set group and other read and execute permissions on files that were already executable by the owner. |
| s    | setgid or sgid    | This setting is typically applied to directories.  If set, any file created in that directory will be associated with the directory's group, rather than with the default file group of the owner. This is useful in setting up directories where many users share access.  This setting is sometimes referred to as the "sticky bit", although that phrase has a historical meaning unrelated to this context. |

Sets of class/operator/mode may separated by commas. Using the above
definitions, the previous (octal notation) example can be done symbolically:

Sets of class/operator/mode may separated by commas. Using the above
definitions, the previous (octal notation) example can be done symbolically:

```console
$ umask
0077
$ touch foo
$ ls -l foo
-rw------- 1 elvis elvis 0 Nov 19 14:49 foo
$ chmod u+x,go+rx foo
$ ls -l foo
-rwxr-xr-x 1 elvis elvis 0 Nov 19 14:49 foo
```
## umask

When a file is created, the permission flags are set according to the file mode
creation mask, which can be set using the `umask` command. The file mode
creation mask (sometimes referred to as "the umask") is a three-digit octal
value whose nine bits correspond to fields 2-10 of the permission flags. The
resulting permissions are calculated via the bitwise AND of the unary
complement of the argument (using bitwise NOT) and the default permissions
specified by the shell (typically 666 for files and 777 for directories).
Common useful values are:

| umask value | File Permissions | Directory Permissions |
|-------------|------------------|-----------------------|
| 002         | -rw-rw-r--       | drwxrwxr-x            |
| 007         | -rw-rw----       | drwxrwx---            |
| 022         | -rw-r--r--       | drwxr-xr-x            |
| 027         | -rw-r-----       | drwxr-x---            |
| 077         | -rw-------       | drwx------            |

An easier way to calculate the permissions is using octal values. For files use `666` and directories use `777` and subtract the umask value.

- File Permission: 666 - umask 
- Directory Permission: 777 - umask

For example a umask value of `002` will be the following: 
 - 666 - 002 = 664 (`rw-rw-r--`)

Here is an example, umask and take note when we create a file named `foo` the permissions are set to `rw-rw-r--` which is `664`:

```console
[shahzeb.siddiqui@login-01 ~]$ umask
0022
[shahzeb.siddiqui@login-01 ~]$ touch foo
[shahzeb.siddiqui@login-01 ~]$ ls -l foo
-rw-r--r-- 1 shahzeb.siddiqui shahzeb.siddiqui.grp 0 Mar 13 14:15 foo
```

## Unix File Groups

Unix file groups provide a means to control access to shared data on
disk and tape.

### Overview of Unix Groups

Every user on a Unix system is a member of one or more Unix groups,
including their primary or default group. Every file (or directory) on
the system has an owner and an associated group. When a user creates a
file, the file's associated group will be the user's default
group. The user (owner) has the ability to change the associated group
to any of the groups to which the user belongs. Unix groups can be
defined that allow users to share data with other users who belong to
the same group.

### Useful Unix Group Commands

| Command          | Description                                  |
|------------------|----------------------------------------------|
|`groups username` |List group membership                         |
|`id username`     |List group membership                         |
|`ls -l`           |List group associated with file or directory  |
|`chgrp`           |Change group associated with file or directory|
|`newgrp`          |Create new shell with different default group |
|`sg`              |Execute command with different default group  |

## Using `getfacl` and `setfacl` for Advanced Access Control

For scenarios where standard file permissions (`chmod`, `chown`) aren't flexible enough to meet your needs. You
can use `getfacl` and `setfacl` to manage Access Control Lists (ACLs) on files and directories at a more granular level. 
This is especially useful for sharing data with specific users or groups on an HPC system.

In example below we see the output of `getfacl` for directory named `/hpc/projects/group.hpc`. We can see below the 
`user` and `group` section is set to `rwx` which means the owner and group have read, write, and execute permissions. The
`other` is set to `---` which means no permissions are set for other users.

```console
[shahzeb.siddiqui@login-01 ~]$ getfacl /hpc/projects/group.hpc
getfacl: Removing leading '/' from absolute path names
# file: hpc/projects/group.hpc
# owner: saransh.kaul
# group: group.hpc
# flags: ss-
user::rwx
group::rwx
other::---
```

### setfacl - Setting ACLs

The `setfacl` command modifies ACLs to grant or revoke specific permissions to users or groups, bypassing limitations of standard permissions. 

The syntax is the following: 

```setfacl -m [u|g]:<name>:<permissions> <file>```

- `u` = user, `g` = group, `<permissions>` = `r` (read), `w` (write), `x` (execute).

### Example: Sharing Data with a User

Scenario: Alice owns file `/hpc/projects/mydata.txt` with permissions `rw-r-----`. Alice wants to share this file with Bob, however Bob, not in the `research` group, needs read/write access.

Steps:

  1. Check current permissions

    ```bash
    ls -l /hpc/projects/mydata.txt
    ```
    
    The output will be similar to:
    
    ```bash
    -rw-r----- 1 alice research 1024 Mar 13 10:00 mydata.txt
    ```
    
    Bob has no access since `other` has no permissions (`---`).

  2. Grant Bob read/write access

    ```bash
    setfacl -m u:bob:rw- /hpc/projects/mydata.txt
    ```

  3. Verify with `getfacl`

    ```bash
    getfacl /hpc/projects/mydata.txt
    ```
  
    The output will be something like:
    
    ```
    # file: /hpc/projects/mydata.txt
    # owner: alice
    # group: research
    user::rw-
    user:bob:rw-    # Bob now has read/write
    group::r--
    others::---
    ```
  
    Bob can now read and write `mydata.txt` despite not being the owner or in the `research` group.


You can also apply recursive sharing to directory and its contents by running the following command:

```bash
setfacl -R -m u:bob:rwx /hpc/projects/team_data
```

You can remove the ACLs for `bob` for `mydata.txt` by running

```bash
setfacl -x u:bob /hpc/projects/mydata.txt
```