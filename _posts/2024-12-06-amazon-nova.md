---
title: Amazon Nova foundation models
date: 2024-12-06 14:54:00
layout: post
tags:
  - aws
  - nova
---

Amazon announced their [Amazon Nova foundation models](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/) on December 3, 2024. The main features are low cost and low latency.

## Amazon Nova

### Micro

- very low cost
- text-only
- great for summarization, translation, and classification
- 128k token context

### Lite

- Multimodal
  - Multiple images
  - Up to 30 minutes of video
- 300k token context
- Find-tuning with model distillation is available

### Pro

- Similar to Lite but with more accuracy
- Serves as a teacher model to distill custom varians of Lite and Micro

### Premier

- Availability in early 2025
