---
id: 422
title: Spring JPA add default timestamp to column
date: 2018-08-14T21:51:36+00:00
author: mrbusche
permalink: /2018/08/14/spring-jpa-add-default-timestamp-to-column/
categories:
  - java
  - hibernate
tags:
  - spring jpa
---

Spring JPA is awesome, but I ran into some issues adding a default timestamp to the column. The database should be set to have a default value, but that wasn't an option here. I found the annotation pretty quickly, but instead of checking the database to see if it worked I was debugging in IntelliJ and that's where the hiccup occurred. The value isn't set on the object at object creation it's only set once the entity has been saved. The following is what I ended up using

```java
@Column(name = "creationDate")
@CreationTimestamp //this adds the default timestamp on save
private Timestamp createDate;
```
