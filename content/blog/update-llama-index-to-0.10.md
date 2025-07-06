---
title: Updating LlamaIndex to version 0.10
date: 2024-02-17 14:12:30
permalink: /2024/02/17/update-llama-index-to-0.10/
tags:
  - llamaindex
  - openai
---

With the release of [LlamaIndex v0.10](https://blog.llamaindex.ai/llamaindex-v0-10-838e735948f8) imports have changed from top level llama_index package to `llama_index.core`, `llama_index.embeddings`, and `llama_index.llms`

`ServiceContext` has also been deprecated and replaced with `Settings`. A concise version of existing code is below

```python
from llama_index import ServiceContext
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.evaluation import FaithfulnessEvaluator, RelevancyEvaluator
from llama_index.llms import AzureOpenAI

def evaluate_llama(dataset):
    llm = AzureOpenAI()
    embed_model = AzureOpenAIEmbedding()
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

    faithfulness_gpt4 = FaithfulnessEvaluator(service_context=service_context)
    relevancy_gpt4 = RelevancyEvaluator(service_context=service_context)

    from llama_index.evaluation import BatchEvalRunner
```

Updated code removes creating and passing `ServiceContext` around with the new `Settings` object, which also reduces passing around llmb and embed_model as well. This part is all straightforward, but the migration tool does not take into account needing to add some new packages to requirements.txt

```shell
pip install llama_index_core llama-index-embeddings-azure-openai llama-index-llms-azure-openai
```

Once you've installed new packages, you should be able to update your imports. A concise version of the changes is listed below.

```python
from llama_index.core import Settings
from llama_index.core.evaluation import FaithfulnessEvaluator, RelevancyEvaluator
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.llms.azure_openai import AzureOpenAI

def evaluate_llama(dataset):
    Settings.llm = AzureOpenAI()
    Settings.embed_model = AzureOpenAIEmbedding()

    faithfulness_gpt4 = FaithfulnessEvaluator()
    relevancy_gpt4 = RelevancyEvaluator()

    from llama_index.core.evaluation import BatchEvalRunner
```
