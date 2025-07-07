---
title: 'Java settting domain on a session cookie'
date: 2018-08-17 08:06:57
permalink: /2018/08/17/java-setting-domain-on-a-session-cookie/
tags: java
---

If you need to override the domain on a session cookie you can add the following method to your `AuthProvidersSecurityConfig` class to do so. It's not common you'd need to do this, but our domain wasn't setting correctly in our cookie and this cleared the issue up.

    public class AuthProvidersSecurityConfig extends WebSecurityConfigurerAdapter {

      @Bean
      public ServletContextInitializer servletContextInitializer() {
        return servletContext -> {
          servletContext.getSessionCookieConfig().setDomain("mrbusche.com");
        };
      }
    }
