---
id: 236
title: Detecting duplicate JavaScript includes on a page
redirect_from:
  - /blog2/2016/08/05/detecting-duplicate-javascript-includes-on-a-page/
date: 2016-08-05T02:37:09+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=236
permalink: /2016/08/05/detecting-duplicate-javascript-includes-on-a-page/
categories:
  - JavaScript
tags:
  - duplicate
  - javascript
  - jquery
---
I started working on a new app recently with some people mostly new to front end development and noticed that on many pages we were including the same JavaScript file multiple times, either on the same page or within an included page, so I wrote up some JavaScript (using jQuery) to detect those on the page.

The script itself is pretty straightforward.

    function findDupes() {
    &nbsp;&nbsp;var allScripts = [];
    &nbsp;&nbsp;var dupe = false;
    &nbsp;&nbsp;$.each(document.getElementsByTagName("script"), function(index, value) {
    &nbsp;&nbsp;&nbsp;&nbsp;if ($.inArray(value.src, allScripts) !== -1 && value.src !== &#039;&#039;) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;console.log(&#039;already loaded :: &#039; + value.src);
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dupe=true;
    &nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;allScripts.push(value.src);
    &nbsp;&nbsp;});
    &nbsp;&nbsp;if(!dupe){
    &nbsp;&nbsp;&nbsp;&nbsp;console.log(&#039;no dupes&#039;);
    &nbsp;&nbsp;}
    });

I turned this into a bookmarklet as well if you want to add it as a bookmark to easily run on the page

`javascript: (function() {var a = []; var b = false;$.each(document.getElementsByTagName("script"), function(index, value) {if ($.inArray(value.src, a) !== -1 && value.src !== &#039;&#039;) {console.log(&#039;already loaded :: &#039; + value.src);b=true;}a.push(value.src);});if(!b){console.log(&#039;no dupes&#039;);}})();`