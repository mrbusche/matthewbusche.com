---
title: 'Current request is not of type HttpServletRequest'
date: 2018-10-24 10:05:57
permalink: /2018/10/24/current-request-is-not-of-type-httpservletrequest/
tags: java
---

Ran into this error this week

`There was an unexpected error (type=Internal Server Error, status=500). Current request is not of type [org.apache.catalina.servlet4preview.http.HttpServletRequest]: ServletWebRequest: uri=/my/url/`

Make sure you imported the correct `HttpServletRequest` import. I wanted `import javax.servlet.http.HttpServletRequest;`
