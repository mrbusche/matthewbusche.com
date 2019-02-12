---
title: 'Detecting a Credit Card number in a field using JavaScript'
date: 2019-02-11 21:14:00
layout: post
tags:
  - JavaScript
  - PCI
---

Given a field such as `<input id="notes" type="text" names="notes">` You can detect a Credit Card number using the following in jQuery

    $('#notes').on('input', function() {
        const ccDetected = $('#notes').val().match(/\b(?:\d{4}[ -]?){3}(?=\d{3,4}\b)/gm);
        if (ccDetected) {
            alert('don''t use credit cards!');
        }
    });
