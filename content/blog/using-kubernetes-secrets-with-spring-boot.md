---
title: Using Kubernetes Secrets with Spring Boot
date: 2020-11-07 21:01:30
permalink: /2020/11/07/using-kubernetes-secrets-with-spring-boot/
tags:
  - kubernetes
  - spring boot
---

First, create a secret, for this example we'll be storing a username and password

```bash
kubectl create secret generic mssqldbcreds --from-literal=spring.db.username=mrbusche --from-literal=spring.db.password=hunter2
```

Second, add a reference to deployment.yml for each key

```yaml
spec:
  template:
    spec:
      containers:
        - env:
            - name: USERNAME
              valueFrom:
                secretKeyRef:
                  name: mssqldbcreds
                  key: spring.db.username
            - name: PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mssqldbcreds
                  key: spring.db.password
```

Finally, reference the value in your application.yml

```yaml
spring:
  db:
    username: ${USERNAME}
    password: ${PASSWORD}
```
