---
id: 291
title: Finding the version of a jar file
redirect_from:
  - /blog2/2017/06/02/finding-the-version-of-a-jar-file/
date: 2017-06-02T02:26:36+00:00
author: mrbusche
permalink: /2017/06/02/finding-the-version-of-a-jar-file/
categories:
  - java
---

I needed to find the version of a jar file I was using to help out our middleware team at work and had never needed to do so before, so I went to googling. I figured it would be pretty straightforward and it is, once you find the correct commands. I initially started out unzipping the jar file and found the version that way through the manifest file by looking at the Implementation-Version. It wasn't too much work, but I knew there had to be a better way and I stumbled upon this [stackoverflow answer](https://stackoverflow.com/a/38313502/1065868)

If you open a terminal window and cd to the directory with your jar file you can do `unzip -p file.jar META-INF/MANIFEST.MF` to view the manifest file without manually unzipping the file.
