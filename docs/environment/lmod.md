# Lmod

We use [Lmod](https://lmod.readthedocs.io/en/latest/)  as its module environment to manage software. 

Lmod is a Lua-based module system that helps manage the user environment
(`PATH`, `LD_LIBRARY_PATH`, etc.) through modulefiles. Lmod is an extension of
environment-modules that supports Tcl modules along
with hierarchical `MODULEPATH`.

## About `module`

`module` is a bash function read by `$LMOD_CMD` which points to the Lmod command
that reads a modulefile and evaluates each modulefile using the `eval` command:

```console
[shahzeb.siddiqui@login-02 ~]$ type module
module is a function
module ()
{
    if [ -z "${LMOD_SH_DBG_ON+x}" ]; then
        case "$-" in
            *v*x*)
                __lmod_sh_dbg='vx'
            ;;
            *v*)
                __lmod_sh_dbg='v'
            ;;
            *x*)
                __lmod_sh_dbg='x'
            ;;
        esac;
    fi;
    if [ -n "${__lmod_sh_dbg:-}" ]; then
        set +$__lmod_sh_dbg;
        echo "Shell debugging temporarily silenced: export LMOD_SH_DBG_ON=1 for Lmod's output" 1>&2;
    fi;
    eval "$($LMOD_CMD $LMOD_SHELL_PRGM "$@")" && eval "$(${LMOD_SETTARG_CMD:-:} -s sh)";
    __lmod_my_status=$?;
    if [ -n "${__lmod_sh_dbg:-}" ]; then
        echo "Shell debugging restarted" 1>&2;
        set -$__lmod_sh_dbg;
    fi;
    unset __lmod_sh_dbg;
    return $__lmod_my_status
}
```

## Command Summary

| Command                            | Description                                                                             | 
| -----------------------------------|-----------------------------------------------------------------------------------------|
| `module list`                      | List active modules in the user environment                                             |
| `module av [module]`               | List available modules in `MODULEPATH`                                                  |    
| `module spider [module]`           | Query all modules in `MODULEPATH` and any module hierarchy                              |
| `module overview [module]`         | List all modules with a count of each module                                            |
| `module load [module]`             | Load a modulefile in the user environment                                               |
| `module unload [module]`           | Remove a *loaded* module from the user environment                                      |
| `module purge`                     | Remove all modules from the user environment                                            |
| `module swap [module1] [module2]`  | Replace `module1` with `module2`                                                        |
| `module show [module]`             | Show content of commands performed by loading `module`                                  |
| `module --raw show [module]`       | Show raw content of modulefile                                                          |  
| `module help [module]`             | Show help for a given module                                                            |
| `module whatis [module]`           | A brief description of the module, generally single line                                |
| `module savelist`                  | List all user collections                                                               |
| `module save [collection]`         | Save active modules in a user collection                                                |
| `module describe [collection]`     | Show content of user collection                                                         |
| `module restore [collection]`      | Load modules from a collection                                                          |
| `module disable [collection]`      | Disable a user collection                                                               |
| `module --config`                  | Show Lmod configuration                                                                 |
| `module use [-a] [path]`           | Prepend or append path to `MODULEPATH`                                                  |
| `module unuse [path]`              | Remove path from `MODULEPATH`                                                           |
| `module --show_hidden av`          | Show all available modules in `MODULEPATH` including hidden modules                     |
| `module --show_hidden spider`      | Show all possible modules in `MODULEPATH` and module hierarchy including hidden modules |

## ml 

Lmod provides another convenient shortcut command for the **module** command
called [ml](https://lmod.readthedocs.io/en/latest/010_user.html#ml-a-convenient-tool)
for user convenience, which mimics the `module` command. 

Invoking the `ml` command without arguments is equivalent to `module list`; any sub-commands to `module`
are usable with the `ml` command. For example, `ml avail` is equivalent to `module avail`; `ml spider` 
is equivalent to `module spider`, etc.

The syntax for loading and unloading modules with the `ml` command differs from the `module` command.
You can type `ml <module>` to load a module, and unload by prepending a minus sign (-): `ml -<module>`.

For instance if we want to load the `gcc` module we can run `ml gcc`. To remove this module from the
set of loaded modules we would run `ml -gcc`. 

```console
shahzeb.siddiqui@login-02 ~]$ ml gcc
[shahzeb.siddiqui@login-02 ~]$ ml

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv   3) gcc/11.3

  Where:
   S:  Module is Sticky, requires --force to unload or purge



[shahzeb.siddiqui@login-02 ~]$ ml -gcc
[shahzeb.siddiqui@login-02 ~]$ ml

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv

  Where:
   S:  Module is Sticky, requires --force to unload or purge

```  

One can load and unload module in a single `ml` command: for instance if you want to unload `gcc` and load
`cuda` you could run: `ml -gcc cuda` or `ml cuda -gcc`. 

## Finding Modules

Lmod provides several commands to help you find modules including `module avail`, `module spider` and even
`module overview`. We will discuss a few of these commands here. 

To see list of available modules, you can run 

```shell
module avail
```

The output of this will be quite long depending on the number of modulefiles, for instance if you want to see all `gcc` modules 
you can run 

```shell
module avail gcc 
```

The `module spider` command reports all modules in your system in `MODULEPATH` along with all module trees in the hierarchical 
system. Note that `module avail` doesn't show modules from all trees in the hierarchical system. If you want to know **all** 
available software on the system, please use `module spider`. 

The output will be a list of software entries with corresponding versions:

```console
[shahzeb.siddiqui@login-02 ~]$ module spider

--------------------------------------------------------------------------------------------------------------
The following is a list of the modules and extensions currently available:
--------------------------------------------------------------------------------------------------------------
  BEAGLE: BEAGLE/2023.06.06
    BEAGLE is a high-performance library that can perform the core calculations at the heart of most Bayesian
    and Maximum Likelihood phylogenetics packages. It can make use of highly-parallel processors such as
    those in graphics cards (GPUs) found in many PCs.

  BEAST: BEAST/1.10.4
    BEAST is a software package for phylogenetic analysis with an emphasis on time-scaled trees.

  BEAST2: BEAST2/2.7.4
    BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis of molecular sequences.

  FASTGA: FASTGA/latest, FASTGA/1.0
    FastGA: Compare two genomes or a genome against itself and output a .1aln, .paf, or .psl file of all
    alignments found.

  FastANI: FastANI/1.34-gcc-12.4
    FastANI
    
  ...  
```

The `module spider` can report all versions of the software. For instance if we want to see all
gcc compilers we can run the following. In this example we have 4 versions of gcc


```console
[shahzeb.siddiqui@login-02 ~]$ module spider gcc

--------------------------------------------------------------------------------------------------------------
  gcc:
--------------------------------------------------------------------------------------------------------------
    Description:
      The GNU Compiler Collection.

     Versions:
        gcc/11.3
        gcc/12.4
        gcc/13.3
        gcc/14.2

--------------------------------------------------------------------------------------------------------------
  For detailed information about a specific "gcc" package (including how to load the modules) use the module's full name.
  Note that names that have a trailing (E) are extensions provided by other modules.
  For example:

     $ module spider gcc/14.2
--------------------------------------------------------------------------------------------------------------
```

Lmod recently introduced a new command called `module overview` which displays each module in short form with a 
number of module versions.  Shown below is a preview of `module overview`

```console
[shahzeb.siddiqui@login-02 ~]$ module overview

----------------------------------------- /hpc/modules/modulefiles/Core ------------------------------------------
StdEnv (1)   proot (1)   slurm (2)

------------------------------------- /hpc/modules/modulefiles/Applications --------------------------------------
BEAGLE    (1)   btop            (1)    emacs    (1)   lightning    (1)   nextflow     (3)   resmap         (1)
BEAST     (1)   caddy           (2)    eman     (1)   mafft        (1)   nextpyp      (1)   rstudio        (1)
BEAST2    (1)   cellprofiler    (1)    fastga   (2)   mamba        (2)   ninja        (1)   rsync          (2)
FASTGA    (2)   cellranger-arc  (1)    fastp    (1)   matlab       (1)   nsight       (1)   ruse           (1)
FastANI   (1)   cellranger-atac (1)    ffmpeg   (1)   maxquant     (1)   nvhpc-sdk    (2)   rust           (1)
FragPipe  (4)   cellranger      (2)    fm-index (1)   meme         (1)   nvhpc        (1)   samtools       (2)
IGV       (1)   chimerax        (2)    fpart    (1)   minimap2     (1)   ollama       (3)   schrodinger    (1)
MrBayes   (1)   cistem          (2)    fragpipe (4)   mongodb      (1)   omnitrace    (1)   spaceranger    (1)
R         (4)   cmake           (1)    gcc      (4)   mongosh      (1)   openmpi      (2)   spectronaut    (1)
STAR      (3)   cryosparc       (4)    gsl      (1)   motioncor2   (1)   oracle-java  (4)   spid           (1)
alphafold (4)   ctffind         (1)    gurobi   (1)   motioncor3   (1)   papi         (1)   squashfs-tools (1)
anaconda  (4)   cuda            (15)   hdf5     (1)   mpifileutils (1)   pixi         (2)   star           (3)
aria2     (1)   cudnn           (6)    hpcx     (1)   mrbayes      (1)   pycharm      (1)   stui           (1)
awscli    (1)   demuxlet        (3)    httm     (1)   msrsync      (1)   r            (4)   turm           (1)
axel      (1)   diann           (1)    hwloc    (1)   mustem-gpu   (1)   raxml-ng-mpi (1)   uv             (2)
beagle    (1)   dragon          (1)    igv      (1)   mzmine       (1)   raxml-ng     (1)   versitygw      (1)
beast     (1)   duc             (1)    imod     (1)   nano         (1)   rclone       (2)   zed            (1)
beast2    (1)   dynamo          (1)    iqtree   (1)   napari       (1)   relion-turbo (3)
bowtie2   (2)   elfindo         (1)    julia    (5)   neovim       (1)   relion       (3)

---------------------------------------- /hpc/modules/modulefiles/Groups -----------------------------------------
comp_micro (1)   czii (1)   data.science (1)   jacobo_group (1)   royerlab (1)
```

Using `module spider` gives the available versions, and suggests to use the
`spider` command on a specific version, which then gives the list of all the
dependency modules you need to load first (modules on any one of the lines
given depending on your user environment choices such as the compiler version):

!!! tip
    Always use `module spider` instead of `module avail` to find out how to `module load`.

## User Collections

Lmod introduced the concept of [user collections](https://lmod.readthedocs.io/en/latest/010_user.html#user-collections),
allowing a user to reference a group of modules with a unique name. This is particularly useful if there
is a set of modules you load regularly to do a particular task. You can save the modules into a collection to
save the trouble of retyping them every time, loading them with the `module restore` command. Note that Lmod 
can load only one user collection at a time.

To save modules in a collection, load the relevant modules and run `module save`. In this example,
we save our active modules into the `default` collection.  

```console
[shahzeb.siddiqui@login-02 ~]$ module purge
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) slurm/default
[shahzeb.siddiqui@login-02 ~]$ module load gcc
[shahzeb.siddiqui@login-02 ~]$ module list

Currently Loaded Modules:
  1) slurm/default (S)   2) gcc/11.3

  Where:
   S:  Module is Sticky, requires --force to unload or purge
   
[shahzeb.siddiqui@login-02 ~]$ module save
Saved current collection of modules to: "default"   
```

Lmod will store user collection in **$HOME/.lmod.d**. You can view all collections using `module savelist`.


```console
[shahzeb.siddiqui@login-02 ~]$ module savelist
Named collection list :
  1) default
```

You can see contents of a collection using `module describe`, which shows the modules that will be loaded
when restoring from the collection. In this next example, we will purge and restore from the collection, 
which will simply load the `gcc` module:

```console
[shahzeb.siddiqui@login-02 ~]$ module purge
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) slurm/default
[shahzeb.siddiqui@login-02 ~]$ module list

Currently Loaded Modules:
  1) slurm/default (S)

  Where:
   S:  Module is Sticky, requires --force to unload or purge



[shahzeb.siddiqui@login-02 ~]$ module restore
Restoring modules from user's default
[shahzeb.siddiqui@login-02 ~]$ module list

Currently Loaded Modules:
  1) slurm/default (S)   2) gcc/11.3

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

## Showing the Contents of Modulefiles

There are several commands to reveal the contents of modulefiles: `module whatis`, 
`module help`, `module show`, and `module spider`.

The `module whatis` is a single line summary of modulefile and `module help` is a multi-line description of the modulefile.

The `module show` command displays the commands executed when loading the module (`module load`).  Shown below are commands run
in your user shell when loading `gcc` module. 

!!! note

    The output of `module show` is not the content of the modulefile. If you want to see the content of the modulefile, add 
    the `--raw` option: `module --raw show gcc`.

```console
[shahzeb.siddiqui@login-02 ~]$ module show gcc
--------------------------------------------------------------------------------------------------------------
   /hpc/modules/modulefiles/Applications/gcc/11.3.lua:
--------------------------------------------------------------------------------------------------------------
family("compiler")
pushenv("mod_gcc_prefix","/hpc/apps/gcc/11.3")
pushenv("mod_prefix","/hpc/apps/gcc/11.3")
pushenv("CFLAGS","-mtune=generic -march=x86-64")
pushenv("CXXFLAGS","-mtune=generic -march=x86-64")
prepend_path("PATH","/hpc/apps/gcc/11.3/bin")
prepend_path("LIBRARY_PATH","/hpc/apps/gcc/11.3/lib")
prepend_path("LIBRARY_PATH","/hpc/apps/gcc/11.3/lib64")
prepend_path("LD_LIBRARY_PATH","/hpc/apps/gcc/11.3/lib")
prepend_path("LD_LIBRARY_PATH","/hpc/apps/gcc/11.3/lib64")
prepend_path("CPATH","/hpc/apps/gcc/11.3/include")
prepend_path("C_INCLUDE_PATH","/hpc/apps/gcc/11.3/include")
prepend_path("CPLUS_INCLUDE_PATH","/hpc/apps/gcc/11.3/include")
prepend_path("OBJC_INCLUDE_PATH","/hpc/apps/gcc/11.3/include")
prepend_path("PKG_CONFIG_PATH","/hpc/apps/gcc/11.3/lib")
prepend_path("PKG_CONFIG_PATH","/hpc/apps/gcc/11.3/lib64")
whatis("Name:        gcc")
whatis("Version:     11.3")
whatis("Category:    compiler")
whatis("URL:         https://gcc.gnu.org/")
whatis("Description: The GNU Compiler Collection.")
```

The `module whatis` command can be used to get a brief description of the module. 

```console
[shahzeb.siddiqui@login-02 ~]$ module whatis gcc
gcc/11.3            : Name:        gcc
gcc/11.3            : Version:     11.3
gcc/11.3            : Category:    compiler
gcc/11.3            : URL:         https://gcc.gnu.org/
gcc/11.3            : Description: The GNU Compiler Collection.
```

The `--loc` option can be used to show the location of the modulefile, which can be useful if you want to find the file and view it yourself. This can 
be joined with `cat` or `grep` command if you desire to view content of file.

```console
[shahzeb.siddiqui@login-02 ~]$ module --loc show gcc
/hpc/modules/modulefiles/Applications/gcc/11.3.lua
```

For example, if you want to see all `prepend_path` set which will update environments like PATH, LIBRARY_PATH, etc... You can run the following. 

!!! note

    You need `--redirect` option to show the content of the modulefile, since it is directed to stderr by default.

```console
[shahzeb.siddiqui@login-02 ~]$ grep prepend_path $(module --redirect --loc show gcc)
prepend_path("PATH",               app.bin)
prepend_path("LIBRARY_PATH",       app.lib)
prepend_path("LIBRARY_PATH",       app.lib64)
prepend_path("LD_LIBRARY_PATH",    app.lib)
prepend_path("LD_LIBRARY_PATH",    app.lib64)
prepend_path("CPATH",              app.incl)
prepend_path("C_INCLUDE_PATH",     app.incl)
prepend_path("CPLUS_INCLUDE_PATH", app.incl)
prepend_path("OBJC_INCLUDE_PATH",  app.incl)
prepend_path("PKG_CONFIG_PATH",         app.pkgconfig)
prepend_path("PKG_CONFIG_PATH",         app.pkgconfig64)
-- prepend_path("MANPATH",         app.man)
```

### Lmod Families

The Lmod `family("name")` Lua function enables the concept of 
[families](https://lmod.readthedocs.io/en/latest/050_lua_modulefiles.html) to
be enforced. 

The basic idea is that modules belong to a family group, and only one module
from the family group can be loaded at a given time.
The purpose is to protect users from loading conflicting modules, e.g., two MPI
libraries such as `openmpi` and `mpich`  that provide the same binaries
`mpicc`, `mpifort`, `mpic++`. 

A quick way to check the active families is to run `module --mt`, which shows the module tables state along with family names. 

```console
[shahzeb.siddiqui@login-02 ~]$ module --mt
_ModuleTable_ = {
  MTversion = 3,
  c_rebuildTime = false,
  c_shortTime = 0.12335109710693,
  depthT = {},
  family = {
    compiler = "gcc",
    scheduler = "slurm",
  },
  mT = {
    gcc = {
      fn = "/hpc/modules/modulefiles/Applications/gcc/11.3.lua",
      fullName = "gcc/11.3",
      loadOrder = 2,
      propT = {},
      stackDepth = 0,
      status = "active",
      userName = "gcc",
      wV = "^00000011.000000003.*zfinal",
    },
    slurm = {
      fn = "/hpc/modules/modulefiles/Core/slurm/default.lua",
      fullName = "slurm/default",
      loadOrder = 1,
      propT = {
        lmod = {
          sticky = 1,
        },
      },
      stackDepth = 0,
      status = "active",
      userName = "slurm",
      wV = "*default.*zfinal",
    },
  },
  mpathA = {
    "/hpc/modules/modulefiles/Core", "/hpc/modules/modulefiles/Applications", "/hpc/modules/modulefiles/Groups",
  },
  systemBaseMPATH = "/hpc/modules/modulefiles/Core:/hpc/modules/modulefiles/Applications:/hpc/modules/modulefiles/Groups",
}
```

Lmod will set the environment variables `LMOD_FAMILIY_<NAME>` and `LMOD_FAMILY_<NAME>_VERSION`, where `<name>` is
the name of family that can be used to reference family.

For example when we have `gcc` loaded we will see the environment variable 
- `LMOD_FAMILY_COMPILER` set to `gcc` 
- `LMOD_FAMILY_COMPILER_VERSION` set to `11.3`

```console
[shahzeb.siddiqui@login-02 ~]$ echo $LMOD_FAMILY_COMPILER $LMOD_FAMILY_COMPILER_VERSION
gcc 11.3
```

Now if we load the `nvhpc` module, this will swap the `gcc` module and set the `LMOD_FAMILY_COMPILER` to `nvhpc` and `LMOD_FAMILY_COMPILER_VERSION` to `2024_2411`

```console
[shahzeb.siddiqui@login-02 ~]$ ml nvhpc

Lmod is automatically replacing "gcc/11.3" with "nvhpc/2024_2411".

[shahzeb.siddiqui@login-02 ~]$ echo $LMOD_FAMILY_COMPILER $LMOD_FAMILY_COMPILER_VERSION
nvhpc 2024_2411
```

## Startup module

We have configured Lmod to provide a module that is loaded by default for all users, called `StdEnv`. This module can be loaded using 
`module load StdEnv`. Likewise, you can restore to the original set of modules by running `module reset`. Let's assume we have a few modules loaded as 
shown below

```console
[shahzeb.siddiqui@login-02 ~]$ ml

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv   3) anaconda/2021_09_16   4) gcc/11.3   5) samtools/1.19

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

When we run `module reset`, we will load the startup modules which may be useful if you want to start from a clean environment. This
may be useful to run tests in a reproducible manner. 

```console
[shahzeb.siddiqui@login-02 ~]$ module reset
Running "module reset". Resetting modules to system default. The following $MODULEPATH directories have been removed: None
[shahzeb.siddiqui@login-02 ~]$ module list

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

Please refer to see https://lmod.readthedocs.io/en/latest/070_standard_modules.html for details 
related to startup modules 

## Useful Tips 

### Redirecting Module Output

Lmod will redirect output to stderr by default, which means this won't work as you expected, since its output 
will not be stored in a file. As shown below the file `active.txt` is empty and output was shown to console

```console
[shahzeb.siddiqui@login-02 ~]$ module list > active.txt

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv

  Where:
   S:  Module is Sticky, requires --force to unload or purge
   
[shahzeb.siddiqui@login-02 ~]$ cat active.txt
[shahzeb.siddiqui@login-02 ~]$   
```

The `--redirect` option to any module command will redirect stderr to stdout so that shell commands 
can capture module commands.

```console
[shahzeb.siddiqui@login-02 ~]$ module --redirect list > active.txt
[shahzeb.siddiqui@login-02 ~]$ cat active.txt

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

### Autoswap modules of the same name

Lmod will automatically swap modules of the same name. For instance, if you load `gcc/11.3`, Lmod will remove `gcc/12.4` from 
your user environment:

```console
[shahzeb.siddiqui@login-02 ~]$ ml

Currently Loaded Modules:
  1) slurm/default (S)   2) StdEnv   3) gcc/11.3

  Where:
   S:  Module is Sticky, requires --force to unload or purge
 
[shahzeb.siddiqui@login-02 ~]$ ml gcc/12.4

The following have been reloaded with a version change:
  1) gcc/11.3 => gcc/12.4
```

### Debugging Modules

If you want to debug the state of modules, any of these command options can help:

- Tracing modules: `module -T`
- Print Module Table: `module --mt`
- Debug Level: `module --debug=[1|2|3]` 

To debug modulefiles themselves, please see https://lmod.readthedocs.io/en/latest/160_debugging_modulefiles.html 

### Parsing output 

Use the `-t` option with  `module avail`, `module spider`, `module list`, `module spider` and `module savelist` commands 
to produce parsable output. 

To see loaded modules in a parsable format, the environment variable `LOADEDMODULES` is a colon separated
list of active modules loaded in your shell.

```console
[shahzeb.siddiqui@login-02 ~]$ echo $LOADEDMODULES
slurm/default:gcc/11.3
```

Similarly, the full path to the modulefiles of active modules can be retrieved using the `_LMFILES_` environment
variable. The output is a colon-separated list of modulefiles.

```console
[shahzeb.siddiqui@login-02 ~]$ echo $_LMFILES_
/hpc/modules/modulefiles/Core/slurm/default.lua:/hpc/modules/modulefiles/Applications/gcc/11.3.lua
```

### Seeing Defaults for Modulefiles

The `module -d avail` command will report the default for every module. Lmod will load the 
default module if you don't specify the full version (i.e., `module load samtools`) since there is 
only one default for every module name. 

For example, to list the default for `samtools`:

```console
[shahzeb.siddiqui@login-02 ~]$ ml -d av samtools

------------------------------------- /hpc/modules/modulefiles/Applications --------------------------------------
   samtools/1.19
```

### Managing User Collection

The user collections is a powerful feature of Lmod that allows you to save and restore a set of modules with a given name. This 
makes it easy to load a set of modules that you use frequently. You can name your collection names as you like and have as many as you want. 
Let's say you want to create the following collections

1. `python` - Set of python modules to load
2. `r` - Set of R modules to load to setup R environment
3. `gpu`: A gpu collection that will load cuda and other gpu related modules

We can do each of these tasks as shown below

Shown below is the python collection
```console
[shahzeb.siddiqui@login-02 ~]$ ml anaconda
[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
anaconda/2021_09_16

[shahzeb.siddiqui@login-02 ~]$ ml save python
Saved current collection of modules to: "python"
```

Next we will create a new environment for R
```command
[shahzeb.siddiqui@login-02 ~]$ ml reset
Running "module reset". Resetting modules to system default. The following $MODULEPATH directories have been removed: None

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv

[shahzeb.siddiqui@login-02 ~]$ module load r

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv
r/4.3

[shahzeb.siddiqui@login-02 ~]$ ml save r
Saved current collection of modules to: "r"
```

Now we will create a `gpu` collection that will load the default `cuda` and `cudnn` modules

```console
[shahzeb.siddiqui@login-02 ~]$ ml reset
Running "module reset". Resetting modules to system default. The following $MODULEPATH directories have been removed: None

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv

[shahzeb.siddiqui@login-02 ~]$ ml cuda cudnn

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv
cuda/12.6.1_560.35.03
cudnn/9.0.0.3_cuda12

[shahzeb.siddiqui@login-02 ~]$ ml save gpu
Saved current collection of modules to: "gpu"
```

First lets confirm all collections have the correct modules, this can be done via `module describe` command

```console
[shahzeb.siddiqui@login-02 ~]$ module describe gpu
Collection "gpu" contains:
   1) slurm    2) StdEnv    3) cuda    4) cudnn

[shahzeb.siddiqui@login-02 ~]$ module describe python

Collection "python" contains:
   1) slurm    2) anaconda

[shahzeb.siddiqui@login-02 ~]$ module describe r
Collection "r" contains:
   1) slurm    2) StdEnv    3) r   
```

Take note how switching between collections dynamically loads modules that were present in each collection

```console
[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv

[shahzeb.siddiqui@login-02 ~]$ ml restore python
Restoring modules from user's python

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
anaconda/2021_09_16
```

Now switching between collections will also unload the modules that were loaded in the previous collection so you dont need 
unload all modules or run `module reset` since Lmod knows how to handle collections. Shown below we will switch to collection `r` and
`gpu`

```console
[shahzeb.siddiqui@login-02 ~]$ ml restore r
Restoring modules from user's r

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv
r/4.3

[shahzeb.siddiqui@login-02 ~]$ ml restore gpu
Restoring modules from user's gpu

[shahzeb.siddiqui@login-02 ~]$ ml -t
slurm/default
StdEnv
cuda/12.6.1_560.35.03
cudnn/9.0.0.3_cuda12
```

## Customize Module Defaults at User Level

Lmod has support for customizing module defaults at the user level. This is
done by creating a file `$HOME/.modulerc.lua`.

Let's assume you want to use the latest gcc module `gcc/14.2` as the default. Currently, the default gcc is `gcc/11.3` as shown below

```console
[shahzeb.siddiqui@login-02 ~]$ ml -t -d av gcc/
/hpc/modules/modulefiles/Applications:
gcc/11.3
```

We can add the following line in `~/.modulerc.lua` file to set the default to `gcc/14.2`

```lua
module_version("gcc/14.2","default")
```

Shown below is the content for `~/.modulerc.lua` file

```console
[shahzeb.siddiqui@login-02 ~]$ cat ~/.modulerc.lua
module_version("gcc/14.2","default")
```

Now with this change the default gcc is `gcc/14.2` as shown below. We can confirm this by loading the module and checking the version

```console
[shahzeb.siddiqui@login-02 ~]$ ml -t -d av gcc/
/hpc/modules/modulefiles/Applications:
gcc/14.2

[shahzeb.siddiqui@login-02 ~]$ ml -d gcc

[shahzeb.siddiqui@login-02 ~]$ gcc --version
gcc (GCC) 14.2.0
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## References

- Documentation: https://lmod.readthedocs.io/en/latest/index.html
- User Guide: https://lmod.readthedocs.io/en/latest/010_user.html
- GitHub: https://github.com/TACC/Lmod
- FAQ: https://lmod.readthedocs.io/en/latest/040_FAQ.html
- Lmod Training: https://gitlab.com/NERSC/lmod-training


