---
id: 110
title: Hard refreshing in Google Chrome
redirect_from:
  - /blog2/2015/05/27/hard-refreshing-in-google-chrome/
date: 2015-05-27T02:30:33+00:00
author: mrbusche
permalink: /2015/05/27/hard-refreshing-in-google-chrome/
categories:
  - chrome
  - dev tools
tags:
  - chrome
  - clear cache
  - hard refresh
---

All of us are probably familiar with ctrl + F5 to hard refresh a page but I ran into a cool feature in Chrome today that will save you a second or two if your hand is already on the mouse. If you have the console open and long press on the refresh button you're given three options

1. Normal Reload
2. Hard Reload
3. Empty Cache and Hard Reload

You can already disable cache while the console is open but this option will empty the entire cache and re-download everything on the current page. The difference is if the current website has content loaded through a CDN this will force a re-download of that content.

 <img src="/images/2015/05/chromerefresh.png" alt="chromerefresh" />
