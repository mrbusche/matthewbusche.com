---
title: Book Notes - LLMs in Production
date: 2024-12-20 11:40:30
permalink: /2024/12/20/book-notes-llms-in-production/
tags:
  - booknotes
  - generative-ai
---

[LLMs in production](https://www.manning.com/books/llms-in-production)

A word of warning: Embrace the future now
All new technology meets resistance and has critics; despite this, technologies keep being adopted, and progress continues. In business, technology can give a company an unprecedented advantage. There's no shortage of stories of companies failing because they didn't adapt to new technologies. We can learn a lot from their failures

Like all other skills, your proximity and willingness to get involved are the two main blockers to knowledge, not a degree or ability to notate—these only shorten your journey toward being heard and understood. If you don't have any experience in this area, it might be good to start by first developing an intuition around what an LLM is and needs by contributing to a project like OpenAssistant. If you're a human, that's exactly what LLMs need. By volunteering, you can start understanding what these models train on and why. If you fall anywhere, from no knowledge up to being a professional machine learning engineer, we'll be imparting the knowledge necessary to shorten your time to understanding considerably.

Our current understanding of language is that language is made up of at least five parts: phonetics, syntax, semantics, pragmatics, and morphology. Each of these portions contributes significantly to the overall experience and meaning being ingested by the listener in any conversation.

- Phonetics is probably the easiest for a language model to ingest, as it involves the actual sound of the language. This is where accent manifests and deals with the production and perception of speech sounds, with phonology focusing on the way sounds are organized within a particular language system.
- Syntax is the place where current LLMs are highest-performing, both in parsing syntax from the user and generating its own. Syntax is generally what we think of as grammar and word order; it is the study of how words can combine to form phrases, clauses, and sentences. Syntax is also the first place language-learning programs start to help people acquire new languages, especially based on where they are coming from natively
- Semantics are the literal encoded meaning of words in utterances, which changes at breakneck speed in waves. People automatically optimize semantic meaning by only using words they consider meaningful in the current language epoch.

In the seminal paper, "Attention Is All You Need," [1] Vaswani et al. take the mathematical shortcut several steps further, positing that for performance, absolutely no recurrence (the "R" in RNN) or any convolutions are needed at all.

Reasoning and Acting (ReAct) is a few-shot framework for prompting that is meant to emulate how people reason and make decisions when learning new tasks. [10] It involves a multistep process for the LLM, where a question is asked, the model determines an action, and then observes and reasons upon the results of that action to determine subsequent actions.

PUSHING THE BOUNDARIES OF COMPRESSION
After going down to int4, there are experimental quantization strategies for going even further down to int2. Int2 70B models still perform decently, much to many peoples' surprise.

We can enhance this approach in an important way that we haven't touched on yet: using knowledge graphs. Knowledge graphs store information in a structure that captures relationships between entities. This structure consists of nodes that represent objects and edges that represent relationships. A graph database like NEO4J makes it easy to create and query knowledge graphs. And as it turns out, knowledge graphs are amazing at answering more complex multipart questions where you need to connect the dots between linked pieces of information. Because they've already connected the dots for us
