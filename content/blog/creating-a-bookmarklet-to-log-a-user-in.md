---
id: 161
title: Creating a bookmarklet to log a user in
date: 2015-07-15T02:33:14+00:00
author: mrbusche
permalink: /2015/07/15/creating-a-bookmarklet-to-log-a-user-in/
categories:
  - Uncategorized
---

As someone who is continually logging into an internal website while writing code I knew there had to be a better way than entering my username and password 100 times a day. To complicate this I'm also alternating between users with different admin rights, access, etc and remembering multiple usernames and passwords can be tedious. The solution? Create a bookmarklet that fills out the elements on the screen and clicks the submit button. I wouldn't recommend you use this for anything other than an internal only application, but if you want to store your password in plain text in your bookmarks that are probably synced between computers go right ahead :).

You'll need to inspect the DOM and get the ID values of the username, password and form to make this work. What you do is set the dcoument into a variable get your element by the ID and set the value to your username. The same goes for the password. If you're having trouble getting this to work make sure your input fields have ID and you have the case typed in correctly.

    javascript:(function(){
      var d=document;
      e=d.getElementById("userId");
      e.value="matt.busche";
      u=d.getElementById("password");
      u.value="hunter2";
      f=d.getElementById("loginForm");
      f.submit();
    })();

Simple copy and paste the above code into the url field of a bookmark and you'll be saving multiple seconds daily.
