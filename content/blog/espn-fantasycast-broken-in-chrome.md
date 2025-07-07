---
id: 258
title: ESPN FantasyCast broken in Chrome
date: 2016-12-18T17:43:03+00:00
author: mrbusche
permalink: /2016/12/18/espn-fantasycast-broken-in-chrome/
categories:
  - Uncategorized
---

Once again ESPN FantasyCast is broken in Chrome. If you're using Chrome and are seeing the game score and stats on two separate lines. Hit F12 and copy the following into the Console and press enter

    $('#real .progame').css('width', '101%')

This increases the container for the game by 1% and allows the page to be fully functional again.
