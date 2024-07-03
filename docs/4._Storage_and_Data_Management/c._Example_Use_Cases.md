# Example Use Cases

## Analysis Pipeline

Suppose we have a pipeline, managed by a workflow tool like `nextflow`. The
incoming raw data for this pipeline is generated from one or more lab
instruments. The pipeline processing will produce

 * intermediate/scratch files
 * quality control results to be web-accessible
 * processed data made available for researcher secondary analysis via local filesystem and globus

The steps in our hypothetical data flow might be:

1. Data moves from instrument(s) to `/hpc/instruments/${INSTRUMENT_NAME}(s)`. Can be push or pull.
2. Pipeline copies data to `/hpc/scratch/${NAME}` as a working location.
3. HPC Cluster jobs perform analysis:
    *  Reference data read from `/hpc/reference/${DBNAME}`
    *  Running jobs use `/tmp` and/or `/local/scratch` and/or `/hpc/scratch/${NAME}` for intermediate and temporary files.
    *  Results written to `/hpc/projects/${NAME}`
4. QC output formatted and written to `/hpc/websites/${NAME}.czbiohub.org`
5. Data to be retained long-term copied to `/hpc/archives/%{NAME}`

This example uses shared and local scratch, instrument storage, projects
storage, website storage and archive storage. As all these are also available
(or can be) via [Globus](https://globus.org), any of these spaces can be
optionally used for data delivery to or sharing with collaborators.