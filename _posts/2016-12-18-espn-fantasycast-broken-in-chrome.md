---
id: 258
title: ESPN FantasyCast broken in Chrome
redirect_from:
  - /blog2/2016/12/18/espn-fantasycast-broken-in-chrome/
date: 2016-12-18T17:43:03+00:00
author: mrbusche
layout: post
permalink: /2016/12/18/espn-fantasycast-broken-in-chrome/
categories:
  - Uncategorized
---
Once again ESPN FantasyCast is broken in Chrome. If you&#8217;re using Chrome and are seeing the game score and stats on two separate lines. Hit F12 and copy the following into the Console and press enter

`$(&#039;#real .progame&#039;).css(&#039;width&#039;, &#039;101%&#039;)`

This increases the container for the game by 1% and allows the page to be fully functional again.