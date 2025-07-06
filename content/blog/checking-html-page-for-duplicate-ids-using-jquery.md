---
id: 29
title: Checking an HTML page for duplicate IDs using jQuery
date: 2013-05-10T02:50:15+00:00
author: mrbusche
permalink: /2013/05/10/checking-html-page-for-duplicate-ids-using-jquery/
---

At work our testers make use of the ID elements on HTML tags quite frequently and when they're not unique, it usually causes them issues with testing. To avoid the manual parsing of trying to find duplicate IDs in the page source I looked for (and <a href="https://stackoverflow.com/questions/482763/jquery-to-check-for-duplicate-ids-in-a-dom/4967254#4967254" target="_blank">found</a>) a JavaScript function that loops through each ID found on the page and outputs any duplicates into your console.

This code does require that jQuery is defined on the page you are testing.

    javascript:(function () {
      var ids = {};
      var found = false;
      $('[id]').each(function() {
        if (this.id &amp;&amp; ids[this.id]) {
          found = true;
          console.warn('Duplicate ID #'+this.id);
        }
        ids[this.id] = 1;
      });
      if (!found) console.log('No duplicate IDs found');
    })();

You can copy and paste the entire JavaScript function into a bookmark for quick access.

    javascript:(function () { var ids = {}; var found = false; $('[id]').each(function() { if (this.id &amp;&amp; ids[this.id]) { found = true; console.warn('Duplicate ID #'+this.id); } ids[this.id] = 1; }); if (!found) console.log('No duplicate IDs found'); })();
