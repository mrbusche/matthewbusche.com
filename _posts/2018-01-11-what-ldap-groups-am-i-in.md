---
id: 368
title: What LDAP groups am I in?
date: 2018-01-11T02:59:41+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=368
permalink: /2018/01/11/what-ldap-groups-am-i-in/
categories:
  - Uncategorized
---
Ever wonder what LDAP groups you&#8217;re a part of? There&#8217;s a super simple command that will tell you

`net user ${windowsUsername} /domain`

In my case

`net user mrbusche /domain`

Keep in mind this will run against your current domain on your computer, so if you&#8217;re a VPN user this may not work correctly if you&#8217;re computer domain is not your companies LDAP domain