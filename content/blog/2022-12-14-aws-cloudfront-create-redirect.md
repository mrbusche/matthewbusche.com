---
title: AWS CloudFront create redirect using CloudFormation
date: 2022-12-14 21:09:30
tags:
  - aws
  - cloudfront
---

When decommissioning a website, it's ideal to set up a permanent redirect for the current domain, so users aren't left in the dark. Below is code to redirect a user from an existing CloudFront distribution to a new URL.

You can use any statusCode, but in this instance a 301 is appropriate because this is a permanent redirect.

```yaml
# The Distribution should already exist. We just need to add the FunctionAssociations
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
        ### new code ###
        FunctionAssociations:
          - EventType: viewer-request
            FunctionARN: !GetAtt BuscheRedirectFunction.FunctionMetadata.FunctionARN #name needs to match redirect function
        ### end new code ###
        HttpVersion: http2

### new function ###
BuscheRedirectFunction: # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html
  Type: AWS::CloudFront::Function
  Properties:
    Name: 'busche-redirect'
    AutoPublish: true
    FunctionCode: |
      function handler(event) {
        return {
          statusCode: 301,
          statusDescription: 'Found',
          headers: {
            'cloudfront-functions': { value: 'generated-by-CloudFront-Functions' },
            'location': { value: 'https://mrbusche.com' }
          }
        };
      }
    FunctionConfig:
      Comment: rewrite requests from busche to mrbusche.com
      Runtime: cloudfront-js-1.0
### end new function ###
```
