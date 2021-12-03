# Connecting with SSH

The most basic and powerful way to connect and use the resources is via `ssh` to a login node. How to accomplish that will depend on what Operating System you use on your laptop or desktop.

## Mac OS X and Linux

Mac OS X and all Linux distributions have, by default, a terminal application
and ssh clients. While Linux has a variety of Terminal applications with an
expansive array of features to choose from, the default Terminal in Mac OS X is
somewhat limited. If you use a Mac, you might want to try
[iTerm2](https://iterm2.com/) as it has many enhancements over the built in
Terminal app.

## Windows

The first step to connecting from Windows is choosing and installing an SSH client. Some available free options are

 * [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
 * [MobaXterm](https://mobaxterm.mobatek.net/)
 * [WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

In particular the combination of [MobaXterm](https://mobaxterm.mobatek.net/)
with [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) can
***almost*** make working from Windows in a Linux environment a much more
pleasant experience (ignoring the pain and effort of getting it set up and
configured, of course).  Any of these will get a functional `ssh` client onto
the system. 

## Making the connection

Once a terminal application is opened, tehn connecting is as simple as `ssh FIRST.LAST@cluster.czbiohub.org`, for example:

```
(base) [griznog@lepomis ~]$ ssh john.hanks@cluster.czbiohub.org
Last login: Thu Oct 14 15:20:09 2021 from 10.79.124.15
[john.hanks@cluster ~]$ 
```

Note, the cluster is only visible on the BioHub network, via the ssh.czbiohub.org jumphost or over a VPN connection.
