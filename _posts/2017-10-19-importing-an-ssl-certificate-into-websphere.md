---
id: 338
title: Importing an SSL certificate into WebSphere
redirect_from:
  - /blog2/2017/10/19/importing-an-ssl-certificate-into-websphere/
date: 2017-10-19T02:18:39+00:00
author: mrbusche
permalink: /2017/10/19/importing-an-ssl-certificate-into-websphere/
categories:
  - websphere
tags:
  - handshake error
  - ssl
  - webservice
  - websphere
---

If you are receiving SSL handshake issues when connecting to a webservice you need to import the SSL certificate into WebSphere.

1. Open WebSphere console
2. Security
3. SSL certificate and key management
4. Key stores and certificates
5. NodeDefaultTrustStore (or maybe CellDefaultTrustStore)
6. Signer Certificates
7. Retrieve from port
8. Host: your.host.name (without https:// and any endpoints)
9. Port: 443
10. Retrieve signer information
11. Click Ok
12. Save
13. Restart WebSphere
