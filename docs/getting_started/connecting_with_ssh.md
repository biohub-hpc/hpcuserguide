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

## Connecting to Bruno

In order to connect to Bruno cluster you can use the following command:

```command
ssh <username>@login.bruno.czbiohub.org
```

Bruno cluster has two login nodes, `login-01` and `login-02`, you can connect to a specific login node by running

```command
ssh <username>@login-01.bruno.czbiohub.org

ssh <username>@login-02.bruno.czbiohub.org
```

We recommend you add the following to your SSH config file (`$HOME/.ssh/config`) that can help you login to various HPC systems
including Chicago, Bruno and CZII. 

```
Host bruno1
	HostName login01.czbiohub.org

Host bruno2
	HostName login02.czbiohub.org

Host bruno
	HostName login.bruno.czbiohub.org

Host czii1
	HostName czii-login-1.czbiohub.org

Host czii2
	HostName czii-login-2.czbiohub.org

Host chi1
	HostName chi-login-1.czbiohub.org

Host chi2
	HostName chi-login-2.czbiohub.org
```

With this in place, you can connect to any system by using the alias names defined by *Host* to any system as shown below

```console
➜  ~ ssh bruno1
          .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
         / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
        `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'

            _                    _
__ __ _____| |__ ___ _ __  ___  | |_ ___
\ V  V / -_) / _/ _ \ '  \/ -_) |  _/ _ \
 \_/\_/\___|_\__\___/_|_|_\___|  \__\___/

                        ____  _____  _    _ _   _  ____
                       |  _ \|  __ \| |  | | \ | |/ __ \
                       | |_) | |__) | |  | |  \| | |  | |
                       |  _ <|  _  /| |  | | . ` | |  | |
                       | |_) | | \ \| |__| | |\  | |__| |
                       |____/|_|  \_\\____/|_| \_|\____/


                                      _                  _         _
                          __ _ _ _   | |_  _ __  __   __| |_  _ __| |_ ___ _ _
                         / _` | ' \  | ' \| '_ \/ _| / _| | || (_-<  _/ -_) '_|
                         \__,_|_||_| |_||_| .__/\__| \__|_|\_,_/__/\__\___|_|
                                          |_|

          .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
         / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
        `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'

     #hpc-community: https://czbiohubnetwork.enterprise.slack.com/archives/C02CF73PLC8
       #hpc-czii: https://czbiohubnetwork.enterprise.slack.com/archives/C058XEVPJLA
      #hpc-chicago: https://czbiohubnetwork.enterprise.slack.com/archives/C07LNP3BW3Y
        #hpc-ny: https://czbiohubnetwork.enterprise.slack.com/archives/C07LCARK7HR

                        User Guide: https://hpc.czbiohub.org


Notice to all users:
   The BRUNO Environments must not be used for storing, processing, or transmitting
   private or protected data, including:
       * Personally Identifiable Information (PII)
       * Protected Health Information (PHI)
       * Any other data protected by obligations of confidentiality

Activate the web console with: systemctl enable --now cockpit.socket

Last login: Thu Jan 30 08:59:25 2025 from 100.64.0.34
```

!!! warning

    Please do not X11 forwarding with `ssh -X`, we recommend you use [Open OnDemand](https://ondemand.czbiohub.org) for 
    GUI applications.

## Troubleshooting SSH issues

### **"Issue: Connection Refused" or "Connection Timed Out"**

Please verify the hostname you are trying to connect. A typo in the hostname can cause this error. You can verify the hostname by running 
`ping <hostname>` or run ssh in verbose mode (`-v`). You may specify additional verbosity with `-vv`, or `-vvv`.

```console
ssh -vvv <user>@<hostname>
```

### **"Issue: Permission denied (publickey)"**

Please confirm your private key is correct and loaded. You should have the following files 

- `~/.ssh/id_rsa`: Private Key
- `~/.ssh/id_rsa.pub`: Public Key

```console
ssh -i ~/.ssh/id_rsa <user>@<hostname>
```

Make sure the key permission are restricted to `600` which can be done by running

```console
chmod 600 ~/.ssh/id_rsa
```

### **"Issue: Host key verification failed"**

This could be a symptom of the server's host key has changed. To address this problem you will need to remove the old key from your **known_hosts** file.
The known hosts file is located at `~/.ssh/known_hosts`. You can remove the entry by running the following command

```console
ssh-keygen -R <hostname>
```

For instance, if you were trying to connect to `login.bruno.czbiohub.org`, you would run

```console
ssh-keygen -R login.bruno.czbiohub.org
```

Once the key is removed, verify you can login to cluster by running

```console
ssh <user>@login.bruno.czbiohub.org
```

### General Tips

1. For any ssh related issues, please review the ssh configuration `~/.ssh/config`. If you need to make change consider making a backup of the file before making any changes.
2. Use ssh verbose mode `ssh -vv` to get more information about the connection.
3. Make sure you are using the correct public and private key pair when connecting.
4. Review files `~/.ssh/authorized_keys` and `~/.ssh/known_hosts` for any issues.
5. Make sure you have a directory `$HOME/.ssh` with permissions `0700`. 

