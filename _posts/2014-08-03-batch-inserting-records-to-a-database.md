---
id: 48
title: Batch inserting records to a database
redirect_from:
  - /blog2/2014/08/03/batch-inserting-records-to-a-database/
date: 2014-08-03T03:32:43+00:00
author: mrbusche
layout: post
permalink: /2014/08/03/batch-inserting-records-to-a-database/
categories:
  - ColdFusion
---

I was writing some code for a client that processed a csv file and inserted each row into a database, when there were a couple hundred rows the processing time was very quick, but when there are 8000 rows this can take quite a while even on a very fast database, so I wrote up some code to batch insert the records (which I&#8217;ve done too many times).

I was using MSSQL, so the max parameters I could send at one time was [2100](http://social.msdn.microsoft.com/Forums/sqlserver/en-US/f2ec73eb-f1e0-4048-95d0-1b1ff6c6fdf3/maximum-parameters-in-where-clause) (210 rows x 10 columns), but your mileage may vary. I&#8217;d set rowsPerInsert as high as possible and decrease as necessary. You should be able to easily modify the pseudo code below.

    <cfscript>
    &nbsp;&nbsp;totalrows = 5000; // this would come from a structCount or something similar
    &nbsp;&nbsp;rowsPerInsert = 210;
    &nbsp;&nbsp;//this creates a struct with alternating values of true/false for test purposes
    &nbsp;&nbsp;stRows = {};
    &nbsp;&nbsp;for (i=1; i<=totalRows; i++) {
    &nbsp;&nbsp;&nbsp;&nbsp;stRows[i] = i MOD 2 ? true : false;
    &nbsp;&nbsp;}
    </cfscript>
    <cfoutput>
    <cfloop from="0" to="#totalRows - 1#" step="#rowsPerInsert#" index="totalRow">
    &nbsp;&nbsp;<br><br>INSERT #totalRow#<br>
    &nbsp;&nbsp;<cfloop from="1" to="#rowsPerInsert#" index="indRow">
    &nbsp;&nbsp;&nbsp;&nbsp;<cfset rowNumber = totalRow + indRow>
    &nbsp;&nbsp;&nbsp;&nbsp;<cfif rowNumber LTE totalRows>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#rowNumber# #stRows[rowNumber]# <!--- SELECT goes here --->
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<cfif indRow NEQ rowsPerInsert AND rowNumber NEQ totalRows> UNION ALL</cfif>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;</cfif>
    &nbsp;&nbsp;</cfloop>
    </cfloop>
    </cfoutput>

This is mostly for me to steal from myself once I need this again, but hopefully you find it useful as well.
