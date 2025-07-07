---
title: Unzip Docker image and contents
date: 2023-02-15 21:09:30
permalink: /2023/02/15/unzip-docker-image-and-contents/
tags:
  - docker
---

If you ever need to see the files inside a docker image, you can save the image locally and then unzip all the contents.

```shell
image_tag=repository:tag

docker save ${image_tag} > image.tar
tar xf image.tar
rm image.tar

for f in */; do
  if [ -d "${f}" ]; then
    cd "${f}" ||
        # unzip each of the layers
        find ./ -type f -name "*.tar" -exec tar xf "{}" \;
    cd ../
  fi
done
```
