---
title: Squash all commits on a git branch
date: 2024-02-05 20:39:30
permalink: /2024/02/05/squash-all-commits-on-a-git-branch/
tags:
  - git
---

To squash all git commits on a branch you can run

    git reset $(git merge-base master $(git branch --show-current))

There are other required steps, such as ensuring you're up to date from main, but the gist if what you need is the singular command above
