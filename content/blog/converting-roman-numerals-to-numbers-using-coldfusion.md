---
id: 68
title: Converting roman numerals to numbers using ColdFusion
date: 2015-01-10T03:42:38+00:00
author: mrbusche
permalink: /2015/01/10/converting-roman-numerals-to-numbers-using-coldfusion/
categories:
  - coldfusion
---

I recently worked on a project that required translating roman numerals to the numerical counterpart, this needed to work for anything from 1-2000. I wrote my own using TDD and eventually came up with this

    component {
      public function romanToDecimal(romanNumber) {
        var newNumber = 0;
        var previousNumber = 0;
        var romanToNumberMapping = {M:1000, D:500, C:100, L:50, X:10, V:5, I:1};
        var romanNumeral = ucase(romanNumber);
        for (var oneChar = romanNumeral.length() - 1; oneChar >= 0; oneChar--) {
          var oneLetter = romanNumeral.charAt(oneChar);
          if (previousNumber > romanToNumberMapping[oneLetter]) {
            newNumber-=romanToNumberMapping[oneLetter];
          } else {
            newNumber+=romanToNumberMapping[oneLetter];
          }
          previousNumber = romanToNumberMapping[oneLetter];
        }
        return newNumber;
      }
    }

It's simple enough that you should be able to add each roman numeral and it's number into the mapping and this should theoretically work for any roman numeral, but I only tested up to 2000. This assumes that you have entered a valid roman numeral that can be translated to 1-2000.

The tests are written in MXUnit, so it's a lot of repetition. I'll be following up with a groovy example using spock that should have a much cleaner looking test. I've attached the test file and additionally have submitted this to cflib for approval.

You can download the test <a href="https://mrbusche.com/blog/enclosures/testRoman.txt" target="_blank">here</a> if you're so inclined.
