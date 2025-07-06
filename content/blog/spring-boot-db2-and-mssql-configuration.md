---
id: 421
title: Spring Boot DB2 and MSSQL Configuration
date: 2018-08-04T20:51:36+00:00
author: mrbusche
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

By default Spring boot does a lot for you in datasource configuration, but if you're using two separate database types &#8211; DB2, MSSQL, MySQL, Oracle, etc. It doesn't know how to infer which database type each is, so if you are configuring multiple different database types in Spring you need to specify the jpa.database type. In a yaml configuration your datasources should be defines like so.

```yaml
spring:
  datasource:
    url: jdbc:sqlserver://${server}:${port};databaseName=${databaseName}
    username: ${username}
    password: ${password}
  jpa:
    database: sql_server
db2:
  datasource:
    jdbcurl: jdbc:db2://${server}:${port}/${databaseName}
    username: ${username}
    password: ${password}
  jpa:
    database: db2
```
