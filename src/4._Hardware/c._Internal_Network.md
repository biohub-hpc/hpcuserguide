# Network View

<nwdiag>
nwdiag {
  node_width = 72;
  login [label = "Login\nNodes"];
  ondemand [label = "OnDemand\nServer"];
  crustations [label = "Crustations"];
  slurm [label = "Slurm\nController"];
  ess [label = "ESS GPFS\nStorage"];
  ddn [label = "DDN Lustre\nStorage"];
  cpu [label = "CPU\nNodes"];
  gpu [label = "GPU\nNodes"];

  network BioHub {
    login;
    ondemand;
    crustations;
  }

  network HPCEthernet {
    login;
    ondemand;
    crustations;
    slurm;
    group {
      cpu;
      gpu;
    }
  }

  network Infiniband {
    ess;
    ddn;
    login;
    slurm;
    ondemand;
    crustations;
    cpu;
    gpu;
  }
}
</nwdiag>
