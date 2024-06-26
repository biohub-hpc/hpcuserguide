---
title: Why is home so small
description: 
published: true
date: 2023-11-19T17:11:06.380Z
tags: 
editor: markdown
dateCreated: 2023-11-19T15:38:00.004Z
---

# Why is my `${HOME}` so small?

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


