---
id: 68
title: Converting roman numerals to numbers using ColdFusion
date: 2015-01-10T03:42:38+00:00
author: mrbusche
layout: post
guid: http://matthewbusche.com/blog2/?p=68
permalink: /2015/01/10/converting-roman-numerals-to-numbers-using-coldfusion/
categories:
  - ColdFusion
---
I recently worked on a project that required translating roman numerals to the numerical counterpart, this needed to work for anything from 1-2000. I wrote my own using TDD and eventually came up with this

    component {
    &nbsp;&nbsp;public function romanToDecimal(romanNumber) {
    &nbsp;&nbsp;&nbsp;&nbsp;var newNumber = 0;
    &nbsp;&nbsp;&nbsp;&nbsp;var previousNumber = 0;
    &nbsp;&nbsp;&nbsp;&nbsp;var romanToNumberMapping = {M:1000, D:500, C:100, L:50, X:10, V:5, I:1};
    &nbsp;&nbsp;&nbsp;&nbsp;var romanNumeral = ucase(romanNumber);
    &nbsp;&nbsp;&nbsp;&nbsp;for (var oneChar = romanNumeral.length() - 1; oneChar >= 0; oneChar--) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var oneLetter = romanNumeral.charAt(oneChar);
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (previousNumber > romanToNumberMapping[oneLetter]) {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;newNumber-=romanToNumberMapping[oneLetter];
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else {
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;newNumber+=romanToNumberMapping[oneLetter];
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;previousNumber = romanToNumberMapping[oneLetter];
    &nbsp;&nbsp;&nbsp;&nbsp;}
    &nbsp;&nbsp;&nbsp;&nbsp;return newNumber;
    &nbsp;&nbsp;}
    }
    

It&#8217;s simple enough that you should be able to add each roman numeral and it&#8217;s number into the mapping and this should theoretically work for any roman numeral, but I only tested up to 2000. This assumes that you have entered a valid roman numeral that can be translated to 1-2000.

The tests are written in MXUnit, so it&#8217;s a lot of repetition. I&#8217;ll be following up with a groovy example using spock that should have a much cleaner looking test. I&#8217;ve attached the test file and additionally have submitted this to cflib for approval.

You can download the test <a href="http://matthewbusche.com/blog/enclosures/testRoman.txt" target="_blank">here</a> if you&#8217;re so inclined.