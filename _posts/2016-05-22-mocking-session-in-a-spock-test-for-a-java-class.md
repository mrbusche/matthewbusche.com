---
id: 218
title: Mocking session in a Spock test for a java class
redirect_from:
  - /blog2/2016/05/22/mocking-session-in-a-spock-test-for-a-java-class/
date: 2016-05-22T21:30:44+00:00
author: mrbusche
permalink: /2016/05/22/mocking-session-in-a-spock-test-for-a-java-class/
categories:
  - Uncategorized
---

Spock is an excellent test framework that is built on top of Groovy and can be used to replace JUnit for testing Java classes. The majority of spock syntax is simple, but sometimes we run into issues where it is difficult to mock a class. Session is one of those examples. Given we want to do something simple, say get the name from Spring Security in session we'd have a method call like this

    private String getUserId() {
      Authentication auth = SecurityContextHolder.getContext().getAuthentication();
      return auth.getName();
    }

To test this we need to mock session for this method and also for any method that calls this private method. To do so you need to mock the Authentication class and the SecurityContext class. Since this mocking is needed in multiple methods I've created a separate method in my spock class to mock the security context. The full test and method look like below

    void "test getUserId"() {
      given:
      setSecurityContext()
      when:
      def response = service.getUserId()
      then:
      response == "hello"
    }

    def setSecurityContext() {
      def authentication = Mock(Authentication)
      authentication.getName() >> "hello"
      def securityContext = Mock(SecurityContext)
      securityContext.getAuthentication() >> authentication
      SecurityContextHolder.setContext(securityContext)
    }

Has anyone found an easier way to do this? Or is this the way it needs to be?
