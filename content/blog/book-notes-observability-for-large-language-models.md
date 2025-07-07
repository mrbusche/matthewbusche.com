---
title: Book Notes - Observability for Large Language Models
date: 2024-11-23 11:39:30
permalink: /2024/11/23/book-notes-observability-for-large-language-models/
tags:
  - booknotes
  - llms
---

[Observability for Large Language Models](https://www.honeycomb.io/resources/observability-for-llms)

- Organizations that lack good tools and data to understand systems in production may find themselves ill-prepared to tackle the challenges posed by a feature that uses LLMs.

- LLMs represent a step change in the capability and accessibility of machine learning (ML) models for organizations. Every product has problems to solve for its users where there is no single solution but rather a set of solutions lying on some spectrum of "correct" or "right."

- However, the very things that make LLMs so useful also give rise to the biggest challenges. End users expect powerful capabilities with reliable behavior, but steering an LLM to reliability for all possible inputs is challenging. Furthermore, the tools that product engineers traditionally lean on for improving reliability - step-by-step debugging and unit testing aren't feasible with LLMs.
- LLMs introduce reliability and predictability challenges that can seem scary when released to production. They are black boxes (you can't debug them like you can a single-threaded client application) that produce nondeterministic outputs based on natural language inputs

- Natural language inputs are broad. Very broad. A natural language, such as English, is infinitely more expressive than any programming language, query language, or UI. What this means is that users of applications with natural language inputs will do things you cannot hope to predict. Yes, there will likely be patterns of similar inputs that users will input for specific reasons-you can account for those-but there is an extremely long tail of inputs your users will create, and users expect those inputs to be handled well

- Finally, attempting to de-risk a product launch through early access programs or limited user testing can introduce bias and create a false sense of security. Early access programs and user testing often fail to capture the full range of user behavior and potential edge cases that arise in real-world usage with a wide range of users.

- Put differently, you should be aware of the following things when building with LLMS:

  - Failure will happen-it's a question of when, not if.
  - Users will do things you can't possibly predict.
  - You will ship a bug fix that breaks something else.
  - You can't write unit tests for LLMS (or practice test-driven development).
  - Early access programs won't really help you.

- By combining OpenTelemetry's automatic tracing instrumentation capabilities with manual instrumentation, you can capture everything you need to begin systematically analyzing user behavior. In this way, you can learn how user behavior impacts the results that a generative AI model will produce.

- Simple LLM Call with a Static Prompt Some prompts are mostly static. That is, they might include user input and some additional info, but inputs are largely the same each time. For these cases, you just need three spans:
  - The overall tracking span for all operations. This is important because it's the span you'll usually query for later on. It represents the end-to-end user experience of your feature that uses an LLM.
  - A child span of the overall tracking span that tracks the call to an LLM (this can be done with automatic instrumentation).
  - A child span of the overall tracking span that tracks any parsing or validation of outputs you do on LLM outputs.
- For many applications, these three spans will suffice for your observability needs
