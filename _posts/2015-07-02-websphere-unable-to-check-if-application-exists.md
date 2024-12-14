---
id: 125
title: Websphere unable to check if application exists
redirect_from:
  - /blog2/2015/07/02/websphere-unable-to-check-if-application-exists/
date: 2015-07-02T20:42:57+00:00
author: mrbusche
permalink: /2015/07/02/websphere-unable-to-check-if-application-exists/
categories:
  - java
  - websphere
tags:
  - ibm
  - websphere
---

I'm still fairly new to Websphere, but this seemed like a pretty common problem someone would have and I couldn't find anything that properly explained the issue to me. I was running into an issue where WebSphere kept saying it was unable to check if application exists when it was being deployed. I thought initially this was a permissions problem, so I fooled around with permissions but had the same issue. If you scroll down a ways on the stack trace it says

> insufficient or empty credentials

I double checked my configuration in Hudson/Jenkins and testing the connection worked fine, so I continued searching for other solutions. There are literally 3 search results on google for &#8220;unable to check if application exists&#8221; and 0 results on bing. Most of the other articles I found offered no help. Eventually I circled back around and decided to look at the access level my user had in WebSphere. Turns out it wasn't listed as a user! I'm still not sure how testing the connection in Hudson worked but I wasn't listed as a user in WebSphere. I checked this half a dozen times just to make sure I wasn't mistaken.

To add a user in WebSphere

1. Users and Groups
2. Administrative user roles
3. Select the Administrator role
4. Enter the user to search for
5. Use the arrow to move the user to the Mapped to role box
6. Click OK
7. Click Save

Step 7 is super important because it requires an additional save than most programs do and I find myself forgetting to do the second confirmation too often. After you've added the appropriate permissions redeploy your ear and you should be all set.

Full stack trace of the error I was getting

    [INFO] No custom module-to-server mappings found -- using default configuration.
    com.insertcompanynamehere.websphere.deployment.client.DeploymentException: Unable to check if application exists 'NewBusiness'
    at com.insertcompanynamehere.websphere.deployment.client.was61.DeploymentManager.applicationExists(DeploymentManager.java:265)
    at com.insertcompanynamehere.websphere.deployment.WebsphereDeploymentTask.execute(WebsphereDeploymentTask.java:59)
    at com.insertcompanynamehere.hudson.plugin.WebSphereDeploymentBuilder.perform(WebSphereDeploymentBuilder.java:194)
    at hudson.tasks.BuildStepMonitor$3.perform(BuildStepMonitor.java:45)
    at hudson.model.AbstractBuild$AbstractBuildExecution.perform(AbstractBuild.java:761)
    at hudson.model.AbstractBuild$AbstractBuildExecution.performAllBuildSteps(AbstractBuild.java:721)
    at hudson.model.Build$BuildExecution.post2(Build.java:183)
    at hudson.model.AbstractBuild$AbstractBuildExecution.post(AbstractBuild.java:670)
    at hudson.model.Run.execute(Run.java:1743)
    at hudson.model.FreeStyleBuild.run(FreeStyleBuild.java:43)
    at hudson.model.ResourceController.execute(ResourceController.java:89)
    at hudson.model.Executor.run(Executor.java:240)
    Caused by: com.ibm.websphere.management.exception.AdminException:
    at com.ibm.websphere.management.application.AppManagementProxy.proxyInvoke(AppManagementProxy.java:189)
    at com.ibm.websphere.management.application.AppManagementProxy.checkIfAppExists(AppManagementProxy.java:266)
    at com.insertcompanynamehere.websphere.deployment.client.was61.DeploymentManager.applicationExists(DeploymentManager.java:263)
    ... 11 more
    Caused by: javax.management.JMRuntimeException: ADMN0022E: Access is denied for the checkIfAppExists operation on AppManagement MBean because of insufficient or empty credentials.
    at com.ibm.ws.management.connector.soap.SOAPConnectorClient.handleAdminFault(SOAPConnectorClient.java:948)
    at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invokeTemplateOnce(SOAPConnectorClient.java:916)
    at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invokeTemplate(SOAPConnectorClient.java:682)
    at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invokeTemplate(SOAPConnectorClient.java:672)
    at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invoke(SOAPConnectorClient.java:658)
    at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invoke(SOAPConnectorClient.java:480)
    at $Proxy43.invoke(Unknown Source)
    at com.ibm.ws.management.AdminClientImpl.invoke(AdminClientImpl.java:224)
    at com.ibm.websphere.management.application.AppManagementProxy.proxyInvoke(AppManagementProxy.java:183)
    ... 13 more
    Build step 'IBM WebSphere v8.0 Deployment' changed build result to FAILURE
    Finished: FAILURE
