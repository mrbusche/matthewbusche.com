---
title: Using Poetry with platform argument
date: 2025-03-06 16:54:00
permalink: /2025/03/06/using-poetry-with-platform-argument/
tags:
  - python
  - poetry
---

Poetry has recently become our enterprise standard, but it still lacking some features that `pip` provides. Thankfully, a pull request has been opened to [add the platform flag](https://github.com/python-poetry/poetry-plugin-bundle/pull/123). Unfortunately, it has not yet been merged.

To get things working, you can install poetry 2.0.1 and the latest commit from the pull request repo. If you're feeling risky, you could point to the branch, but we were more comfortable pointing to a specific commit

```python
python3 -m pip install poetry==2.0.1
python3 -m pip install git+BrandonLWhite/poetry-plugin-bundle-bw.git@640529e823cd2cb678831409e646c1f641279953
python3 -m poetry bundle --platform manylinux2014_x86_64
```
