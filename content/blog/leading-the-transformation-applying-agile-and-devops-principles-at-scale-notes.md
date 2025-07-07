---
id: 400
title: 'Leading the Transformation: Applying Agile and DevOps Principles at Scale Notes'
date: 2018-05-20T03:08:20+00:00
author: mrbusche
permalink: /2018/05/20/leading-the-transformation-applying-agile-and-devops-principles-at-scale-notes/
categories:
  - book review
tags:
  - book notes
---

My personal notes from [Leading the Transformation](https://www.amazon.com/Leading-Transformation-Applying-DevOps-Principles-ebook/dp/B07B43BLLB/) by [Gary Gruver](https://twitter.com/gruvergary)

- Additional reading &#8211; Many specifics referenced in this book are leveraged from a case study of transformation at HP, detailed in [A Practical Approach to Large-Scale Agile Development, by Gary Gruver, Mike Young, and Pat Fulghum](https://ptgmedia.pearsoncmg.com/images/9780321821720/samplepages/9780321821720.pdf).
- How teams come together to deliver value in large organizations is a first-order effect. How individual teams work is a second-order effect
- Done means
  - feature is signed off
  - defect free
  - test automation is complete
- Software development is such a discover process that many assumptions made in planning can quickly become obsolete during development
- Capacity of an organization to absorb change is the biggest constraint to rolling out improvements
- Should always set objective and review at the end of each iteration
- When estimates are off many organizations react by spending more and more in planning instead of focusing on delivering software
- Instead of scolding people who commit on a red build, create a process that eliminates the problem
  - Usually roll back the last commit
- Many organizations ask their manual testers to learn to automation what they have been doing manually for years. Some orgs buy tools to record what the manual testers are doing and that's even worse
  - Record and playback is awful because if any UI changes the whole test is trash
- An acceptance test should test one thing and one thing only.
- All configurations should be in version control
  - You can automate checking successful deployments by querying your log management software for a successful deployment
- Developers want to do a good job, and they assume they have until they get feedback to the contrary
- ROI on DevOps is substantial but you will never achieve full benefit until you get your automated testing built out and integrated into the development pipeline
- Applying DevOps principles at scale really requires the executive to drive the cultural and technical changes for improving the stability of trunk. This is vitally important because of the productivity gains that are possible when you eliminate branches and integrate all work across the teams on trunk. To get your code trunk to this level of quality and to keep it there, you need to begin using a CD pipeline with both code and component-level gating. This pipeline must incorporate a robust test automation framework. You will need to have component-based automated tests. Executives will need some simple metrics that are auto-generated each day to understand what is working and what is not so that they can focus resources in the right place every day.
