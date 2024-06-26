---
title: Why cant I use sudo?
description: 
published: true
date: 2023-11-19T17:11:09.142Z
tags: 
editor: markdown
dateCreated: 2023-11-19T15:38:02.773Z
---

# Why can't I use `sudo`?

The cluster environment is a shared resource, with many people and groups
accessing it. Because of that, data privacy is 100% dependent on unix file
permissions and ACLs. Anyone with `sudo` access can bypass those permissions,
which means as a rule we cannot give out `sudo` to individual users who are not
approved admins for the cluster. Additionally, the cluster environment is
complex and administrative activities need to be carried out in a restricted,
planned and well communicated fashion, something that becomes less realistic to
accomplish as the number of people with `sudo` access increases. In order to
keep the environment as stable and secure as possible, access to `sudo` is very
restricted.

The flip side of that requirement is that it means we (sysadmins) have to be
***very*** responsive to address user requirements. If you have a need that you
believe requires `sudo`, contact us and we'll either take care of the parts
requiring `sudo` access or help you achieve the same goal from userspace
without needing `sudo`. As an example of why `sudo` is rarely a hard
requirement, the cluster application stack (`module` environment) is almost
entirely configured without the use or need of `sudo` access.
