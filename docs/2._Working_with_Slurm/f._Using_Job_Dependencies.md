# Job Dependencies


## Slurm Man Page Description

The following excerpt from the [Slurm `sbatch` man
page](https://slurm.schedmd.com/sbatch.html#OPT_dependency) fully describes
Slurm dependencies:
<hr>
`-d, --dependency=<dependency_list>`

: Defer  the  start  of  this job until the specified dependencies have been
  satisfied.  `<dependency_list>` is of the form

    ```
    `<type:job_id[:job_id][,type:job_id[:job_id]]>` 
      or
    `<type:job_id[:job_id][?type:job_id[:job_id]]>`
    ```

: All  dependencies  must be satisfied if the "," separator is used.  Any
  dependency may be satisfied if the "`?`" separator is used.  Only one
  separator may be used. For instance:
 
    ```
  -d afterok:20:21,afterany:23
     ```

: means that the job can run only after a 0 return code of jobs 20 and 21 AND the
  completion of job 23. However: 

    ```
         -d afterok:20:21?afterany:23
    ```

: means that any of the conditions (`afterok:20` OR `afterok:21` OR
  `afterany:23`) will be  enough  to release  the  job.  Many  jobs  can  share
  the  same dependency and these jobs may even belong to different  users. The
  value may be changed after job submission using the scontrol command.
  Dependencies on remote jobs are allowed in a federation.  Once  a job
  dependency fails due to the termination state of a preceding job, the
  dependent job will never be run, even if the preceding job is requeued and
  has a different termination state in a subsequent execution.


    `after:job_id[[+time][:jobid[+time]...]]`
    
    : After the specified jobs start or are cancelled and 'time' in minutes from
      job start or  cancellation  hap‐ pens,  this  job can begin execution. If no
      'time' is given then there is no delay after start or cancellation.
    
    `afterany:job_id[:jobid...]`
    
    : This job can begin execution after the specified jobs have terminated.   This
      is  the  default  dependency type.
    
    `afterburstbuffer:job_id[:jobid...]`
    
    : This job can begin execution after the specified jobs have terminated and any
      associated burst buffer stage out operations have completed.
    
    `aftercorr:job_id[:jobid...]`
    
    : A task of this job array can begin execution after the corresponding task ID
      in the specified job has  completed successfully (ran to completion with an
      exit code of zero).
    
    `afternotok:job_id[:jobid...]`
    
    : This  job  can begin execution after the specified jobs have terminated in
      some failed state (non-zero exit code, node failure, timed out, etc).
    
    `afterok:job_id[:jobid...]`
    
    : This job can begin execution after the specified jobs have successfully
      executed (ran to completion with an exit code of zero).
    
    `singleton`
    
    : This  job  can  begin  execution after any previously launched jobs sharing
      the same job name and user have terminated.  In other words, only one job by
      that name and owned by that user can be running  or  suspended at  any  point
      in  time.  In a federation, a singleton dependency must be fulfilled on all
      clusters unless DependencyParameters=disable_remote_singleton is used in
      slurm.conf.
    
<hr>

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


