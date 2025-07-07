---
id: 368
title: What LDAP groups am I in?
date: 2018-01-11T02:59:41+00:00
author: mrbusche
permalink: /2018/01/11/what-ldap-groups-am-i-in/
categories:
  - Uncategorized
---

Ever wonder what LDAP groups you're a part of? There's a super simple command that will tell you

    net user ${windowsUsername} /domain

In my case

    net user mrbusche /domain

Keep in mind this will run against your current domain on your computer, so if you're a VPN user this may not work correctly if you're computer domain is not your companies LDAP domain

If you need more details and are the logged in user you can also run the following. This provides a lot more detail and the ldap groups aren't split into two columns where you potentially can't see the full name.

    gpresult /user mrbusche /r
