# Job Dependencies

Job dependencies are features of SLURM that are used to delay the start time of a job until specific job dependencies have been satisfied. SLURM will then run them in the proper order based on the conditions supplied.  

This is useful when you want to use the output of a job, as the input of another job, without having to continuously check or create an automation that would execute this when the job is complete. 

These features are typically initiated with the `--dependency` option to `sbatch`, `salloc` or `srun`.

## Command Line


The `--dependency` option is typically used on the command line when invoking slurm job related client commands.


```
$ sbatch --dependency=<type:job_id[:job_id][,type:job_id[:job_id]]> ...
```


| Dependency Type | Description |
| -------- | -------- |
| after:jobid[:jobid...] | Job can begin after the specified jobs have started|
| afterany:jobid[:jobid...] | Job can begin after the specified jobs have terminated|
| afternotok:jobid[:jobid...] | Job can begin after the specified jobs have failed|
| afterok:job_id[:jobid...]     | Job can begin after the specified jobs have run to completion with an exit code of zero (see the user guide for caveats).|
|singleton |Jobs can begin execution after all previously launched jobs with the same name and user have ended. This is useful to collate results of a swarm or to send a notification at the end of a swarm.|


Multiple job id's can be appended to a dependency type and mulyiple dependency types can be added a job's dependency.

**Example:**

```
[randall.white@login-02 ~]$ sbatch job_submission1.sh
Submitted batch job 11719432
[randall.white@login-02 ~]$ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          11719432   preview send_msg randall.  R       2:13      1 cpu-c-1
[randall.white@login-02 ~]$ sbatch --dependency=afterany:11719432 job_submission2.sh
Submitted batch job 11719434
[randall.white@login-02 ~]$ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          11719434   preview send_msg randall. PD       0:00      1 (Dependency)
          11719432   preview send_msg randall.  R       2:37      1 cpu-c-1
```



## Job Script
The `--dependency` option is typically used on the command line when invoking slurm job related client commands.

```
#!/bin/bash

#SBATCH --job-name=SimpleJobScript
#SBATCH --time=1:00
#SBATCH -p cpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --dependency=afterany:11719432

hostname

```

Submission
```
[randall.white@login-02 ~]$ sbatch job_submission2.sh
Submitted batch job 11719436
[randall.white@login-02 ~]$ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          11719436   preview send_msg randall. PD       0:00      1 (Dependency)
          11719432   preview send_msg randall.  R       6:43      1 cpu-c-1
```



## Tips and Tricks for Working With Dependencies

### Capturing JOBID for use with subsequent dependent jobs

```
[john.hanks@login-01 ~]$ JOBID=$(sbatch --parsable --wrap "sleep 300")
[john.hanks@login-01 ~]$ JOBID=$(sbatch --parsable --dependency=afterok:${JOBID} --wrap "sleep 300")
[john.hanks@login-01 ~]$ JOBID=$(sbatch --parsable --dependency=afterok:${JOBID} --wrap "sleep 300")
[john.hanks@login-01 ~]$ JOBID=$(sbatch --parsable --dependency=afterok:${JOBID} --wrap "sleep 300")
[john.hanks@login-01 ~]$ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          11598986       cpu     wrap john.han PD       0:00      1 (Dependency)
          11598985       cpu     wrap john.han PD       0:00      1 (Dependency)
          11598984       cpu     wrap john.han PD       0:00      1 (Dependency)
          11598983       cpu     wrap john.han  R       1:22      1 cpu-c-1

```

## Official Slurm Documentation

[SBATCH - Dependencies](https://slurm.schedmd.com/srun.html#OPT_dependency)