---
tags: [learning-system, architectural-style]
qa:
  - Why does the 2017 paper's real claim concern permutation equivariance and parallelism rather than "attention" itself?
  - Why scale the dot product by √d_k rather than by d_k or not at all?
  - What does each positional-encoding scheme (sinusoidal, learned, rotary, additive bias) inject that recurrence supplied for free?
  - What changes mechanistically between pre-layer-norm and post-layer-norm placement?
  - Why has exact quadratic attention survived a decade of efficiency work, and what did FlashAttention change?
  - Does the architecture explain emergent capability, or do data and scale do the work?
  - Multi-head, multi-query, and grouped-query attention: compression, regularisation, or both?
  - What actually travels in the residual stream, and how do heads read from and write to it?
  - Why did encoder-only, decoder-only, and encoder–decoder designs diverge, and what does each buy?
  - What would a post-transformer architecture have to beat in order to displace attention?
---

# Transformer System

> A **Transformer** is a sequence-processing architecture built from uniformly repeated blocks of multi-head self-attention and position-wise feed-forward networks, bound by residual connections and layer normalization, with positional information injected into the input rather than carried by recurrence. It was introduced by Vaswani et al. in *Attention Is All You Need* (2017).

**Disambiguation.** Four things travel under one name and must not be conflated. 

- **Attention** is a mechanism — a learnt, content-addressed weighted read over a key–value store in which every retained position contributes. This inverts the psychological sense of the word: attending there means dropping the unattended, while here nothing is dropped and only masking excludes. The name is a misnomer the field kept.
- The **transformer** is an architecture — how those mechanisms are stacked, ordered, and bound.
- A **BERT/GPT/T5 model** is a trained object realizing that architecture.
- An **LLM** is a capability class usually, though not necessarily, reached through a transformer. This note characterizes the architecture together with the system that produces and serves models from it.

## Formulation

### What is this technical instance?

> The Transformer system is the arrangement — plus the training, control, and serving apparatus — that turns token sequences into contextual representations and continuations. Its operative core is a stack of identical blocks: each routes every position's representation through a multi-head self-attention sublayer and then through a position-wise feed-forward sublayer, each wrapped in a residual connection and a normalization. Order enters only through an injected positional signal, or through a rotary or relative substitute for one. The 2017 encoder–decoder binding is the reference configuration: six encoder and six decoder layers, eight heads, 512-dimensional model width, 2048-dimensional feed-forward width, trained with Adam under a warmup schedule on translation.

### How to think about the 'Transformer'?

- **Process:**  `Context (Initial Condition) → Context Extension & Verification → Unfolding (Next Token) → Context Extension & Verification → Further Unfolding Until Stop`.
- **Mechanism:** Successive context-conditioned computations, with each generated token extending the context for subsequent predictions.
- **Central question:** How does the system exploit regularities in the current context to unfold a trajectory of continuations?
- **Note:** Modern systems involve substantially more engineering, including dedicated memory mechanisms, tool use, verification, and other supporting capabilities.

### What technical element type does this technical instance belong to?

**The Transformer belongs to the `Production Technical System` technical element type, readable as a `Technical Architecture` and as a `Technical Element Set`.**

```text
Production Technical System
└── Transformer System (architecture + trained model + training and serving apparatus)
    readable as Technical Architecture (the 2017 block design)
    readable as Technical Element Set (model family + tooling + practices)
```

It is a system because it is an organized composition of a block architecture, a trained model object with concrete parts and parameters, a training practice that reaches down to individual acts, an inference apparatus with its own interfaces, evaluations that verify and validate the result, and an evolutionary trajectory — all cooperating to realize one capability: sequence transduction. A framework *implements* the architecture's mechanisms; a checkpoint *realizes* the architecture; a deployment *instantiates* the system; the 2017 paper *specifies* it.

### Is the type of this `technical element instance` ambiguous?

Yes, and the ambiguity is not loose vocabulary — the same word names five genuinely different technical elements:

- **Architecture** — the structural organization of blocks, projections, and residual paths introduced in 2017.
- **Blueprint** — the paper and reference implementation that let anyone regenerate such a system.
- **Object** — a trained checkpoint: tensors, buffers, and configuration.
- **Technique** — the practice of pretraining, adapting, and serving it.
- **System** — the organized set that binds all of the above into one capability.

The guide's default for a multi-typed instance is multi-root decomposition, one root per candidate type. This note takes the system root, because the title, the corpus location, and the content all span training, control, and realization rather than the design alone; the architecture appears as a subtree instead of as a second table. A reader concerned only with "what the 2017 design is" can read the `Technical Architecture` branch as a self-contained decomposition root.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one vendor-neutral transformer system — the architecture, its reference binding, the mechanisms and parameters that make it concrete, the practices that train and serve it, and the evaluations that verify and validate it. Named models, repositories, and measured configuration values appear only as leaves.
>
> Stopping rule: a row is terminal when it names a concrete formula term, a measured configuration value, a named repository, a named model, or a named actor.
>
> Identity: the Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a framework *implements* the architecture; a trained checkpoint *realizes* it; a deployment *instantiates* the system; the paper *specifies* it.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Transformer System | Vendor-neutral sequence-processing system: architecture, trained model, training and serving apparatus. |
| `Production Technical System` → Transformer System → `Technical Architecture` | Grouping: the structural organization the system is built from. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture | Uniform repeated blocks of multi-head self-attention plus position-wise feed-forward; no recurrence; order injected. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Principle` | Grouping: principles the architecture obeys. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Principle` → Uniform Block Repetition | One block shape repeated N times, making depth a parameter rather than a design variable. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Principle` → Permutation Equivariance | Without a positional signal the block commutes with input order; the design's claim is relational, not sequential. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Principle` → Parallelism Over Positions | Every position is computed simultaneously during training; the serial dependency of recurrence disappears. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Principle` → Residual Stream With Normalization | Every sublayer reads and adds to one shared width-d_model channel, keeping gradient paths short in depth. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Configuration` | Grouping: configuration choices that define an architecture variant. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Configuration` → Layer-Norm Placement | Normalize before each sublayer (pre-LN) or after the residual addition (post-LN). |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Configuration` → Positional Signal Scheme | Sinusoidal, learnt absolute, rotary, or additive-bias encoding of position. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Configuration` → Head Split | Number of heads h and per-head width d_k = d_model / h. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Configuration` → Decoder Masking Policy | Causal mask, fully bidirectional attention, or hybrid prefix masking. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Configuration` → Attention Read Pattern | Self-attention, cross-attention, or multi-query and grouped-query key sharing. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Trade-off` | Grouping: tensions the design resolves. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Trade-off` → Bidirectional Versus Causal Context | Reading both sides of a token buys representation, but forbids autoregressive generation. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Trade-off` → Exact Versus Approximate Attention | Dense attention preserves retrieval fidelity at quadratic cost; sparsity buys context at accuracy risk. |
| `Production Technical System` → Transformer System → `Technical Architecture` → Attention-Based Sequence Architecture → `Technical Trade-off` → Training Parallelism Versus Inference Memory | Parallel training admits long sequences; KV-cache growth makes long-context inference memory-bound. |
| `Production Technical System` → Transformer System → `Production Technical Object` | Grouping: production objects realizing the system. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model | Vendor-neutral trained model object; checkpoints and deployments realize it. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` | Grouping: parts constituting the model. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack | N stacked bidirectional blocks producing contextual representations. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` | Grouping: parts constituting the stack. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer | h parallel attention heads over the same sequence, concatenated and projected. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Mechanism` | Grouping: mechanisms the sublayer executes. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Mechanism` → Scaled Dot-Product Attention | softmax(QKᵀ/√d_k)·V — similarity, normalization, weighted read. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Mechanism` → Scaled Dot-Product Attention → `Technical Parameter` | Grouping: parameters of the scoring function. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Mechanism` → Scaled Dot-Product Attention → `Technical Parameter` → Scaling Factor √d_k | Keeps score variance near one so the softmax does not saturate. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Interface` | Grouping: interfaces of the attention sublayer. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Interface` → Query-Key-Value Boundary | The three learnt projections through which a position proposes, advertises, and offers content. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Parameter` | Grouping: parameters of the attention sublayer. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Multi-Head Self-Attention Sublayer → `Technical Parameter` → Head Count h = 8 | Eight heads of width 64 (exemplar, base configuration). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Position-Wise Feed-Forward Sublayer | Two linear maps with a nonlinearity, applied identically at every position. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Position-Wise Feed-Forward Sublayer → `Technical Parameter` | Grouping: parameters of the feed-forward sublayer. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Position-Wise Feed-Forward Sublayer → `Technical Parameter` → Inner Width d_ff = 2048 | Four times the model width (exemplar, base configuration). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Encoder Stack → `Constitutive Technical Object` → Add-Normalize Wrapper | Add-and-normalize wrapper around every sublayer. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Decoder Stack | N stacked causal blocks with cross-attention onto the encoder output. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Token Embedding | Lookup from vocabulary ids into width-d_model vectors, scaled by √d_model. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Positional Encoding | Sinusoidal signal added to embeddings so that order becomes addressable. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Constitutive Technical Object` → Output Head | Linear map to vocabulary logits, normalized into a next-token distribution. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` | Grouping: parameters of the model. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Model Width d_model = 512 | Residual-stream and embedding width (exemplar, base configuration). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Stack Depth N = 6 | Number of identical blocks in each stack (exemplar, base configuration). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Per-Head Width d_k = d_v = 64 | Width of each head's key and value projection (exemplar, base configuration). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Dropout Rate 0.1 | Regularization applied to sublayer outputs and embeddings (exemplar value). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Label Smoothing 0.1 | Softens targets during training (exemplar value). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Context Length | Maximum number of positions the positional scheme and attention span admit (exemplar per model). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Parameter Count | Total trainable tensors across embeddings, blocks, and output projection (exemplar per model). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Parameter` → Training Compute 6ND | Forward and backward FLOPs for N parameters over D training tokens (exemplar per run). |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Constraint` | Grouping: bounds the model operates under. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Constraint` → Quadratic Attention Cost | O(n²·d) time and memory in sequence length for dense attention. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Constraint` → Fixed Context Window | Attention spans a bounded position range fixed at training time. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Constraint` → No Native Recurrent State | No hidden state carried between calls; a key–value cache substitutes for it. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Capability` | Grouping: capabilities the model realizes. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Capability` → Sequence Transduction | Maps an input sequence to an output sequence across vocabularies and modalities. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Capability` → In-Context Retrieval | Pulls facts placed in the prompt without weight updates. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Capability` → Transfer From Pretraining | Reaches downstream tasks by adaptation rather than training from scratch. |
| `Production Technical System` → Transformer System → `Production Technical Object` → Transformer Model → `Technical Capability` → Parallel Training | Trains on all positions of a sequence at once rather than step by step. |
| `Production Technical System` → Transformer System → `Technical Blueprint` | Grouping: generative descriptions of the system. |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) | Paper specifying block structure, hyperparameters, and training recipe. |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` | Grouping: specifications the paper states. |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` → Base Configuration Table | Table 3 of the paper: N=6, d_model=512, h=8, d_ff=2048, dropout 0.1. |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` → Base Configuration Table → `Technical Parameter` | Grouping: measured training settings of the base run. |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` → Base Configuration Table → `Technical Parameter` → Training Steps 100,000 | Scheduling horizon for the base run (exemplar). |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` → Base Configuration Table → `Technical Parameter` → Batch 25,000 Tokens | Token budget per optimizer step (exemplar). |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` → Base Configuration Table → `Technical Parameter` → Warmup 4,000 Steps | Linear warmup before inverse-square-root decay (exemplar). |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Technical Specification` → Base Configuration Table → `Technical Parameter` → Adam β2 0.98 | Second-moment decay chosen for stability at high learning rate (exemplar). |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Production Technical Object` | Grouping: production objects shipped with the paper. |
| `Production Technical System` → Transformer System → `Technical Blueprint` → Attention Is All You Need (2017) → `Production Technical Object` → Tensor2Tensor Reference Implementation | Reference codebase that regenerates the specified system. |
| `Production Technical System` → Transformer System → `Technical Practice` | Grouping: practices that produce and operate the system. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice | Repeatable practice: pretrain, adapt, and serve a model. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` | Grouping: tasks the practice decomposes into. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining | Objective-driven training over a large corpus; produces the base model. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` | Grouping: generalized methods used for the task. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction | Causal modelling: predict position t+1 from its prefix. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Masked Token Prediction | Bidirectional modelling: reconstruct masked positions from context. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Span Corruption | Span corruption: reconstruct a target sequence from a corrupted source. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` | Grouping: situated methods applied when running the technique. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → AdamW Schedule | Optimizer and schedule that keep large-batch training stable. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → Mixed-Precision Training | Low-precision compute with high-precision master weights. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → Gradient Accumulation | Emulates a large batch under a fixed memory budget. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → Sequence Packing | Concatenates short sequences so the context is fully used. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → AdamW Schedule → `Technical Act` | Grouping: acts performed under the optimizer technique. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → AdamW Schedule → `Technical Act` → Forward Pass | Computes logits and loss for one batch. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → AdamW Schedule → `Technical Act` → Backward Pass | Reverse-mode differentiation through the block stack. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Pretraining → `General Technique` → Next-Token Prediction → `Operative Technique` → AdamW Schedule → `Technical Act` → Optimizer Step | Updates weights, advances the schedule, and increments the step counter. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Fine-Tuning | Adapts base weights to instructions, preferences, or a target task. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Technical Task` → Inference Serving | Autoregressive decoding with caching, batching, and sampling. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Constitutive Technique` | Grouping: techniques embodied in the architecture itself. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Constitutive Technique` → Scaled Dot-Product Scoring | Similarity computation embodied in the attention mechanism. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Constitutive Technique` → Softmax Normalization | Convex weighting across positions embodied in the mechanism. |
| `Production Technical System` → Transformer System → `Technical Practice` → Transformer Training Practice → `Constitutive Technique` → Residual Accumulation | Additive state update embodied in every block. |
| `Production Technical System` → Transformer System → `Technical Interface` | Grouping: boundaries through which the system exchanges information. |
| `Production Technical System` → Transformer System → `Technical Interface` → Tokenizer Boundary | Text-to-id boundary: vocabulary, merge rules, special tokens. |
| `Production Technical System` → Transformer System → `Technical Interface` → Query-Key-Value Boundary | The learnt projections through which positions exchange content. |
| `Production Technical System` → Transformer System → `Technical Interface` → KV-Cache Boundary | Cached keys and values exchanged at each decoding step. |
| `Production Technical System` → Transformer System → `Technical Interface` → Logits Boundary | Vocabulary distribution exposed to sampling and to callers. |
| `Production Technical System` → Transformer System → `Technical Evaluation` | Grouping: determinations of conformance and adequacy. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Verification` | Grouping: conformance evaluations. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Verification` → Shape Parity Checks | Dimensions, masking, and numerical parity against the reference implementation. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Validation` | Grouping: adequacy evaluations. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Validation` → Perplexity | Held-out likelihood under the training objective. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Validation` → BLEU | Translation quality — the 2017 headline metric. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Validation` → GLUE | Sentence-level understanding suite. |
| `Production Technical System` → Transformer System → `Technical Evaluation` → `Validation` → SQuAD | Extractive question answering. |
| `Production Technical System` → Transformer System → `Technical Evolution` | Grouping: the trajectory that produced and succeeded the design. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Recurrent Encoder-Decoder | Fixed-state sequence transduction before attention. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Additive Attention | Alignment weights over encoder states: the first content-based read. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Self-Attention Architecture | 2017 removal of recurrence and convolution. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Encoder-Only Pretraining | BERT: bidirectional masked pretraining, adaptation by fine-tuning. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Decoder-Only Scaling | GPT line: parameter and data scale as the capability lever. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Efficient Attention | Sparse, linear, and IO-aware exact attention. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Long-Context Extension | Rotary scaling, additive biases, and position interpolation. |
| `Production Technical System` → Transformer System → `Technical Evolution` → Sparse Mixture State-Space Hybrids | Conditional computation and post-attention sequence models. |
| `Production Technical System` → Transformer System → `Technical Element Set` | Grouping: the family of architectures and model objects implementing the design. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set | Encoder-only, decoder-only, encoder–decoder, and vision bindings of one design. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` | Grouping: model objects realizing the family. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Encoder-Only Model | Bidirectional encoder pretrained by masking; adapts by fine-tuning. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Encoder-Only Model → BERT-Base | Exemplar: 12 layers, 768 width, 110M parameters. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Decoder-Only Model | Causal decoder trained by next-token prediction; generates autoregressively. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Decoder-Only Model → GPT-3 175B | Exemplar: 96 layers, 12,288 width, 175B parameters. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Encoder-Decoder Model | Text-to-text binding: encoder context, causal decoder with cross-attention. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Encoder-Decoder Model → T5-11B | Exemplar: 24 encoder and 24 decoder layers, span-corruption objective. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Vision Transformer | Patch embedding feeding an encoder stack; images as token sequences. |
| `Production Technical System` → Transformer System → `Technical Element Set` → Transformer Family Set → `Production Technical Object` → Vision Transformer → ViT-B/16 | Exemplar: 12 layers, 768 width, 16×16 patches. |

### What is a critical conceptual evaluation of this technical element instance?

> **Concept under evaluation:** *Transformer*, under the precising definition declared above — uniformly repeated blocks of multi-head self-attention and position-wise feed-forward layers, bound by residual connections and normalization, with no recurrence and with position injected rather than carried. Criteria and ratings follow the *Philosophia Conceptuum et Operis*.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Weak | One word carries five elements — architecture, blueprint, trained object, technique, system — and its neighbours (*attention*, *LLM*, *foundation model*) are separated by convention, not by stated criteria. See **Disambiguation**. |
| Definitional Clarity | Moderate | The block conditions are precise enough to check mechanically; what falls outside them is left to context. |
| Conceptual Determinacy | Weak | No membership rule. Kernel attention, a hybrid with two attention layers in twelve, a sparse mixture, and a single self-attention block are all undecided by the definition. |
| Internal Consistency | Strong | Attention, feed-forward, residual, and normalization conditions are mutually compatible; "no native recurrent state" follows from the block rather than competing with it. |
| Extensional Fidelity | Moderate | Clean at the canonical members (BERT, GPT, T5, ViT); leaks at hybrids, mixture-of-experts variants, and retrieval-augmented systems that keep the name without the block. |
| Intensional Adequacy | Moderate | The defining properties capture the 2017 design exactly, and nothing about what later made the family capable — outside the concept's job, inside the reader's expectation. |
| Ontological Adequacy | Strong as architecture; category error otherwise | The concept denotes a design schema, a class of artifacts. Applied to a checkpoint, a deployment, or a capability it names the wrong kind of entity. |
| Discriminative Power | Weak at the LLM boundary | Separates the transformer from recurrent and convolutional sequence models; does not separate it from *LLM* or *foundation model* in current usage. |
| Granularity Adequacy | Weak | The root aggregates encoder-only, decoder-only, encoder–decoder, vision, and hybrid bindings; the `Transformer Family Set` exists to recover distinctions a capability claim depends on. |
| Conceptual Distinctiveness | Moderate | Distinct from *attention* in content but not in name: the mechanism is content-addressed aggregation, not selective filtering. Redundant with *LLM* in ordinary speech. |
| Boundary Differentiation | Weak against the neighbouring concept of attention | The word is borrowed from psychological attention, whose defining property is selection by exclusion — the unattended is dropped. The operation drops nothing: a convex softmax read in which every retained position keeps its key and receives a weight. Masking is the only exclusion, and it is a constraint on the read, not an act of attending. |
| Epistemic Leverage | High | Supplies the vocabulary later work reasons with: residual stream, head, depth, context, key–value cache. |
| Explanatory Power | Moderate | Explains parallel training at bounded cost; does not explain capability at scale, which runs through data, objective, and optimization. |
| Falsifiability | Strong for the 2017 claim; weak for capability | Permutation equivariance and the absence of recurrence are testable; "transformer scaling explains capability" is not a claim the concept can carry. |
| Temporal Stability | Weak | The referent drifted from a 2017 translation encoder–decoder to a decoder-only hybrid family while the word stayed fixed, concealing the change. |
| Operationalizability | Strong in the laboratory; weak in discourse | Sublayer count, mask shape, and position-injection site decide membership mechanically; ordinary usage is not decidable at all. |
| Purpose Adequacy | Split | Adequate for engineering description and cost reasoning; inadequate for capability claims, and for policy discourse where the word stands in for *AI*. |

> **Verdict.** *Transformer* is a prototype-structured concept, not a natural kind. It has no necessary and sufficient conditions as used; it has a prototype — the 2017 post-norm encoder–decoder block — around which membership grades. What the concept buys is anatomical and fiscal rather than predictive: it names the parts later work reasons with (residual stream, head, depth, context, key–value cache) and licenses cost inference (6ND training FLOPs, quadratic attention, linear cache growth). On Epistemic Leverage and Information Compression it scores high; on Inferential Productivity it splits sharply — strong for cost, nearly empty for capability.

> **Verdict.** Determinacy fails exactly where it matters. The concept cannot decide from its own definition whether linear or kernel attention, a twelve-layer stack carrying two attention layers, or a sparse mixture qualifies; membership is settled by lineage and convention, and the field advances by departing from the prototype. That is not a defect a better definition repairs — the boundary is where the work is. The naming compounds it: *attention* imports a psychological concept defined by exclusion, while the operation retains everything and merely reweights, so the reader must supply the inversion on every use. The same instability is temporal: the 2017 referent was a translation encoder–decoder, the current one a decoder-only hybrid family, and the fixed word conceals the drift.

> **Verdict.** The remedy is the guide's own instrument: precising, not abandoning. The architecture reading declared in the Formulation is the operative definition, and the reader should take it as the extension of *this* note. *Model*, *LLM*, and *system* are separate concepts, not further readings of this one — the decomposition keeps them apart under `Production Technical Object`, `Technical Practice`, and the system root. Under that definition the concept is Purpose-adequate for engineering description and cost reasoning, and inadequate as an explanation of capability; the residual accordingly sits in the `Technical Evolution`, `Technical Practice`, and `Technical Evaluation` branches, not in the architecture.

## QA

### What is the historical lineage of the Transformer architecture?

> Lineage: recurrent encoder–decoder translation (Sutskever et al., 2014) → additive attention over encoder states (Bahdanau et al., 2015) → self-attention with no recurrence at all (Vaswani et al., 2017) → pretrained encoders (BERT, 2018), decoder-only scaling (GPT, 2018–2020), text-to-text unification (T5, 2020), and vision adaptation (ViT, 2020).

## References

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*, 5998–6008. https://arxiv.org/abs/1706.03762
- [Attention Is All You Need — NeurIPS proceedings](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. *International Conference on Learning Representations*. https://arxiv.org/abs/1409.0473
- Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to sequence learning with neural networks. *Advances in Neural Information Processing Systems, 27*. https://arxiv.org/abs/1409.3215
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL-HLT*, 4171–4186. https://arxiv.org/abs/1810.04805
- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems, 33*. https://arxiv.org/abs/2005.14165
- Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., & Liu, P. J. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research, 21*(140), 1–67. https://arxiv.org/abs/1910.10683
- Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. *International Conference on Learning Representations*. https://arxiv.org/abs/2010.11929
- Dehghani, M., Gouws, S., Vinyals, O., Uszkoreit, J., & Kaiser, Ł. (2019). Universal transformers. *International Conference on Learning Representations*. https://arxiv.org/abs/1807.03819
- Su, J., Lu, Y., Pan, S., Murtadha, A., Wen, B., & Liu, Y. (2024). RoFormer: Enhanced transformer with rotary position embedding. *Neurocomputing, 568*. https://arxiv.org/abs/2104.09864
- Press, O., Smith, N. A., & Lewis, M. (2022). Train short, test long: Attention with linear biases enables input length extrapolation. *International Conference on Learning Representations*. https://arxiv.org/abs/2108.12409
- Shazeer, N. (2019). Fast transformer decoding: One write-head is all you need. *arXiv*. https://arxiv.org/abs/1911.02150
- Ainslie, J., Lee-Thorp, J., de Jong, Z., Zemlyanskiy, Y., Lebrón, F., & Sanghai, S. (2023). GQA: Training generalized multi-query transformer models from multi-head checkpoints. *EMNLP*. https://arxiv.org/abs/2305.13245
- Child, R., Gray, S., Radford, A., & Sutskever, I. (2019). Generating long sequences with sparse transformers. *arXiv*. https://arxiv.org/abs/1904.10509
- Beltagy, I., Peters, M. E., & Cohan, A. (2020). Longformer: The long-document transformer. *arXiv*. https://arxiv.org/abs/2004.05150
- Katharopoulos, A., Vyas, A., Pappas, N., & Fleuret, F. (2020). Transformers are RNNs: Fast autoregressive transformers with linear attention. *International Conference on Machine Learning*. https://arxiv.org/abs/2006.16236
- Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022). FlashAttention: Fast and memory-efficient exact attention with IO-awareness. *Advances in Neural Information Processing Systems, 35*. https://arxiv.org/abs/2205.14135
- Xiong, R., Yang, Y., He, D., Zheng, K., Zheng, S., Xing, C., Zhang, H., Lan, Y., Wang, L., & Liu, T.-Y. (2020). On layer normalization in the transformer architecture. *International Conference on Machine Learning*. https://arxiv.org/abs/2002.04745
- Zhang, B., & Sennrich, R. (2019). Root mean square layer normalization. *Advances in Neural Information Processing Systems, 32*. https://arxiv.org/abs/1910.07467
- Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). Scaling laws for neural language models. *arXiv*. https://arxiv.org/abs/2001.08361
- Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., Casas, D. de L., Hendricks, L. A., Welbl, J., Clark, A., et al. (2022). Training compute-optimal large language models. *Advances in Neural Information Processing Systems, 35*. https://arxiv.org/abs/2203.15556
- Phuong, M., & Hutter, M. (2022). Formal algorithms for transformers. *arXiv*. https://arxiv.org/abs/2207.09238
- Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., Askell, A., Bai, Y., Chen, A., Conerly, T., et al. (2021). A mathematical framework for transformer circuits. *Transformer Circuits Thread*. https://transformer-circuits.pub/2021/framework/index.html

- Gu, A., & Dao, T. (2023). Mamba: Linear-time sequence modeling with selective state spaces. *arXiv*. https://arxiv.org/abs/2312.00752
- [The Post-Transformer Era: State Space Models, Mamba, and What Comes After Attention](https://blog.serendeep.tech/blog/the-post-transformer-era)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html) — Rush et al., line-by-line PyTorch walkthrough of the 2017 paper.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Alammar, diagram-first explanation of the block and its data flow.
- [Transformers from Scratch](https://peterbloem.nl/blog/transformers) — Bloem, builds the architecture from attention primitives upward.
- [Transformers from Scratch (e2eml)](https://e2eml.school/transformers.html) — tensor-level walkthrough of self-attention and multi-head attention.
- [Transformers](https://brandonrohrer.com/transformers.html) — Rohrer, visual treatment of attention as a differentiable lookup.
- [The Transformer Family v2](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — Weng, taxonomy of efficiency and long-context variants.
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) — interactive GPT-2 visualization of the block in operation.
- [nanoGPT](https://github.com/karpathy/nanoGPT) — minimal, readable GPT training and sampling implementation.
- [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Karpathy, builds a working decoder-only model line by line.
- [Coding a Transformer from scratch on PyTorch](https://www.youtube.com/watch?v=ISNdQcPhsts) — Jamil, full encoder–decoder implementation with training and inference.
- [Transformers: Zero to Hero](https://www.youtube.com/watch?v=rPFkX5fJdRY) — CodeEmporium, architecture-to-code series.
- [tensor2tensor](https://github.com/tensorflow/tensor2tensor) — the reference implementation accompanying the 2017 paper.
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) and the [language-modeling training recipe](https://huggingface.co/docs/transformers/tasks/language_modeling).
- [Transformers.js](https://github.com/xenova/transformers.js) — the same models executed in the browser via ONNX.
- [An Explanation Is All You Need](https://github.com/IParraMartin/An-Explanation-Is-All-You-Need) — guided reimplementation with explanatory notebooks.
- [Transformer from Scratch in PyTorch](https://www.mislavjuric.com/transformer-from-scratch-in-pytorch/) — and the [companion Kaggle notebook](https://www.kaggle.com/code/lusfernandotorres/transformer-from-scratch-with-pytorch).
- [transformer-training-monitoring](https://github.com/csiglab/transformer-training-monitoring) — training-run observation harness.
- [Attention and Transformers notebooks](http://bactra.org/notebooks/nn-attention-and-transformers.html) — dated reading notes with useful provenance.
- [Transformer](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)) and [Generative pre-trained transformer](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer) — encyclopedic entry points.
- Papadimitriou, I., & Jurafsky, D. (2025). Between circuits and Chomsky: Pre-pretraining on formal languages imparts linguistic biases. *arXiv*. https://arxiv.org/abs/2502.19249
- [Procedural Pretraining: Warming Up Language Models with Abstract Data](https://arxiv.org/abs/2601.21725)
- [Learning Music Helps You Read: Using Transfer to Study Linguistic Structure in Language Models](https://arxiv.org/abs/2004.14601)
- [Do LLMs Benefit From Their Own Words?](https://arxiv.org/abs/2602.24287)
- [IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse](https://arxiv.org/abs/2603.12201)
- [LLM Neuroanatomy: How I Topped the LLM Leaderboard Without Changing a Single Weight](https://dnhkng.github.io/posts/rys/)
- [Experts Have World Models. LLMs Have Word Models.](https://www.latent.space/p/adversarial-reasoning)
- [Attention](note.html?n=technica/ais/system/transformer/attention.md) — the mechanism this architecture is built from.
- [Transformer System: Training](note.html?n=technica/ais/system/transformer/transformer-system-training.md) — the training half of this system.
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) — the schema and decomposition contract this note follows.
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) — the evaluation criteria applied above.

