---
id: 64
title: "Using grails assets when you can't use the asset tag"
redirect_from:
  - /blog2/2015/01/05/using-grails-assets-when-you-cant-use-the-asset-tag/
date: 2015-01-05T03:40:33+00:00
author: mrbusche
permalink: /2015/01/05/using-grails-assets-when-you-cant-use-the-asset-tag/
categories:
  - grails
---

In Grails 2.4+ the asset pipeline plugin is included by default and you can access files in the assets folder by using an asset tag

      <asset:javascript src="application.js"/>
      <asset:stylesheet src="application.css"/>
      <asset:image src="logo.png" width="200" height="200"/>

However, it's not always feasible to be able to use that syntax. One example is when loading an svg image with a png fallback. The code would ideally look like this when the HTML is generated.

    <svg width="180" height="60">
      <image xmlns:xlink="https://www.w3.org/1999/xlink" xlink:href="logo.svg" src="logo.png"></image>
    </svg>

Rather than using an asset tag you can use assetPath() to find the file just like using the asset tag would do. In this case our SVG and PNG images are stored in variables named logoSVG and logoPNG. When the HTML is generated the resulting HTML is as desired.

    <svg width="180" height="60">
      <image xmlns:xlink="https://www.w3.org/1999/xlink" xlink:href="${assetPath(src: logoSVG)}" src="${assetPath(src: logoPNG)}"></image>
    </svg>

One important thing to note is the asset plugin is not recursive, so if your file is not located in assets/images you will need to include the path relative to the images folder in your src. If your images were in an imgs folder the syntax would be like so

    <svg width="180" height="60">
      <image xmlns:xlink="https://www.w3.org/1999/xlink" xlink:href="${assetPath(src: 'imgs/' + logoSVG)}" src="${assetPath(src: 'imgs/' + logoPNG)}"></image>
    </svg>
