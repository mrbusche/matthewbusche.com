---
id: 80
title: Checking an HTML page for duplicate IDs using JavaScript
date: 2015-04-13T03:48:47+00:00
author: mrbusche
permalink: /2015/04/13/checking-an-html-page-for-duplicate-ids-using-javascript/
categories:
  - javascript
---

A couple years back I wrote a post about [Checking an HTML page for duplicate IDs using jQuery](https://mrbusche.com/2013/05/10/checking-html-page-for-duplicate-ids-using-jquery/). A pretty useful tool when you need to ensure IDs on a page are unique. The downside to that code was that it required jQuery and the app I'm currently working with does not use jQuery, so I modifed the existing code to write a pure JavaScript solution that does the same thing.

    var allElements = document.getElementsByTagName("*");
    var allIds = {};
    var found = false;
    for (var i = 0, n = allElements.length; i < n; ++i) {
      var id = allElements[i].id;
      if (id) {
        if (allIds[id] === undefined) {
          allIds[id] = 1;
        } else {
          found = true;
          console.warn('Duplicate ID #' + id);
        }
      }
    }
    if (!found) {
      console.log('No duplicate IDs found');
    }

All you need to do is create a new bookmark with the following as the URL

    javascript: (function() {var allElements = document.getElementsByTagName('*');var allIds = {};var found = false;for (var i = 0, n = allElements.length; i < n; ++i) {var id = allElements[i].id;if (id) {if (allIds[id] === undefined) {allIds[id] = 1;} else {found = true;console.warn('Duplicate ID #' + id);}}}if (!found) {console.log('No duplicate IDs found');}})();

Or you can simply drag the bookmarklet below onto your bookmark toolbar

[Duplicate ID Checker](javascript: (function() {var allElements = document.getElementsByTagName('\*');var allIds = {};var found = false;for (var i = 0, n = allElements.length; i < n; ++i) {var id = allElements[i].id;if (id) {if (allIds[id] === undefined) {allIds[id] = 1;} else {found = true;console.warn('Duplicate ID #' + id);}}}if (!found) {console.log('No duplicate IDs found');}})();)

Update: [Ryan Guill](https://twitter.com/ryanguill) let me know he wrote something similar and he's saved it as a [Gist](https://gist.github.com/ryanguill/36af48201e6d68dbbbe3/). It's interesting seeing the different approaches to accomplish the same thing.
