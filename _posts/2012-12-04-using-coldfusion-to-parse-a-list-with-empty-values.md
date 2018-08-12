---
id: 16
title: Using ColdFusion to parse a list with empty values
redirect_from:
  - /blog2/2012/12/04/using-coldfusion-to-parse-a-list-with-empty-values/
date: 2012-12-04T02:13:53+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=16
permalink: /2012/12/04/using-coldfusion-to-parse-a-list-with-empty-values/
categories:
  - ColdFusion
---
I was parsing through a csv file today and having issues with empty values. The data I&#8217;m receiving is in a format the 3rd party cannot update, so my data looked something like this

    1,,abc,32,,gef


Dumping the list provides the expected list, but looping through the list it skips over values

    <cfoutput>
    &nbsp;&nbsp;<cfloop list="#list1#" index="i">
    &nbsp;&nbsp;&nbsp;&nbsp;#i#<br>
    &nbsp;&nbsp;</cfloop>
    </cfoutput>




produces

    1
    abc
    32
    gef


After googling this for a bit I gave up and asked my [brother](http://twitter.com/busches). He told me to use the &#8216;includeemptyfields&#8217; attribute in [listtoarray()](http://help.adobe.com/en_US/ColdFusion/9.0/CFMLRef/WSc3ff6d0ea77859461172e0811cbec22c24-7f0f.html). I knew I could turn a list into an array, but I wasn&#8217;t aware of the third attribute until today, the default is obviously false, so blank values were never included.

The code below produces the desired output. Notice I am now looping through an array instead of a list.

    <cfset newlist = listToArray(list1,&#039;,&#039;,true) />
    <cfoutput>
    &nbsp;&nbsp;<cfloop array="#newlist#" index="i">
    &nbsp;&nbsp;&nbsp;&nbsp;#i#<br>
    &nbsp;&nbsp;</cfloop>
    </cfoutput>

    1

    abc
    32

    gef