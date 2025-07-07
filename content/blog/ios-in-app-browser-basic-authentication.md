---
title: iOS in app browser basic authentication
date: 2020-11-06 21:01:30
permalink: /2020/11/06/ios-in-app-browser-basic-authentication/
tags:
  - ios
  - basicauth
---

If you're having issues not getting a basic auth prompt when using the iOS in app browser you can pass the username and password in the url. This obviously isn't a solution if this is a production issue, but works great for test environments.

`https://username:password@mywebsite.com`
