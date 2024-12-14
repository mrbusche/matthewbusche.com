---
title: 'Updating all sub modules in a git project'
date: 2018-12-19 11:56:57
tags:
  - git
---

This command will find all the submodules in your current git projects and pull down changes from master for each submodule.

`git submodule -q foreach git pull -q origin master`

Once you pull down changes make sure you push the changes back to your project to see the changes.

What is this actually doing?

`git submodule` basically gets all the submodules in your project

`-q` means `quiet` which means it doesn't output the name of the submodule as it loops through them. This parameter is not required.

`foreach` um, it loops through each submodule

`git pull -q origin master` this pulls down the changes from master on the submodule and doesn't output the changes. Again, the `-q` is not required, but will reduce the conole output.
