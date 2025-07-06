---
title: 'jQuery Validate unique email addresses'
date: 2019-07-01 20:06:57
permalink: /2019/07/01/jquery-validate-unique-email-address/
author: mrbusche
categories: jQuery
tags: ['jQuery']
---

jQuery Validate offers a lot of great features out of the box, but one feature it's lacking is validating if something is not found is a list. Fortunately, it's super easy to add your own validators. In my case I want to find if something doesn't exist in a list.

    jQuery.validator.addMethod('uniqueEmail', function(value) {
        var currentEmails = 'an array from somewhere with emails lower cased';
        //NOTE: this check is case sensitive, so make sure you lower case both values being compared
        return $.inArray(value.toLowerCase(), currentEmails) === -1;
    }, 'Email has already been added.')

    $('#ccEmail').validate({
        errorElement: 'div',
        rules: {
            CCEmail_Address: {
                email: true,
                uniqueEmail: true //use the custom validator
            }
        }
    });
