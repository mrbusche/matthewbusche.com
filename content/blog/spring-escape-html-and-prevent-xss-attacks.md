---
id: 261
title: Spring Escape HTML and prevent XSS attacks
date: 2016-12-27T21:30:43+00:00
author: mrbusche
permalink: /2016/12/27/spring-escape-html-and-prevent-xss-attacks/
categories:
  - java
tags:
  - html escape
  - spring
  - xss not working
---

TL;DR &#8211; If you think the context-param isn't working, make sure you're not outputting the value on the page somewhere not inside a spring form.

I ran into an issue recently where after a security scan was ran we were told when you enter a variable into the URL i.e. `?endDate=someJavaScript` it was being executed on the page. Assumed it was an easy enough fix, so googled around and found, this solution for [Spring Framework](https://stackoverflow.com/questions/2147958/how-do-i-prevent-people-from-doing-xss-in-spring-mvc)

    <context-param>
      <param-name>defaultHtmlEscape</param-name>
      <param-value>true</param-value>
    </context-param>

I put that into the web.xml, restarted and it didn't work, so I tried adding the page level and form level tags, but those didn't work either. After messing around for a few hours I realized there was another place on the page where we were outputting the variable endDate, and it wasn't inside a spring form.

What defaultHtmlEscape does is add that parameter to every _spring tag_ in your application, pretty obvious in hindsight, but what I needed to do was make sure everywhere those values were displayed that they were displayed using a jstl c:out tag, i.e. `<c:out value="${endDate}"></c:out>` which also defaults to not allowing HTML to be rendered.
