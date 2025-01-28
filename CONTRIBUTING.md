# CONTRIBUTING GUIDE

This guide will discuss how you can contribute back to this project. 

To get started, you should have a [GitHub account](http://github.com/join) in order to contribute back.

## Fork repo

First, you'll need to fork the repo https://github.com/czbiohub-sf/hpcuserguide

You might need to setup your SSH keys in your git profile if you are using ssh option for cloning. For more details on
setting up SSH keys in your profile, follow instruction found in https://help.github.com/articles/connecting-to-github-with-ssh/

SSH key will help you pull and push to repository without requesting for password for every commit. Once you have forked the repo, clone your local repo by running

```bash
git clone git@github.com:czbiohub-sf/hpcuserguide.git
```

## Adding Upstream Remote

First you need to add the ``upstream`` repo, to do this you can issue the
following

```bash
git remote add upstream git@github.com:czbiohub-sf/hpcuserguide.git
```

The `upstream` tag is used to sync changes from upstream repo to keep your
repo in sync before you contribute back.

Make sure you have set your user name and email set properly in git configuration.
We don't want commits from unknown users. This can be done by setting the following:

```bash
git config user.name "First Last"
git config user.email "abc@example.com"
```

For more details see [First Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

## Sync your branch from upstream

The `main` from upstream will get Pull Requests from other contributors, in-order
to sync your forked repo with upstream, run the commands below:

```bash
git checkout main
git fetch upstream main
git pull upstream main
```

Once the changes are pulled locally you can sync main branch with your
fork as follows:

```bash
git checkout main
git push origin main
```

You should sync your fork whenever you want to contribute back.

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

Once your branch is created, please create a [Pull Request](https://github.com/czbiohub-sf/hpcuserguide/compare) with
destination branch `main` and your base branch is your branch from your fork.

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

You can navigate to file `site/index.html` and open it on your browser or via command 

```console
open site/index.html
```