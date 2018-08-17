---
id: 394
title: Adding java properties to Websphere Liberty
redirect_from:
  - /blog2/2018/05/15/adding-java-properties-to-websphere-liberty/
date: 2018-05-15T01:59:35+00:00
author: mrbusche
layout: post
permalink: /2018/05/15/adding-java-properties-to-websphere-liberty/
categories:
  - java
  - websphere
---

My latest project was moving a bunch of applications from running on WebSphere using Java 6 to running on Liberty running Java 8. For the most part this was pretty straightforward, but one major issue we ran into was a bean defined like so

<pre>&lt;bean id="environment" class="org.springframework.jndi.JndiObjectFactoryBean"&gt;
  &lt;property name="jndiName" value="java:comp/env/string/nw/environment"/&gt;
&lt;/bean&gt;
</pre>

What the heck does java:comp/env/string mean?

Turns out it&#8217;s pretty obvious once you know. It&#8217;s a JNDI Entry in Liberty (Namespace binding in WebSphere). You need to enter a new JNDI entry with a name of string/nw/environment with a value of dev, it, pt, prod, whatever your environment name is. This is generally something you&#8217;d add to a properties file, but considering this app is crazy old maybe that wasn&#8217;t an option.
