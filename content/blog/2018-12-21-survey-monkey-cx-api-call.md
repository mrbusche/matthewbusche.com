---
title: 'SurveyMonkey CX API call'
date: 2018-12-21 20:56:57
tags:
  - surveymonkey
---

SurveyMonkey has a great new API available that allows you to easily send someone an email programmatically. I ran into some hiccups while setting it up and there's almost zero documentation out there.

Endpoint: This is provided at the end of setting up a survey. Should look like

    https://cx.surveymonkey.com/api/v1/surveys/${fromSurvey}/replies

Headers

    name="Content-Type" value="application/json"
    name="Authorization" value="Token token=#apiToken#"

Body

    {
        "person": {
            "email": "emailAddress",
            "first_name": "first name",
            "last_name": "last name",
            "fields": {
                "Custom Field": ["custom field value"]
            }
        },
        "delay": 0
    }

The custom fields must match _exactly_ what you put in your admin and you must pass it in as a list. If you don't pass a list it won't register. The delay is the number of days to delay sending the survey.

My full postman request is below with sensitive information redacted.

```json
{
	"info": {
		"_postman_id": "d16018c3-53d9-4ebd-a47f-61a84505a04d",
		"name": "SurveyMonkey",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Survey Monkey",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"type": "text"
					},
					{
						"key": "Authorization",
						"value": "Token token=${apiToken}",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"person\": {\r\n    \"email\": \"email@gmail.com\",\r\n    \"first_name\": \"First\",\r\n    \"last_name\": \"Last\",\r\n    \"fields\": {\r\n      \"Products\": [\"Acme M500\", \"Acme B7500\"]},\r\n  \"facets\": {\r\n    \"Job ID\": \"1234\"\r\n  },\r\n  \"delay\": 24\r\n}"
				},
				"url": {
					"raw": "https://cx.surveymonkey.com/api/v1/surveys/${fromSurvey}/replies",
					"protocol": "https",
					"host": ["cx", "surveymonkey", "com"],
					"path": ["api", "v1", "surveys", "${fromSurvey}", "replies"]
				}
			},
			"response": []
		}
	]
}
```
