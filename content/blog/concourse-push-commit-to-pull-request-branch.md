---
title: Concourse push commit to pull request branch
date: 2021-12-21 21:01:30
permalink: /2021/12/21/concourse-push-commit-to-pull-request-branch/
tags:
  - concourse
---

We run prettier against our repository, but rather than fail a pull-request check if users don't run it locally, we wanted to update the branch, push a commit, and run the other checks. Here's what we were able to get working

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
    webhook_token: token
    public: true
    source:
      repository: github.com/mrbusche/your-repository
      access_token: ((git-access-token))
      v3_endpoint: https://github.com/api/v3/
      v4_endpoint: https://github.com/api/graphql

jobs:
  - name: test-pull-request
    build_log_retention:
      builds: 30
      days: 30
      minimum_succeeded_builds: 10
    public: true
    plan:
    - get: pull-request
      trigger: true
      version: every
    - put: pull-request
      params:
        path: pull-request
        context: UI Tests
        status: pending
    - task: prettier
      config:
        platform: linux
        image_resource:
          type: docker-image
          source:
            repository: image-with-node-git-and-jq
        inputs:
        - name: pull-request
        # this makes pull-request available to subsequent tasks
        outputs:
          - name: pull-request
        params:
          USERNAME: ((git-username))
          ACCESS_TOKEN: ((git-access-token))
        run:
          path: sh
          dir: pull-request
          args:
          - -exc
          - |

            prNumber=$(cat .git/resource/metadata.json | jq -r '.[] | select(.name=="pr") | .value')
            branchName=$(curl 'https://'${USERNAME}:${ACCESS_TOKEN}'@github.com/api/v3/repos/mrbusche/your-repository/pulls/'${prNumber} | jq -r '.head.ref')

            git fetch
            git checkout ${branchName}

            # find last committer email and username, concourse-ci by default
            commitUserId=$(curl 'https://'${USERNAME}:${ACCESS_TOKEN}'@github.com/api/v3/repos/mrbusche/your-repository/pulls/'${prNumber} | jq -r '.user.login')
            git config user.email ${commitUserId}
            git config user.name "$(git log -1 --pretty=format:'%an')"

            # run some command that modifies files
            npm install -g prettier
            npm run prettier:fix

            git add .

            # if you try to commit and push without changes the task fails
            if [[ ! -z "$(git status --porcelain)" ]]; then
              git commit -m "prettier fix"

              git push --set-upstream origin ${branchName}
            else
              echo "no changes found"
            fi

    - task: test-ui
      config:
        platform: linux
        image_resource:
        type: registry-image
        source:
          repository: timbru31/node-chrome
          tag: 14-slim
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
          CYPRESS_INSTALL_BINARY=0 npm ci --quiet
          npm run test:headless
        caches:
        - path: .npm
        - path: pull-request/node_modules
      on_success:
        put: pull-request
        params:
        path: pull-request
        context: UI Tests
        status: success
      on_failure:
        put: pull-request
        params:
        path: pull-request
        context: UI Tests
        status: failure
    - put: pull-request
      params:
        path: pull-request
        status: success
```
