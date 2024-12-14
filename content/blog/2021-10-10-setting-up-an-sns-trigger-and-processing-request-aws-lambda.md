---
title: Setting up an SNS trigger and processing the request in AWS Lambda
date: 2021-10-10 15:05:30
tags:
  - lambda
  - sns
---

Setting up an SNS topic is pretty well documented, but I struggled with how to take action when the event is triggered.

Turns out it's pretty straightforward. The `event['detail-type']` will be `Scheduled Event`.

```yaml
myFunction:
  Type: AWS::Serverless::Function
  Properties:
    Handler: app.handler
    Events:
      SNSTopicTrigger:
        Type: SNS
        Properties:
          Topic: !Ref rSNSTopic

rSNSTopic:
  Type: AWS::SNS::Topic
  Properties:
    DisplayName: SNSTrigger

anotherFunction:
  Properties:
    Policies:
      - AWSLambdaExecute
      - Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action:
              - sns:Publish
            Resource: !Ref rSNSTopic
```

SNS calling function

```javascript
const message = {
	default: JSON.stringify({
		name: 'John Doe',
		timestamp: new Date(),
	}),
};
var params = {
	TopicArn: YOUR_SNS_TOPIC,
	Subject: 'An Important Event',
	MessageStructure: 'json',
	Message: JSON.stringify(message),
};
await sns.publish(params).promise();
```

SNS processing function

```javascript
if (event.Records && event.Records[0].EventSource === 'aws:sns') {
	const message = JSON.parse(event.Records[0].Sns.Message);
	console.log(['SNS event', message]);
	doSomething(message);
}
```
