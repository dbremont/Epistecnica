---
tags: [tool]
---

# spaCy

 : Natural Language Processing (NLP) (Natural%20Language%20Processing%20(NLP)%20f18437a3d82f4a7a9e20cde1feb5b027.md)

> **Industrial**-strength **Natural Language Processing (NLP)** in **Python**.
> 

## ❓QA

- Would you like help selecting the best model for your use case (e.g., semantic search, clustering, summarization)?

## 🖥️ CLI

> `python -m spacy download`.
> 

## 🔍 Models

> spaCy provides a range of **pre trained NLP models** (called pipelines) designed for various languages and tasks. These models vary in size, speed, accuracy, and architecture.
> 

| Model | Embedding Type | Size | Transformer | Notes |
| --- | --- | --- | --- | --- |
| `en_core_web_sm` | None (contextual only) | ~11MB | ❌ | Fast, no vectors |
| `en_core_web_md` | Static GloVe | ~40MB | ❌ | OK similarity |
| `en_core_web_lg` | Static GloVe | ~800MB | ❌ | Best static similarity |
| `en_core_web_trf` | Contextual (BERT) | ~500MB | ✅ | Best semantic performance |

## Visualizer

> 

## 🔧 Custom Models

You can:

- Fine-tune transformer models using `spacy train`
- Use HuggingFace models via `spacy-transformers`
- Add custom components to the pipeline (e.g., text classification)

## 🧩 Case Study

```python
import spacy

nlp = spacy.load("en_core_web_trf")
doc = nlp("SpaCy is a powerful NLP library.")

print("Vector:", doc.vector[:5])
print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])

```

## 📚 References

- https://github.com/explosion/spaCy
- https://spacy.io/usage/visualizers
- https://spacy.io/api/cli
- https://spacy.io/models
