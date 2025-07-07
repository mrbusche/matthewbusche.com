---
id: 123
title: Cross browser compatible numbers only textbox
date: 2015-07-06T01:28:29+00:00
author: mrbusche
permalink: /2015/07/06/cross-browser-compatible-numbers-only-textbox/
tags:
  - chrome
  - firefox
  - internet explorer
  - regex
---

While working on a browser compatibility project recently I ran into an issue where using an onkeypress attribute on an input field was firing when using the left and right arrows keys and the delete button. This functionality differs from how IE and Chrome work, so the old code that used to be IE only compatible wouldn't let a user do anything except type numbers (Good!) and use the backspace (Bad!). The users needed to be able to use arrow keys and the delete button in Firefox.

Since we're only supporting the latest browsers, IE 11, Chrome, Safari and Firefox, We thought using an input with type=&#8221;number&#8221; was a good solution, but it adds awful looking up/down arrow buttons in the field and it actually doesn't do anything to prevent letters from being entered, so that was obviously out.

We tried countless regEx patterns but finally settled on the following which lets you use all arrow keys and the delete key, but still only allows you to enter numbers into the text field. Big thanks to [Scott Busche](https://twitter.com/busches) for coming up with the correct regEx

    $('.numbersOnly').keyup(function() {
      var pattern = new RegExp(/\D/);
      var validString = $(this).val().replace(pattern, '');
      if ($(this).val() !== validString) {
        $(this).val(validString);
      }
    });

Rather than calling a function on key press however we decided to add a specific class to these fields and handle the result with a jQuery selector. The downside to this function is that you are actually allowed to type letters and special characters and they will show up for a millisecond, but they will be removed from the input box.

If anyone has anything that works better and is compatible on all the latest browsers I'd love to hear your solution.
