---
title: Moving repositories from Azure DevOps to Github
date: 2020-10-15 21:05:00
layout: post
tags:
  - git
---

To do this you'll need an Azure Devops Personal Access Token and a Github access token

Thanks to [CoderDave](https://github.com/n3wt0n/AzureDevOpsToGitHubRepoMigrator) for the great starting point.

Here's a shell script you can use that'll copy a repository, including tags, branches and full commit history.

It's important to note that the local copy of the repository will be left in an unusable state. That's why the shell script checks out a fresh copy of the repository and deletes it.

```bash
azurepat=''
ghpat=''

# start in the correct directory
cd c:/AppDev/code/azuretogithub/
# checkout your azure repository, --mirror is important
git clone --mirror https://${azurepat}@dev.azure.com/test-app
# change directory to repository just cloned
cd test-app.git/
# add new origin
git remote add GHorigin "https://${ghpat}@github.com/mrbusche/test-app.git"
# push the new origin
git push --mirror GHorigin
# delete the old origin
git remote rm origin
# rename new origin
git remote rename GHorigin origin
# delete git repo from local file system
rm -rf ../test-app.git
```
