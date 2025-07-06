---
id: 301
title: Adding rows to an excel spreadsheet using apache poi
date: 2017-07-02T02:35:19+00:00
author: mrbusche
permalink: /2017/07/02/adding-rows-to-an-excel-spreadsheet-using-apache-poi/
categories:
  - coldfusion
  - java
  - poi
tags:
  - add rows
  - apache poi
  - coldfusion
  - java
  - poi
  - shiftRows
---

In a recent project for a client I was tasked with modifying an existing excel spreadsheet to add data from a query. Being familiar with Java and ColdFusion I assumed this would be a pretty trivial exercise. Read the existing file, get the sheet and then write the data, but I ran into an issue where adding rows using [shiftRows](<https://poi.apache.org/apidocs/org/apache/poi/hssf/usermodel/HSSFSheet.html#shiftRows(int,%20int,%20int)>) didn't make them writable and/or visible to apache poi. I realized I needed to literally add the rows and the columns to the excel spreadsheet to be able to change the values. Not a big deal code-wise and also really fast to complete, but frustrating to figure out.

    currentCharterTemplate = 'existingWorkbook.xlsx';
    currentFilePath = getDirectoryFromPath(getCurrentTemplatePath());
    javaFile = createObject('java', 'java.io.File').init(currentFilePath & currentCharterTemplate);
    excelFile = createObject('java', 'java.io.FileInputStream').init(javaFile);
    xssfWorkbook = createObject('java', 'org.apache.poi.xssf.usermodel.XSSFWorkbook').init(excelFile);

    summarySheet = xssfWorkbook.getSheetAt(0);
    totalColumns = 12;
    rowsToAdd = query.recordCount;
    //add enough rows/columns to the spreadsheet to handle the record count of the query and the sort fields
    for (rows = 1; rows <= rowsToAdd; rows++) {
      summarySheet.createRow(rows);
      theCurrentRow = summarySheet.getRow(rows);
      for (columns = 0; columns <= totalColumns; columns++) {
        theCurrentRow.createCell(columns);
        theCurrentRow.getCell(columns);
      }
    }
