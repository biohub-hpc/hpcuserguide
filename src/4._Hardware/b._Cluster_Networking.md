# Network View

<nwdiag>
nwdiag {
  node_width = 72;
  login [label = "Login\nNodes"];
  loginpriv [label = "Private\nLogin"];
  ondemand [label = "OnDemand"];
  globus [label = "Globus"];
  slurm [label = "Slurm\nController"];
  samba [label = "Samba"];
  ess [label = "ESS GPFS\nStorage"];
  ddn [label = "DDN Lustre\nStorage"];
  nas [label = "ZFS/NAS\nStorage"];
  cpu [label = "CPU\nNodes"];
  gpu [label = "GPU\nNodes"];

  group {
    cpu;
    gpu;
  }

  network HPCEthernet {
    login;
    loginpriv;
    ondemand;
    globus;
    samba;
    slurm;
    nas;
    ess;
    cpu;
    gpu;
  }

  network Infiniband {
    login;
    loginpriv;
    ondemand;
    globus;
    samba;
    slurm;
    nas;
    ddn;
    cpu;
    gpu;
  }
}
</nwdiag>
