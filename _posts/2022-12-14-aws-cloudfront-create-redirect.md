---
title: AWS CloudFront create redirect
date: 2022-12-14 21:09:30
layout: post
tags:
  - aws
  - CloudFront
---

When decommissioning a website, it's ideal to set up a permanent redirect for the current domain, so users aren't left in the dark. Below is code to redirect a user from an existing CloudFront distribution to a new URL.

You can use any statusCode, but in this instance a 301 is appropriate because this is a permanent redirect.

```yaml
# The Distribution should already existing. We just need to add the FunctionAssociations
Resources:
  rDistribution:
    Type: AWS::CloudFront::Distribution # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html
    Properties:
      DistributionConfig:
        Enabled: True
        DefaultRootObject: index.html
        DefaultCacheBehavior:
          TargetOriginId: BuscheOrigin
          ViewerProtocolPolicy: redirect-to-https
        FunctionAssociations:
          - EventType: viewer-request
            FunctionARN: !GetAtt BuscheRedirectFunction.FunctionMetadata.FunctionARN #name needs to match redirect function
        HttpVersion: http2
        
BuscheRedirectFunction: # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html
    Type: AWS::CloudFront::Function
    Properties:
      Name: "busche-redirect"
      AutoPublish: true
      FunctionCode: |
        function handler(event) {
          return {
            statusCode: 301, 
            statusDescription: 'Found',
            headers: {
              'cloudfront-functions': { value: 'generated-by-CloudFront-Functions' },
              'location': { value: 'https://matthewbusche.com' }
            }
          };
        }
      FunctionConfig:
        Comment: rewrite requests from busche to matthewbusche.com
        Runtime: cloudfront-js-1.0
```
