---
id: 268
title: ColdFusion and Apache POI modifying an existing file
redirect_from:
  - /blog2/2017/02/26/coldfusion-and-apache-poi-modifying-an-existing-file/
date: 2017-02-26T16:46:17+00:00
author: mrbusche
layout: post
permalink: /2017/02/26/coldfusion-and-apache-poi-modifying-an-existing-file/
categories:
  - ColdFusion
tags:
  - ColdFusion
  - poi
---
I was tasked with creating an excel spreadsheet that mimics a template from a vendor and after a couple hours of struggling I realized it was fruitless and it&#8217;d be easier to modify the existing file. The existing file had macros that were ran to validate certain things and all I was adding was names, date of birth, weight and gender.

The following is the gist of what I ended up doing. This is 100% using the poi built into ColdFusion and does not require extra jars or adding anything to the classpath.

    <cfscript>
    &nbsp;&nbsp;currentTemplate = &#039;filename.xlsx&#039;;
    &nbsp;&nbsp;currentFilePath = getDirectoryFromPath(getCurrentTemplatePath());
    &nbsp;&nbsp;javaFile = createObject(&#039;java&#039;, &#039;java.io.File&#039;).init(currentFilePath & currentTemplate);
    &nbsp;&nbsp;excelFile = createObject(&#039;java&#039;, &#039;java.io.FileInputStream&#039;).init(javaFile);
    &nbsp;&nbsp;xssfWorkbook = createObject(&#039;java&#039;, &#039;org.apache.poi.xssf.usermodel.XSSFWorkbook&#039;).init(excelFile);

    &nbsp;&nbsp;// get the first sheet index is 0 based in Java
    &nbsp;&nbsp;sheet1 = xssfWorkbook.getSheetAt(0);
    &nbsp;&nbsp;rowIterator = sheet1.iterator();
    &nbsp;&nbsp;while (rowIterator.hasNext()) {
    &nbsp;&nbsp;&nbsp;&nbsp;currentRow = rowIterator.next();

    &nbsp;&nbsp;&nbsp;&nbsp;// row 8 is where we want to start writing the names
    &nbsp;&nbsp;&nbsp;&nbsp;if (currentRow.getRowNum() > 7) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cellIterator = currentRow.iterator();

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while (cellIterator.hasNext()) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//1 - last name, 2 first name, 3 middle, 4 DOB, 5 Gender, 6 Weight
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell = cellIterator.next();
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//when in doubt of methods dump out the whole java object
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//writeDump(currentCell); abort;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCellNumber = currentCell.getColumnIndex();
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentQueryRow = currentRow.getRowNum() - 7;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// writing an empty row made the macro think I was adding a user
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (len(trim(getTravelers[&#039;lastName&#039;][currentQueryRow]))) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (currentCellNumber == 1) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell.setCellValue(getTravelers[&#039;lastName&#039;][currentQueryRow]);
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (currentCellNumber == 2) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell.setCellValue(getTravelers[&#039;firstName&#039;][currentQueryRow]);
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (currentCellNumber == 3) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell.setCellValue(getTravelers[&#039;middle&#039;][currentQueryRow]);
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (currentCellNumber == 4) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell.setCellValue(dateFormat(getTravelers[&#039;dob&#039;][currentQueryRow], &#039;mm/dd/yyyy&#039;));
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (currentCellNumber == 5) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell.setCellValue(left(getTravelers[&#039;gender&#039;][currentQueryRow], 1));
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (currentCellNumber == 6) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentCell.setCellValue(getTravelers[&#039;weight&#039;][currentQueryRow]);
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;}

    &nbsp;&nbsp;// need to force formulas to be recalculated once the file is written
    &nbsp;&nbsp;formulaEvaluator = createObject(&#039;java&#039;, &#039;org.apache.poi.xssf.usermodel.XSSFFormulaEvaluator&#039;);
    &nbsp;&nbsp;formulaEvaluator.evaluateAllFormulaCells(xssfWorkbook);
    &nbsp;&nbsp;// and once the workbook is opened
    &nbsp;&nbsp;xssfWorkbook.setForceFormulaRecalculation(true);

    &nbsp;&nbsp;// close the file input stream
    &nbsp;&nbsp;excelFile.close();
    &nbsp;&nbsp;// create a new excel file
    &nbsp;&nbsp;newFileName = &#039;roster.xlsx&#039;;
    &nbsp;&nbsp;newFile = createObject(&#039;java&#039;, &#039;java.io.File&#039;).init(currentFilePath & newFileName);
    &nbsp;&nbsp;newExcelFile = createObject(&#039;java&#039;, &#039;java.io.FileOutputStream&#039;).init(newFile);
    &nbsp;&nbsp;xssfWorkbook.write(newExcelFile);
    &nbsp;&nbsp;newExcelFile.close();
    </cfscript>