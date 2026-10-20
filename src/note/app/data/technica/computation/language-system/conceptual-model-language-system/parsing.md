---
tags: [language-system, parsing, problema]
---

# Parsing

- [Bytecode Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/bytecode-virtual-machine.md), [Declarative Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/declarative-model-of-computation.md), [Compiler System](note.html?n=technica/computation/language-system/conceptual-model-language-system/compiler-system.md), [Grammar](note.html?n=technica/computation/language-system/conceptual-model-language-system/grammar.md), [Interpreter System](note.html?n=technica/computation/language-system/conceptual-model-language-system/interpreter-system.md), [Binary Parsing](note.html?n=technica/computation/language-system/conceptual-model-language-system/binary-parsing.md)

> In this note we will introduce the concept of parsing (from the French *parser*, meaning “to analyze grammatically” or “to break into parts”).
> 

> The **computational process** of parsing has the goal of reverse engineering the process of derivation (grammar expansion), answering the question: which derivation tree has generated this sentence of the grammar?
> 

> A **parser** takes the flat sequence of tokens and builds a tree structure that mirrors the nested nature of the grammar. These trees have a couple of different names—parse tree or abstract syntax tree—depending on how close to the source language’s bare syntactic structure. In practice, language hackers call them syntax trees, **ASTs**, or often just trees.
> 

QA:

- How to **parse log files**?

## Formulation

> Computational Problem: Given a sentence, generate a representation of the process that produces de sentences from the grammar.
> 

> Parsing: Sentence * Grammar → Parse Tree Sentence Representation.
> 

> **Correctness Model:** A parse is considered correct if the resulting parse tree, when evaluated under the grammar’s production rules, generates exactly the input sentence. Formally, a parse tree $T$  is correct iff: $\text{yield}(T) = w \quad \text{and} \quad T \in \mathcal{T}_G$ where $w$ is the input sentence and $\mathcal{T}_G$ is the set of valid derivation trees under grammar $G$.
> 

> **What happens when parsing is non invertible?** How this get’s handle by our correctness  model? **It is handled by redefining correctness** from a unique inverse reconstruction into a relation-based condition requiring that the parser produce a sound (and ideally complete or optimally selected) set of derivation trees whose yields match the input sentence under the grammar.
> 

![](https://craftinginterpreters.com/image/a-map-of-the-territory/ast.png)

## Grammar

> Parsing Method → Grammar
> 

> See [Grammar](note.html?n=technica/computation/language-system/conceptual-model-language-system/grammar.md).
> 

## Parsing Model Space

> What is a **parsing model**? A **parsing model** is a formal computational system that defines how an observed sentence is mapped, under a given grammar, to a structured representation of its latent syntactic derivations (parse trees), typically by specifying the space of admissible structures and the algorithmic or probabilistic principles used to select, enumerate, or rank them.
> 

> A parsing model is not a single algorithm—it is a structured composition of several interacting dimensions that jointly define how sentence-to-structure inference is performed.
> 

> **What are the types of elements that makes us a given parsing model?** A **parsing model** is a structured tuple of (grammar, strategy, technique, search policy, representation scheme, scoring function, correctness criteria, and complexity regime) that jointly defines how sentence-to-derivation inference is computed or approximated.
> 

| **Parsing Model** | **Description** | **Usage Requirement** |
| --- | --- | --- |
| **Rule-Based CFG Parser** | Deterministic parsing over a context-free grammar without probabilities or learning components | Requires explicit CFG; used when structure is fully specified and ambiguity is limited or handled via enumeration |
| **Top-Down Parser (e.g., Recursive Descent)** | Expands from start symbol toward input sentence via predictive rule application | Requires non-left-recursive grammars or backtracking control; best for simple or constrained grammars |
| **Bottom-Up Parser (Shift-Reduce)** | Constructs parse by reducing input tokens into higher-level constituents | Requires grammars compatible with shift-reduce actions; commonly used in compiler design |
| **Chart Parsing (Earley / CYK family)** | Dynamic programming over substrings storing partial derivations | Requires CFG; used when ambiguity is high and reuse of substructure is essential |
| **Probabilistic CFG Parser (PCFG)** | Extends CFG with probabilities over production rules | … |
| **Beam Search Neural Parser** | Uses learned scoring functions over partial parse states with pruning | Requires trained model; used in data-driven NLP systems |
| **Dependency Parser** | Produces graph of head–dependent relations instead of constituency trees | Requires dependency formalism; used for semantic-syntactic structure extraction |
| **Unification / Feature Grammar Parser** | Uses structured feature constraints (agreement, case, etc.) during parsing | Requires rich linguistic annotation; used in high-precision linguistic modeling |
| **Neural End-to-End Parser (Transformer-based)** | Learns implicit grammar and parses via latent representations | Requires large datasets; used when explicit grammar is unavailable or too rigid |

## Technique Type Space

> Which are **types of techniques** used to **build a parsing system**?
> 

| **Technique Type** | **Description** | **Instance(s)** | **Role** |
| --- | --- | --- | --- |
| **Top-Down Expansion Techniques** | Constructs parses by expanding from the start symbol toward the input; prediction-driven derivation | Recursive Descent, Predictive Parsing, LL(k) parsing | Guides parse construction by predicting rule expansions from the start symbol to match input left-to-right |
| **Bottom-Up Reduction Techniques** | Builds structure from tokens upward by reducing them into higher constituents | Shift-Reduce Parsing, LR Parsing (LR(0), SLR, LALR, LR(1)) | Assembles parse trees by reducing input tokens into nonterminals until reaching the start symbol |
| **Dynamic Programming Decomposition** | Reuses substructure solutions by storing intermediate spans or states | CYK Algorithm, Earley Parser, Inside–Outside Algorithm | Solves parsing efficiently by combining solutions to overlapping subproblems (e.g., spans, states) |
| **Chart-Based Memoization Techniques** | Stores partial parses in a shared structure to avoid recomputation in ambiguous grammars | Chart Parsing, Earley Items, Packed Parse Forests | Caches partial parse results to enable polynomial-time handling of ambiguity |
| **Constraint Satisfaction Techniques** | Enforces grammatical or feature constraints during parse construction | Unification-based parsing, Feature Structure resolution, Constraint-based grammars | Filters or validates parses by requiring feature agreement and constraint consistency |
| **Probabilistic Inference Techniques** | Uses probability distributions over rules or structures to guide selection | PCFG parsing, Viterbi decoding, Inside-Outside re-estimation | Ranks or selects the most likely parse(s) using learned or grammar-based probabilities |
| **Heuristic Search Techniques** | Uses heuristics to guide exploration of parse space efficiently | A* parsing, Best-first parsing, agenda-based parsing | Prunes unpromising search directions using heuristic scores to find high-quality parses faster |
| **Pruned Search Techniques** | Limits search space to reduce combinatorial explosion | Beam Search, k-best parsing, pruning thresholds | Reduces computational cost by discarding low-scoring partial hypotheses at each step |
| **Graph Construction Techniques** | Builds dependency or constituency structures as graphs rather than trees over derivations | Arc-factored dependency parsing, MST parsing, transition-based graph construction | Produces parse structures as graphs (e.g., dependency trees, forests) by optimizing over edges |
| **Transition System Techniques** | Defines parsing as sequence of discrete actions over a parser state machine | Arc-standard, Arc-eager, Swap-based parsing | Models parsing as a deterministic or guided series of state transitions over a stack/buffer |
| **Neural Representation Techniques** | Learns distributed representations of parse states and transitions | Transformer encoders, BiLSTM encoders, contextual embeddings | Encodes rich, non-local features into vector representations to improve prediction |
| **Differentiable Parsing Techniques** | Makes parsing operations continuous/learnable via gradients | Softmax-over-structures, Neural CRF parsing, Differentiable CKY | Enables end‑to‑end learning by relaxing discrete parsing decisions into differentiable operations |
| **Sampling / Stochastic Techniques** | Approximates parse distributions via random sampling | MCMC parsing, Monte Carlo Tree Search, ancestral sampling in latent trees | Estimates parses or expectations over structures when exact inference is intractable |
| **Energy-Based Techniques** | Defines compatibility score over structures and selects low-energy parses | Structured energy models, Neural energy-based parsing | Scores parse structures via an energy function; lower energy indicates better parse |
| **Global Optimization Techniques** | Solves parsing as a global argmax problem over full structures | ILP-based parsing, maximum spanning tree decoding | Directly optimizes a global objective over entire parse trees without incremental greediness |

## References

- [Parsing](https://www.wikiwand.com/en/Parsing)
- [LL Parser](https://en.wikipedia.org/wiki/LL_parser)
- [LR Parser](https://en.wikipedia.org/wiki/LR_parser)
- [CYK Parser](https://en.wikipedia.org/wiki/CYK_algorithm)
- [Earley Parser](https://en.wikipedia.org/wiki/Earley_parser)
- [LALR Parsing](https://en.wikipedia.org/wiki/LALR_parser)
- [Shift-reduce parser](https://www.wikiwand.com/en/Shift-reduce_parser)
- [Top-down LR Parsing](https://pavpanchekha.com/blog/top-down-lr.html)
- Chomsky, N. (1980). Rules and Representations. 3(1), 1–15.
- Chomsky, N. (1956). Three models for the description of language. 2(3), 113–124.
- Everaert, M. B. H., Huybregts, M. A. C., Chomsky, N., Berwick, R. C., Bolhuis, J. J. (2015). Structures, Not Strings: Linguistics as Part of the Cognitive Sciences. 19(12), 729–743.