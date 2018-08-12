---
id: 150
title: Showing all hidden elements on a page using jQuery
redirect_from:
  - /blog2/2015/07/10/showing-all-hidden-elements-on-a-page-using-jquery/
date: 2015-07-10T23:31:49+00:00
author: mrbusche
layout: post
permalink: /2015/07/10/showing-all-hidden-elements-on-a-page-using-jquery/
categories:
  - jQuery
tags:
  - hidden fields
  - jquery
---
I&#8217;ve been working on a large browser compatibilty project which involves also giving the page a facelift to bootstrap. We&#8217;re mostly modifying XML which creates the markup and there are a few pages with a lot of rules that hide element based on certain scenarios and hitting those scenarios became very tedious when we were already 98% sure the page would work. The divs are hidden on the page and aren&#8217;t just not generated server side. The elements are hidden both by adding a class of hidden and by using display:none.

I ended up writing a bookmarklet that runs through all the elements in the DOM and removes the style attribute and removes the hidden class from all elements. This isn&#8217;t being used anywhere other than on a developers machine, so efficiency wasn&#8217;t the goal here. The goal was to show all hidden elements to make sure they&#8217;re being styled correctly. They&#8217;re being styled with classes, so that&#8217;s why removing the style attribute was an easier option.

Here&#8217;s the jQuery code

    $(function() {
    &nbsp;&nbsp;$("body *").each(function() {
    &nbsp;&nbsp;&nbsp;&nbsp;$(this).removeAttr("style");
    &nbsp;&nbsp;&nbsp;&nbsp;$(this).removeClass("hidden");
    &nbsp;&nbsp;})
    });


Here&#8217;s the bookmarklet. You can simply create a new bookmark with this as the URL and click it to show the hidden elements.


    javascript:(function(){$(function(){$("body *").each(function(){$(this).removeAttr("style"),$(this).removeClass("hidden")})})})()