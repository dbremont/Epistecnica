---
tags: [ml, mechanism]
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

## Formulation

### What is this technical instance?

> Attention is a differentiable, content-addressed weighted read: each query is scored against every retained key, the scores are normalized into a convex combination, and the answer is the corresponding mixture of the values.

Given:

- **Keys** $K \in \mathbb{R}^{m \times d_k}$ — what each position advertises.
- **Queries** $Q \in \mathbb{R}^{n \times d_k}$ — what each position is looking for.
- **Values** $V \in \mathbb{R}^{m \times d_v}$ — what each position passes forward if it contributes.

Attention computes:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

This implements three operations:

1. **Similarity computation** ($QK^T$) — pairwise compatibility between every query and every key.
2. **Normalization** (softmax) — scores become non-negative weights summing to one.
3. **Weighted aggregation** — each output is a linear combination of the values.

$Q$, $K$, and $V$ are learned linear views of the same input representation: $Q = XW_Q$, $K = XW_K$, $V = XW_V$. Nothing in the mechanism assigns them meaning; training fits the projections so that dot products become useful similarities and mixtures become useful context.

> **Caution.** "Differentiable key–value retrieval" and "kernel smoothing" describe the functional form, not the identity. What makes it *attention* in machine learning is that $W_Q$, $W_K$, and $W_V$ are learned: the metric and the value space are fitted rather than given.

### What technical element type does this technical instance belong to?

**Attention belongs to the `Technical Mechanism` technical element type, readable as a `Constitutive Technique` and as a `Technical Element Set`.**

```text
Technical Mechanism
└── Attention (content-addressed weighted read)
    readable as Constitutive Technique (embodied in every transformer block)
    readable as Technical Element Set (the family of attention variants)
```

It is a mechanism because it is the logical arrangement through which a function — context-conditioned mixing — is produced. A variant *implements* the mechanism; a trained head *realizes* it; a block *embeds* it as a constitutive technique; a paper *specifies* it.

### Is the type of this `technical element instance` ambiguous?

Yes, and the ambiguity is between genuinely different technical elements:

- **Mechanism** — the weighted read itself: scoring, normalization, aggregation.
- **Constitutive Technique** — the technique embodied in the block that makes the architecture operate.
- **Element Set** — the family: self, cross, multi-head, sparse, linear, memory-augmented, and their relatives.
- **Operator** — the mathematical map, which is a property of the mechanism rather than a separate element.

The guide's default for a multi-typed instance is multi-root decomposition. This note takes the mechanism root, because the mechanism is what a reader can name, implement, and inspect; the technique and the family appear as branches instead of as rival roots. A reader concerned only with "what counts as attention" can read the `Technical Element Set` branch as a self-contained decomposition root.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one vendor-neutral attention mechanism — its principles, its scoring realizations, the parameters and interfaces that make it concrete, the family it belongs to, the techniques it embodies, and the evaluations that verify and validate it. Named papers and measured configuration values appear only as leaves.
>
> Stopping rule: a row is terminal when it names a concrete formula term, a measured configuration value, a named paper, or a named mechanism variant.
>
> Identity: the Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a variant *implements* the mechanism; a trained head *realizes* it; a block *embeds* it as a constitutive technique.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Mechanism` → Attention | Content-addressed weighted read: every query is scored against every retained key and answered with a convex mixture of the values. |
| `Technical Mechanism` → Attention → `Technical Principle` | Grouping: principles the mechanism obeys. |
| `Technical Mechanism` → Attention → `Technical Principle` → Every Retained Position Contributes | No exclusion by default: each key receives a weight. Masking is the only exclusion, and it constrains the read rather than performing it. |
| `Technical Mechanism` → Attention → `Technical Principle` → Content-Addressed Scoring | The score depends on the query–key pair, not on position or address. |
| `Technical Mechanism` → Attention → `Technical Principle` → Differentiable Aggregation | The output is a smooth function of the parameters, so both the metric and the value space are fitted end to end. |
| `Technical Mechanism` → Attention → `Technical Principle` → Order Independence Without Position | Pairwise scoring commutes with input order; sequence order must be injected elsewhere. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention | The reference realization: similarity, scaling, softmax, weighted read. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → Similarity Scoring | $QK^T$ — pairwise compatibility between every query and key. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → Score Scaling | Divide the scores by $\sqrt{d_k}$ so their variance stays near one as head width grows. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → Softmax Normalization | Map scores to non-negative weights summing to one over the retained keys. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → Weighted Aggregation | Return $\sum_i w_i v_i$ — always a mixture of values, never the selection of one. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Parameter` | Grouping: parameters of the scoring function. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Parameter` → Scale $\sqrt{d_k}$ | Variance-control factor fixed by the head width. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Interface` | Grouping: boundaries of the mechanism. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Interface` → Query-Key-Value Boundary | The three learned projections through which a position proposes, advertises, and offers content. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Constraint` | Grouping: bounds the mechanism operates under. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Constraint` → Causal Mask | Upper-triangular exclusion of future keys, so position $t$ reads only its prefix. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Constraint` → Quadratic Cost in Sequence Length | $O(n^2 \cdot d)$ time and memory for dense pairwise scoring. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Trade-off` | Grouping: tensions the mechanism resolves. |
| `Technical Mechanism` → Attention → Scaled Dot-Product Attention → `Technical Trade-off` → Exact Versus Approximate Scoring | Dense scoring preserves retrieval fidelity at quadratic cost; sparse and linear variants buy asymptotics at fidelity risk. |
| `Technical Mechanism` → Attention → Additive Attention | A small network scores each pair (Bahdanau). |
| `Technical Mechanism` → Attention → Additive Attention → `Technical Parameter` | Grouping: parameters of the alignment network. |
| `Technical Mechanism` → Attention → Additive Attention → `Technical Parameter` → Alignment Network Weights | The learned scoring network $W_1$, $W_2$, and $v$. |
| `Technical Mechanism` → Attention → Multi-Head Attention | $h$ parallel reads of the same sequence, concatenated and projected. |
| `Technical Mechanism` → Attention → Multi-Head Attention → `Technical Parameter` | Grouping: parameters of the head split. |
| `Technical Mechanism` → Attention → Multi-Head Attention → `Technical Parameter` → Head Count $h$ | Number of parallel reads. |
| `Technical Mechanism` → Attention → Multi-Head Attention → `Technical Parameter` → Per-Head Width $d_k = d_{model} / h$ | Width of each head's query and key projection. |
| `Technical Mechanism` → Attention → Multi-Head Attention → `Technical Interface` | Grouping: boundaries of the composition. |
| `Technical Mechanism` → Attention → Multi-Head Attention → `Technical Interface` → Head Concatenation and Output Projection | $\text{Concat}(\text{head}_1, \dots, \text{head}_h)W_O$ — rejoins the reads into one width-$d_{model}$ vector. |
| `Technical Mechanism` → Attention → `Technical Element Set` | Grouping: the family reading of attention. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set | The mechanisms that count as attention by lineage and function, not only by exact softmax form. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` | Grouping: members of the set, typed as mechanisms. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Self-Attention | Queries, keys, and values drawn from one sequence. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Cross-Attention | Queries from one sequence, keys and values from another. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Multi-Query Attention | One shared key/value projection across all query heads. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Grouped-Query Attention | Query heads partitioned into groups that share a key/value projection. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Sparse Attention | Fixed or learned sparsity patterns reduce the set of scored pairs. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Linear Attention | Kernel feature maps replace the softmax so scoring runs in linear time. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Memory-Augmented Attention | Keys and values stored from earlier context and re-read later. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Axial Attention | Independent attention along each image or tensor axis. |
| `Technical Mechanism` → Attention → `Technical Element Set` → Attention Variant Set → `Technical Mechanism` → Hierarchical Attention | Attention applied at successive levels, such as word, sentence, and paragraph. |
| `Technical Mechanism` → Attention → `Technical Practice` | Grouping: practice embodied in the mechanism. |
| `Technical Mechanism` → Attention → `Technical Practice` → `Constitutive Technique` | Grouping: techniques the mechanism embodies. |
| `Technical Mechanism` → Attention → `Technical Practice` → `Constitutive Technique` → Scaled Dot-Product Scoring | Similarity computation embodied in the mechanism. |
| `Technical Mechanism` → Attention → `Technical Practice` → `Constitutive Technique` → Softmax Normalization | Convex weighting across positions embodied in the mechanism. |
| `Technical Mechanism` → Attention → `Technical Practice` → `Constitutive Technique` → Convex Aggregation | Returning a mixture rather than a choice, embodied in the mechanism. |
| `Technical Mechanism` → Attention → `Technical Evaluation` | Grouping: determinations about the mechanism. |
| `Technical Mechanism` → Attention → `Technical Evaluation` → `Verification` | Grouping: conformance checks. |
| `Technical Mechanism` → Attention → `Technical Evaluation` → `Verification` → Attention-Mass Check | Every query's weights are non-negative and sum to one over the retained keys. |
| `Technical Mechanism` → Attention → `Technical Evaluation` → `Verification` → Shape and Mask Parity | Head widths, mask shape, and numerical parity against the reference implementation. |
| `Technical Mechanism` → Attention → `Technical Evaluation` → `Validation` | Grouping: adequacy checks. |
| `Technical Mechanism` → Attention → `Technical Evaluation` → `Validation` → Alignment Quality | Whether the weights align the positions they purport to relate, in translation and retrieval. |
| `Technical Mechanism` → Attention → `Technical Evaluation` → `Validation` → Downstream Task Metric | Whether the read improves the task the block serves. |

### What is a critical conceptual evaluation of this technical element instance?

> **Concept under evaluation:** *Attention*, under the precising definition declared above — a learned, content-addressed weighted read: score every query against every retained key, normalize the scores into a convex combination, and return the corresponding mixture of values. Criteria and ratings follow the *Philosophia Conceptuum et Operis*.

> **Verdict.** Attention is a mechanism concept with a precise core and a fuzzy perimeter. The formula is exact — score, normalize, mix — and everything inside it is measurable and inspectable. What the definition does not fix is where the concept stops: linear and kernel attention keep the function but change the normalization, sparse attention keeps the softmax but drops most pairs, and hard selection keeps the vocabulary but removes the mixture. Membership is settled by lineage, not by the definition.

> **Verdict.** The name is the weakest part. In psychology, attending means excluding — the unattended is dropped. Here nothing is dropped: every retained position keeps its key and receives a weight, and masking is a constraint on the read rather than an act of attention. Kernel smoothing is the closer neighbour in functional form, and the real difference is that the kernel is learned rather than given. The term survives because it is vivid, not because it is accurate, and every reader must supply the inversion.

> **Verdict.** The remedy is precising, not renaming. Take the declared definition — learned $W_Q$, $W_K$, $W_V$, softmax over retained keys, convex mixture of values — as the operative extension. Variants that keep the mixture qualify; hard selection and non-differentiable lookup are routing, close relatives that should be named as such. Under that definition the concept is Purpose-adequate as an implementation primitive and inadequate as an explanation of what a model does, which is why the circuit-level and capability-level questions belong to the transformer note rather than here.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Weak | One word names the operation, the family, the mathematical map, and the psychological namesake. Only the formula separates them, and the formula is narrower than the usage. |
| Definitional Clarity | Strong as an operation | The defining expression fixes the operation exactly: three steps, three projections, one normalization. |
| Conceptual Determinacy | Weak | No membership rule. Kernel or linear attention, hard top-k selection, routing by a learned gate, and a plain weighted average are all near the boundary, and lineage decides rather than the definition. |
| Definitional Completeness | Moderate | Necessary conditions are explicit; the exclusions are implicit. Nothing in the definition says that hard, non-differentiable selection is not attention. |
| Internal Consistency | Strong | The three steps are mutually compatible and jointly sufficient for the formula; no step presupposes a rival account. |
| Extensional Fidelity | Moderate | Canonical members are clean; leaks at linear and kernel variants, at hard attention, and at retrieval hybrids that share the functional form but not the softmax. |
| Intensional Adequacy | Moderate | The defining properties capture soft content-addressed mixing, but not what the field means by "attention" when it names a head, a block, or an architectural choice. |
| Ontological Adequacy | Strong as mechanism; weak when used for the technique or the family | The concept denotes a logical arrangement producing a function. Applied to the technique embodied in a block, or to the variant family, it names the wrong kind of element. |
| Discriminative Power | Moderate | Separates attention from convolution and recurrence; does not separate it from kernel smoothing or from soft retrieval, which share the functional form. |
| Granularity Adequacy | Moderate | The mechanism level is the right resolution for implementation and inspection; it is too coarse for "what does this head compute", which needs the circuit level. |
| Conceptual Distinctiveness | Moderate | Distinct from kernel smoothing by its learned metric and value space; distinct from retrieval by returning a mixture rather than an index; not distinct from psychological attention except by convention. |
| Boundary Differentiation | Weak against psychological attention and kernel smoothing | Psychological attention selects by exclusion; this keeps everything and reweights. Kernel smoothing averages, but with a fixed kernel; this learns the kernel through $W_Q$ and $W_K$. |
| Epistemic Leverage | High | The query–key–value vocabulary and the softmax read are the working primitives of mechanistic interpretability and of every efficiency technique. |
| Explanatory Power | Moderate | Explains how context is mixed and why the operation parallelizes; does not explain what a head computes or why a mixture helps at scale. |
| Falsifiability | Moderate | Attention-mass and ablation tests are checkable; "attention is the explanation of model behaviour" is not a claim the concept can carry. |
| Temporal Stability | Moderate | The referent widened from a softmax read to any content-addressed mix, and drifted into the name of the block that contains it. |
| Operationalizability | Strong | The formula is executable, the weights are inspectable, and membership in the canonical form is decidable mechanically. |
| Purpose Adequacy | Split | Adequate as a mechanism description and as an implementation primitive; inadequate as an explanation of capability or of model behaviour. |

## Type Space

> **Self-attention** is a clever trick that uses similarities between all pairs of inputs. This makes the network care about relationships between inputs, independently of their order (permutation equivariance / invariance). That's the real contribution of the **2017 transformer paper**.

| **Attention Type** | **Description** | **Use Cases** | **Formula (Simplified)** |
| --- | --- | --- | --- |
| **Dot-Product Attention** | Computes similarity using the dot product between queries and keys. | Transformers, NLP | $\text{softmax}(QK^T)V$ |
| **Scaled Dot-Product Attention** | Dot-product attention with the scores divided by $\sqrt{d_k}$ before the softmax. | Transformers (e.g., GPT, BERT) | $\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ |
| **Additive (Bahdanau) Attention** | Uses a small neural network to compute attention scores. | Seq2Seq, Machine Translation | $e_{ij} = v^T \tanh(W_1 q_i + W_2 k_j)$ |
| **Multiplicative (Luong) Attention** | Uses matrix multiplication instead of an MLP for scoring. | Seq2Seq, Speech Processing | $e_{ij} = q_i^T k_j$ |
| **Self-Attention** | Each token attends to all other tokens in the sequence. | Transformers (e.g., GPT, BERT) | $\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ |
| **Cross-Attention** | Queries come from one sequence, keys and values from another. | Vision-Language Models (e.g., CLIP, DALL-E) | $\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ |
| **Multi-Head Attention** | Uses multiple attention heads in parallel. | All modern Transformers | $\text{Concat}(\text{head}_1, \dots, \text{head}_h)W_O$ |
| **Sparse Attention** | Limits attention to a subset of tokens to reduce complexity. | Efficient Transformers (e.g., Longformer, BigBird) | Dot-product attention over a sparsity pattern |
| **Global vs. Local Attention** | Global attends to all tokens, local to a window of nearby tokens. | Long Texts, Vision Transformers | Attention with adaptive masks |
| **Axial Attention** | Splits attention across different axes (e.g., height and width in images). | Image Transformers (e.g., Axial-DeepLab) | Attention along independent axes |
| **Linear Attention** | Replaces the softmax with kernel feature maps for linear-time scoring. | Efficient Transformers (e.g., Performer) | $\phi(Q)(\phi(K)^T V)$ |
| **Memory-Augmented Attention** | Stores past keys and values to recall information later. | Meta-learning, Few-shot Learning | Attention over a stored key–value store |
| **Hierarchical Attention** | Applies attention at different levels (word, sentence, paragraph). | Document Classification | Multi-stage aggregation of attention weights |

## QA

### How does attention produce the next token?

> It does not. Attention produces a representation; the output head maps that representation to logits, softmax turns the logits into a distribution over the vocabulary, and sampling selects a token. Temperature changes how sharply the distribution is sampled, not whether the distribution exists. The distribution is context-dependent, and the vocabulary is fixed by the tokenizer.

### Is attention just kernel smoothing?

> In functional form, yes: a weighted average of values with weights that decay with distance in some space. In machine learning the difference is that the kernel is learned — $W_Q$ and $W_K$ fit the metric, $W_V$ fits what is averaged. Kernel smoothing fixes the kernel; attention fits it.

### What does each of $Q$, $K$, and $V$ bring?

> The query says what a position is looking for, the key says what a position advertises, and the value says what it passes forward if it contributes. All three are linear views of the same input, so the distinctions are functional, not structural.

### Are $W_Q$, $W_K$, and $W_V$ learned parameters or model state?

> Parameters. They are learned during training, shared across positions, and fixed at inference. $Q$, $K$, and $V$ are activations computed from them for a given input.

### Where do $Q$, $K$, and $V$ come from during inference?

> From the same learned projections applied to the prompt's token representations. The key–value cache stores the computed $K$ and $V$ per layer so they are not recomputed at each step; it does not introduce a different mechanism.

### What is the role of training in shaping $Q$, $K$, and $V$?

> Training fits the projections so that dot products become useful similarities and the resulting mixtures become useful context for the objective. Nothing in the mechanism assigns meaning to a key or a value; the meaning, if any, is whatever the objective made useful.

### What do multiple heads do, and how are they merged?

> Each head reads the sequence with its own projections, so the heads can specialize. Their outputs are concatenated and projected by $W_O$ into one width-$d_{model}$ vector, and that single vector is what the residual stream carries forward.

### Why is attention described as a continuous lookup?

> Because the weights are soft: the output is a convex mixture of all retained values rather than the value at one index. The mixture is differentiable with respect to the query, which is what lets the lookup be learned end to end.

### Can a single head encode several operators?

> A head has finite capacity, but mechanistic work finds heads composing into operators — copying, induction, simple arithmetic — and finds features distributed across heads rather than cleanly partitioned. The honest answer is that a head can participate in several operators and that the circuit, not the head, is the right unit.

### Does the capability come from the architecture or from the data?

> The architecture fixes what is learnable and at what cost; data and scale determine what is actually learned. Attention makes context-mixing parallel and differentiable, which permits scale; it does not by itself produce capability. This remains an open question rather than a settled one.

## References

- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) — the schema and decomposition contract this note follows.
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) — the evaluation criteria applied above.
- [Transformer System](note.html?n=technica/ais/system/transformer/transformer.md) — the architecture this mechanism is embedded in.
- [Transformer System: Training](note.html?n=technica/ais/system/transformer/transformer-system-training.md) — how the projections are fitted.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*, 5998–6008. https://arxiv.org/abs/1706.03762
- Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. *International Conference on Learning Representations*. https://arxiv.org/abs/1409.0473
- Tsai, Y.-H. H., Bai, S., Yamada, M., Morency, L.-P., & Salakhutdinov, R. (2019). Transformer dissection: A unified understanding of Transformer's attention via the lens of kernel. In *Proceedings of EMNLP-IJCNLP 2019* (pp. 4344–4353). https://aclanthology.org/D19-1443/
- [A Gentle Introduction to Transformers](https://alexsemendinger.github.io/transformers-gentle-introduction) — worked introduction to the mechanism.
- [MicroGPT](https://growingswe.com/blog/microgpt) — minimal implementation walkthrough.
- [Attention and Transformers notebooks](http://bactra.org/notebooks/nn-attention-and-transformers.html) — dated reading notes with provenance.
- [Kernel smoother](https://en.wikipedia.org/wiki/Kernel_smoother) — the fixed-kernel neighbour attention resembles.
- Britz, D., Goldie, A., Luong, M.-T., & Le, Q. V. (2017). Massive exploration of neural machine translation architectures. In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing* (pp. 1442–1451). Association for Computational Linguistics. [ACL Anthology](https://doi.org/10.18653/v1/D17-1151)
- Cheng, J., Dong, L., & Lapata, M. (2016). Long short-term memory-networks for machine reading. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing* (pp. 551–561). Association for Computational Linguistics. [ACL Anthology](https://doi.org/10.18653/v1/D16-1053)
- Graves, A., Wayne, G., & Danihelka, I. (2014). *Neural Turing machines*. arXiv. [arXiv:1410.5401](https://arxiv.org/abs/1410.5401)
- Graves, A., Wayne, G., Reynolds, M., Harley, T., Danihelka, I., Grabska-Barwińska, A., ... Hassabis, D. (2016). Hybrid computing using a neural network with dynamic external memory. *Nature, 538*(7626), 471–476. [Nature](https://doi.org/10.1038/nature20101)
- Lin, Z., Feng, M., Santos, C. N. dos, Yu, M., Xiang, B., Zhou, B., & Bengio, Y. (2017). A structured self-attentive sentence embedding. In *Proceedings of the 5th International Conference on Learning Representations* (ICLR 2017). [arXiv:1703.03130](https://arxiv.org/abs/1703.03130)
- Luong, T., Pham, H., & Manning, C. D. (2015). Effective approaches to attention-based neural machine translation. In *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing* (pp. 1412–1421). Association for Computational Linguistics. [ACL Anthology](https://doi.org/10.18653/v1/D15-1166)
- Nadaraya, E. A. (1964). On estimating regression. *Theory of Probability & Its Applications, 9*(1), 141–142. [SIAM](https://doi.org/10.1137/1109020)
- Parikh, A. P., Täckström, O., Das, D., & Uszkoreit, J. (2016). A decomposable attention model for natural language inference. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing* (pp. 2249–2255). Association for Computational Linguistics. [ACL Anthology](https://doi.org/10.18653/v1/D16-1244)
- Sukhbaatar, S., Szlam, A., Weston, J., & Fergus, R. (2015). End-to-end memory networks. In *Advances in Neural Information Processing Systems* (Vol. 28, pp. 2440–2448). Curran Associates. [arXiv:1503.08895](https://arxiv.org/abs/1503.08895)
- Watson, G. S. (1964). Smooth regression analysis. *Sankhyā: The Indian Journal of Statistics, Series A, 26*(4), 359–372. [JSTOR](http://www.jstor.org/stable/25049340)
- Watson, J. B. (1913). Psychology as the behaviorist views it. *Psychological Review, 20*(2), 158–177. [APA PsycNet DOI](https://doi.org/10.1037/h0074428)
- Brauwers, G., & Frasincar, F. (2023). A general survey on attention mechanisms in deep learning. *IEEE Transactions on Knowledge and Data Engineering, 35*(4), 3279–3298. https://doi.org/10.1109/TKDE.2021.3126456
- Bricken, T., & Pehlevan, C. (2021). Attention approximates sparse distributed memory. In *Advances in Neural Information Processing Systems* (Vol. 34).
- Chaudhari, S., Mithal, V., Polatkan, G., & Ramanath, R. (2021). An attentive survey of attention models. *ACM Transactions on Intelligent Systems and Technology, 12*(5), Article 53. https://doi.org/10.1145/3465055
- Choromanski, K., Likhosherstov, D., Dohan, D., Song, X., Gane, A., Sarlos, T., Hawkins, P., Davis, J., Mohiuddin, A., Kaiser, Ł., Belanger, D. B., Colwell, L., & Weller, A. (2021). Rethinking attention with Performers. In *International Conference on Learning Representations (ICLR 2021)*. https://arxiv.org/abs/2009.14794
- Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022). FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In *Advances in Neural Information Processing Systems* (Vol. 35). https://arxiv.org/abs/2205.14135
- Dong, Y., Cordonnier, J.-B., & Loukas, A. (2021). Attention is not all you need: Pure attention loses rank doubly exponentially with depth. In *Proceedings of the 38th International Conference on Machine Learning* (pp. 2793–2803). PMLR. https://proceedings.mlr.press/v139/dong21a.html
- Galassi, A., Lippi, M., & Torroni, P. (2021). Attention in natural language processing. *IEEE Transactions on Neural Networks and Learning Systems, 32*(10), 4291–4308. https://doi.org/10.1109/TNNLS.2020.3019893
- Jain, S., & Wallace, B. C. (2019). Attention is not explanation. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)* (pp. 3543–3556). Association for Computational Linguistics. https://doi.org/10.18653/v1/N19-1357
- Katharopoulos, A., Vyas, A., Pappas, N., & Fleuret, F. (2020). Transformers are RNNs: Fast autoregressive Transformers with linear attention. In *Proceedings of the 37th International Conference on Machine Learning* (pp. 5156–5165). PMLR. https://proceedings.mlr.press/v119/katharopoulos20a.html
- Shaw, P., Uszkoreit, J., & Vaswani, A. (2018). Self-attention with relative position representations. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)* (pp. 464–468). Association for Computational Linguistics. https://doi.org/10.18653/v1/N18-2074
- Vinyals, O., Fortunato, M., & Jaitly, N. (2015). Pointer networks. In *Advances in Neural Information Processing Systems* (Vol. 28).
- Wiegreffe, S., & Pinter, Y. (2019). Attention is not not explanation. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing* (pp. 11–20). Association for Computational Linguistics. https://doi.org/10.18653/v1/D19-1002
- Xu, K., Ba, J., Kiros, R., Cho, K., Courville, A., Salakhutdinov, R., Zemel, R., & Bengio, Y. (2015). Show, attend and tell: Neural image caption generation with visual attention. In *Proceedings of the 32nd International Conference on Machine Learning* (pp. 2048–2057). PMLR. https://proceedings.mlr.press/v37/xuc15.html
