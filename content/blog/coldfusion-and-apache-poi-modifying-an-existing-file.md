---
id: 268
title: ColdFusion and Apache POI modifying an existing file
date: 2017-02-26T16:46:17+00:00
author: mrbusche
permalink: /2017/02/26/coldfusion-and-apache-poi-modifying-an-existing-file/
categories:
  - coldfusion
tags:
  - coldfusion
  - poi
---

I was tasked with creating an excel spreadsheet that mimics a template from a vendor and after a couple hours of struggling I realized it was fruitless and it'd be easier to modify the existing file. The existing file had macros that were ran to validate certain things and all I was adding was names, date of birth, weight and gender.

The following is the gist of what I ended up doing. This is 100% using the poi built into ColdFusion and does not require extra jars or adding anything to the classpath.

    <cfscript>
      currentTemplate = 'filename.xlsx';
      currentFilePath = getDirectoryFromPath(getCurrentTemplatePath());
      javaFile = createObject('java', 'java.io.File').init(currentFilePath & currentTemplate);
      excelFile = createObject('java', 'java.io.FileInputStream').init(javaFile);
      xssfWorkbook = createObject('java', 'org.apache.poi.xssf.usermodel.XSSFWorkbook').init(excelFile);

      // get the first sheet index is 0 based in Java
      sheet1 = xssfWorkbook.getSheetAt(0);
      rowIterator = sheet1.iterator();
      while (rowIterator.hasNext()) {
        currentRow = rowIterator.next();

        // row 8 is where we want to start writing the names
        if (currentRow.getRowNum() > 7) {
          cellIterator = currentRow.iterator();

          while (cellIterator.hasNext()) {
            //1 - last name, 2 first name, 3 middle, 4 DOB, 5 Gender, 6 Weight
            currentCell = cellIterator.next();
            //when in doubt of methods dump out the whole java object
            //writeDump(currentCell); abort;
            currentCellNumber = currentCell.getColumnIndex();
            currentQueryRow = currentRow.getRowNum() - 7;
            // writing an empty row made the macro think I was adding a user
            if (len(trim(getTravelers['lastName'][currentQueryRow]))) {
              if (currentCellNumber == 1) {
                currentCell.setCellValue(getTravelers['lastName'][currentQueryRow]);
              }
              if (currentCellNumber == 2) {
                currentCell.setCellValue(getTravelers['firstName'][currentQueryRow]);
              }
              if (currentCellNumber == 3) {
                currentCell.setCellValue(getTravelers['middle'][currentQueryRow]);
              }
              if (currentCellNumber == 4) {
                currentCell.setCellValue(dateFormat(getTravelers['dob'][currentQueryRow], 'mm/dd/yyyy'));
              }
              if (currentCellNumber == 5) {
                currentCell.setCellValue(left(getTravelers['gender'][currentQueryRow], 1));
              }
              if (currentCellNumber == 6) {
                currentCell.setCellValue(getTravelers['weight'][currentQueryRow]);
              }
            }
          }
        }
      }

      // need to force formulas to be recalculated once the file is written
      formulaEvaluator = createObject('java', 'org.apache.poi.xssf.usermodel.XSSFFormulaEvaluator');
      formulaEvaluator.evaluateAllFormulaCells(xssfWorkbook);
      // and once the workbook is opened
      xssfWorkbook.setForceFormulaRecalculation(true);

      // close the file input stream
      excelFile.close();
      // create a new excel file
      newFileName = 'roster.xlsx';
      newFile = createObject('java', 'java.io.File').init(currentFilePath & newFileName);
      newExcelFile = createObject('java', 'java.io.FileOutputStream').init(newFile);
      xssfWorkbook.write(newExcelFile);
      newExcelFile.close();
    </cfscript>
