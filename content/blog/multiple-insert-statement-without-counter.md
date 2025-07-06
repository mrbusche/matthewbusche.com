---
id: 193
title: Multiple insert statement without counter
date: 2016-02-09T02:41:10+00:00
author: mrbusche
permalink: /2016/02/09/multiple-insert-statement-without-counter/
categories:
  - coldfusion
  - SQL Server
tags:
  - coldfusion
  - multiple insert
  - SQL Server
---

I often have a need to write an INSERT statement that adds multiple rows to a database. Obviously you can run any number of inserts separately, but that's innefficient, so I loop over a list with a counter to know when to end. Recently I learned that the counter is unnecessary and you can create a fake SELECT statement to avoid needing a counter

    <cfquery>
    INSERT INTO Attendees (Schedule_ID, Attendee_ID, Meeting_ID, User_ID)
    <cfloop list="#variables[eventlocation]#" index="i">
      SELECT #Schedule_ID#, #i#, #Meeting_ID#, 1
      UNION ALL
    </cfloop>
    <!--- returns no rows --->
    SELECT 0, 0, 0, 0
    WHERE 1 = 0
    </cfquery>

For the sake of brevity I've avoided omitted the cfqueryparam's that should always be used in queries.
