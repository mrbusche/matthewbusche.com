---
id: 73
title: Using an if statement to conditionally run a target in Hudson
redirect_from:
  - /blog2/2015/03/23/using-an-if-statement-to-conditional-run-a-target-in-hudson/
date: 2015-03-23T03:44:31+00:00
author: mrbusche
permalink: /2015/03/23/using-an-if-statement-to-conditional-run-a-target-in-hudson/
categories:
  - hudson
---

We're running a horribly outdated version of Hudson at work (2.2.1), so this may not be relevant for people using a version of Hudson updated in the past 4 years. I was trying to conditionally run a block of code in a Hudson build and thought by setting parameters in the Ant build properties I could turn off running unit tests (based on looking at other build XML files).

I had this code in my Ant build properties

    do.test=false

This didn't work, so I echoed the value into the console and it was correctly registering at false, but the tests were still being run.

     <echo message="Do test? ${do.test}" />
      <target name="test" depends="compile" description="execute unit and functional tests" if="do.test">
        <cobertura-instrument todir="${temp.dir}/instrumented-classes" datafile="${temp.dir}/cobertura.ser">
        </cobertura-instrument>
      </target>

After quite a while trying to find an answer through Google I found out if there's a parameter called `do.test` with ANY value then that is a true statement and the block will run. My solution was to rename the parameter to \_do.test. You could obviously also delete the parameter, but once I had resolved my build issue I was going to turn the tests back on.
