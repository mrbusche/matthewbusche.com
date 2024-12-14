---
title: 'Bash loop through folders recursively and lower case files'
date: 2018-10-25 09:35:57
tags:
  - bash
  - linux
---

This script will loop through all files and folders recursively and make them lower case. _Please_ do not just blindly run this against your intended directory. The `echo` is there for testing and once you know that works then use the `mv` command

You can perform any command you'd like after the tr. In my case it's replace all upper case letters with lower case ones.

If you don't include the `if` statement, you'll get a warning message if it tries to rename to the same case, so that keeps the console clean.

```
find /home/buschm3/bananas -depth -name '*' -print0 |
while IFS= read -r -d '' src; do
    dst=`dirname "${src}"`/`basename "${src}" | tr '[A-Z]' '[a-z]'`
    echo "$src"
    echo "$dst"
    if [ "${src}" != "${dst}" ]
    then
        #mv "$src" "$dst"
    fi
done
```
