# Introduction

!!! warning "Draft Draft Draft"

    This is a draft of the storage descriotion, layout and recommended usage.
    Comments/suggestions/critiques to us in Slack #hpc-community.


+----------------------+---------------------------+---------------------------+
| Unix Path            | Backups                   | Typical Use Cases         |
|                      |                           |                           |
+======================+===========================+===========================+
| `/local/scratch`<br> | None                      | - Temp/intermediate files |
| `/hpc/nodes/${NODE}` |                           | - Copies of data          |
+----------------------+---------------------------+---------------------------+
| `/hpc/scratch`       | None                      | - Temp/intermediate files |
|                      |                           | - Copies of data          |
+----------------------+---------------------------+---------------------------+
| `/hpc/projects`      | - On-site Replicas        | - Working data            |
|                      | - Off-site Replicas[^1]   |                           |
|                      | - Snapshots (history)[^2] |                           |
+----------------------+---------------------------+---------------------------+
| `/hpc/archives`      | - On-site Replicas        | - Archival periods req.   |
|                      | - Off Site Replicas[^1]   | - Disaster recovery req.  |
|                      | - Cloud Archive           | - High cost data          |
|                      | - Snapshots (history)[^2] |                           |
+----------------------+---------------------------+---------------------------+
| `/hpc/mydata`        | - On-site Replicas        | - Personal Workspace      |
|                      | - Snapshots (history)[^2] |                           |
+----------------------+---------------------------+---------------------------+
| `/home`              | - On-site Replicas        | - Private data            |
|                      | - Snapshots (history)[^2] |                           |
+----------------------+---------------------------+---------------------------+

[^1]:
    Off-site replicas available on a per-project basis, subject to contraints
    on space and available inter-site bandwidth.
[^2]:
    Snapshot polices will vary based on space constraints and the underlying
    storage snapshot features. Dynamic workflow patterns, with frequent
    writes/re-writes/deletes, typically requires reducing snapshot lifespan.
