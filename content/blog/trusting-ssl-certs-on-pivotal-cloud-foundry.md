---
id: 328
title: Trusting SSL certs on Pivotal Cloud Foundry
date: 2017-09-17T01:37:26+00:00
author: mrbusche
permalink: /2017/09/17/trusting-ssl-certs-on-pivotal-cloud-foundry/
categories:
  - java
tags:
  - pcf
  - pivotal cloud foundry
  - trust certs
---

If you run into a scenario where you're using a temporary SSL cert or a wildcard cert with Pivotal Cloud Foundry you may run into an issue where your cert is not being trusted. This is NOT something you should use in production, but if you're trying to get things up and running for a proof of concept the solution below should get you past an SSL errors.

Note: the TRUST_CERTS: is indented under the env: and since this would be going into a yaml file the indentation does matter

```yaml
- name: mbusche
  instances: 1
  memory: 1024M
  disk_quota: 1024M
  buildpack: java_buildpack
  path: target/myapp.jar
  stack: cflinuxfs2
  timeout: 180
  services:
    - mbusche-config-server
  env:
    TRUST_CERTS: test.mrbusche.com
```
