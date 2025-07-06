---
id: 75
title: Adding the stack trace to a Java Server Page error page
date: 2015-03-28T03:46:16+00:00
author: mrbusche
permalink: /2015/03/28/adding-the-stack-trace-to-a-java-server-page-error-page/
categories:
  - java
---

I've recently been switched to a Java project and one of the most frustrating parts of the application (other than barely knowing Java) is the error page would only show a &#8220;An error as occurred&#8221; message and not the actual stack trace. In production this is a perfectly valid scenario, but when developing having to go back to RAD and scroll through the console to find the error message was wasting a lot of time, so after a decent amount of googling I found a way to [dump the stack trace](https://www.coderanch.com/t/292791/JSP/java/Printing-Stacktrace-error-jsp) to the page.

The code ended up looking like this. In the message board post they used exception instead of error, but hopefully you get the point.

```java
<jsp:useBean id="error" scope="request" class="java.lang.Throwable" />
<%
  Object billingError = request.getSession().getAttribute(RequestParamConstants.UNKNOWN_BILLING_ERROR);
  error = (Throwable)billingError;
%>
<%@page isErrorPage="true" import="java.io.*"%>
<pre>
  <%
    error.printStackTrace(new PrintWriter(out));
  %>
</pre>
```

A while after implementing this I ran into an error where the first line was about 400 characters long, so I had to scroll way over to the right. This is because by default the [pre](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre) tag does not wrap, so I added this simple css fix which [allows the pre tag to wrap](https://www.impressivewebs.com/css-white-space/)

```css
pre {
	white-space: pre-wrap;
}
```
