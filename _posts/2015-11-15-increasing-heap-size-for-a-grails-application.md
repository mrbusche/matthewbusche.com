---
id: 175
title: Increasing heap size for a Grails application
redirect_from:
  - /blog2/2015/11/15/increasing-heap-size-for-a-grails-application/
date: 2015-11-15T15:46:53+00:00
author: mrbusche
permalink: /2015/11/15/increasing-heap-size-for-a-grails-application/
categories:
  - grails
tags:
  - grails
  - heap size
---

I had been running into a lot of issues with Grails running out of heap space on my computer and finally found a solution. In the Grails command line documentation is mentions you can set a maximum heap space when you run grails through the command line. I would keep forgetting to set this and have to restart the app.

    export GRAILS_OPTS="-XX:PermSize=128m -XX:MaxPermSize=512m -Xms256m -Xmx512m"
    grails run-app

I knew that had to be an easier way, so I created an Environment Variable called GRAILS_OPTS and set the value to

    -XX:PermSize=128m -XX:MaxPermSize=512m -Xms256m -Xmx512m -server

Now these settings are used anytime I run grails.
