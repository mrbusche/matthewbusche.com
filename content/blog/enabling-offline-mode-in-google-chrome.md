---
id: 117
title: Enabling offline mode in Google Chrome
date: 2015-06-21T19:25:21+00:00
author: mrbusche
permalink: /2015/06/21/enabling-offline-mode-in-google-chrome/
categories:
  - chrome
tags:
  - chrome
  - offline
---

In April and May I was traveling every other week for work and to keep myself occupied I would open a bunch of articles in chrome on my phone to read them on the plane. Much to my chagrin the first time I did this about half the articles were automatically reloaded by chrome and I wasn't able to read them because I didn't have an internet connection. I started trying to fix this by looking for a way to disable the setting that would reload tabs, but was unsuccessful. What I did find was an option to reload an article from the cache if you were offline.

Simply type `chrome://flags` into your address bar and find the Enable Show Saved Copy Button setting.

> **Enable Show Saved Copy Button** Mac, Windows, Linux, Chrome OS, Android setting.

> When a page fails to load, if a stale copy of the page exists in the browser cache, a button will be presented to allow the user to load that stale copy. The primary enabling choice puts the button in the most salient position on the error page; the secondary enabling choice puts it secondary to the reload button. #show-saved-copy

You can enable this setting as a primary or secondary button. Primary will enable this setting as the most noticeable option when you're offline and secondary will make it the secondary option to reloading the page.

Before I found this setting I stumbled upon [Pocket](https://getpocket.com/) which is a much better option for saving articles overall, but won't help you recall a webpage you visited earlier. The other downside to pocket is it's much easier to forget about than an open tab and you'll probably let articles sit in their forever before you read them.
