---
title: 'ColdFusion Removing duplicate values from a list'
date: 2019-03-30 15:00:00
tags:
  - coldfusion
  - java
---

To get the number unique values from a list you can create a Java `set`, which does not allow duplicate values

    createObject("java", "java.util.HashSet").init(listToArray(valueList(eventsQuery.event_id))).size();

The `init` values requires a list, so if you already have a list, you can just pass that in to return a Java set object. You will need to convert the set back to a list to make it easy to work with in ColdFusion although you could iterate over it if you'd like. Here's the easiest version.

    listWithDupes = [1,2,3,1,3];
    noDupes = createObject("java", "java.util.HashSet").init(listWithDupes);
    noDupesArray = createObject("java", "java.util.ArrayList").init(noDupes);
    writeDump(noDupesArray); //returns 1,2,3
