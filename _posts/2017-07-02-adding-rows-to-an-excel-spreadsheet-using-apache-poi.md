---
id: 301
title: Adding rows to an excel spreadsheet using apache poi
date: 2017-07-02T02:35:19+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=301
permalink: /2017/07/02/adding-rows-to-an-excel-spreadsheet-using-apache-poi/
categories:
  - ColdFusion
  - java
  - poi
tags:
  - add rows
  - apache poi
  - ColdFusion
  - java
  - poi
  - shiftRows
---
In a recent project for a client I was tasked with modifying an existing excel spreadsheet to add data from a query. Being familiar with Java and ColdFusion I assumed this would be a pretty trivial exercise. Read the existing file, get the sheet and then write the data, but I ran into an issue where adding rows using [shiftRows](https://poi.apache.org/apidocs/org/apache/poi/hssf/usermodel/HSSFSheet.html#shiftRows(int,%20int,%20int)) didn&#8217;t make them writable and/or visible to apache poi. I realized I needed to literally add the rows and the columns to the excel spreadsheet to be able to change the values. Not a big deal code-wise and also really fast to complete, but frustrating to figure out.

    currentCharterTemplate = &#039;existingWorkbook.xlsx&#039;;
    currentFilePath = getDirectoryFromPath(getCurrentTemplatePath());
    javaFile = createObject(&#039;java&#039;, &#039;java.io.File&#039;).init(currentFilePath & currentCharterTemplate);
    excelFile = createObject(&#039;java&#039;, &#039;java.io.FileInputStream&#039;).init(javaFile);
    xssfWorkbook = createObject(&#039;java&#039;, &#039;org.apache.poi.xssf.usermodel.XSSFWorkbook&#039;).init(excelFile);
    
    summarySheet = xssfWorkbook.getSheetAt(0);
    totalColumns = 12;
    rowsToAdd = query.recordCount;
    //add enough rows/columns to the spreadsheet to handle the record count of the query and the sort fields
    for (rows = 1; rows <= rowsToAdd; rows++) {
    &nbsp;&nbsp;summarySheet.createRow(rows);
    &nbsp;&nbsp;theCurrentRow = summarySheet.getRow(rows);
    &nbsp;&nbsp;for (columns = 0; columns <= totalColumns; columns++) {
    &nbsp;&nbsp;&nbsp;&nbsp;theCurrentRow.createCell(columns);
    &nbsp;&nbsp;&nbsp;&nbsp;theCurrentRow.getCell(columns);
    &nbsp;&nbsp;}
    }