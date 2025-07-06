---
title: Testing Node AWS Lambda handler function locally
date: 2020-11-05 21:01:30
permalink: /2020/11/05/testing-node-aws-lambda-handler-function-locally/
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

You can execute this script by running

```javascript
npm run local
```
