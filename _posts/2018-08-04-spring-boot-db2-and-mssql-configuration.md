---
id: 421
title: Spring Boot DB2 and MSSQL Configuration
redirect_from:
  - /blog2/2018/08/04/spring-boot-db2-and-mssql-configuration/
date: 2018-08-04T20:51:36+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=421
permalink: /2018/08/04/spring-boot-db2-and-mssql-configuration/
categories:
  - java
  - spring boot
tags:
  - datasource configuration
  - db2
  - mssql
  - mysql
  - oracle
  - spring boot
---
By default Spring boot does a lot for you in datasource configuration, but if you&#8217;re using two separate database types &#8211; DB2, MSSQL, MySQL, Oracle, etc. It doesn&#8217;t know how to infer which database type each is, so if you are configuring multiple different database types in Spring you need to specify the jpa.database type. In a yaml configuration your datasources should be defines like so.

<pre>spring:
&nbsp;&nbsp;datasource:
&nbsp;&nbsp;&nbsp;&nbsp;url: jdbc:sqlserver://${server}:${port};databaseName=${databaseName}
&nbsp;&nbsp;&nbsp;&nbsp;username: ${username}
&nbsp;&nbsp;&nbsp;&nbsp;password: ${password}
&nbsp;&nbsp;jpa:
&nbsp;&nbsp;&nbsp;&nbsp;database: sql_server
db2:
&nbsp;&nbsp;datasource:
&nbsp;&nbsp;&nbsp;&nbsp;jdbcurl: jdbc:db2://${server}:${port}/${databaseName}
&nbsp;&nbsp;&nbsp;&nbsp;username: ${username}
&nbsp;&nbsp;&nbsp;&nbsp;password: ${password}
&nbsp;&nbsp;jpa:
&nbsp;&nbsp;&nbsp;&nbsp;database: db2
</pre>