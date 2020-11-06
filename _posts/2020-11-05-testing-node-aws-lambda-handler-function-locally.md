---
title: Testing Node AWS Lambda handler function locally
date: 2020-11-05 21:01:30
layout: post
tags:
  - node
  - lambda
---

Add a script to your `package.json` file

```javascript
"scripts": {
    "local": "node -e \"console.log(require('./index').handler({}));\""
}
```

where index is the name of your js file with the code you want to execute
