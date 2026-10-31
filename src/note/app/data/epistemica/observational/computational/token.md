---
tags: [data-representation, representation]
---

# Token

 : Input Representation (Input%20Representation%20188c0f5171ec80f98609c2fb11567e53.md)

> A **token** is a discrete unit derived from raw input data (usually text), used as the **atomic element** in feature extraction, embedding, or model training.
> 

> A **token** is the smallest **representational unit** that a model operates on. It bridges raw input data and the model’s **internal representation**—whether that’s a word, a byte, a visual patch, or a chunk of sound.
> 

## Tokenization

| **Model** | **Type** | **Language Support** | **Key Features** | **Use Cases** |
| --- | --- | --- | --- | --- |
| **Byte Pair Encoding (BPE)** | Subword Tokenization | Multilingual | Merges frequent byte pairs iteratively, balances vocabulary size and granularity. | GPT, RoBERTa, and other transformer models. |
| **WordPiece** | Subword Tokenization | Multilingual | Similar to BPE but uses a probabilistic model to choose merges. | BERT, DistilBERT, and other BERT variants. |
| **SentencePiece** | Subword/Character Tokenization | Multilingual | Tokenizes text without requiring pre-tokenization, supports BPE and unigram models. | T5, ALBERT, and other multilingual models. |
| **Unigram** | Subword Tokenization | Multilingual | Probabilistic model that selects subwords based on likelihood. | Used in SentencePiece and other frameworks. |
| **Byte-level BPE** | Subword Tokenization | Multilingual | Operates at byte level, avoids out-of-vocabulary tokens. | GPT-2, GPT-3, and GPT-4. |
| **Character Tokenization** | Character-level Tokenization | Multilingual | Splits text into individual characters. | Simple models, text preprocessing. |
| **Whitespace Tokenization** | Word-level Tokenization | Multilingual | Splits text based on whitespace. | Basic NLP tasks, simple tokenization. |
| **Moses Tokenizer** | Rule-based Tokenization | Multilingual | Language-specific rules for tokenization. | Machine translation, preprocessing. |
| **Spacy Tokenizer** | Rule-based Tokenization | Multilingual | Customizable, supports advanced linguistic features. | General NLP tasks, dependency parsing. |
| **Tiktoken** | Subword Tokenization | Multilingual | Optimized for OpenAI models, fast and efficient. | GPT-3.5, GPT-4, and other OpenAI models. |

## References

- https://news.ycombinator.com/item?id=42488853
- https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html
- https://news.ycombinator.com/item?id=44366494
