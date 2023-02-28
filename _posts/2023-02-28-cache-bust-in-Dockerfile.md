---
title: Cache bust file in Dockerfile
date: 2023-02-15 21:09:30
layout: post
tags:
  - docker
---

If you have an application without a build system, but need to cache bust a js file, this will do the trick

```Dockerfile
FROM nginx:1

COPY --chown=nginx:nginx html/ /usr/share/nginx/html

EXPOSE 8080

# Cache bust js file by appending date to scan.js file
RUN sed -i "s/scan.js/scan.js?a=$(date '+%Y%m%d%H%M')/g" /usr/share/nginx/html/index.html

ENTRYPOINT ["nginx", "-g", "daemon off;"]
```
