---
id: 225
title: Hibernate returning BigDecimal instead of Long
redirect_from:
  - /blog2/2016/06/08/hibernate-returning-bigdecimal-instead-of-long/
date: 2016-06-08T14:07:03+00:00
author: mrbusche
permalink: /2016/06/08/hibernate-returning-bigdecimal-instead-of-long/
categories:
  - java
tags:
  - addscalar
  - bigdecimal
  - hibernate
  - java
  - long
---

I was trying to run a query to get a list of IDs from a database table and then compare that list to individual Ids on the page. The logic was pretty straightforward. Get IDs via a query and then check if other IDs are found in that list of IDs. The query itself was working fine (I've reduced the complexity of the query a lot), but my contains statement wasn't finding any matches (even though they were mostly all matches). It turns out that Hibernate was returning a List of BigDecimal rather than a list of Long and my comparison was a Long value. What I needed to do was force the column to return the datatype I wanted.

    addScalar(columnName, dataType)

    public List<Long> retrieveOrgTypeWithoutParent() {
     Session session = getHibernateTemplate().getSessionFactory().openSession();

     List<Long> orgTypeIds = session.createSQLQuery(
      "SELECT typeId FROM org_type_cd").addScalar("typeId", StandardBasicTypes.LONG).list();

     session.close();
     return orgTypeIds;
    };
