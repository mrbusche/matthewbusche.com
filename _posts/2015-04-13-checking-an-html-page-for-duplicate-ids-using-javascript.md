---
id: 80
title: Checking an HTML page for duplicate IDs using JavaScript
redirect_from:
  - /blog2/2015/04/13/checking-an-html-page-for-duplicate-ids-using-javascript/
date: 2015-04-13T03:48:47+00:00
author: mrbusche
layout: post
permalink: /2015/04/13/checking-an-html-page-for-duplicate-ids-using-javascript/
categories:
  - JavaScript
---
A couple years back I wrote a post about [Checking an HTML page for duplicate IDs using jQuery](http://matthewbusche.com/blog/index.cfm/2013/5/10/Checking-HTML-page-for-duplicate-IDs-using-jQuery). A pretty useful tool when you need to ensure IDs on a page are unique. The downside to that code was that it required jQuery and the app I&#8217;m currently working with does not use jQuery, so I modifed the existing code to write a pure JavaScript solution that does the same thing.

    var allElements = document.getElementsByTagName("*");
    var allIds = {};
    var found = false;
    for (var i = 0, n = allElements.length; i < n; ++i) {
    &nbsp;&nbsp;var id = allElements[i].id;
    &nbsp;&nbsp;if (id) {
    &nbsp;&nbsp;&nbsp;&nbsp;if (allIds[id] === undefined) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allIds[id] = 1;
    &nbsp;&nbsp;&nbsp;&nbsp;} else {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;found = true;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.warn(&#039;Duplicate ID #&#039; + id);
    &nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;}
    }
    if (!found) {
    &nbsp;&nbsp;console.log(&#039;No duplicate IDs found&#039;);
    }


All you need to do is create a new bookmark with the following as the URL

    javascript: (function() {var allElements = document.getElementsByTagName(&#039;*&#039;);var allIds = {};var found = false;for (var i = 0, n = allElements.length; i < n; ++i) {var id = allElements[i].id;if (id) {if (allIds[id] === undefined) {allIds[id] = 1;} else {found = true;console.warn(&#039;Duplicate ID #&#039; + id);}}}if (!found) {console.log(&#039;No duplicate IDs found&#039;);}})();


Or you can simply drag the bookmarklet below onto your bookmark toolbar

[Duplicate ID Checker](javascript: (function() {var allElements = document.getElementsByTagName('*');var allIds = {};var found = false;for (var i = 0, n = allElements.length; i < n; ++i) {var id = allElements[i].id;if (id) {if (allIds[id] === undefined) {allIds[id] = 1;} else {found = true;console.warn('Duplicate ID #' + id);}}}if (!found) {console.log('No duplicate IDs found');}})();)

Update: [Ryan Guill](https://twitter.com/ryanguill) let me know he wrote something similar and he&#8217;s saved it as a [Gist](https://gist.github.com/ryanguill/36af48201e6d68dbbbe3/). It&#8217;s interesting seeing the different approaches to accomplish the same thing.