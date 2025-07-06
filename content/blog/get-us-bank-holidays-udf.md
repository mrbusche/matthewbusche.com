---
id: 12
title: get US Bank Holidays UDF
redirect_form:
  - /blog2/2012/11/26/get-us-bank-holidays-udf/
date: 2012-11-26T23:55:09+00:00
author: mrbusche
permalink: /2012/11/26/get-us-bank-holidays-udf/
categories:
  - coldfusion
---

I was looking for an existing UDF on cflib.org for current bank holidays but the only one I could find was for <a href="https://cflib.org/udf/getBankHolidays" target="_blank">German holidays only</a>. With this function you can pass in a year otherwise it will assume the current year is to be used.

The following holidays are calculated using this UDF.

<table>
  <tr>
    <td>Holiday</td>
    <td>Official Date</td>
  </tr>
  <tr>
    <td>New Year's Day</td>
    <td>January 1</td>
  </tr>
  <tr>
    <td>Independence Day</td>
    <td>July 4</td>
  </tr>
  <tr>
    <td>Veterans Day</td>
    <td>November 11</td>
  </tr>
  <tr>
    <td>Christmas Day</td>
    <td>December 25</td>
  </tr>
  <tr>
    <td>Inauguration Day</td>
    <td>January 20th (Year after election year &#8211; multiple of 4)</td>
  </tr>
  <tr>
    <td>MLK's Birthday</td>
    <td>Third Monday in January</td>
  </tr>
  <tr>
    <td>George Washington's Birthday</td>
    <td>Third Monday in February</td>
  </tr>
  <tr>
    <td>Memorial Day</td>
    <td>Last Monday in May</td>
  </tr>
  <tr>
    <td>Labor Day</td>
    <td>First Monday in September</td>
  </tr>
  <tr>
    <td>Columbus Day</td>
    <td>Second Monday in October</td>
  </tr>
  <tr>
    <td>Thanksgiving Day</td>
    <td>Fourth Thursday in November</td>
  </tr>
</table>

    <cffunction name="getUSBankHolidays" access="public" output="false" returntype="struct" hint="general bank holidays for US">
      <cfargument name="iYear" default="#Year(now())#" />
      <cfset var currentYear = arguments.iYear />
      <cfset var strResult =
      { NewYears = createDate(currentYear, 1, 1),
        Independence = createDate(currentYear, 7, 4),
        Veterans = createDate(currentYear, 11, 11),
        Christmas = createDate(currentYear, 12, 25)
      } />

      <cfif NOT (currentYear - 1) MOD 4>
        <cfset strResult.Inauguration = createDate(currentYear, 1, 20) />
      </cfif>
      <cfset strResult.MLKBirthday = createDate(currentYear, 1, GetNthOccOfDayInMonth(3, 2, 1, currentYear)) />
      <cfset strResult.WashingtonsBirthday = createDate(currentYear, 2, GetNthOccOfDayInMonth(3, 2, 2, currentYear)) />
      <cfset strResult.MemorialDay = createDate(currentYear, 5, (DaysInMonth(createDate(2012, 5, 1))) &#8211; (DayOfWeek(createDate(2012, 5, DaysInMonth(createDate(2012, 5, 1)))) &#8211; 2)) />
      <cfset strResult.LaborDay = createDate(currentYear, 9, GetNthOccOfDayInMonth(1, 2, 9, currentYear)) />
      <cfset strResult.ColumbusDay = createDate(currentYear, 10, GetNthOccOfDayInMonth(2, 2, 10, currentYear)) />
      <cfset strResult.Thanksgiving = createDate(currentYear, 11, GetNthOccOfDayInMonth(4, 6, 11, currentYear)) />
      <cfreturn strResult />
    </cffunction>

This function is long overdue for me as monitors that run on week days run on Holidays and result in a lot of false positive &#8216;down' notifications. If the array returned is empty then the scheduled task should run. If the array has records then it's a holiday

This UDF requires the <a href="https://cflib.org/index.cfm?event=page.udfbyid&udfid=179" target="_blank">getNthOccOfDayInMonth</a> function from <a href="https://cflib.org/" target="_blank">cflib.org</a>
