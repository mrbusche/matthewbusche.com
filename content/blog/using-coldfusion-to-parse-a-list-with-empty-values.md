---
id: 16
title: Using ColdFusion to parse a list with empty values
date: 2012-12-04T02:13:53+00:00
author: mrbusche
permalink: /2012/12/04/using-coldfusion-to-parse-a-list-with-empty-values/
categories:
  - coldfusion
---

I was parsing through a csv file today and having issues with empty values. The data I'm receiving is in a format the 3rd party cannot update, so my data looked something like this

    1,,abc,32,,gef

Dumping the list provides the expected list, but looping through the list it skips over values

    <cfoutput>
      <cfloop list="#list1#" index="i">
        #i#<br>
      </cfloop>
    </cfoutput>

produces

    1
    abc
    32
    gef

After googling this for a bit I gave up and asked my [brother](https://twitter.com/busches). He told me to use the &#8216;includeemptyfields' attribute in [listtoarray()](https://help.adobe.com/en_US/ColdFusion/9.0/CFMLRef/WSc3ff6d0ea77859461172e0811cbec22c24-7f0f.html). I knew I could turn a list into an array, but I wasn't aware of the third attribute until today, the default is obviously false, so blank values were never included.

The code below produces the desired output. Notice I am now looping through an array instead of a list.

    <cfset newlist = listToArray(list1,',',true) />
    <cfoutput>
      <cfloop array="#newlist#" index="i">
        #i#<br>
      </cfloop>
    </cfoutput>

    1

    abc
    32

    gef
