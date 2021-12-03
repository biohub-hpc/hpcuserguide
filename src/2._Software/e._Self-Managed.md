# Self-managed software

When working with software that is under development, one-off testing, or other
needs which require quick install/upgrade turnaround, it's often convenient to
self-manage the installation. All storage in the cluster environment is mounted
with no restrictions on executing applications, so apps can be self-installed
into `${HOME}` or any project/scratch storage space as needed.

TODO:

1. simple `configure; make; make install` example showing use of `--prefix=`.
1. breakdown/pointer to availabe storage locations for software installs.
1. example of using personal Lmod modules.
