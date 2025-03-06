# The Conda Module

[Anaconda Python](https://www.anaconda.com/) is a very popular Python
environment/distribution, which is made available via the centrally managed
`anaconda` module. Typical usage of `conda` is to use it to manage/access
multiple virtual environments, allowing the install of Python tools and
packages that would otherwise conflict and be impossible to install into the
same location. 

To get started, you need to load `anaconda` module this will grant you access to `conda`.

```console
[shahzeb.siddiqui@login-02 ~]$ module load anaconda
[shahzeb.siddiqui@login-02 ~]$ conda --version
conda 4.12.0
```

You can see list of conda environments installed with the centrally managed `anaconda` module by running `conda env list`:

```console
[shahzeb.siddiqui@login-02 ~]$ conda env list
# conda environments:
#
base                  *  /hpc/apps/x86_64/anaconda/2021_09_16
alphafold_v2.2.0         /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphafold_v2.2.0
alphapept                /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphapept
alphapept-gui            /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphapept-gui
excellxgene              /hpc/apps/x86_64/anaconda/2021_09_16/envs/excellxgene
jupyter-test             /hpc/apps/x86_64/anaconda/2021_09_16/envs/jupyter-test
labelstudio              /hpc/apps/x86_64/anaconda/2021_09_16/envs/labelstudio
napari                   /hpc/apps/x86_64/anaconda/2021_09_16/envs/napari
stui                     /hpc/apps/x86_64/anaconda/2021_09_16/envs/stui
tensorboard              /hpc/apps/x86_64/anaconda/2021_09_16/envs/tensorboard
```

!!! warning "Warning: `conda init` breaks things"
    Running `conda init` will add code to your `${HOME}/.bashrc` file which will
    place `conda` installed python and dependent libraries in your `${PATH}`. This will
    potentially break other applications which depend on the system installed python
    and libraries in many subtle ways. 

## Creating Conda Environments

The `conda create` command is responsible for creating a conda environment. There are few ways to 
create conda environment which we can discuss briefly.

The easiest way to create an environment is by named environment. In command below we create an environment named `myenv` using python=3.8

```console
conda env create -n myenv python=3.8
```

You can also create conda environments with prefix path such as one below

```console
conda env create -n custom_env -p /tmp/.conda-envs python=3.9
```

You can also create conda environments from an `environment.yml` file which is a conda specific environment file used
for creating environments. 

```console
conda env create -f environment.yml
```

```yaml
Shown below we create a conda environment named `myenv`

```console
[shahzeb.siddiqui@login-02 ~]$ conda create -n myenv python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /hpc/mydata/shahzeb.siddiqui/.conda-envs/myenv

  added / updated specs:
    - python=3.8


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu
  ca-certificates    pkgs/main/linux-64::ca-certificates-2025.2.25-h06a4308_0
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.40-h12ee557_0
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_1
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0
  openssl            pkgs/main/linux-64::openssl-3.0.16-h5eee18b_0
  pip                pkgs/main/linux-64::pip-24.2-py38h06a4308_0
  python             pkgs/main/linux-64::python-3.8.20-he870216_0
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0
  setuptools         pkgs/main/linux-64::setuptools-75.1.0-py38h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.45.3-h5eee18b_0
  tk                 pkgs/main/linux-64::tk-8.6.14-h39e8969_0
  wheel              pkgs/main/linux-64::wheel-0.44.0-py38h06a4308_0
  xz                 pkgs/main/linux-64::xz-5.6.4-h5eee18b_1
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_1


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate myenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

Conda will show you message on how to activate/deactivate environment which allows you to switch between environments. To use
this environment you can activate it using `conda activate myenv`. Take note that the `python` wrapper is installed in the conda environment


```console
[shahzeb.siddiqui@login-02 ~]$ conda activate myenv
(/hpc/mydata/shahzeb.siddiqui/.conda-envs/myenv) [shahzeb.siddiqui@login-02 ~]$ which python
/hpc/mydata/shahzeb.siddiqui/.conda-envs/myenv/bin/python
```

When you run `conda env list`, conda will show the active conda environment using the asterik symbol (`*`) and you can see below

```console
(/hpc/mydata/shahzeb.siddiqui/.conda-envs/myenv) [shahzeb.siddiqui@login-02 ~]$ conda env list
# conda environments:
#
base                     /hpc/apps/x86_64/anaconda/2021_09_16
alphafold_v2.2.0         /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphafold_v2.2.0
alphapept                /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphapept
alphapept-gui            /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphapept-gui
excellxgene              /hpc/apps/x86_64/anaconda/2021_09_16/envs/excellxgene
jupyter-test             /hpc/apps/x86_64/anaconda/2021_09_16/envs/jupyter-test
labelstudio              /hpc/apps/x86_64/anaconda/2021_09_16/envs/labelstudio
napari                   /hpc/apps/x86_64/anaconda/2021_09_16/envs/napari
stui                     /hpc/apps/x86_64/anaconda/2021_09_16/envs/stui
tensorboard              /hpc/apps/x86_64/anaconda/2021_09_16/envs/tensorboard
myenv                 *  /hpc/mydata/shahzeb.siddiqui/.conda-envs/myenv
```

To deactivate the conda environment, you just run `conda deactivate` and your prompt will change. Take note the path to `python`
interpreter is now using one provided by anaconda which is shared by all users.

```console
(/hpc/mydata/shahzeb.siddiqui/.conda-envs/myenv) [shahzeb.siddiqui@login-02 ~]$ conda deactivate
[shahzeb.siddiqui@login-02 ~]$ which python
/hpc/apps/anaconda/2021_09_16/bin/python
```

Conda environments will be installed in HOME directory at `$HOME/.conda/envs` which is subject to quota limits since quota
is small. We recommend you store your conda environments in **$MYDATA** which has a larger quota limit.

To install conda environments in $MYDATA, you can use the `conda create -p` option which specifies a prefix file path where
conda environments will be written.

As shown below we create a conda environment in $MYDATA:

```console
[shahzeb.siddiqui@login-02 ~]$ conda create -p $MYDATA/.conda/test_env python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /hpc/mydata/shahzeb.siddiqui/.conda/test_env

  added / updated specs:
    - python=3.8


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu
  ca-certificates    pkgs/main/linux-64::ca-certificates-2024.12.31-h06a4308_0
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.40-h12ee557_0
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_1
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0
  openssl            pkgs/main/linux-64::openssl-3.0.15-h5eee18b_0
  pip                pkgs/main/linux-64::pip-24.2-py38h06a4308_0
  python             pkgs/main/linux-64::python-3.8.20-he870216_0
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0
  setuptools         pkgs/main/linux-64::setuptools-75.1.0-py38h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.45.3-h5eee18b_0
  tk                 pkgs/main/linux-64::tk-8.6.14-h39e8969_0
  wheel              pkgs/main/linux-64::wheel-0.44.0-py38h06a4308_0
  xz                 pkgs/main/linux-64::xz-5.6.4-h5eee18b_1
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_1


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate /hpc/mydata/shahzeb.siddiqui/.conda/test_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

You can see the conda environment in output of `conda env list` and we can activate the environment directly. We can see that
`python` is installed in the conda environment in `$MYDATA`:

```console
[shahzeb.siddiqui@login-02 ~]$ conda env list | grep $MYDATA
                         /hpc/mydata/shahzeb.siddiqui/.conda/test_env
                         
[shahzeb.siddiqui@login-02 ~]$ conda activate /hpc/mydata/shahzeb.siddiqui/.conda/test_env

(/hpc/mydata/shahzeb.siddiqui/.conda/test_env) [shahzeb.siddiqui@login-02 ~]$ which python
/hpc/mydata/shahzeb.siddiqui/.conda/test_env/bin/python                         
```

In this example below we have an `environment.yml` file which we can use to create a conda environment. 
The `environment.yml` file is the following. This configuration will install python 3.9, numpy, pandas, scipy. 

```yaml
name: dev_environment  # Name of the environment
dependencies:
  - python=3.9  # Specify Python version
  - numpy
  - pandas
  - scipy
```

Shown below we see the installation from environment, you can see that packages `numpy`, `pandas` and `scipy` are installed during
the creation of the conda environment.

```console
[shahzeb.siddiqui@login-02 ~]$ conda env create -f environment.yml
Collecting package metadata (repodata.json): done
Solving environment: done

Downloading and Extracting Packages
pybind11-abi-4       | 14 KB     | ########################################################################################################################## | 100%
numpy-2.0.2          | 11 KB     | ########################################################################################################################## | 100%
mkl_random-1.2.8     | 319 KB    | ########################################################################################################################## | 100%
numpy-base-2.0.2     | 7.9 MB    | ########################################################################################################################## | 100%
numexpr-2.10.1       | 173 KB    | ########################################################################################################################## | 100%
pandas-2.2.3         | 12.9 MB   | ########################################################################################################################## | 100%
libgfortran-ng-11.2. | 20 KB     | ########################################################################################################################## | 100%
mkl_fft-1.3.11       | 199 KB    | ########################################################################################################################## | 100%
python-dateutil-2.9. | 279 KB    | ########################################################################################################################## | 100%
mkl-service-2.4.0    | 68 KB     | ########################################################################################################################## | 100%
bottleneck-1.4.2     | 126 KB    | ########################################################################################################################## | 100%
pytz-2024.1          | 212 KB    | ########################################################################################################################## | 100%
libgfortran5-11.2.0  | 2.0 MB    | ########################################################################################################################## | 100%
scipy-1.13.1         | 22.0 MB   | ########################################################################################################################## | 100%
setuptools-72.1.0    | 2.4 MB    | ########################################################################################################################## | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate dev_environment
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```
### Creating conda environment automatically in $MYDATA

In order to install conda environments in $MYDATA which has a larger quota limit, you can add the following line to your `~/.condarc` file

```console
[shahzeb.siddiqui@login-02 ~]$ cat ~/.condarc
envs_dirs:
  - $MYDATA/.conda-envs
```

With this change you can create conda environments in $MYDATA without specifying the full path. We can confirm by 
`conda config --show envs_dirs` which will show the path where conda environments are installed. Conda will look for 
environments in the order specified in `envs_dirs` and will create environments in the first directory that is writable.

Since $HOME/.conda/envs is the default location, by adding $MYDATA/.conda-envs first in the list, conda will prefer 
to install environments in $MYDATA.

```console
[shahzeb.siddiqui@login-02 ~]$ conda config --show envs_dirs
envs_dirs:
  - /hpc/mydata/shahzeb.siddiqui/.conda-envs
  - /home/shahzeb.siddiqui/.conda/envs
  - /hpc/apps/x86_64/anaconda/2021_09_16/envs
```

Now let's install a conda environment, take note of the environment location. 

```console
[shahzeb.siddiqui@login-02 ~]$ conda create -n demo python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /hpc/mydata/shahzeb.siddiqui/.conda-envs/demo

  added / updated specs:
    - python=3.8


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu
  ca-certificates    pkgs/main/linux-64::ca-certificates-2025.2.25-h06a4308_0
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.40-h12ee557_0
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_1
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0
  openssl            pkgs/main/linux-64::openssl-3.0.16-h5eee18b_0
  pip                pkgs/main/linux-64::pip-24.2-py38h06a4308_0
  python             pkgs/main/linux-64::python-3.8.20-he870216_0
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0
  setuptools         pkgs/main/linux-64::setuptools-75.1.0-py38h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.45.3-h5eee18b_0
  tk                 pkgs/main/linux-64::tk-8.6.14-h39e8969_0
  wheel              pkgs/main/linux-64::wheel-0.44.0-py38h06a4308_0
  xz                 pkgs/main/linux-64::xz-5.6.4-h5eee18b_1
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_1


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate demo
#
# To deactivate an active environment, use
#
#     $ conda deactivate

[shahzeb.siddiqui@login-02 ~]$ conda env list | grep demo
demo                     /hpc/mydata/shahzeb.siddiqui/.conda-envs/demo
```

## Installing Packages in conda environment

You can install packages in conda environment using `conda install` command. First you will need to be in a conda environment
before you install packages. For this example, I have created a conda environment `myenvironment`

```console
[shahzeb.siddiqui@login-02 ~]$ conda activate myenvironment
```

Once you have activated an environment, you can install packages. In example below we will install `matplotlib` and `numpy` and pin the versions

```console
(myenvironment) [shahzeb.siddiqui@login-02 ~]$ conda install matplotlib=3.5 numpy=1.21
```

Once installation is complete, we can confirm the packages are installed using the `conda list` command

```console
(myenvironment) [shahzeb.siddiqui@login-02 ~]$ conda list | grep -E 'matplotlib|numpy'
matplotlib                3.5.3           py310h06a4308_0
matplotlib-base           3.5.3           py310hf590b9c_0
numpy                     1.21.6          py310h5f9d8c6_1
numpy-base                1.21.6          py310hb5e798b_1
```

To understand more about your current conda environment and its configuration details, it would be helpful to run `conda info` which 
shows relevant information about the conda environment, path where conda is installed along with python version and conda channels.

```console
(myenvironment) [shahzeb.siddiqui@login-02 ~]$ conda info

     active environment : myenvironment
    active env location : /home/shahzeb.siddiqui/.conda/envs/myenvironment
            shell level : 1
       user config file : /home/shahzeb.siddiqui/.condarc
 populated config files :
          conda version : 4.12.0
    conda-build version : 3.21.4
         python version : 3.8.8.final.0
       virtual packages : __linux=4.18.0=0
                          __glibc=2.28=0
                          __unix=0=0
                          __archspec=1=x86_64
       base environment : /hpc/apps/x86_64/anaconda/2021_09_16  (read only)
      conda av data dir : /hpc/apps/x86_64/anaconda/2021_09_16/etc/conda
  conda av metadata url : None
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /hpc/apps/x86_64/anaconda/2021_09_16/pkgs
                          /home/shahzeb.siddiqui/.conda/pkgs
       envs directories : /home/shahzeb.siddiqui/.conda/envs
                          /hpc/apps/x86_64/anaconda/2021_09_16/envs
               platform : linux-64
             user-agent : conda/4.12.0 requests/2.32.3 CPython/3.8.8 Linux/4.18.0-553.33.1.el8_10.x86_64 rocky/8.10 glibc/2.28
                UID:GID : 5839:5839
             netrc file : None
           offline mode : False
```

You can also install conda packages while creating a conda environment. Let's create an environment named `myenv` with packages `numpy` and `pandas` 
as follows

```console
[shahzeb.siddiqui@login-02 ~]$ conda create -n myenv numpy pandas
```

If you want to know location where packages are installed, you can run `pip show -f <package_name>` which will show you the location 
of the package. Typically, they are installed in a directory named `site-packages` which can be shown below

```console
(myenv) [shahzeb.siddiqui@login-02 ~]$ pip show -f numpy | grep Location
Location: /home/shahzeb.siddiqui/.conda/envs/myenv/lib/python3.13/site-packages
```

To get full path to the package, lets say `numpy` you can import and print the file path.

```console
(myenv) [shahzeb.siddiqui@login-02 ~]$ python -c "import numpy; print(numpy.__file__)"
/home/shahzeb.siddiqui/.conda/envs/myenv/lib/python3.13/site-packages/numpy/__init__.py
```

You may also install packages directly using `pip` instead of `conda install`. For instance, if you want to install a package named 
**PyYAML** you can run the following

```console
(myenv) [shahzeb.siddiqui@login-02 ~]$ pip install PyYAML
Collecting PyYAML
  Downloading PyYAML-6.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
Downloading PyYAML-6.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (759 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 759.5/759.5 kB 28.9 MB/s eta 0:00:00
Installing collected packages: PyYAML
Successfully installed PyYAML-6.0.2
```

If you have a **requirements.txt** file with list of python dependencies, you can also install them with

```console
pip install -r requirements.txt
```

## Removing conda environment

To remove a conda environment, you will need to inspect the name or path you want to remove. To see list of conda 
environments you can run `conda env list`

```console
[shahzeb.siddiqui@login-02 ~]$ conda env list
# conda environments:
#
python_3.9               /home/shahzeb.siddiqui/.conda/envs/python_3.9
base                  *  /hpc/apps/x86_64/anaconda/2021_09_16
alphafold_v2.2.0         /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphafold_v2.2.0
alphapept                /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphapept
alphapept-gui            /hpc/apps/x86_64/anaconda/2021_09_16/envs/alphapept-gui
excellxgene              /hpc/apps/x86_64/anaconda/2021_09_16/envs/excellxgene
jupyter-test             /hpc/apps/x86_64/anaconda/2021_09_16/envs/jupyter-test
labelstudio              /hpc/apps/x86_64/anaconda/2021_09_16/envs/labelstudio
napari                   /hpc/apps/x86_64/anaconda/2021_09_16/envs/napari
stui                     /hpc/apps/x86_64/anaconda/2021_09_16/envs/stui
tensorboard              /hpc/apps/x86_64/anaconda/2021_09_16/envs/tensorboard
                         /hpc/mydata/shahzeb.siddiqui/.conda/test_env
```

For demonstration, we will remove the environment `python_3.9` which can be done by running the following command:

```console
[shahzeb.siddiqui@login-02 ~]$ conda env remove --name python_3.9

Remove all packages in environment /home/shahzeb.siddiqui/.conda/envs/python_3.9:
```

To remove an environment by prefix, you can do this via `-p` option. This may be useful if you have named a conda environment
without an environment name. In example below we will remove the environment `/hpc/mydata/shahzeb.siddiqui/.conda/test_env`:

```console
[shahzeb.siddiqui@login-02 ~]$ conda env remove -p /hpc/mydata/shahzeb.siddiqui/.conda/test_env

Remove all packages in environment /hpc/mydata/shahzeb.siddiqui/.conda/test_env:
```

If you have a conda environment with packages, you can remove the environment and uninstall all packages as follows.

```console
conda remove --name <env_name> --all
```

In example below I have a conda environment name `dev_environment` 

```console
[shahzeb.siddiqui@login-02 ~]$ conda remove --name dev_environment --all

Remove all packages in environment /hpc/mydata/shahzeb.siddiqui/.conda-envs/dev_environment:


## Package Plan ##

  environment location: /hpc/mydata/shahzeb.siddiqui/.conda-envs/dev_environment


The following packages will be REMOVED:

  _libgcc_mutex-0.1-main
  _openmp_mutex-5.1-1_gnu
  blas-1.0-mkl
  bottleneck-1.4.2-py39ha9d4c09_0
  ca-certificates-2025.2.25-h06a4308_0
  intel-openmp-2023.1.0-hdb19cb5_46306
  ld_impl_linux-64-2.40-h12ee557_0
  libffi-3.4.4-h6a678d5_1
  libgcc-ng-11.2.0-h1234567_1
  libgfortran-ng-11.2.0-h00389a5_1
  libgfortran5-11.2.0-h1234567_1
  libgomp-11.2.0-h1234567_1
  libstdcxx-ng-11.2.0-h1234567_1
  mkl-2023.1.0-h213fc3f_46344
  mkl-service-2.4.0-py39h5eee18b_2
  mkl_fft-1.3.11-py39h5eee18b_0
  mkl_random-1.2.8-py39h1128e8f_0
  ncurses-6.4-h6a678d5_0
  numexpr-2.10.1-py39h3c60e43_0
  numpy-2.0.2-py39h5f9d8c6_0
  numpy-base-2.0.2-py39hb5e798b_0
  openssl-3.0.16-h5eee18b_0
  pandas-2.2.3-py39h6a678d5_0
  pip-25.0-py39h06a4308_0
  pybind11-abi-4-hd3eb1b0_1
  python-3.9.21-he870216_1
  python-dateutil-2.9.0post0-py39h06a4308_2
  python-tzdata-2023.3-pyhd3eb1b0_0
  pytz-2024.1-py39h06a4308_0
  readline-8.2-h5eee18b_0
  scipy-1.13.1-py39h5f9d8c6_1
  setuptools-72.1.0-py39h06a4308_0
  six-1.16.0-pyhd3eb1b0_1
  sqlite-3.45.3-h5eee18b_0
  tbb-2021.8.0-hdb19cb5_0
  tk-8.6.14-h39e8969_0
  tzdata-2025a-h04d1e81_0
  wheel-0.45.1-py39h06a4308_0
  xz-5.6.4-h5eee18b_1
  zlib-1.2.13-h5eee18b_1


Proceed ([y]/n)?
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

- Managing conda environments: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- Conda Cheat Sheet: https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html
- Configuring conda configuration with .condarc: https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html