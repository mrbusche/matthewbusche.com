---
title: GitHub Actions - Dynamic Status Checks
date: 2026-02-27 16:42:00
permalink: /2026/02/27/github-actions-dynamic-status-checks/
tags:
  - github-actions
---

If you maintain a library of Docker images, you know the power of the strategy matrix in GitHub Actions. It's the easiest way to support multiple language versions (Node 22, 24, 25) across different OS variants (Debian 12, 13) without writing a thousand lines of YAML.

But there's a catch: Required Status Checks.

```yaml
jobs:
  build:
    strategy:
      matrix:
        node-versions: [25, 24, 22, 20]
        debian-versions: [13, 12]
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building Docker image..."
```

When you point a GitHub branch protection rule at a specific matrix job, it looks for a static name like `build (node-25, debian-13)`. As soon as you bump your matrix to Node 26, the old check disappears, and the new one, `build (node-26, debian-13)`, isn't recognized as the "required" check yet. Your PRs end up stuck in a "Waiting for status to be reported" state.

To combat this, I implemented an `all-checks-passed` job. Instead of making the individual matrix names "required" in repository settings, you can make this single, static job the required one.

{% raw %}

```yaml
jobs:
  build:
    strategy:
      matrix:
        node-versions: [25, 24, 22, 20]
        debian-versions: [13, 12]
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building Docker image..."

  all-checks-passed:
    runs-on: ubuntu-latest
    needs: [build] # List your dynamic job here
    if: always() # Ensures this runs even if others fail
    steps:
      - name: Check status of all required jobs
        run: |
          if [[ "${{ contains(needs.*.result, 'failure') ||
            contains(needs.*.result, 'cancelled') }}" == "true" ]]; then
            echo "One or more dynamic checks failed."
            exit 1
          fi
          echo "All checks passed!"
```

{% endraw %}
