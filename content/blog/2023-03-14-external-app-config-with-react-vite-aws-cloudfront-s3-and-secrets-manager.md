---
title: External app config with React, Vite, AWS CloudFront, S3, and Secrets Manager
date: 2023-03-14 21:09:30
tags:
  - aws
  - cloudfront
  - s3
  - secrets-manager
  - react
  - vite
---

_Putting secrets in your git repo is a no no, learn how to accomplish this using React, S3, and AWS Secrets Manager_

### Create a secret (you can also do this manually through the UI)

```yaml
rSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
        Description: Secrets used to create application configuration
        Name: !Sub '${pProduct}'
        SecretString: '{}'
        Tags:
        - Key: Environment
            Value: !Ref pEnvironment

Outputs:
  oSecrets:
    Value: !Ref rMyAppConfig
```

### Add your secrets using Secrets Manager in your AWS account

[Adding secrets to AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html)

### Create a CodePipeline step to deploy your application to S3

```yaml
- Name: Build_and_Deploy_To_S3
  ActionTypeId:
    Category: Build
    Owner: AWS
    Provider: CodeBuild
    Version: '1'
  Configuration:
    ProjectName: !Sub ${pProduct}-${pBusinessUnit}-S3Upload-${AWS::Region}
    # The env variables are necessary to retrieve the secret id, you can omit if you'd like to hard code it
    EnvironmentVariables: !Sub '[{"name":"S3_BUCKETS_ARTIFACT_VAR", "value":"CODEBUILD_SRC_DIR_${pBusinessUnit}S3", "type":"PLAINTEXT"}, {"name":"S3_BUCKETS_ARTIFACT_FILE", "value":"${pBusinessUnit}S3Buckets.json", "type":"PLAINTEXT"}]'
    PrimarySource: Source
  InputArtifacts:
    - Name: Source
```

### Update your deploy to S3 step to pull in the secrets

```shell
profile=your-profile

npm ci
viteFilename=.env.production #.env.production is pulled in by default vite build, your name may vary depending on what vite build command you're running

# Pull the secret you created earlier from secrets manager and output as json file
appConfigSecret=$(jq .oSecrets ${!S3_BUCKETS_ARTIFACT_VAR}/${S3_BUCKETS_ARTIFACT_FILE} -r)
aws secretsmanager get-secret-value --secret-id ${appConfigSecret} --query SecretString --profile ${profile} | jq -r > secrets.json

# use jq to update your secrets from json to VITE_SECRET=secret-value
jq -r 'to_entries|map("VITE_\(.key|ascii_upcase)=\(.value|tostring)")|.[]' secrets.json > ${viteFilename}

# Run your build, it is very important you run your build after the secret is already on the file system, otherwise your application will not have access to the secrets
vite build

# copy your application files to s3
s3BucketPath=s3://your-bucket-path
aws s3 rm ${s3BucketPath} --recursive --profile ${profile} --quiet
aws s3 cp ./dist/ ${s3BucketPath} --recursive --sse AES256 --profile ${profile} --quiet
```

Finally, add a script to your package.json file to allow new developers to download the `.env` file from your S3 bucket to your local file system

```shell
"config": "npx path-exists-cli .env && echo 'exists' || aws s3 cp s3://insert-your-bucket-path/.env.production ./.env",
```

The beautiful thng about React plus vite is this file isn't exposed on your file system anywhere
