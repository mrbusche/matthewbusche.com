---
id: 243
title: Using hibernate default schema as a variable
date: 2016-09-05T01:53:44+00:00
author: mrbusche
permalink: /2016/09/05/using-hibernate-default-schema-as-a-variable/
categories:
  - java
tags:
  - hibernate
  - java
  - native sql query
---

Given you have set up a default_schema in your hibernate configuration

    <hibernate-configuration>
       <session-factory>
          <property name="hibernate.default_schema">mySchema</property>
       </session-factory>
    </hibernate-configuration>

Rather than writing a native SQL query like `SELECT x FROM mySchema.tableName` you can write your query as `SELECT x FROM {h-schema}tableName` rather than trying to do a find/replace when your schema name inevitably changes. Note that the . after the schema name is not only not required it will not work if it is added.
