---
title: "User added in Jenkins doesn't have access"
date: 2018-08-15 08:06:57
permalink: /2018/08/16/added-jenkins-user-doesnt-have-access/
tags: jenkins
---

I was helping a team at work recently and we needed to add a few users to Jenkins. We added the users and then asked them to login and make sure they could run jobs. 2 out of 3 people were able to run jobs, but the 3rd person was not. We had added them the same as everyone else, but it wasn't working. I had them logout and back in and that's when I realized the issue - `Jenkins is case sensitive` If you add a user as `mrbusche` but they login as `MRBUSCHE` they're not recognized in Jenkins.

Long story short

# Jenkins is case sensitive
