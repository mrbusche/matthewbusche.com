---
title: 'Detecting a Credit Card number in a field using JavaScript'
date: 2019-02-11 21:14:00
permalink: /2019/02/11/detecting-a-credit-card-number-in-javascript/
tags:
  - javascript
  - PCI
---

Given a field such as `<input id="notes" type="text" names="notes">` You can detect a Credit Card number using the following in jQuery. This will detect 15 or 16 digit credit card numbers because of the `d{3,4}`. To only detect 15 or 16 change that to be only `d{3}` for 15 or `d{4}` for 16.

    $('#notes').on('input', function() {
        const ccDetected = $('#notes').val().match(/\b(?:\d{4}[ -]?){3}(?=\d{3,4}\b)/gm);
        if (ccDetected) {
            alert('don''t use credit cards!');
        }
    });
