---
id: 66
title: Enabling multiple cursors based on a selection in Sublime Text
redirect_from:
  - /blog2/2015/01/07/enabling-multiple-cursors-based-on-a-selection-in-sublime-text/
date: 2015-01-07T03:41:59+00:00
author: mrbusche
permalink: /2015/01/07/enabling-multiple-cursors-based-on-a-selection-in-sublime-text/
categories:
  - sublime text
---

I was writing a bunch of unit tests for a roman numeral translator function that I'm working on and I was copy/pasting the number and roman numeral from a few websites to validate my function was correction. My plan is to write a test for the first 5000 roman numerals, but using ctrl+d to make 5000 selections and format the selection correctly was going to take quite a while and I knew there had to be a better way.

I googled around for a while and eventually found this [Stack Overflow](https://stackoverflow.com/a/22099974/1065868) answer. You can enable multiple cursors by making a selection and then pressing ctrl+shift+l (l as in Linux). The cursors will be automatically placed at the end of the line, but you can use ctrl+shift+left arrow key (windows command) to move word by word through your selection.

This option is also available from the Sublime menu by going to Selection > Split into Lines, where it will also tell you the shortcut if you're not using Windows.

Keep in mind, once you're past a couple hundred selections Sublime can be very slow even on a fast computer, so be patient if you're enabling hundreds of cursors.
