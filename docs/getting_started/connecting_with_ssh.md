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

