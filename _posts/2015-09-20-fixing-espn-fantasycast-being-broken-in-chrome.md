---
id: 169
title: Fixing ESPN FantasyCast being broken in Chrome
redirect_from:
  - /blog2/2015/09/20/fixing-espn-fantasycast-being-broken-in-chrome/
date: 2015-09-20T19:59:19+00:00
author: mrbusche
permalink: /2015/09/20/fixing-espn-fantasycast-being-broken-in-chrome/
categories:
  - Uncategorized
---

This is the 2nd year in a row that ESPN has had a bug in their Fantasy Cast website so it does not render properly in Chrome. If your page looks like this, it's broken. The good news is it's easy to fix with a simple bookmarklet.

 <img src="/images/2015/09/fantasy.png" alt="fantasy" />

Simply create a bookmark with this as the url

    javascript:(function(){$('#real .progame-list').css("width", "101%");})()

and click on it to fix the page. Once clicked the page will look like this, which is much more user friendly.

 <img src="/images/2015/09/ESPNFantasyCastChromeFixed.png" alt="ESPNFantasyCastChromeFixed" />
