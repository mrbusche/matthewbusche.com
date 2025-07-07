---
id: 60
title: 'Grails - Reloading a service without stopping your app'
date: 2014-12-20T03:38:18+00:00
author: mrbusche
permalink: /2014/12/20/grails-reloading-a-service-without-stopping-your-app/
categories:
  - grails
---

When a grails application is started most Grails artificats are reloaded as they are changed &#8211; controllers, filters, tag libraries, but the opposite is true if you strongly type your services like below.

```java
FakeService fakeService
```

However if you use untyped injected like

```java
def fakeService
```

then the service will be reloaded as changes are made. This may have been obvious to most people, but I was originally going through the hassle of either restarting my app after each change (huge time waster) or creating a fakeServiceHelper where I made all my changes and introducing a needless extra layer to my application to avoid restarting my app after each change.
