---
title: Setting up a cron job and processing the request in AWS Lambda
date: 2021-10-10 15:01:30
tags:
  - lambda
  - cron
---

Setting up a cron job in AWS lambda is pretty trivial, but I struggled with how to take action when the event is triggered. Turns out it's pretty straightforward. The `event['detail-type']` will be `Scheduled Event`.

```yaml
myFunction:
  Type: AWS::Serverless::Function
  Properties:
    Handler: app.handler
    Events:
      myCron:
        Type: Schedule
        Properties:
          Schedule: 'cron(? 10 * * Mon *)'
```

```javascript
if (event['detail-type'] === 'Scheduled Event') {
	console.log('cron triggered');
	return await somethingThatWasScheduled(event);
}
```
