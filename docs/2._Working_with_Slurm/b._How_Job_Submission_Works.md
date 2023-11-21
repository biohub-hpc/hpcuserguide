
# How Job Submission Works

Before diving into a job submission, let's stop for a moment to consider what
happens when a job is submitted to Slurm. A simplified diagram of the basic
process is:

```kroki-actdiag
actdiag {
  submit -> parseargs -> accept -> schedule -> assign -> run -> writeoutput -> exit -> writejobrecord -> reviewoutput

  lane user {
     label = "User"
     submit [label = "Submit Job\nsbatch, srun, salloc"];
     reviewoutput [label = "slurm-JOBID.out"];
  }
  lane slurmctld {
     label = "Slurm Controller"
     parseargs [label = "Parse job options"];
     accept [label = "Accept job submission"];
     schedule [label = "Schedule job for\nexecution"];
     assign [label = "Assign job to\nresources"];
     writejobrecord [label = "Write job record\nto accounting db"];
  }
  lane slurmd {
     label = "Slurm Node\nDaemon(s)";
     run [label = "Run job script on\nnodes(s)"];
     writeoutput [label = "Write stdio/stderr\nto output file"];
     exit [label = "Return script exit\ncode"];
  }
}
```

