---
title: Cypress - Failed to deserialize the snapshot blob
date: 2021-08-06 16:01:30
tags:
  - cypress
---

Trying to run `npx cypress open` and I received an error of

```
It looks like this is your first time using Cypress: 8.2.0

Cypress failed to start.

# Fatal error in , line 0
# Failed to deserialize the V8 snapshot blob. This can mean that the snapshot blob file is corrupted or missing.
```

Deleting `node_modules` and running `npm install` had no effect, but I was able to get it working again running `npx cypress install --force`.

If that doesn't work you can also rename the Cypress cache folder. On windows it's [`\AppData\Local\Cypress\Cache\<version>`](https://github.com/cypress-io/cypress/issues/5440#issuecomment-546377052)
