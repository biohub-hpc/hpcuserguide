# Submitting Jobs

There are few ways to submit jobs to scheduler
- 
- **sbatch**: Batch job submission 
- **salloc**: Interactive batch job
- **srun**: Run parallel job 


## sbatch: Batch Job Submission

The `sbatch` command is used to submit a [batch job](./batch_jobs.md) to the scheduler for later execution. A batch script is a file 
containing a series of commands to be executed.

### Example Batch Script

Shown below is an example batch script

```bash
#!/bin/bash

#SBATCH --job-name=ExampleJob
#SBATCH --output=example_job.out
#SBATCH --error=example_job.err
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=cpu

# Your commands go here
echo "Hello, SLURM!"
```

Submit the job with:

```bash
sbatch example_job.sh
```

## salloc: Interactive Batch Job

The `salloc` command is used to allocate resources for an [interactive job](./interactive_jobs.md).
This is useful when you need to run a job interactively.

### Example Interactive Job

The example below will request 1 node, 1 task on *cpu* partition for 1hr 

```bash
salloc --time=01:00:00 --nodes=1 --ntasks=1 --partition=cpu
```

Once the resources are allocated, you can run your commands interactively.

## srun: Run Parallel Job

The `srun` command is used to run parallel jobs. It can be used within a batch script or interactively.

### Example Usage

```bash
[shahzeb.siddiqui@login-01 ~]$ srun --time=01:00:00 --nodes=1 --ntasks=4 hostname
cpu-b-3
cpu-b-3
cpu-b-3
cpu-b-3
```

## Common SLURM Options

Here are some commonly used SLURM options that can be included in your job scripts or commands:

| Option | Description |
| ------------------- | -------------------------------------------------------|
| `--time=24:00:00` | Time limit, formatted as `[DD-][HH]:[MM]:[SS]` |
| `--nodes=N` | Number of nodes |
| `--partition=PARTITION_NAME` | Partition(s) to run in |
| `--ntasks=N` | Number of tasks to start in the job |
| `--cpus-per-task=N` | Number of cores to request per task |
| `--job-name=NAME_OF_JOB` | Gives the job a friendly name |
| `--gpus=N` | Number of GPUs for the job |
| `--constraint=CONSTRAINTS` | A list of constraints to place on the job |

## Additional Resources

For more detailed information, refer to the SLURM documentation:

- [`sbatch` man page](http://slurm.schedmd.com/sbatch.html)
- [`srun` man page](http://slurm.schedmd.com/srun.html)
- [`salloc` man page](http://slurm.schedmd.com/salloc.html)

If you need further assistance, please contact your system administrator or refer to the [SLURM User Guide](http://slurm.schedmd.com/documentation.html).


This guide provides an overview of the different ways to submit jobs using SLURM, along with examples and common options.
