# Operating System

The HPC environment is built on [Rocky Linux 8](https://rockylinux.org/) as the
base operating system. A full suite of OS supplied software is installed,
including most expected Linux/Unix tools, several desktop environments, Office
and Internet applications and development libraries and tools. Where there is
an option to install a package using a supported RPM for [Rocky Linux
8](https://rockylinux.org/), this is the preferred way to get the application
into the cluster environment. 

Shown below is the Operating System version

```console
[shahzeb.siddiqui@login-02 ~]$ cat /etc/os-release
NAME="Rocky Linux"
VERSION="8.10 (Green Obsidian)"
ID="rocky"
ID_LIKE="rhel centos fedora"
VERSION_ID="8.10"
PLATFORM_ID="platform:el8"
PRETTY_NAME="Rocky Linux 8.10 (Green Obsidian)"
ANSI_COLOR="0;32"
LOGO="fedora-logo-icon"
CPE_NAME="cpe:/o:rocky:rocky:8:GA"
HOME_URL="https://rockylinux.org/"
BUG_REPORT_URL="https://bugs.rockylinux.org/"
SUPPORT_END="2029-05-31"
ROCKY_SUPPORT_PRODUCT="Rocky-Linux-8"
ROCKY_SUPPORT_PRODUCT_VERSION="8.10"
REDHAT_SUPPORT_PRODUCT="Rocky Linux"
REDHAT_SUPPORT_PRODUCT_VERSION="8.10"
```

## System Software RPMs

As part of the OS installation, a number of software packages are installed as RPMs using `dnf` which is the preferred package manager for installing software. If 
you prefer `yum` you may also use this since its a symlink to `dnf`. 

For instance if you want to see all installed packages, you can run either of the following which will show list of RPMs installed. 

```console
yum list --installed

rpm -qa
```

To see what files are provided by a particular RPM, you can run the following command. 

```console
rpm -ql <package_name>
```

For instance if you want to see all files provided by package name `bash` you can run the following command. 

```console
[shahzeb.siddiqui@login-02 ~]$ rpm -ql bash
/etc/skel/.bash_logout
/etc/skel/.bash_profile
/etc/skel/.bashrc
/usr/bin/alias
/usr/bin/bash
/usr/bin/bashbug
/usr/bin/bashbug-64
/usr/bin/bg
/usr/bin/cd
/usr/bin/command

...
```

For instance if you want to find out what RPM provides the `bzip2` command, you can run the following command. 

```console
[shahzeb.siddiqui@login-02 ~]$ rpm -q --whatprovides /usr/bin/bzip2
bzip2-1.0.6-27.el8_10.x86_64
```

We can confirm this package does provide the `/usr/bin/bzip2` program

```console
[shahzeb.siddiqui@login-02 ~]$ rpm -ql bzip2 | grep /usr/bin/bzip2
/usr/bin/bzip2
/usr/bin/bzip2recover
```

If you would like to have a particular package installed that is not already available, please contact the HPC team and we will work to get it installed.
