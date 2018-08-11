---
id: 62
title: Run groovy scripts in sublime text
date: 2014-12-21T03:39:45+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=62
permalink: /2014/12/21/run-groovy-scripts-in-sublime-text/
categories:
  - groovy
---
Wondering how to run Groovy files in Sublime Text? It&#8217;s really quite simple &#8211; to create a new build system in Sublime Text go to Tools > Build System > New Build System and copy/paste the [code below](https://gist.github.com/kdabir/2203530)

    {
    &nbsp;&nbsp;"cmd": ["groovy","$file"],
    &nbsp;&nbsp;"selector": "source.groovy",
    &nbsp;&nbsp;"windows":
    &nbsp;&nbsp;{
    &nbsp;&nbsp;&nbsp;&nbsp;"shell": "cmd.exe"
    &nbsp;&nbsp;}
    }
    

Once the build system is saved you should be able to type Ctrl + B to run the code and output to the Sublime console. If nothing happens you may need to go to Tools > Build System and select groovy.

This is extremely handy if you&#8217;re creating tests in Grails and want to test things without creating a full test case beforehand, writing/running tests in Grails can be excrutiating and testing within your file can help you spot mistakes much quicker than running test-app and waiting for everyting to compile and output your results.