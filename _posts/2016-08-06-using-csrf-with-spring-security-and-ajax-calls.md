---
id: 239
title: Using CSRF with Spring Security and AJAX calls
date: 2016-08-06T01:10:28+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=239
permalink: /2016/08/06/using-csrf-with-spring-security-and-ajax-calls/
categories:
  - java
  - jQuery
tags:
  - ajax
  - beforesend
  - csrf
---
I&#8217;m fairly new to Spring and especially Spring Security, so I had quite the time figuring out why ajax calls were failing after enabling CSRF (to allow ClearTrust)

First we allowed CSRF which is a strange syntax in my opinion

`<security:csrf disabled="false" />`

After we did that we were getting &#8220;405: Method Not Allowed&#8221; responses on all of our ajax requests. After some googling we discovered this is a security precaution to prevent cross site attacks, which makes a lot of sense. The biggest problem was we had probably 25 ajax calls and didn&#8217;t want to spend all day updating them individually, so we ended up adding in the csrf token and header name into the head meta tags in our application. This meant they were available on every page automatically and since they stay valid as long as the users&#8217; session this made the most sense.

Added to the header template
  


    <meta name="_csrf" content="${_csrf.token}"/>
    <meta name="_csrf_header" content="${_csrf.headerName}"/>

Added to each JavaScript template (or could be added to a global JS file as well)

    var token = $("meta[name=&#039;_csrf&#039;]").attr("content");
    var header = $("meta[name=&#039;_csrf_header&#039;]").attr("content");

Added to each ajax call

    , beforeSend: function( xhr ) {
    &nbsp;&nbsp;xhr.setRequestHeader(header, token);
    }