# Lmod modules

For more complex software, packages which conflict with others in command
namespace or which need multiple versions of the same package to be available,
the installation is maintained in `/hpc/apps` using the `module` command to add
and remove these applications to and from the working environment as needed.
We've chosen [Lmod modules](https://lmod.readthedocs.io/en/latest/) as the
package to provide the `module` command, it's based on the [Lua programming
language](https://www.lua.org/) and has more flexibility and features than the
TCL based `environment-modules`.

Some common `module` commands and usage are described below.

## `module load`

Using `module` managed software is as easy as `module load APPLICATION`, for
example:

```
[john.hanks@cluster ~]$ which R
/usr/bin/which: no R in (/home/john.hanks/.local/bin:/home/john.hanks/bin:/hpc/slurm/current/../utils:/hpc/slurm/current/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin)
[john.hanks@cluster ~]$ module load R
[john.hanks@cluster ~]$ which R
/hpc/apps/x86_64/r/4.1/bin/R
[john.hanks@cluster ~]$ R --version
R version 4.1.1 (2021-08-10) -- "Kick Things"
Copyright (C) 2021 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under the terms of the
GNU General Public License versions 2 or 3.
For more information about these matters see
https://www.gnu.org/licenses/.

[john.hanks@cluster ~]$
```

## `module list`

To see what software you have loaded, `module list`:

```
[john.hanks@cluster ~]$ module list

Currently Loaded Modules:
  1) slurm/current (S)   2) StdEnv   3) R/4.1

  Where:
   S:  Module is Sticky, requires --force to unload or purge

[john.hanks@cluster ~]$ 
```

## `module spider`

To get information about a specific module, especially how to load it, `module spider`:
```
[randall.white@cluster ~]$ module spider cryosparc

-------------------------------------------------------------------------------------------------------------------------------
  cryosparc:
-------------------------------------------------------------------------------------------------------------------------------
    Description:
      CryoSparc

     Versions:
        cryosparc/4.4.0-motioncor2-1.6.4
        cryosparc/4.4.1-motioncor2-1.6.4
        cryosparc/4.5.1-motioncor2-1.6.4
     Other possible modules matches:
        sbgrid/cryosparc-tools

-------------------------------------------------------------------------------------------------------------------------------
  To find other possible module matches execute:

      $ module -r spider '.*cryosparc.*'

-------------------------------------------------------------------------------------------------------------------------------
  For detailed information about a specific "cryosparc" package (including how to load the modules) use the module's full name.
  Note that names that have a trailing (E) are extensions provided by other modules.
  For example:

     $ module spider cryosparc/4.5.1-motioncor2-1.6.4
-------------------------------------------------------------------------------------------------------------------------------



[randall.white@cluster ~]$ module spider cryosparc/4.5.1-motioncor2-1.6.4

-------------------------------------------------------------------------------------------------------------------------------
  cryosparc: cryosparc/4.5.1-motioncor2-1.6.4
-------------------------------------------------------------------------------------------------------------------------------
    Description:
      CryoSparc


    This module can be loaded directly: module load cryosparc/4.5.1-motioncor2-1.6.4

```


## `module unload|purge`

As implied in the `module list` output, to remove things from the environment you can `module purge`
to completely clean it or `module unload` to remove a specific package.

```
[john.hanks@cluster ~]$ which R
/hpc/apps/x86_64/r/4.1/bin/R
[john.hanks@cluster ~]$ module unload R
[john.hanks@cluster ~]$ which R
/usr/bin/which: no R in (/home/john.hanks/.local/bin:/home/john.hanks/bin:/hpc/slurm/current/../utils:/hpc/slurm/current/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin)
[john.hanks@cluster ~]$ 
```

