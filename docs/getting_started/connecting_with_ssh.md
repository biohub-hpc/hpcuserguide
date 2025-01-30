# Connecting with SSH

The most basic and powerful way to connect and use the resources is via `ssh`
to a login node. How to accomplish that will depend on what Operating System
you use on your laptop or desktop.

## Mac OS X and Linux

Mac OS X and all Linux distributions have, by default, a terminal application
and ssh clients. While Linux has a variety of Terminal applications with an
expansive array of features to choose from, the default Terminal in Mac OS X is
somewhat limited. If you use a Mac, you might want to try
[iTerm2](https://iterm2.com/) as it has many enhancements over the built in
Terminal app.

## Windows

The first step to connecting from Windows is choosing and installing an SSH
client. Some available free options are

 * [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
 * [MobaXterm](https://mobaxterm.mobatek.net/)
 * [WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

In particular the combination of [MobaXterm](https://mobaxterm.mobatek.net/)
with [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) can
***almost*** make working from Windows in a Linux environment an acceptable
experience (ignoring the pain and effort of getting it set up and configured,
of course).  Any of these will get a functional `ssh` client onto the system. 

## Making the connection

Once at a terminal with an available `ssh`, connecting is as simple as `ssh
USERNAME@HOSTNAME`, for example, to connect to BRUNO I would use my username, john.hanks, and `ssh` to the BRUNO login nodes:

```
(base) [griznog@lepomis ~]$ ssh john.hanks@login.bruno.czbiohub.org
Last login: Thu Oct 14 15:20:09 2021 from 10.79.124.15
[john.hanks@login-01 ~]$ 
```

