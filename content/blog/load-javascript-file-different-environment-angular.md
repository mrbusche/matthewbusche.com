---
title: 'Angular Loading JavaScript file in different environments'
date: 2018-09-15 09:43:57
permalink: /2018/09/15/load-javascript-file-different-environment-angular/
tags: angular
---

If you ever need to load two different files in production vs test, you can add some code to your `main.ts` file in your Angular project. The existing code includes the `if` statement and `enableProdMode()`, but you can easily add in the else to conditionally load a different file. In my case I don't want google analytics posting to my production account.

    import { environment } from './environments/environment';

    //create a new element
    const script = document.createElement('script');
    if (environment.production) {
        enableProdMode();
        script.src = 'analytics.js';
    } else {
        script.src = 'test-analytics.js';
    }
    //append that element into the dom
    document.head.appendChild(script);
