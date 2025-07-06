---
id: 43
title: ColdFusion Query of Queries strips whitespace
date: 2014-06-10T03:27:58+00:00
author: mrbusche
permalink: /2014/06/10/coldfusion-query-of-queries-strips-whitespace/
categories:
  - coldfusion
---

I was tasked with tracking down a defect at work this week. We are creating a URL based on the results of a query and somehow a string of &#8221; ABC DEF 12345&#8243; was being turned into &#8220;ABC DEF 12345&#8221; (DB2 FTW!) The webservice we were using was unchanged and was still returning the whitespace, so I knew the issue was something on my end. We have a few pieces of code that strip out duplicate spaces and extra line breaks, so I removed those, but the issue still persisted. After working through about a dozen solutions I called over <a href="https://twitter.com/busches" target="_blank">Scott Busche</a> and we repeated everything I had already gone through, but when we stumbled upon a Query of Queries, Scott suggested that could be the culprit.

The query of queries was used to filter a result set down to the past two years only (the webservice we're using just ignores end date, which is awesome in itself), so we googled and quickly found that QoQ trims leading and trailing whitespace from columns and has been doing this since ColdFusion 6, so I don't think this is considered a bug, just something to be aware of.

How to solve the issue?

We googled and found this <a href="https://stackoverflow.com/questions/5750763/how-do-i-discard-a-row-from-a-coldfusion-query" target="_blank">stack overflow question</a>, but that solution only worked for Railo and then we found a post on <a href="https://stackoverflow.com/questions/5750763/how-do-i-discard-a-row-from-a-coldfusion-query" target="_blank">Ben Nadel's blog</a> (obviously) that pointed out a Java function that would do what we needed, but when removing more than one row in the query you would eventually run into an index out of bounds error the way he had it structured, but that's easy enough to fix.

    <cfloop from="#myQuery.recordCount#" to="1" step="-1" index="currentRow">
      <cfif myQuery.runDate[currentRow] LT left(getStartDateTime(),8)>
        <cfset myQuery.removeRows(currentRow - 1, 1)>
      </cfif>
    </cfloop>

After implementing this fix our query was working correctly, but we still needed to add <a href="https://help.adobe.com/livedocs/coldfusion/8/htmldocs/help.html?content=functions_t-z_10.html" target="_blank">URLEncodedFormat</a> to our URL parameters, so the whitespace wouldn't be stripped (and because it should have been done in the first place).

FWIW Railo 4.2 does NOT strip out whitespace. Test case below

    <cfset q = queryNew("columnA", "varchar", [["   AAA"]])>
    <cfquery name="test" dbtype="query">
    SELECT columnA
    FROM q
    </cfquery>

    <cfdump eval=test>
    <cfdump eval=len(test.columnA)>
    <cfdump var="#replace(test.columnA,' ','a space','all')#">

Returns

number 6

string a spacea spacea spaceAAA

You can also run this code on <a href="https://www.trycf.com/scratch-pad/pastebin?id=wrzxdALb" target="_blank">trycf.com</a>

UPDATE: Adam Cameron [pinged](https://twitter.com/dacCfml/status/476628676394897408) me on Twitter (and Ray added in the comments) that this is fixed in ColdFusion 11.
