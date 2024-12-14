---
id: 71
title: Converting roman numerals to numbers using Groovy/Grails
redirect_from:
  - /blog2/2015/01/18/converting-roman-numerals-to-numbers-using-groovygrails/
date: 2015-01-18T03:43:36+00:00
author: mrbusche
permalink: /2015/01/18/converting-roman-numerals-to-numbers-using-groovygrails/
categories:
  - groovy
---

I wrote up a [post](https://mrbusche.com/2015/01/10/converting-roman-numerals-to-numbers-using-coldfusion/) last week about my experience converting roman numerals to numbers using ColdFusion and I promised a follow-up doing the same thing in Grails.

I did learn an interesting tidbit about Grails, the maximum numbers of tests you can have in a where clause is 999. Not a big deal as this is a somewhat contrived example, but something to note nonetheless. Without further ado here is my code, once again this assumes you have entered a valid roman numeral and I've tested the accuracy up to 2000.

    class RomanService {
      Integer romanToDecimal(String romanNumber) {
        Integer newNumber = 0, previousNumber = 0
        Map romanToNumberMapping = [M:1000, D:500, C:100, L:50, X:10, V:5, I:1]
        for (Integer oneChar = romanNumber.length() - 1; oneChar >= 0; oneChar--) {
          String oneLetter = romanNumber.charAt(oneChar)
          newNumber = processNumber(romanToNumberMapping[oneLetter], previousNumber, newNumber)
          previousNumber = romanToNumberMapping[oneLetter]
        }
        return newNumber
      }

      Integer processNumber(Integer currentNumber, Integer previousNumber, Integer newNumber) {
        return previousNumber > currentNumber ? newNumber - currentNumber : newNumber + currentNumber
      }
    }

On the whole it's really not much different than the ColdFusion version, semicolons are optional in most places (pretty much anything that's not a for loop) and you can strongly type the return values, although that's definitely not a requirement. I wrote the example above exactly how I'd write it for a project, but also wanted to point out some of what I'm doing isn't really required.

One interesting thing about Groovy and not one I'm terribly fond of is if you don't have a return statement the last piece of code executed is returned, so newNumber doesn't need a return statement in the romanToDecimal function and in processNumber the only line is returned. I've left the return statements off in the code below, but it's not something I'd normally do, it saves .1 seconds of typing to not type it and can make the code confusing in my opinion. I also left off the types of variables, but my opinion is the same as not typing out return, it doesn't save much time to not declare the type and it can cause some unnecessary confusion especially when it's left off in the arguments.

    class RomanService {
      def romanToDecimal(romanNumber) {
        def newNumber = 0, previousNumber = 0
        def romanToNumberMapping = [M:1000, D:500, C:100, L:50, X:10, V:5, I:1]
        for (def oneChar = romanNumber.length() - 1; oneChar >= 0; oneChar--) {
          def oneLetter = romanNumber.charAt(oneChar)
          newNumber = processNumber(romanToNumberMapping[oneLetter], previousNumber, newNumber)
          previousNumber = romanToNumberMapping[oneLetter]
        }
        newNumber
      }

      def processNumber(currentNumber, previousNumber, newNumber) {
        previousNumber > currentNumber ? newNumber - currentNumber : newNumber + currentNumber
      }
    }

I've attached my test case as an external file given the size
