# Frequently Asked Questions

## `${THING}` used to work, broken now.

When something that was working, stops working, here are some of the common things to look for:

* Has anything been added to your `${HOME}/.bashrc` or `${HOME}/.bash_profile`?
* Have you,possibly inadvertently, installed something into `${HOME}/.local` which causes a conflict in binaries or libraries?
* Are you hitting a quota or full disk isssue? 
* Has your input data or parameters changed? Now using a larger data set, for instance.
* Have you tested from an incognito browser window and/or flushed the browser cache?

If none of those things seem to be the issues, reach out to us for additional help troubleshooting.

## Why can't I use `sudo`?

The cluster environment is a shared resource, with many people and groups
accessing it. Because of that, data privacy is 100% dependent on unix file
permissions and ACLs. Anyone with `sudo` access can bypass those permissions,
which means as a rule we cannot give out `sudo` to individual users who are not
approved admins for the cluster. Additionally, the cluster environment is
complex and administrative activities need to be carried out in a restricted,
planned and well communicated fashion, something that becomes less realistic to
accomplish as the number of people with `sudo` access increases. In order to
keep the environment as stable and secure as possible, access to `sudo` is very
restricted.

The flip side of that requirement is that it means we (sysadmins) have to be
***very*** responsive to address user requirements. If you have a need that you
believe requires `sudo`, contact us and we'll either take care of the parts
requiring `sudo` access or help you achieve the same goal from userspace
without needing `sudo`. As an example of why `sudo` is rarely a hard
requirement, the cluster application stack (`module` environment) is almost
entirely configured without the use or need of `sudo` access.

## Why is my `${HOME}` so small?

Cluster operation has a hard dependency on a fast, responsive `${HOME}` and
software application stack filesystem. Without a working `${HOME}` and ability to
start applications, the cluster cannot function. The small quota on `${HOME}` is
to discourage people from running jobs against `${HOME}` and negatively impacting
performance. The `${HOME}` filesystem is specifically tuned to work well with
user owned software installs and scripts, configuration files, etc., but is not
a good place to store intermediate files from jobs or large data sets. Project
and scratch spaces are provided and optimized for these use cases, see the
Storage section for more details about what is available and the best location
for different uses. 

It is, however, convenient to be able to access locations through the `${HOME}`
path. By using symlinks, you can create your own personal namespace in `${HOME}`.
For example:

```
[john.hanks@cluster ~]$ mkdir mydata
[john.hanks@cluster ~]$ cd mydata
[john.hanks@cluster mydata]$ ln -s /path/to/something ./something
[john.hanks@cluster mydata]$ ln -s /path/to/somethingelse ./somethingelse
[john.hanks@cluster mydata]$ ls
something  somethingelse
[john.hanks@cluster mydata]$ 
```

By using symlinks there a location was created which can be referred to in
scripts as `${HOME}/mydata` and has links to the actual storage locations I
use, making them all easy to navigate to from `${HOME}`. 

!!! warning "Warning: Use a subdirectory for symlinks in `${HOME}`"

    Only put symlinks to other filesystems in a subdirectory of
    `${HOME}` not directly into `${HOME}`. Symlinks directly in `${HOME}` will need
    to resolve during login and if a given storage system is down, will block login. 


