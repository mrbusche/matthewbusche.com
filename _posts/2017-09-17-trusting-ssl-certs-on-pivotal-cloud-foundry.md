---
id: 328
title: Trusting SSL certs on Pivotal Cloud Foundry
redirect_from:
  - /blog2/2017/09/17/trusting-ssl-certs-on-pivotal-cloud-foundry/
date: 2017-09-17T01:37:26+00:00
author: mrbusche
layout: post
permalink: /2017/09/17/trusting-ssl-certs-on-pivotal-cloud-foundry/
categories:
  - java
tags:
  - pcf
  - pivotal cloud foundry
  - trust certs
---
If you run into a scenario where you&#8217;re using a temporary SSL cert or a wildcard cert with Pivotal Cloud Foundry you may run into an issue where your cert is not being trusted. This is NOT something you should use in production, but if you&#8217;re trying to get things up and running for a proof of concept the solution below should get you past an SSL errors.

Note: the TRUST_CERTS: is indented under the env: and since this would be going into a yaml file the indentation does matter

<pre>- name: mbusche
&nbsp;&nbsp;instances: 1
&nbsp;&nbsp;memory: 1024M
&nbsp;&nbsp;disk_quota: 1024M
&nbsp;&nbsp;buildpack: java_buildpack
&nbsp;&nbsp;path: target/myapp.jar
&nbsp;&nbsp;stack: cflinuxfs2
&nbsp;&nbsp;timeout: 180
&nbsp;&nbsp;services:
&nbsp;&nbsp;- mbusche-config-server
&nbsp;&nbsp;env:
&nbsp;&nbsp;&nbsp;&nbsp;TRUST_CERTS: test.matthewbusche.com
</pre>