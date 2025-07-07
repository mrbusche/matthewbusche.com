---
id: 236
title: Detecting duplicate JavaScript includes on a page
date: 2016-08-05T02:37:09+00:00
author: mrbusche
permalink: /2016/08/05/detecting-duplicate-javascript-includes-on-a-page/
categories:
  - javascript
tags:
  - duplicate
  - javascript
---

I started working on a new app recently with some people mostly new to front end development and noticed that on many pages we were including the same JavaScript file multiple times, either on the same page or within an included page, so I wrote up some JavaScript (using jQuery) to detect those on the page.

The script itself is pretty straightforward.

    function findDupes() {
      var allScripts = [];
      var dupe = false;
      $.each(document.getElementsByTagName("script"), function(index, value) {
        if ($.inArray(value.src, allScripts) !== -1 && value.src !== '') {
          console.log('already loaded :: ' + value.src);
          dupe=true;
        }
        allScripts.push(value.src);
      });
      if(!dupe){
        console.log('no dupes');
      }
    });

I turned this into a bookmarklet as well if you want to add it as a bookmark to easily run on the page

    javascript: (function() {var a = []; var b = false;$.each(document.getElementsByTagName("script"), function(index, value) {if ($.inArray(value.src, a) !== -1 && value.src !== '') {console.log('already loaded :: ' + value.src);b=true;}a.push(value.src);});if(!b){console.log('no dupes');}})();
