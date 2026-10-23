---
tags: [neural-network-learning-system, technique]
qa:
  - Which are the components of attention?
  - When is kernel smoothing used in the attention mechanism?
  - What does the query bring to the table?
  - What does values bring to the table?
  - What does \(W_V\) do?
  - What is the nature of \(V\)? What kind of representation is it? Do we even know? Does it matter, or is \(V\) simply a computational representation that a self-organizing system can learn to use without its components having predefined meanings?
  - Are \(W_Q\), \(W_K\), and \(W_V\) learned parameters, or are they part of the model's state?
  - How does attention operate in general?
  - What emergent phenomena are powered by attention?
  - What are the scope and limitations of attention?
  - Where does the query, key and value comes from?
  - During inference, are the queries simply the transformed representations of the prompt tokens, or do they originate from a different mechanism?
  - Are keys and values computed as learned transformations of the prompt token representations or something else?
  - What is the **role of training** shaping the `Key, Query and Value`**?**
  - How should I think about the `Key, Query and Value` ?
  - Is attention just kernel smoothing? Sort of - in the functional form - but in ML  the parameters - that underpins the formation o the K,Q,V are learned.
---

# Attention

> In this note, we examine the attention mechanism underlying transformer architectures.

> **Note:** It is difficult to assign a specific role or meaning to individual network components. Do they primarily enable self-organization? The meaning of a component need not be determined solely by its position in the network.

Guiding Questions:

- Old View
    
    Attention as a sophiticated pattern matcher-> and the how  - of the continuation - or next token generation.
    LLM are are not about next token generation (that the effect) what matter is the driver of the effect (a powerfull patttern matching mechanism called attention).
    
    The curernt context (the continuation of the promot) for the selction fo the next token added to that context - the entire context - and the vocabulary - are match - the match is driven by the attention mechanism to select the next token. ??? is this right?
    
    How is the next 'token generated' from the current context? How are tokens from the vacabulary always choose from (never inveting words)?
    
    Is the next token selection by the attention mechanism or what? Not necesarlly in vocacylary embedign form? but in another repersentaiton - and other layers just do some dump projection?
    
    Attetnoin produces a rerpsention a vector that guides next token selection - it affect teh probabilty distrituioj of a token being selecte dis never - the distribution is itself fixed - but the selection is control by the temprature paramter.
    
    - Temperature modulates sampling stochasticity, not the distribution’s existence.
    - The distribution is context-dependent, not “fixed.”
    
    Which are the paramters used to  pick the next token?
    
    How to think about attention; how attention creates a new represention of the 'context' to guide the next token selection? why people think about of as a continous look up?
    
    How to think about attention; how attention changes the context tokens; to guide next token selection?
    
    what multipole - parallel attention heads can do? does the output of each its meerge before it process by the upper layers?
    
    the representation captures a correlation between the token; or how it';s meaingn encded>?  or what is teh anture of the output represntatoin?
    
    the effectieness of this new rpresntation are based on ?
    
    What maeks this represntation computaitno via attention, so powerfull in basically encoding operators?
    
    Attention doesn’t just “correlate tokens”; it transforms them into functional representations.
    
    These representations are powerful because they can encode relationships, rules, and even operators, purely through learned, differentiable linear combinations + non-linear transformations.
    
    This is why Transformers can, e.g., add numbers, sort lists, or implement logic, even without being explicitly programmed to do so.
    
    How trasnfomers can learn operators?
    
    How can transfoerms synthetize many operators at one? That is being a universal system?
    
    dos the same attention head is able to encode many operators; or its a maximu  that they dan encode/
    
    Why is the Subword flexibility token representation relevant?
    
    - The magic frmo llm does not comes actually from the architecture or ideas in teh architecure - it comes from teh emernge that comes from huge data set used to trained; the more the better. there are a lot of phase changes, and tipping points.

## Formulation

> At a high level, **attention is a differentiable key–value retrieval mechanism**. (nop this is an interpretation not the core !!!)

> Query, Key, and Value are simply different learned linear views of the same input representation.

Given:

- (“What information do I contain?”) A set of **keys** $K \in \mathbb{R}^{m \times d_k}$
- (“What information am I looking for?”) A set of **queries** $Q \in \mathbb{R}^{n \times d_k}$
- ( “What do I pass forward if selected?”) A set of **values** $V \in \mathbb{R}^{m \times d_v}$

Attention computes:

- $\text{Attention}(Q, K, V) =
\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$

This implements:

1. **Similarity computation** ( $QK^T$ ) → pairwise compatibility between queries and keys.
2. **Normalization** Softmax → converts scores into a probability distribution.
3. **Weighted aggregation** Linear combination of values according to relevance.

## Type Space

> **Self-attention** is a clever trick that uses similarities between all pairs of inputs. This makes the network care about relationships between inputs, independently of their order (permutations equivariance / invariance). That's the real contribution of the **2017 transformer paper**.

| **Attention Type** | **Description** | **Use Cases** | **Formula (Simplified)** |
| --- | --- | --- | --- |
| **Dot-Product Attention** | Computes similarity using dot product between queries and keys. | Transformers, NLP | $\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}}) V$ |
| **Scaled Dot-Product Attention** | Same as dot-product but scales by $dk\sqrt{d_k}$ to prevent large values. | Transformers (e.g., GPT, BERT) | $\text{softmax}(\frac{QK^T}{\sqrt{d_k}}) V$ |
| **Additive (Bahdanau) Attention** | Uses a small neural network to compute attention scores. | Seq2Seq, Machine Translation | $e_{ij} = v^T \tanh(W_1 Q + W_2 K)$ |
| **Multiplicative (Luong) Attention** | Uses matrix multiplication instead of MLP scoring. | Seq2Seq, Speech Processing | $e_{ij} = Q K^T$ |
| **Self-Attention** | Each token attends to all other tokens in the sequence. | Transformers (e.g., GPT, BERT) | $\text{softmax}(QK^T) V$ |
| **Cross-Attention** | Queries come from one sequence, keys/values from another. | Vision-Language Models (e.g., CLIP, DALL-E) | $\text{softmax}(QK^T)V$ |
| **Multi-Head Attention** | Uses multiple attention heads in parallel. | All modern Transformers | $\text{Concat}(\text{head}_1, ..., \text{head}_h)W_O$ |
| **Sparse Attention** | Limits attention to a subset of tokens to reduce complexity. | Efficient Transformers (e.g., Longformer, BigBird) | Similar to dot-product but with sparsity patterns |
| **Global vs. Local Attention** | Global attends to all tokens, local to a window of nearby tokens. | Long Texts, Vision Transformers | Adaptive attention masks |
| **Axial Attention** | Splits attention across different axes (e.g., height/width in images). | Image Transformers (e.g., Axial-DeepLab) | Attention along independent axes |
| **Linear Attention** | Approximates softmax attention for efficiency. | Fast Transformers (e.g., Performer) | Uses kernel tricks for fast approximation |
| **Memory-Augmented Attention** | Stores past attention states to recall information later. | Meta-learning, Few-shot Learning | Stores past keys/values for retrieval |
| **Hierarchical Attention** | Applies attention at different levels (word, sentence, paragraph). | Document Classification | Multi-stage aggregation of attention weights |

## References

- http://bactra.org/notebooks/nn-attention-and-transformers.html
- https://growingswe.com/blog/microgpt
- [A Gentle Introduction to Transformers](https://alexsemendinger.github.io/transformers-gentle-introduction)
- Tsai, Y.-H. H., Bai, S., Yamada, M., Morency, L.-P., & Salakhutdinov, R. (2019). Transformer dissection: A unified understanding of Transformer’s attention via the lens of kernel. In Proceedings of EMNLP-IJCNLP 2019 (pp. 4344–4353). ACL Anthology paper
- Transformer (Transformer%203f35bea9676546abbc588911bfd83c41.md), Chain-of-thought (CoT) (Chain-of-thought%20(CoT)%2017fc0f5171ec8083b650de8675c4325e.md)
- https://en.wikipedia.org/wiki/Kernel_smoother
- Kenel Term Disambiguation.
