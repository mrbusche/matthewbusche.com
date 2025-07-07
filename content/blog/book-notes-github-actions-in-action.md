---
title: Book Notes - GitHub Actions in Action
date: 2024-11-23 11:42:30
permalink: /2024/11/23/book-notes-github-actions-in-action/
tags:
  - booknotes
  - github-actions
---

[GitHub Actions in Action](https://www.manning.com/books/github-actions-in-action)

Generating an SBOM using the Microsoft SBOM tool

```yaml
name: Generate SBOM
  run: |
    curl -Lo $RUNNER_TEMP/sbom-tool https://github.com/microsoft/sbomtool/releases/latest/download/sbom-tool-linux-x64
    chmod +x $RUNNER_TEMP/sbom-tool
    $RUNNER_TEMP/sbom-tool generate -b ./buildOutput -bc . -pn Test -pv 1.0.0 -ps mycompany -nsb https://sbom.mycompany.com -V Verbose
```

Job summaries

```yaml
Here is an example that adds Markdown and plain HTML to the job summary:
  - run: echo '### Hello world! :rocket:' >> $GITHUB_STEP_SUMMARY
  - run: echo '### Love this feature! :medal_sports:' >> $GITHUB_STEP_SUMMARY
  - run: echo '<h1>Great feature!</h1>' >> $GITHUB_STEP_SUMMARY
```

Built-in functions in GitHub for expressions

```shell
toJSON()
fromJSON()
hashFiles()
contains(search, item)
startsWith()
endsWith()
format() // replaces values in string
```

Functions to check status of workflow job

```bash
success()
always()
cancelled()
failure()
```

Chaining workflow jobs

```yaml
job_1:

job_2:
  needs: job_1
```
