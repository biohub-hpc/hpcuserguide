# Storage

HPC storage systems are designed to cater to different data needs, from temporary scratch space to long-term archival storage. 
They offer a combination of high capacity, redundancy, and accessibility to support the demanding requirements of large-scale computational tasks and data management. 
Understanding the types and uses of different storage paths helps users optimize their workflow and ensure data integrity on our HPC systems.


!!! warning "Draft Draft Draft"

    This is a draft of the storage description, layout and recommended usage.
    Comments/suggestions/critiques to us in Slack #hpc-community.

## Storage Namespaces

The following table outlines the available storage namespaces in which storage is either already available or can be provisioned upon request.

| Unix Path                  | Disk/Server<br>Redundancy | Snapshots | On-Site<br>Replica | Off-Site<br>Replica | AWS Glacier<br>Deep Archive | Best used for/data which is: |
|----------------------------|---------------------------|-----------|--------------------|---------------------|-----------------------------|------------------------------|
| `${HOME}`                  | High                      | Yes       | Yes                | No                  | No                          | - private data/applications  |
| `/hpc/mydata/${USER}`      | High                      | Yes       | Yes                | No                  | No                          | - personal working space     |
| `/local/scratch`<br>`/hpc/nodes/${NODE}` | Low        | No        | No                 | No                  | No                          | - scratch data<br>- easily reproducible data<br>- intermediate job files |
| `/hpc/scratch/${NAME}`     | Low/Medium                | No        | No                 | No                  | No                          | - scratch data<br>- easily reproducible data<br>- intermediate job files |
| `/hpc/projects/${NAME}`    | High                      | Yes [^2]  | Yes                | Optional [^1]       | Optional [^3]               | - working/active data sets<br>- results<br>- difficult to reproduce data |
| `/hpc/archives/${NAME}`    | High                      | Yes [^2]  | Yes                | Optional [^1]       | Optional [^3]               | - completed projects<br>- data with retention requirements |
| `/hpc/user_apps/${GROUP}`  | High                      | Yes [^2]  | Yes                | Yes [^4]            | No                          | - shared application installations |
| `/hpc/reference/${NAME}`   | High                      | Yes [^2]  | Optional           | Optional            | No                          | - easy to re-download<br>- easy to reproduce<br>- write-once, read-many<br>- storage optimized for reads |
| `/hpc/instruments/${NAME}` | High                      | Yes [^2]  | Yes                | Optional [^1]       | Optional [^3]               | - raw or preprocessed instrument data<br>- directory per-instrument |
| `/hpc/websites/${VHOST}`   | Variable                  | Optional  | Optional           | Optional            | Optional                    | - static web content<br>- requires a vhost name for website |



[^1]:
    Off-site replicas available on a per-project basis, subject to constraints
    on space and available inter-site bandwidth.
[^2]:
    Snapshot polices will vary based on space constraints and the underlying
    storage snapshot features. Dynamic workflow patterns, with frequent
    writes/re-writes/deletes, typically requires reducing snapshot lifespan.
[^3]:
    Long-term archiving a copy of data to Deep Archive is available upon request.
[^4]:
    `/hpc/user_apps` may be replicated read-only and require a specific host or
    hosts for writes.

## Namespace Details

###  Home Directory - `${HOME}`

The user `${HOME}` directory, also known as `~` and on Scientific Computing
systems, always located at `/home/${USER}`, is for private user data. The
system uses this location to store sensitive data, website caches/cookies,
Kerberos ticket data, credentials, etc., and because of this should always have
permissions of `0700` and ownership of `${USER}:${USER}.grp`. This location
should NEVER be shared with another account or user on the system. If there is a
need for multiple people to share an account, please request a shared service
account that is not a real person.

###  Extended Personal Workspace - `/hpc/mydata/${USER}`

This location is provided to give each user 1 TB of personal working space
where they can relax permissions to share data or work on small collaborations
without needed to request storage spaces. It's intended to provide a space to
try things out and once a project has matured, to then request project, archive
or other explicit space for the project.

###  Local Scratch - `/local/scratch`, `/hpc/nodes/${NODE}`

!!! Warning

    This space is subject to being purged at each node reboot.

Each node has some amount of local working storage. This can always be accessed
via `/tmp` which is a per-user namespace only available when on the node.
`/local/scratch` is available for use where a project might want to stage data
which remains on the node across multiple jobs. `/local/scratch` on each node
is then NFS exported to all other nodes and can be found at
`/hpc/nodes/${NODENAME}`. Please consult with us before using this space as
local storage is not treated as a consumable by Slurm and filling a node's
local disks can negatively impact other jobs.

### Shared Scratch - `/hpc/scratch/${NAME}`

!!! warning

    NEVER LEAVE THE ONLY COPY OF IMPORTANT DATA ON A SCRATCH SPACE.

Shared scratch storage areas are available via this namespace. The locations
will be tuned for maximum performance and the cost of reliability. Scratch
spaces are subject to being lost as a result of very few disk failures or being
purged and rebuilt on relatively short notice to address performance or space
issues.

###  Project Space - `/hpc/projects/${NAME}`

Project spaces are intended to be good working spaces with high reliability.
Snapshots, where possible, provide a history to help recover from mistaken
deletes or changes, but as noted above the amount of retained history is
subject to the usage pattern of the project. The level of replication/backup
and long term archiving can be adjusted as needed for a given projects
requirements.

### Archive Space - `/hpc/archives/${NAME}`

Archive spaces are intended to be write-once and then never or extremely rarely
updated, until they reach a pre-determined end-of-life and are removed. The
underlying on-prem/site storage will be optimized for reliability and read
performance and this is a good location to park data which needs to be made
available via the web or [Globus](https://globus.org) on a long term basis.

###  Application Space - `/hpc/user_apps/${GROUP}`

This location provides an optimized location for installing shared
applications. It is organized by groups, with each PI/lab group having a
location where they can install applications, with permissions to share those
as widely as need. Optionally a `module` can be added so that applications here
can be managed with `module load appname/version` after doing `module load
${GROUP}`.

###  Reference Data - `/hpc/reference/${NAME}`

The reference location is provided as a place to store on-site copies of public
or other reference data to avoid re-downloading the same datasets repeatedly.
Many NCBI datasets fall into this category, where it makes sense to manage one
copy everyone can access and use. Only things easy to reproduce or re-download
should be kept here. This space is optimized for reading to support being used
in scale-out workflows that need to access reference data.

###  Instrument Data - `/hpc/instruments/${NAME}`

Storing data from instruments presents some special problems. It's common to
have an instrument controlled by a Windows PC which cannot be updated due to
vendor/support restrictions and is at increased risk for malware or ransomware.
To limit the impact of an infected instrument PC, each instrument can have a
separate service account such that a given instrument can only reach/modify its
own data. Additionally, by having this space accept data but be treated as
read-only to all other systems, it's possible to maintain a long snapshot
history to enable recovering from a potential ransomware infection with minimal
data loss. 

### Static Websites - `/hpc/websites/${VHOST}`

It's often convenient to be able to produce static website content from the HPC
environment and make it available via a public website. The most basic use of
this location is to create a hostname, say `myproject.czbiohub.org`, then any
data written to `/hpc/websites/myproject.czbiohub.org` will be available via
[https://myproject.czbiohub.org](https://myproject.czbiohub.org). Additional
features, like authentication and access control can be made available upon
request.


## Viewing Quota

You can use the `quota` command to view quota for VAST, or NFS storage, but if you want to view quota for Lustre filesystem please 
see [View Lustre Quota](./lustre.md#managing-quotas).

You can view quota for a specific filesystem by running `quota -s -f /path/to/filesystem` which will show the quota for that filesystem.
For instance if you want to view quota for $MYDATA you can run `quota -s -f $MYDATA`.

```console
[shahzeb.siddiqui@login-01 ~]$ quota -s -f $MYDATA
quota: Cannot resolve mountpoint path /hpc/scratch/loupe-1: Stale file handle
quota: Cannot resolve mountpoint path /hpc/scratch/loupe-2: Stale file handle
Disk quotas for user shahzeb.siddiqui (uid 5839):
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
vast-sf.mammoth.infiniband:/mydata/shahzeb.siddiqui
                  7203M    885G    932G           48336       0       0
```
