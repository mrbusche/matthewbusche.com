---
id: 150
title: Showing all hidden elements on a page using jQuery
date: 2015-07-10T23:31:49+00:00
author: mrbusche
permalink: /2015/07/10/showing-all-hidden-elements-on-a-page-using-jquery/
tags:
  - hidden fields
---

I've been working on a large browser compatibilty project which involves also giving the page a facelift to bootstrap. We're mostly modifying XML which creates the markup and there are a few pages with a lot of rules that hide element based on certain scenarios and hitting those scenarios became very tedious when we were already 98% sure the page would work. The divs are hidden on the page and aren't just not generated server side. The elements are hidden both by adding a class of hidden and by using display:none.

I ended up writing a bookmarklet that runs through all the elements in the DOM and removes the style attribute and removes the hidden class from all elements. This isn't being used anywhere other than on a developers machine, so efficiency wasn't the goal here. The goal was to show all hidden elements to make sure they're being styled correctly. They're being styled with classes, so that's why removing the style attribute was an easier option.

Here's the jQuery code

    $(function() {
      $("body *").each(function() {
        $(this).removeAttr("style");
        $(this).removeClass("hidden");
      })
    });

Here's the bookmarklet. You can simply create a new bookmark with this as the URL and click it to show the hidden elements.

    javascript:(function(){$(function(){$("body *").each(function(){$(this).removeAttr("style"),$(this).removeClass("hidden")})})})()
