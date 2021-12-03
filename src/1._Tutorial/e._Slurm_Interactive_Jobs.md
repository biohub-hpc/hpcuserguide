# Slurm: Job Submission

Before diving into a job submission, let's stop for a moment to consider what
happens when a job is submitted to Slurm. A simplifed diagram of the basic
steps is:

<actdiag>
actdiag {
  submit -> accept -> parseargs -> schedule -> assign -> run -> writeoutput -> exit -> writejobrecord -> reviewoutput

  lane user {
     label = "User"
     submit [label = "Submit Job\nsbatch, srun, salloc"];
     reviewoutput [label = "slurm-JOBID.out\n--ouptut=/path/to/output"];
  }
  lane slurmctld {
     label = "Slurm Controller"
     accept [label = "Accept job submission"];
     parseargs [label = "Parse job options"];
     schedule [label = "Schedule job for execution"];
     writejobrecord [label = "Write job record to accounting db"];
  }
  lane slurmd {
     label = "Slurm Node Daemon(s)";
     run [label = "Run job script on nodes(s)"];
     writeoutput [label = "Write stdio/stderr to output file"];
     exit [label = "Return script exit code"];
  }
}
</actdiag>

# Interactive Jobs

There are many occasions when it's desirable to have a node for interactive use
with a specific hardware configuration. For instance, manually editing a 256GB
file in vim might work better on a node with a fast connection to the storage
and > 256 GB of memory, rather than a login node that is shared and may have
memory usage restirctions.  node. Or you may want to start a series of
graphical applications and display them on your local workstation while still
having fast access to the underlying storage. In these cases a straightforward
interactive shell obtained with {{{srun}}} is a good solution. Some examples:

```
srun --pty bash -l
```

TODO: expanded examples of intractive jobs. 


