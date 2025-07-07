---
title: Book Notes - Generative AI in Action
date: 2024-11-23 11:40:30
permalink: /2024/11/23/book-notes-generative-ai-in-action/
tags:
  - booknotes
  - generative-ai
---

[Generative AI in Action](https://www.manning.com/books/generative-ai-in-action)

Not a lot of notes because a lot was things I've already learned. Would be a great resource for anyone new to the space.

> In the past, we would need to use a named entity recognition (NER) model for entity extraction; furthermore, that model would need to have seen the data and be trained as part of its dataset. With LLM models, we can do this without any training, and they are more accurate. While traditional NER methods are effective, they often require manual effort and domain-specific customization. LLMs have significantly reduced this burden, offering a more efficient and often more accurate approach to NER across various domains. A key reason is the Transformer architecture, which we will cover in the next few chapters. This is a great example of traditional AI being more rigid and less flexible than generative AI.

Counting tokens for GPT

```python
import tiktoken as tk

def count_tokens(string: str, encoding_name: str) -> int:
  # Get the encoding
  encoding = tk.get_encoding(encoding_name)

  # Encode the string
  encoded_string = encoding.encode(string)

  # Count the number of tokens
  num_tokens = len(encoded_string)

  return num_tokens

# Define the input string
prompt = “I have a white dog nam

# Display the number of tokens in the String
print(“Number of tokens:” , count_tokens(prompt, “cl100k_base”))
# Running this code, as expected, gives us the following output:
# python countingtokens.py
# Number of tokens: 7
```
