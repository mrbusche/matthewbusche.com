---
title: 'Java setting tracking mode for session'
date: 2018-08-18 08:06:57
permalink: /2018/08/18/java-setting-tracking-mode-for-session/
tags: java
---

If you avoid using xml for you configuration files like I do, but don't want to pass the `jsessionid` around through the URL you can create a `@Bean` and use a lambda to set the tracking mode as follows

    public class AuthProvidersSecurityConfig extends WebSecurityConfigurerAdapter {

        @Bean
        public ServletContextInitializer servletContextInitializer() {
          return servletContext -> {
            servletContext.setSessionTrackingModes(EnumSet.of(SessionTrackingMode.COOKIE));
          };
        }
    }
