---
title: 'Finding md5 hash of file'
date: 2018-09-30 10:05:57
permalink: /2018/09/30/finding-md5-hash-of-file/
tags: md5
---

Fun tip I learned today. If you need to find the md5 hash of a file you can simply user the following command.

    certutil -hashfile {path+filename} md5

certutil is included in windows by default, so you aren't required to have anything additional installed.
