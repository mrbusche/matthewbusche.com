---
title: Cache bust JavaScript, CSS or other file in Dockerfile
date: 2023-02-15 21:09:30
permalink: /2023/02/28/cache-bust-in-Dockerfile/
tags:
  - docker
---

If you have an application without a build system, but need to cache bust a js file, this will do the trick

```dockerfile
FROM nginx:1

COPY --chown=nginx:nginx html/ /usr/share/nginx/html

EXPOSE 8080

# Cache bust js file by appending date to scan.js file
RUN sed -i "s/scan.js/scan.js?a=$(date '+%Y%m%d%H%M')/g" /usr/share/nginx/html/index.html

ENTRYPOINT ["nginx", "-g", "daemon off;"]
```
