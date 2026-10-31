---
tags: [representation, technique]
---

# Representation

 : Input Representation (Input%20Representation%20188c0f5171ec80f98609c2fb11567e53.md)

> In this note we will explore the term **‘Representation’** in AI.
> 

> Note: **Representation** is not a concept - is just a term  - we need to add  a ‘last name’  in order to become a concept in the proper sense.
> 

> In **machine learning**, meaning **is not stored but enacted**—revealed only through computational invocation.
> 

> Note:  **Rich representations emerge** when the model is forced to compress structured variation under limited capacity. Poverty is ‘thinking resources’ is actually -  a feature not a bug, and to the emergence of **`Intelligence`**.
> 

## Term Linguistic

> How is the term ‘representation’ used across the `AI field`?
> 

| **Context** | **Meaning** |
| --- | --- |
| Feature Representation | Encoded input used for learning or inference |
| Latent Representation | Hidden variables capturing compressed structure |
| Distributed Representation | `Information` spread across many units |
| Representation Learning | Process of learning **useful encodings** |
| Internal Representation | Activations within a model |
| Semantic Representation | Encoding of meaning (especially in NLP) |
| State Representation (RL) | Encoding of environment state for decision-making |
| Symbolic Representation | Explicit, human-readable structures |
| Representation Space | Geometry induced by encoding |
| Representation Capacity | What structures a model can encode |

## General Property Set

> Which are the set of properties that applies to all types of representations?
> 
- **Sufficiency**: retains all information needed for the task
- **Minimality**: compresses irrelevant variability
- **Structure**: exposes latent factors (e.g., disentanglement, geometry)
- **Composability**: supports hierarchical or modular reuse

## Evaluation

> How to evaluate a given representation of any type?
> 
- Facilitate **task-relevant computation**
- Improve **statistical efficiency** (generalization, sample complexity)
- Enable **linear or low-complexity decision boundaries** for downstream tasks

## **Pipeline Position**

- **Raw Input**: Unprocessed data in its original form (e.g., pixels, tokens, sensor signals), typically high-dimensional and unstructured with respect to the task.
- **Initial Representation**: Early encoding of input into a model-compatible format (e.g., embeddings, normalized tensors), capturing low-level structure and local statistics.
- **Intermediate Representations**: Layer-wise transformed states that progressively extract, recombine, and reorganize features; partial invariances and higher-order patterns begin to emerge.
- **Final Representation**: Task-aligned encoding optimized for downstream use (e.g., classification logits, contextual embeddings), where relevant information is maximally accessible for decision-making.

## QA

### What does ‘distributed representation’ really mean? Can the notions of state and operator (transformation) be disentangled? What is the notion of the term information in this context?

> Is the idea of **distributed representation**—after removing all the fuss—just an internal representation–enrichment mechanism distributed across layers,  operationalized through **transformations (elicited) (*suscitar*)**, making internal representations richer and improving downstream task performance?
> 

### Which are the underlying mechanisms that encode internal representations?

> Modern ML models encode information implicitly in parameterized transformations; representations are not explicitly stored but are **functionally realized and become observable only through appropriate computational readouts.**
> 

> Note: Modern ML is not just representation (or some  memory analog) - is also computation.
> 

> **Modern ML systems** should not be understood as mere representation or memory analogues; they are coupled representation–computation systems in which encoded states are continuously transformed through learned operators.
> 

## References

- **(Add this Paper to Thesaurus)** https://arxiv.org/abs/1206.5538
- https://stats.stackexchange.com/questions/506610/what-exactly-is-a-representation-in-the-context-of-machine-learning
- https://wikidocs.net/255195
