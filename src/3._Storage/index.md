# Introduction

!!! warning "Draft Draft Draft"

    This is a draft of the storage descriotion, layout and recommended usage.
    Comments/suggestions/critiques to us in Slack #hpc-community.

| Unix Path | Disk Redundancy | Backup Regimen | Typical Use Cases |
|:---------:|:---------------:|:--------------:|:-----------------:|
| `/local/scratch`<br>`/hpc/nodes/${NODENAME}` | None, Minimal | None<br>Subject to deletion | Intermediate files<br>temporary job data<br>reference/training/input data copies |
| `/hpc/projects` | High<br>performance tuned | On Site Replica<br>Optional Off-site Replica(s) | Working data<br>raw instrument data<br>scripts<br>documents<br>computational results<br>non-temporary data files |
| `/hpc/archives` | High<br>space optimized | On Site Replica<br> Optional Off-site Replica(s)<br>AWS Deep Archive | Publication associated data<br>data with long retention requirements<br> Disaster recovery data |


