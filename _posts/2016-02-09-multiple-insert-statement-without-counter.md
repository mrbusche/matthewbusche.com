---
id: 193
title: Multiple insert statement without counter
date: 2016-02-09T02:41:10+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=193
permalink: /2016/02/09/multiple-insert-statement-without-counter/
categories:
  - ColdFusion
  - SQL Server
tags:
  - ColdFusion
  - multiple insert
  - SQL Server
---
I often have a need to write an INSERT statement that adds multiple rows to a database. Obviously you can run any Â number of inserts separately, but that&#8217;s innefficient, so I loop over a list with a counter to know when to end. Recently I learned that the counter is unnecessary and you can create a fake SELECT statement to avoid needing a counter

    <cfquery>
    INSERT INTO Attendees (Schedule_ID, Attendee_ID, Meeting_ID, User_ID)
    <cfloop list="#variables[eventlocation]#" index="i">
    &nbsp;&nbsp;SELECT #Schedule_ID#, #i#, #Meeting_ID#, 1
    &nbsp;&nbsp;UNION ALL
    </cfloop>
    <!--- returns no rows --->
    SELECT 0, 0, 0, 0
    WHERE 1 = 0
    </cfquery>

For the sake of brevity I&#8217;ve avoided omitted the cfqueryparam&#8217;s that should always be used in queries.