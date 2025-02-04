# Troubleshooting User Environment Issues

If you are facing issues with your user environment, we have some recommendations to help you diagnose the problem.

First, we recommend you check the [shell startup](shell_startup.md) files used by your shell type
(`bash`, `sh`, `csh`, `zsh`, `tcsh`). Most user environment issues can be resolved by reviewing the content of your user startup
files. For `bash` users, check your `$HOME/.bashrc` file to see if an environment issue is caused by this file. For `csh`,
check `$HOME/.cshrc` and for zsh, check `$HOME/.zshrc`.
If you update your startup files, you can source the files to apply the changes to the current shell (`source $HOME/.bashrc`) or
log out and log back in.

If you want to know where environment variables are set, you will need to understand the shell startup files. When you `ssh`
into BRUNO system you are in an **interactive login shell**. For `bash` user you will want to look at the table outlined in
[bash startup files](shell_startup.md#bash-startup-files). The `/etc/profile` script, which is typically sourced during shell login,
is available on any Linux distribution, but its contents may vary by distribution. During shell initialization, the shell 
will source files in `/etc/profile.d/*` -- startup files added by the site administrator to provide system-wide defaults to 
all users. We encourage you review the content of each file if you need to troubleshoot your environment. Note that 
`/etc/profile` and files in `/etc/profile.d/*` are owned by the **root** user, so you wouldn't be able to edit them, 
but it's good to check these files when tracing issues related to the startup environment.

Second, you can review the modules loaded at startup. All user environments are initially loaded with a pre-determined 
set of modulefiles selected by the site administrators. You should review the content of your active modules by running 
`module list`, then analyze the content of each modulefile by running `module show <modulefile>`. Many users include
`module load` statements in their `~/.bashrc` to customize their startup modules, but this can cause unexpected 
side-effects when loading other modules.

Here are some additional tips to help you troubleshoot environment issues:

- Check for environments like `PATH`, `LD_LIBRARY_PATH` in startup scripts such as `~/.bashrc` that may cause issues.
A common mistake is to reset one of these environment variables instead of prepending or appending additional paths.
Setting `export PATH=/path/to/dir` will corrupt your shell -- instead set `export PATH=/path/to/dir:$PATH`, which will 
prepend a directory to $PATH.
- Check all environment variables set in your terminal via `env` or `printenv`. If you are looking for a particular pattern,
you can `grep` for it within the long output, e.g., `printenv | grep -i petsc` (the `-i` ignores capitalization).
- Always check the path to the binary that is being run. For instance, if you want to run a python script, double-check the 
path to the python wrapper by invoking `which python` and see if the path makes sense.
- Check whether you are in login or compute node by invoking `hostname`. If you see an output start with `login` then chances
are you are in login node.
- If your shell prompt gets clobbered, try running `reset`, which will reset your terminal settings.

## Troubleshooting Shell Scripts

### Running Shell Scripts

You can run a shell script with your preferred shell (i.e., `bash script.sh`, `csh script.sh`, `sh script.sh`) or you can specify a
full or relative path to the script. A shell script must be executable in order to run when specifying the full path. In example below
there is a permission error, since the file doesn't have execute permission (`x`). You can fix this by running `chmod +x script.sh`.

```shell
[shahzeb.siddiqui@login-01 ~]$ ./script.sh
bash: permission denied: ./script.sh

[shahzeb.siddiqui@login-01 ~]$ ls -l script.sh
-rw-r--r-- 1 shahzeb.siddiqui shahzeb.siddiqui.grp 125 Feb  4 09:33 script.sh
```

### Using Strict Running Modes

Running a script in a stricter mode can help in the debugging process. For example, the default behavior of the bash shell is to
run a script to completion regardless of the success of any commands within the script. Using `set -e` makes the script terminate
immediately when a simple command exits with a non-zero exit status (effectively, upon encountering an error).

The [set](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) 
command is a built-in option that changes shell behavior in `bash` and `sh`.

!!! note
    In `csh`, the `set` command is used for setting variables (`set FOO=BAR`). This is very different from how `set` works in
    `bash` or `sh`: in these shells' syntax, `set` changes the behavior of the current shell.  

In the following example, bash stops execution after running `XYZ` (which is an invalid command). The command `whoami` is not 
run because the script terminates immediately after the invalid command. Note the non-zero script exit code, retrieved by `$?`.

```shell
[shahzeb.siddiqui@login-01 ~]$ cat script.sh
#!/bin/bash
set -e
hostname

# invalid command. Bash will terminate immediately
XYZ

# This command won't be executed
whoami

[shahzeb.siddiqui@login-01 ~]$ bash script.sh
login-01
script.sh: line 6: XYZ: command not found

[shahzeb.siddiqui@login-01 ~]$ echo $?
127
```

The [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) is a character sequence (`!#`) at the beginning of a 
script used to indicate which shell interpreter to use when processing the script. You can also pass any shell options
in the shebang line. In the previous example, we specified `set -e` within the script to modify the behavior of the bash shell.
This option can be passed on the shebang line `#!/bin/bash -e`, which is also equivalent to invoking the script with 
`/bin/bash -e <script>.sh`. Likewise, to enable strict mode for the csh/tcsh shell, you can use `#!/bin/csh -e` and `#!/bin/tcsh -e`.

If we were to `source` this script, the setting would be applied to the current shell. When `set -e` is enabled in the 
current shell or set as a result of sourcing some script, an invalid command (even a typo!) will terminate your shell. 
**Watch out for this behavior if you source any script that enables `set -e`.**

```shell
[shahzeb.siddiqui@login-01 ~]$ source script.sh
login-01
bash: XYZ: command not found...

Connection to login.bruno.czbiohub.org closed.
```

Running in the mode in which the execution of a script terminates upon detecting a non-zero exit status can help you determine 
what went wrong in your script. You can check the exit code of your last command as follows:

```shell
# bash, sh, zsh
echo $?

# csh, tcsh
echo $status
```

For complicated commands, `set -e` may not be sufficient to determine whether there was an error. For example in `bash`, 
the exit code for a piped command (`|`) will be the last command in the pipe. Below we show two examples of non-zero exit 
codes within the pipe operator. The command `grep123` is a typo -- we meant `grep`. In the first example we see a non-zero 
exit code, however in the second example we see a 0 exit code because `wc -l` returned 0:

```shell

[shahzeb.siddiqui@login-01 ~]$ ls -ld | grep123 $user
 grep123: command not found
[shahzeb.siddiqui@login-01 ~]$ echo $?
127

[shahzeb.siddiqui@login-01 ~]$ ls -ld | grep123 $user | wc -l
 grep123: command not found
0
[shahzeb.siddiqui@login-01 ~]$ echo $?
0
```

If you want bash to report the piped command as a failure, consider also running `set -o pipefail`. If we add this setting and 
rerun the same example, we now see the exit code is 127 instead of 0.

```shell
[shahzeb.siddiqui@login-01 ~]$ set -o pipefail
[shahzeb.siddiqui@login-01 ~]$ ls -ld | grep123 $user | wc -l
 grep123: command not found
0
[shahzeb.siddiqui@login-01 ~]$ echo $?
127
```