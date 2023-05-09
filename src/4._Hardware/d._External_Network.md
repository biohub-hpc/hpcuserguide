# Network View

<nwdiag>
nwdiag {
  node_width = 72;
  login [label = "Login\nNodes"];
  loginpriv [label = "Private\nLogin"];
  ondemand [label = "OnDemand"];
  services [label = "Misc.\nServices"];
  slurm [label = "Slurm\nController"];
  globus [label = "Globus"];
  samba [label = "Samba\nServers"];

  network Internet {
    login;
    ondemand;
    globus;
    services;
  }

  network BioHub {
    loginpriv;
    samba;
    slurm;
  }
}
</nwdiag>
