# CONTRIBUTING GUIDE

This guide will discuss how you can contribute back to this project. 

To get started, you should have a [GitHub account](http://github.com/join) in order to contribute back.

Make sure you have set your username and email set properly in git configuration.
We don't want commits from unknown users. This can be done by setting the following:

```bash
git config --global user.name "First Last"
git config --global user.email "abc@example.com"
```

For more details see [First Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

## Clone repo

First, you'll need to clone the repo https://github.com/biohub-hpc/hpcuserguide/

```bash
git clone git@github.com:biohub-hpc/hpcuserguide.git
```

You might need to setup your SSH keys in your git profile if you are using ssh option for cloning. For more details on
setting up SSH keys in your profile, follow instruction found in https://help.github.com/articles/connecting-to-github-with-ssh/

SSH key will help you pull and push to repository without requesting for password for every commit. 

## Sync your branch 

The `main` from origin will get Pull Requests from other contributors, in-order
to sync your repo with upstream (GitHub), run the commands below:

```bash
git checkout main
git fetch origin main
git pull origin main
```

Once the changes are pulled locally you can are ready to start the contribution process

## Contribution Workflow

If you want to contribute back, you should create a feature branch from `main`
and add your files, commit and push them to your fork. The workflow can be summarized
as follows:

```console
git checkout main
git checkout -b featureX
git add <file1> <file2> ...
git commit -m "commit message"
git push origin featureX
```

Once your branch is created, please create a [Pull Request](https://github.com/biohub-hpc/hpcuserguide/compare) with
destination branch `main` and your base branch is your branch from your fork.

**PLEASE CONSIDER USING MEANINGFUL BRANCH NAMES AND COMMIT MESSAGES. DO NOT USE SAME BRANCH NAME FOR EVERY PR**

## Building Documentation

You can build the documentation locally or let it run in GitHub workflow. If you would like to build the docs
locally, create your own python virtual environment on your laptop or HPC cluster.

```console
python -m venv ./env
source ./env/bin/activate
```

Once you have a python environment install the dependencies by running

```console
pip install -r requirements.txt
```

Next you build the docs by running, the files will be generated in directory *site*

```console
mkdocs build
```

Next, run the following command to serve the documentation locally, the url will be displayed in the console

```console
(hpcuserguide) ➜  hpcuserguide git:(update_contributing) ✗ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.27 seconds
INFO    -  [15:37:49] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [15:37:49] Serving on http://127.0.0.1:18080/hpc-user-guide/
```

The documentation is rsync into https://onsite.czbiohub.org/hpcdocs/ at Pull Request which can be used
to view rendered documentation if you don't want to build docs locally. Please note if multiple GitHub 
actions are triggered by different Pull Request the rsync can be clobbered and results may vary.

For more detail on the GitHub workflow see [.github/workflows/build.yml](https://github.com/czbiohub-sf/hpcuserguide/blob/main/.github/workflows/build.yml) 

The production workflow [.github/workflows/sync.yml](https://github.com/czbiohub-sf/hpcuserguide/blob/main/.github/workflows/sync.yml) will
sync the files to **/hpc/websites/hpc.czbiohub.org/** which are hosted by apache server at  https://hpc.czbiohub.org/