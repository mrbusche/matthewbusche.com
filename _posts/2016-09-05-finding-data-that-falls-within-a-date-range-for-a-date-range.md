---
id: 250
title: Finding data that falls within a date range for a date range
redirect_from:
  - /blog2/2016/09/05/finding-data-that-falls-within-a-date-range-for-a-date-range/
date: 2016-09-05T14:12:29+00:00
author: mrbusche
permalink: /2016/09/05/finding-data-that-falls-within-a-date-range-for-a-date-range/
categories:
  - SQL Server
tags:
  - date range
  - dates
  - sql
---

The title of this is horribly confusing, but hopefully this is helpful for some people. The problem I was trying to solve is I have a report that shows where travelers are based on certain dates. For example a client requests a report to know where all of their travelers are that are traveling 9/1 &#8211; 9/2. Given that we know the departure and arrival dates of their trip this is pretty straightforward.

Given that their departure date is stored in depDateTime and their return date is stored in arvDateTime and startDate and endDate are timestamps then this will return all users who are traveling during 9/1 &#8211; 9/2

    WHERE ((depDateTime BETWEEN #startDate# AND #endDate#)
        OR (arvDateTime BETWEEN #startDate# AND #endDate#))

This works great for most trips, but what if the person departs on 8/31 and returns on 9/3? The current WHERE statement will not return them as a result. I fiddled with dozens of scenarios until I realized it's pretty simple. For the user to not show with the current logic their trip needs to begin before the startDate and end after the endDate, so it required one additional OR statement

    WHERE ((depDateTime BETWEEN #startDate# AND #endDate#)
        OR (arvDateTime BETWEEN #startDate# AND #endDate#)
        OR (depDateTime < #startDate# AND arvDateTime > #endDate#))
