---
title: Bruno Infrastructure
description: Description/listing of what resources are currently in Bruno
---
# Nodes

Note: Future nodes show delivery ETA in <font color=red> red </font>.


| Name              | Cores     | Memory      | TmpFS    | GPUs                | GPU Type | Date  |
| ----------------- | --------: | ----------: | -------: | ------------------: | :------: | :---: |
|`login-[01-02]`    |  128/node | 1 TB/node   | 4 TB     | none                | N/A      | 2021  |
|`login-fry1`       |  16/node  | 512 GB      | 15 TB    | 4 x TitanXP         | PCIe     | ?     |
|`login-fry2`       |  16/node  | 256 GB      | 15 TB    | 4 x TitanXP         | PCIe     | ?     |
|`login-falcon`     |  32/node  | 256 GB      | 85 TB    | 3 x TitanRTX        | PCIe     | ?     |
|`cpu-a-[1-2]`      |  128/node | 4 TB/node   | 4 TB     | none                | N/A      | 2021  |
|`cpu-b-[1-6]`      |  128/node | 4 TB/node   | 4 TB     | none                | N/A      | 2021  |
|`cpu-c-[1-4]`      |  24/node  | 128 GB/node | 4 TB     | none                | N/A      | ?     |
|`cpu-d-1`          |  32/node  | 2 TB/node   | 6.5 TB   | none                | N/A      | ?     |
|`cpu-e-[1-2]`      |  128/node | 4 TB/node   | 4 TB     | none                | N/A      | <font color=red> 2023Q4 </font> |
|`gpu-a-[1-4]`      |  128/node | 2 TB/node   | 14 TB    | 4 x A100(40GB)/node | SXM4     | 2021  |
|`gpu-b-[1-6]`      |  128/node | 512 GB/node | 14 TB    | 4 x A6000/node      | PCIe     | 2022  |
|`gpu-c-[1-4]`      |  30/node  | 480 GB/node | 7 TB     | 2 x A40 / node      | PCIe SLI | 2023  |
|`gpu-d-[1-2]`      |  128/node | 2 TB/node   | 45 TB    | 4 x A100(80GB)/node | SXM4     | 2023  |
|`gpu-e-[1-4]`      |  16/node  | 512 GB/node | 7 TB     | 1 x A40 / node      | PCIe     | <font color=red> 2023Q4 </font> |
|`gpu-sm01-[01-20]` |  16/node  | 256 GB/node | 1.8 TB   | 1 x A40 / node      | PCIe     | 2022  |
|`gpu-sm02-[01-20]` |  16/node  | 256 GB/node | 1.8 TB   | 1 x A40 / node      | PCIe     | 2022  |
[ Computational Resources ]

* Total User Partitions CPU cores: 
    * Today: 2336
    * EOY: 3296
* Total GPUs: 
    * Today: 107
    * EOY: 111

<hr>

# GPU Summary

Note: Future GPUs show delivery ETA in <font color=red> red </font>.

| GPU Type       | Bruno Total            | (to be delivered)                   |
| :------------: | :--------------------: | :---------------------------------: |
| A100 (40 GB)   | 16                     |                                     |
| A100 (80 GB)   | 8                      |                                     |
| A6000 (48 GB)  | 24                     |                                     |
| A40 (48GB)     | 48                     | 4 (<font color=red> 2023Q4 </font>) |
| TitanXP        | 8                      |                                     |
| TitanRTX       | 3                      |                                     |
[ GPU Totals by type ]

# Storage Nodes/Appliances

Note: Future storage nodes/appliances show delivery ETA in <font color=red> red </font>.

| Name                 | FileSystem   | Size        | Date  |
| -------------------- | ------------ | ----------- | ----- |
| `storage-a-0[1-2]`   | ZFS/NFS      | 900 TB/node | 2019? |
| `storage-b-0[1-2]`   | ZFS/NAS      | 38 TB/node  | 2022  |
| `storage-odb2-[1-2]` | ZFS/NAS      | 4.7 PB      | 2022  |
| `storage-odb5-[1-2]` | ZFS/NAS      | 4.7 PB      | 2022  |
| `storage-c-1`        | ZFS/NAS      | ~ 4 PB      | <font color=red> 2023Q4 </font> |
| DDN Appliance EXA1   | Lustre       | 5.9 PB      | 2023  |
| IBM ESS Appliance    | GPFS         | 4.1 PB      | 2018  |
| VAST TBD             | VAST/\[p]NFS | 1 PB        | <font color=red> 2023Q4 </font> |
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

