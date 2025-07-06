---
id: 48
title: Batch inserting records to a database
date: 2014-08-03T03:32:43+00:00
author: mrbusche
permalink: /2014/08/03/batch-inserting-records-to-a-database/
categories:
  - coldfusion
---

I was writing some code for a client that processed a csv file and inserted each row into a database, when there were a couple hundred rows the processing time was very quick, but when there are 8000 rows this can take quite a while even on a very fast database, so I wrote up some code to batch insert the records (which I've done too many times).

I was using MSSQL, so the max parameters I could send at one time was [2100](https://social.msdn.microsoft.com/Forums/sqlserver/en-US/f2ec73eb-f1e0-4048-95d0-1b1ff6c6fdf3/maximum-parameters-in-where-clause) (210 rows x 10 columns), but your mileage may vary. I'd set rowsPerInsert as high as possible and decrease as necessary. You should be able to easily modify the pseudo code below.

    <cfscript>
      totalrows = 5000; // this would come from a structCount or something similar
      rowsPerInsert = 210;
      //this creates a struct with alternating values of true/false for test purposes
      stRows = {};
      for (i=1; i<=totalRows; i++) {
        stRows[i] = i MOD 2 ? true : false;
      }
    </cfscript>
    <cfoutput>
    <cfloop from="0" to="#totalRows - 1#" step="#rowsPerInsert#" index="totalRow">
      <br><br>INSERT #totalRow#<br>
      <cfloop from="1" to="#rowsPerInsert#" index="indRow">
        <cfset rowNumber = totalRow + indRow>
        <cfif rowNumber LTE totalRows>
          #rowNumber# #stRows[rowNumber]# <!--- SELECT goes here --->
          <cfif indRow NEQ rowsPerInsert AND rowNumber NEQ totalRows> UNION ALL</cfif>
          <br>
        </cfif>
      </cfloop>
    </cfloop>
    </cfoutput>

This is mostly for me to steal from myself once I need this again, but hopefully you find it useful as well.
