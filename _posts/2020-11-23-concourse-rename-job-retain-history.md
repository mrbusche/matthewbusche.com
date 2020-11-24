---
title: Concourse rename job and retain history
date: 2020-11-23 21:01:30
layout: post
tags:
  - concourse
---

To rename a Concourse job and retain history, you can use the `old_name` attribute.

```yaml
jobs:
  - name: build-8-jdk-centos
    old_name: 8-jdk-centos
```

Once you've fly'd the pipeline with the new old_name attribute you can remove it and fly it again.

A good reason to rename a job would be because of the recent concourse deprecations with valid identifiers. Our existing job started with a number, which stop being allowed in a future Concourse version.

```
DEPRECATION WARNING:

jobs.8-jdk-centos: '8-jdk-centos' is not a valid identifier: must start with a lowercase letter
```
