---
id: 254
title: Java Format date with 4, 5 or 6 milliseconds
date: 2016-12-14T15:21:02+00:00
author: mrbusche
permalink: /2016/12/14/java-format-date-with-milliseconds/
categories:
  - Uncategorized
---

The title of this is wrong as far as terminology, but that's what I was googling when trying to figure out my issue, so hopefully someone is helped by my struggles. I had a date `2016-06-01 13:20:24.60807` that I was trying to format into mm/dd/yyyy hh:mm:ss aa and the time was not accurate. I was using yyyy-MM-dd HH:mm:ss.SSSSSS as the format for SimpleDateFormat.

    Date date = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").parse(2019-06-01 13:20:24.60807);

Was my exact Code and it kept outputting 06/01/2016 01:21:24 PM which was mostly accurate but not rounding up. I tried every variation of .\* including just a dot and 1-6 S's, but couldn't get the value to work. The fewer S I tried the more off the result was. It wasn't until I stumbled upon this [StackOverflow question](https://stackoverflow.com/questions/12000673/string-date-conversion-with-nanoseconds) that I found out the issue. In Java 7 and below Date does not have enough precision to handle nanoseconds which is what the 4th, 5th and/or 6th digit after the period was, so rather than just truncating nano seconds it was adding 60,807 ms to my current time. Makes sense once you know the issue, but this data was coming from a stored proc and I could just truncate off the nanoseconds, so I ended up taking the left 23 characters of the current Date and then applying a pattern of &#8220;yyyy-MM-dd HH:mm:ss.SSS&#8221; and then using DateUtils.round to get the correct result. The resulting code, absent my try/catches is below.

    public static String parseDate(final String currentDateStr, String currentFormat, String expectedFormat) {
        String currentDate = StringUtils.left(currentDateStr, 23);
        Date date = DateUtils.round(date, Calendar.SECOND);
        return new SimpleDateFormat(expectedFormat).format(date);
      }
    parseDate(processDate, "yyyy-MM-dd HH:mm:ss.SSS", "MM/dd/yyyy hh:mm:ss a");
