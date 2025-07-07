---
title: Creating a downloadable csv file from an HTML table via java
date: 2020-07-12 21:05:00
permalink: /2020/07/12/creating-a-downloadable-csv-file-from-an-html-table-via-java/
tags:
  - html
  - javascript
  - java
  - jsoup
---

If you have a `<table>` on your website and you'd like users to be able to download the content of that table to a csv file via java, I've got you covered. We'll need HTML, JavaScript, Java, and the [jsoup](https://jsoup.org/) Java HTML parser.

Add a button on your page

```html
<button id="download">Download</button>
```

Add an empty form to your page that posts to your controller action

```html
<form id="myForm" method="post" action="/csvExport">
	<input id="reportData" type="hidden" name="policyDetails" />
</form>
```

JavaScript to grab the HTML

```javascript
document.getElementById('download').onclick = function () {
	let theData = document.getElementById('reportData');
	// this gets the first table on the screen and pulls the HTML, but you can target by id, class, etc
	theData.value = document.getElementsByClassName('table')[0].outerHTML;
	document.getElementById('myForm').submit();
};
```

Add [jsoup](https://mvnrepository.com/artifact/org.jsoup/jsoup) to your build file. Use the latest version.

```
compile 'org.jsoup:jsoup:1.13.1'
```

Create a java controller

```java
@PostMapping(value = "/csvExport", produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
public ResponseEntity<ByteArrayResource> export(@RequestParam("policyDetails") String policyDetails) {
    try {
        String csvText = generateExcel(policyDetails);
        ByteArrayInputStream bais = new ByteArrayInputStream(csvText.getBytes());
        byte[] byteArray = IOUtils.toByteArray(bais);
        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=cat.csv");
        return ResponseEntity.ok()
                             .headers(headers)
                             .contentLength(byteArray.length)
                             .contentType(MediaType.APPLICATION_OCTET_STREAM)
                             .body(new ByteArrayResource(byteArray));
    } catch (Exception e) {
        // log and redirect user to an error page
    }
}
```

```java
public String generateExcel(String policyDetails) {
    StringBuilder sb = new StringBuilder();
    try {
        Document doc = Jsoup.parseBodyFragment(policyDetails);
        Elements rows = doc.getElementsByTag("tr");
        // loop through all the tr
        for (Element row : rows) {
            // loop through all the td
            Elements cells = row.getElementsByTag("td");
            for (Element cell : cells) {
                sb.append(cell.text().concat(","));
            }
            // add a line separator
            sb.append("\n");
        }
    } catch (Exception e) {
        e.getStackTrace();
    }
    return sb.toString();
}
```
