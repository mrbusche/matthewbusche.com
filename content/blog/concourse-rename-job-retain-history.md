---
title: Concourse rename job and retain history
date: 2020-11-23 21:01:30
permalink: /2020/11/23/concourse-rename-job-retain-history/
tags:
  - concourse
---

To rename a Concourse job and retain history, you can use the [`old_name`](https://concourse-ci.org/jobs.html#schema.job.old_name) attribute.

```yaml
jobs:
  - name: build-8-jdk-centos
    old_name: 8-jdk-centos
```

Once you've fly'd the pipeline with the new and old_name attributes you can remove old_name and fly it again, it's no longer needed.

A good reason to rename a job would be because of recent concourse deprecations with valid identifiers. Our existing job started with a number, which will stop being allowed in a future Concourse version.

```
DEPRECATION WARNING:

jobs.8-jdk-centos: '8-jdk-centos' is not a valid identifier: must start with a lowercase letter
```
