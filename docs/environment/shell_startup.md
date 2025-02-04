# Shell Startup

## What is interactive shell?

An **interactive shell** interacts with user inputs such as typing commands whereas non-interactive shell 
recieves input from another source such as script. An interactive shell will typically set the variable 
`PS1` that is used to display the prompt in your shell. This variable is unset for non-interactive shell.
You can test this by running following command in your shell 

```bash
if [ -z "$PS1" ]; then
         echo This shell is not interactive
else
         echo This shell is interactive
fi
```

## What is login shell?

A **login shell** is created upon log in to a machine which is done via `ssh`. A non-login shell is typically 
started when you start another shell, run a program, or start graphical console. You can test if you 
are in login shell via following command: 

``` console
[shahzeb.siddiqui@login-01 ~]$ shopt -q login_shell && echo 'Login shell' || echo 'Not login shell'
Login shell
```

!!! note
    
    `shopt` is builtin command for bash shell. This will not work if you are using `csh/tcsh`.
    
A script (including a jobscript submitted via `sbatch`) runs in a non-login shell, however one can configure script to run in login
shell via `bash --login <script>` or `csh -l <script>`.

For more details on bash see following links:

  - [Bash Startup Files](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bash-Startup-Files)
  - [Interactive Shells](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Interactive-Shells)

## Bash startup files 

In table below you can see the bash startup files sourced depending on the shell mode. The numbers 
indicate the order of files being sourced.

!!! note
    For Interactive Login, bash will read the files  in the following order `~/.bash_profile`, `~/.bash_login` 
    and `~/.profile` and find first one that exists and is readable (`r` permission). For more details see 
    [bash startup files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html).
    
!!! note    
    BASH_ENV is an environment variable that generally points a file that is sourced when bash 
    is in non-interactive mode such as running a script. Shown below is the expected value
    
    ```bash
    [shahzeb.siddiqui@login-01 ~]$ echo $BASH_ENV                                          
    /hpc/modules/lmod/lmod/init/bash
    ```
      
| File                        | Interactive Login | Interactive Non Login | Non Interactive Non Login |
|-----------------------------|-------------------|-----------------------|---------------------------|
| `/etc/profile`              | 1                 |                       |                           |
| `/etc/bashrc`               | 1                 |                       |                           |
| `~/.bashrc`                 |                   | 2                     |                           |                       
| `~/.bash_profile`           | 2                 |                       |                           |                        
| `~/.bash_login`             | 3                 |                       |                           |                          
| `~/.profile`                | 4                 |                       |                           |                        
| `~/.bash_logout`            | 5 (logout)        |                       |                           |                          
| Path included in `BASH_ENV` |                   |                       | 1                         |                         

A few important rules to remember when working with bash shell.

- `~/.bash_logout` is also run on both interactive and non-interactive login shells upon exit 
    
- `bash --noprofile` can be used to prevent loading startup files `/etc/profile` or any of the user
   startup files: `~/.bash_profile`, `~/.bash_login`, or `~/.profile` when bash is invoked in login 
   shell. This can be useful to help isolate issues with your startup configuration.      
 
- When you ssh into BRUNO systems (interactive login) the `$HOME/.bashrc` is sourced on Interactive Login shell. 
  This was done to ensure consistency between startup configuration files (`~/.bashrc` vs `~/.bash_profile`). 
  The `~/.bashrc` is typically used for defining alias and functions that needs to be accessible in subshells or as part 
  of scripts whereas `~/.bash_profile` is used for specifying configuration in your login shell that you expect to 
  use in your terminal. 
    
- `bash --rcfile` option can be used to inform bash to execute commands from an alternate file instead of `~/.bashrc` when 
  running in interactive shell. You can avoid bash from reading any rc file by specifying `bash --norc` which will inform bash 
  from not reading `~/.bashrc`. 
    
- The `~/.profile` is the original profile script for Bourne Shell (`sh`) whereas `bash` introduced `~/.bash_profile`
  that is read by bash which is incompatible with standard Bourne Shell. If you want to define configuration compatible with `sh` 
  and `bash` you should specify this in `~/.profile`.  For users changing shell from `sh` to `bash` please review the
  [major difference in Bourne Shell](https://www.gnu.org/software/bash/manual/bash.html#Major-Differences-From-The-Bourne-Shell). 

- Submitting a job such via `sbatch` will inherit the user environment, however you can use `sbatch --export=NONE` to
  prevent any environments to be set on compute node when running job. The default behavior of slurm is
  `--export=ALL` which will export all user environment into compute node. 
  For more details on sbatch see man pages (`man sbatch`)

![Bash Startup Files](https://shreevatsa.files.wordpress.com/2008/03/bashstartupfiles1.png)

## CSH startup files

| File              | Interactive Login | Interactive Non Login  |
|-------------------|-------------------|------------------------|
| `/etc/csh.cshrc`  | 1                 | 1                      |   
| `/etc/csh.login`  | 2                 |                        |  
| `~/.tcshrc`       | 3                 | 2                      |  
| `~/.cshrc`        | 4                 | 3                      |  
| `~/.history`      | 5                 |                        |  
| `~/.login`        | 6                 |                        |
| `~/.cshdirs`      | 7                 |                        |
| `~/.logout`       | 8 (logout)        |                        |
| `/etc/csh.logout` | 9 (logout)        |                        |

!!! note
    `csh` will read the following files (3-7) in table above in the order specified, if file is found csh will not 
    read the remaining files.
    
For more details on csh see https://linux.die.net/man/1/csh    

## ZSH startup files

| File            | Interactive Login | Interactive Non Login  |
|-----------------|-------------------|------------------------|
| `/etc/zshenv`   | 1                 | 1                      |   
| `~/.zshenv`     | 2                 | 2                      |  
| `/etc/zprofile` | 3                 |                        | 
| `~/.zprofile`   | 4                 |                        |  
| `/etc/zshrc`    | 5                 | 3                      |   
| `~/.zshrc`      | 6                 | 4                      |  
| `/etc/zlogin`   | 7                 |                        |    
| `~/.login`      | 8                 |                        |
| `~/.zlogout`    | 9 (logout)        |                        |
| `/etc/zlogout`  | 10 (logout)       |                        |
   
In zsh the `*profile` files are sourced before `*rc` files. 

For more details on the zsh startup behavior see 
[section 5.1 Startup/Shutdown Files](https://zsh.sourceforge.io/Doc/Release/Files.html).  

You may find this article on 
[Zsh/Bash startup files](https://shreevatsa.wordpress.com/2008/03/30/zshbash-startup-files-loading-order-bashrc-zshrc-etc/) 
useful to understand which files get sourced.