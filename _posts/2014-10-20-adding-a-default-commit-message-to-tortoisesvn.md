---
id: 53
title: Adding a default commit message to TortoiseSVN
redirect_from:
  - /blog2/2014/10/20/adding-a-default-commit-message-to-tortoisesvn/
date: 2014-10-20T03:34:47+00:00
author: mrbusche
permalink: /2014/10/20/adding-a-default-commit-message-to-tortoisesvn/
categories:
  - version control
---

I always seem to struggle finding how to do this since I do it so infrequently, so I'm posting this here to save me a few minutes next time I need to do this. It's really a very simple process and provides a nice reminder of what should be included in the commit message (if you have any sort of guidelines around it).

Find the folder you want to add the default message to and right click it. Go to TortoiseSVN > Properties

 <img src="/images/2015/05/tortoisesvnproperties.png" alt="tortoisesvnproperties" />

From there select New > Other and then enter &#8220;tsvn:logtemplate&#8221; (without the quotes) as the Property Name and your default message as the Property value.

 <img src="/images/2015/05/log-description.png" alt="log description" />

I tend not to apply the property recursively as 99.8% of my commits are based off of the main folder, but feel free to check that value if you want it to show up even if you commit a single file or from a single folder within your parent folder.
