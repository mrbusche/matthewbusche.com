---
title: Generating a Cybersource Flex Key using ColdFusion
date: 2021-09-01 15:01:30
permalink: /2021/09/01/generating-a-cybersource-flex-key-using-coldfusion/
tags:
  - cybersource
  - coldfusion
---

Cybersource is a payment provider with poor examples and poor documentation. I struggled through this for about 25 hours before I found the right combination of settings.

First you need to include the [cybersource-rest-client-java](https://mvnrepository.com/artifact/com.cybersource/cybersource-rest-client-java) and [AuthenticationSDK](https://mvnrepository.com/artifact/com.cybersource/AuthenticationSdk) jars on your classpath. You can do this by adding the following to your Application.cfc or by dropping them into the `\cfusion\lib` folder

```java
this.javaSettings = {LoadPaths = [".\libs\cybersource-rest-client-java-0.0.35.jar", ".\libs\AuthenticationSdk-0.0.17.jar"], loadColdFusionClassPath = true, reloadOnChange = false};
```

I've created a struct to house the default [Cybersource](https://www.cybersource.com/) credentials as the `sample` environment. You'll want to replace `test` and `production` with your credentials, ideally pulling them from secrets and not hardcoded and placed into source control. The second parameter is your target origin, which varies by environment and potentially by user workstation as well.

```java
<cfscript>
writeDump(retrieveFlexKey('sample', 'http://localhost:8500'));

public String function retrieveFlexKey(String environment, String targetOrigin) throws Exception {

  var flexPublicKey = "NoKeyReturned";

  var environmentDetails = {
    sample: {
      merchantID: "testrest",
      runEnvironment: "apitest.cybersource.com",
      merchantKeyId: "08c94330-f618-42a3-b09d-e1e43be5efda",
      merchantsecretKey: "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="
    },
    test: {
      merchantID: "testrest",
      runEnvironment: "apitest.cybersource.com",
      merchantKeyId: "08c94330-f618-42a3-b09d-e1e43be5efda",
      merchantsecretKey: "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="
    },
    production: {
      merchantID: "testrest",
      runEnvironment: "apitest.cybersource.com",
      merchantKeyId: "08c94330-f618-42a3-b09d-e1e43be5efda",
      merchantsecretKey: "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="
    }
  };

  try {
    var details = structKeyExists(environmentDetails, environment) ? environmentDetails[environment] : environmentDetails['sample'];
    props = createObject('java', 'java.util.Properties');
    props.setProperty("authenticationType", "http_signature");
    props.setProperty("merchantID", details['merchantID']);
    props.setProperty("runEnvironment", details['runEnvironment']);
    props.setProperty("merchantKeyId", details['merchantKeyId']);
    props.setProperty("merchantsecretKey", details['merchantsecretKey']);

    requestInfo = createObject('java', 'Model.GeneratePublicKeyRequest');
    requestInfo.encryptionType("RsaOaep256");
    requestInfo.targetOrigin(arguments.targetOrigin);

    merchantConfig = createObject('java', 'com.cybersource.authsdk.core.MerchantConfig').init(props);
    apiClient = createObject('java', 'Invokers.ApiClient');
    apiClient.merchantConfig = merchantConfig;

    keyGenerationApi = createObject('java', 'Api.KeyGenerationApi').init(apiClient);
    response = keyGenerationApi.generatePublicKey("JWT", requestInfo);

    responseCode = apiClient.responseCode;
    status = apiClient.status;
    writeDump(responseCode);
    writedump(status);
    if (responseCode == '200' && status == 'OK') {
      return response.getKeyId();
    }
  } catch (Exception e) {
    writeDump(e);
    // you'll want to login any errors somewhere
  }

  return flexPublicKey;
}
</cfscript>

```
