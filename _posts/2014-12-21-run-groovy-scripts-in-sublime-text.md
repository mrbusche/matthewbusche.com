---
id: 62
title: Run groovy scripts in sublime text
redirect_from:
  - /blog2/2014/12/21/run-groovy-scripts-in-sublime-text/
date: 2014-12-21T03:39:45+00:00
author: mrbusche
permalink: /2014/12/21/run-groovy-scripts-in-sublime-text/
categories:
  - groovy
---

Wondering how to run Groovy files in Sublime Text? It's really quite simple &#8211; to create a new build system in Sublime Text go to Tools > Build System > New Build System and copy/paste the [code below](https://gist.github.com/kdabir/2203530)

    {
      "cmd": ["groovy","$file"],
      "selector": "source.groovy",
      "windows":
      {
        "shell": "cmd.exe"
      }
    }

Once the build system is saved you should be able to type Ctrl + B to run the code and output to the Sublime console. If nothing happens you may need to go to Tools > Build System and select groovy.

This is extremely handy if you're creating tests in Grails and want to test things without creating a full test case beforehand, writing/running tests in Grails can be excrutiating and testing within your file can help you spot mistakes much quicker than running test-app and waiting for everyting to compile and output your results.
