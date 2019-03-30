---
id: 37
title: Connecting MS SQL database to Railo datasource
redirect_from:
  - /blog2/2014/01/16/connecting-ms-sql-database-to-railo-datasources/
date: 2014-01-16T03:22:29+00:00
author: mrbusche
layout: post
permalink: /2014/01/16/connecting-ms-sql-database-to-railo-datasources/
categories:
  - ColdFusion
---

Tonight was the 2nd time I&#8217;ve struggled getting Microsoft SQL Server set up to communicate with Railo (and really anything at all), so I thought I&#8217;d write up some quick tips on what I had to do. Once you think you have everything set up there are 2 steps that are left.

Go to Microsoft SQL Server 20XX > Configuration Tools > SQL Server Configuration Manager

 <img src="/images/2015/05/sqlconfig.png" alt="sqlconfig" />

From there open up TCP/IP and make sure Listen All is set to No

 <img src="/images/2015/05/tcpipproperties.png" alt="tcpipproperties" />

After that go to the IP Addresses tab and make sure Active and Enabled are yes (enabled defaults to no) and make sure you&#8217;re using the IP and correct TCP Port when configuring your datasource.

Thanks to [this MSDN post](https://blogs.msdn.com/b/sqlblog/archive/2009/07/17/how-to-configure-sql-server-to-listen-on-different-ports-on-different-ip-addresses.aspx) for getting me on the right track.
