---
title: Bruno Infrastructure
description: Description/listing of what resources are currently in Bruno
---
# Nodes

| Name              | Cores     | CPU Type | Memory      | TmpFS    | GPUs                | GPU Type |
| ----------------- | --------: | :------: | ----------: | -------: | ------------------: | :------: |
|`login-[01-02]`    |  128/node |  AMD Epyc 7003   | 1 TB/node   | 4 TB     | none                | N/A      |
|`login-fry1`       |  16/node  |  INTEL Xeon E5 2609 v4   | 512 GB      | 15 TB    | 4 x TitanXP         | PCIe     |
|`login-fry2`       |  16/node  |  INTEL Xeon E5 2609 v4   | 256 GB      | 15 TB    | 4 x TitanXP         | PCIe     |
|`login-falcon`     |  32/node  |  INTEL Xeon E5 2667 v4  | 256 GB      | 85 TB    | 3 x TitanRTX        | PCIe     |
|`cpu-a-[1-2]`      |  128/node |  AMD Epyc 7H12   | 4 TB/node   | 4 TB     | none                | N/A      |
|`cpu-b-[1-6]`      |  128/node |  AMD Epyc 7H12   | 4 TB/node   | 4 TB     | none                | N/A      |
|`cpu-c-[1-4]`      |  24/node  |  INTEL Xeon Gold 6126  | 128 GB/node | 4 TB     | none                | N/A      |
|`cpu-d-1`          |  32/node  |  AMD Epyc 7601   | 2 TB/node   | 6.5 TB   | none                | N/A      |
|`cpu-e-[1-2]`      |  128/node |  AMD Epyc 7763   | 4 TB/node   | 4 TB     | none                | N/A      |
|`gpu-a-[1-4]`      |  128/node |  AMD Epyc 7742   | 2 TB/node   | 14 TB    | 4 x A100(40GB)/node | SXM4     |
|`gpu-b-[1-6]`      |  128/node |  AMD Epyc 7742   | 512 GB/node | 14 TB    | 4 x A6000/node      | PCIe     |
|`gpu-c-1`      |  30/node  |  AMD Epyc 7773X   | 480 GB/node | 7 TB     | 8 x A40 / node      | PCIe SLI |
|`gpu-d-[1-2]`      |  128/node |  AMD Epyc 7773X   | 2 TB/node   | 45 TB    | 4 x A100(80GB)/node | SXM4     |
|`gpu-e-[1-8]`      |  16/node  |  AMD Epyc 7313P   | 512 GB/node | 7 TB     | 1 x A40 / node      | PCIe     |
|`gpu-f-[1-6]` |  112/node  |  INTEL Xeon Platinum 8480c   | 2 TB/node | 2 TB   | 8 x H100 / node      | SXM4     |
|`gpu-sm01-[01-20]` |  16/node  |  AMD Epyc 7302P   | 256 GB/node | 1.8 TB   | 1 x A40 / node      | PCIe     |
|`gpu-sm02-[01-20]` |  16/node  |  AMD Epyc 7302P   | 256 GB/node | 1.8 TB   | 1 x A40 / node      | PCIe     |
[ Computational Resources ]

*Note: Change*

* Total User Partitions CPU cores: 
    * Today: 2336
    * EOY: 3296
* Total GPUs: 
    * Today: 107
    * EOY: 111

<hr>

# GPU Summary

| GPU Type       | Bruno Total            |
| :------------: | :--------------------: |
| A100 (40 GB)   | 16                     |
| A100 (80 GB)   | 8                      |
| A6000 (48 GB)  | 24                     |
| A40 (48GB)     | 48                     |
| H100 (80 GB) | 48 |
[ GPU Totals by type ]

# Storage Nodes/Appliances


| Name                 | FileSystem   | Size        |
| -------------------- | ------------ | ----------- |
| `storage-a-0[1-2]`   | ZFS/NFS      | 900 TB/node |
| `storage-b-0[1-2]`   | ZFS/NAS      | 38 TB/node  |
| `storage-odb2-[1-2]` | ZFS/NAS      | 4.7 PB      |
| `storage-odb5-[1-2]` | ZFS/NAS      | 4.7 PB      |
| `storage-c-1`        | ZFS/NAS      | ~ 4 PB      |
| DDN Appliance EXA1   | Lustre       | 5.9 PB      |
| VAST             | VAST/\[p]NFS | 1 PB        |
[ Storage servers and appliances ]

# Network View

## Bruno Cluster Network

```kroki-nwdiag
nwdiag {
  node_width = 96;
  internet [label = "Internet", shape = cloud];
  firewall [label = "Firewall", shape = roundedbox, width = 72];
  internet -- firewall;
  login [label = "Login\nNodes", stacked];
  ondemand [label = "OnDemand"];
  globus [label = "Globus"];
  webgateway [label = "Web\nGateway", shape = circle, stacked];

  ess [label = "ESS GPFS\nStorage"];
  ddn [label = "DDN Lustre\nStorage"];
  nas [label = "ZFS/NAS\nStorage"];
  cpu [label = "CPU\nNodes", stacked];
  gpu [label = "GPU\nNodes", stacked];

  group {
    label = "Compute Nodes";
    cpu;
    gpu;
  }

  network BioHub {
    label = "BioHub\nScience DMZ";
    color = blue;
    firewall;
    login;
    ondemand;
    globus;
    webgateway;
  }

  network HPCEthernet {
    label = "Ethernet\n400/200/100";
    color = yellow;
    login;
    ondemand;
    globus;
    webgateway;
    nas;
    ess;
    cpu;
    gpu;
  }

  network Infiniband {
    label = "Infiniband\nHDR/EDR";
    color = "green";
    login;
    ondemand;
    globus;
    webgateway;
    nas;
    ddn;
    cpu;
    gpu;
  }
}
```

