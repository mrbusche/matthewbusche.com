---
id: 29
title: Checking an HTML page for duplicate IDs using jQuery
redirect_from:
  - /blog2/2013/05/10/checking-html-page-for-duplicate-ids-using-jquery/
date: 2013-05-10T02:50:15+00:00
author: mrbusche
layout: post
permalink: /2013/05/10/checking-html-page-for-duplicate-ids-using-jquery/
categories:
  - jQuery
---

At work our testers make use of the ID elements on HTML tags quite frequently and when they&#8217;re not unique, it usually causes them issues with testing. To avoid the manual parsing of trying to find duplicate IDs in the page source I looked for (and <a href="http://stackoverflow.com/questions/482763/jquery-to-check-for-duplicate-ids-in-a-dom/4967254#4967254" target="_blank">found</a>) a JavaScript function that loops through each ID found on the page and outputs any duplicates into your console.

This code does require that jQuery is defined on the page you are testing.

    javascript:(function () {
    var ids = {};
    var found = false;
    $(&#039;[id]&#039;).each(function() {
    if (this.id &amp;&amp; ids[this.id]) {
    found = true;
    console.warn(&#039;Duplicate ID #&#039;+this.id);
    }
    ids[this.id] = 1;
    });
    if (!found) console.log(&#039;No duplicate IDs found&#039;);
    })();

You can copy and paste the entire JavaScript function into a bookmark for quick access.

    javascript:(function () { var ids = {}; var found = false; $(&#039;[id]&#039;).each(function() { if (this.id &amp;&amp; ids[this.id]) { found = true; console.warn(&#039;Duplicate ID #&#039;+this.id); } ids[this.id] = 1; }); if (!found) console.log(&#039;No duplicate IDs found&#039;); })();
