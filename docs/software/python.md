# Python

In order to use `python` please use the anaconda module 

```console
module load anaconda
```

## Python Virtual Environment via venv

You can also create light-weight virtual environments using the [venv](https://docs.python.org/3/library/venv.html) module. This
is provided by python distribution. To get started you need to specify path to write virtual environment. In example below we will
write virtual environment in **~/.pyenv/test**:

```console
[shahzeb.siddiqui@login-02 ~]$ python -m venv ~/.pyenv/test
```

This will create a directory structure similar to python virtual environment that contains `bin`, `include`, `lib`, etc...

```console
[shahzeb.siddiqui@login-02 ~]$ ls ~/.pyenv/test/
bin  include  lib  lib64  pyvenv.cfg
```

To activate the environment you can run the following:

```console
[shahzeb.siddiqui@login-02 ~]$ . ~/.pyenv/test/bin/activate
```

The `python` interpreter can be shown using `which python` which comes from the virtual environment. We can see with output of `pip list` this
is a smaller virtual environment as posed to conda environment. This may be useful when you want to create a light-weight virtual environment.

```console
(test) [shahzeb.siddiqui@login-02 ~]$ which python
~/.pyenv/test/bin/python

(test) [shahzeb.siddiqui@login-02 ~]$ pip list
Package    Version
---------- -------
pip        20.2.3
setuptools 49.2.1
WARNING: You are using pip version 20.2.3; however, version 25.0.1 is available.
You should consider upgrading via the '/home/shahzeb.siddiqui/.pyenv/test/bin/python -m pip install --upgrade pip' command.
```

To exit the environment you can run `deactivate` which will change your prompt and your python interpreter will be changed to the
system python interpreter.

```console
(test) [shahzeb.siddiqui@login-02 ~]$ deactivate
[shahzeb.siddiqui@login-02 ~]$

[shahzeb.siddiqui@login-02 ~]$ which python
/hpc/apps/anaconda/2021_09_16/bin/python
```

To remove the virtual environment you will need to manually `rm -rf` the location since they were created outside of 
`conda` environment management. 

## Pipenv 

[Pipenv](https://pipenv.pypa.io/en/latest/) is a tool that aims to bring the best of all packaging worlds 
(bundled dependencies, virtual environments, and package management) to the Python world. It automatically creates and 
manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. 
It also generates the ever-important **Pipfile.lock**, which is used to produce deterministic builds.

To get started you can install `pipenv` using `pip` which is the python package manager. 

```console
[shahzeb.siddiqui@login-02 ~]$ pip install --user pipenv
```

I have this installed in my home directory at `~/.local/bin/pipenv`, if its not set in your $PATH you may want to update the PATH environment


```console
[shahzeb.siddiqui@login-02 ~]$ which pipenv
~/.local/bin/pipenv
```

pipenv is designed to work well for developers, you can create virtual environment in same location as your project code. For demonstration, 
we have a directory named `pipenv/demo`, we can navigate to this directory and create a virtual environment using `pipenv`:

```console
[shahzeb.siddiqui@login-02 ~]$ mkdir -p pipenv/demo
[shahzeb.siddiqui@login-02 ~]$ cd pipenv/demo
```

To create a python virtual environment you can run the following command. The `--python` option can be used to specify the python version:

```console
[shahzeb.siddiqui@login-02 demo]$ pipenv --python 3.8
Creating a virtualenv for this project...
Pipfile: /home/shahzeb.siddiqui/pipenv/demo/Pipfile
Using /usr/bin/python3.8 (3.8.17) to create virtualenv...
⠼ Creating virtual environment...Using base prefix '/usr'
New python executable in /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2/bin/python3.8
Also creating executable in /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2/bin/python
Installing setuptools, pip, wheel...done.
Running virtualenv with interpreter /usr/bin/python3.8

✔ Successfully created virtual environment!
Virtualenv location: /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2
Creating a Pipfile for this project...
```

You can see there is a bit more information provided by `pipenv` when creating a virtual environment, including location of the virtual
environment and python interpreter. To activate the environment you can run `pipenv shell` and you will see the prompt change. Note that 
`pipenv` knows how to activate the environment as pose to `venv` where you need to specify the path to the `activate` script.


```console
[shahzeb.siddiqui@login-02 demo]$ pipenv shell
Launching subshell in virtual environment...
 . /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2/bin/activate
[shahzeb.siddiqui@login-02 demo]$  . /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2/bin/activate

(demo) [shahzeb.siddiqui@login-02 demo]$ which python
~/.local/share/virtualenvs/demo-xfXBTVr2/bin/python
```

To deactivate the environment you can run `exit` which will change the prompt back to the system python interpreter.

```console
(demo) [shahzeb.siddiqui@login-02 demo]$ exit
[shahzeb.siddiqui@login-02 demo]$ which python
/hpc/apps/anaconda/2021_09_16/bin/python
```

The virtual environment can be reactivated by  navigating to the desired directory and running `pipenv shell` which
will reactivate the same environment.

```console
[shahzeb.siddiqui@login-02 demo]$ pipenv shell
Launching subshell in virtual environment...
 . /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2/bin/activate
[shahzeb.siddiqui@login-02 demo]$  . /home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2/bin/activate
```

To remove the environment, you will need to exit the environment first and run the `pipenv --rm` command which will infer the virtual
environment based on your current working directory

```console
[shahzeb.siddiqui@login-02 demo]$ pipenv --rm
Removing virtualenv (/home/shahzeb.siddiqui/.local/share/virtualenvs/demo-xfXBTVr2)...
```

Pipenv is a great alternative when it comes to managing light weight virtual environment and you are working open-source projects on GitHub/GitLab. 
For example, let's assume you want to clone a project from GitHub and setup the environment locally. You can clone the project and use `pipenv` to 
create the virtual environment in the project directory which will create a `Pipfile`.

For demonstration, we will clone a project named `buildtest` which requires python and its dependencies are provided in `requirements.txt`. We 
can do this as follows

```console
[shahzeb.siddiqui@login-02 github]$ git clone https://github.com/buildtesters/buildtest.git
Cloning into 'buildtest'...
remote: Enumerating objects: 41496, done.
remote: Counting objects: 100% (236/236), done.
remote: Compressing objects: 100% (163/163), done.
remote: Total 41496 (delta 131), reused 106 (delta 73), pack-reused 41260 (from 3)
Receiving objects: 100% (41496/41496), 55.45 MiB | 56.27 MiB/s, done.
Resolving deltas: 100% (28217/28217), done.

[shahzeb.siddiqui@login-02 github]$ cd buildtest/
```

Next, we will create a virtual environment using `pipenv`

!!! note

    We need python 3.9 or higher to install buildtest

```console
[shahzeb.siddiqui@login-02 buildtest]$ pipenv --python 3.9
Creating a virtualenv for this project...
Pipfile: /home/shahzeb.siddiqui/github/buildtest/Pipfile
Using /usr/bin/python3.9 (3.9.20) to create virtualenv...
⠴ Creating virtual environment...Using base prefix '/usr'
New python executable in /home/shahzeb.siddiqui/.local/share/virtualenvs/buildtest-AfgnSl8c/bin/python3.9
Also creating executable in /home/shahzeb.siddiqui/.local/share/virtualenvs/buildtest-AfgnSl8c/bin/python
Installing setuptools, pip, wheel...done.
Running virtualenv with interpreter /usr/bin/python3.9

✔ Successfully created virtual environment!
Virtualenv location: /home/shahzeb.siddiqui/.local/share/virtualenvs/buildtest-AfgnSl8c
requirements.txt found in /home/shahzeb.siddiqui/github/buildtest instead of Pipfile! Converting...
✔ Success!
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did.
We recommend updating your Pipfile to specify the "*" version, instead.
```

Next, we will activate the environment and install the dependencies, for purposes we omitted the output since output is too long

```console
[shahzeb.siddiqui@login-02 buildtest]$ pipenv shell
Launching subshell in virtual environment...
 . /home/shahzeb.siddiqui/.local/share/virtualenvs/buildtest-AfgnSl8c/bin/activate
[shahzeb.siddiqui@login-02 buildtest]$  . /home/shahzeb.siddiqui/.local/share/virtualenvs/buildtest-AfgnSl8c/bin/activate

(buildtest) [shahzeb.siddiqui@login-02 buildtest]$ pip install -r requirements.txt
```

To properly install buildtest we can `source` the setup.sh script which will properly install buildtest and update the PATH environment that
provides the `buildtest` command.

```console
(buildtest) [shahzeb.siddiqui@login-02 buildtest]$ source setup.sh
(buildtest) [shahzeb.siddiqui@login-02 buildtest]$ which buildtest
~/github/buildtest/bin/buildtest

(buildtest) [shahzeb.siddiqui@login-02 buildtest]$ buildtest -V
buildtest version 2.1
```

## References

- Python Documentation: https://docs.python.org/3/
- Pipenv: https://pipenv.pypa.io/en/latest/
- Python Virtual Environment: https://docs.python.org/3/library/venv.html
