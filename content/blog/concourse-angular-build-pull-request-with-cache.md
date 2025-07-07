---
title: Concourse build angular app on pull request with cache
date: 2021-01-27 21:01:30
permalink: /2021/01/27/concourse-angular-build-pull-request-with-cache/
tags:
  - concourse
  - angular
---

```yaml
resource_types:
  - name: pull-request
    type: registry-image
    source:
      repository: teliaoss/github-pr-resource

resources:
  - name: pull-request
    type: pull-request
    icon: source-pull
    check_every: 8760h
    webhook_token: ((webhook-token))
    public: true
    source:
      repository: ((your-repository))
      access_token: ((access-token.git-access-token))

jobs:
  - name: test-pull-request
    plan:
      - get: pull-request
        trigger: true
        version: every
      - put: pull-request
        params:
          path: pull-request
          status: pending
      - task: unit-test
        config:
          platform: linux
          image_resource:
            type: registry-image
            source:
              repository: node
              tag: alpine # you can use any node image, alpine is the smallest
          inputs:
            - name: pull-request
          run:
            path: /bin/sh
            args:
              - -exc
              - |
                npm config set cache $(pwd)/.npm --global
                cd pull-request
                export NG_CLI_ANALYTICS=false
                # execute whatever commands you need here
                npm install --quiet
                npm run build:test
          caches:
            - path: .npm
            - path: pull-request/node_modules
        on_failure:
          put: pull-request
          params:
            path: pull-request
            status: failure
      - put: pull-request
        params:
          path: pull-request
          status: success
```

Github webhook URL - `https://${concourse-url}/api/v1/teams/${concourse-team-name}/pipelines/{pipeline-name}/resources/pull-request/check/webhook?webhook_token=((webhook-token))`
`((webhook-token))` can be anything you want it to be as long as it's used consistently in your webhook URL and in your pipeline
