# Network View

## Bruno Cluster Network

<nwdiag>
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
</nwdiag>
