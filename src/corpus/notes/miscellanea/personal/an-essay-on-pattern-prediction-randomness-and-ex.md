---
tags: [note]
---

# An Essay on Pattern, Prediction, Randomness and Explanation


> An explanation is a connection between the phenomenon to be explained (explanandum) and the account that explains it (explanans).
> 

> **Randomness** is the **absence of exploitable pattern** relative to a given descriptive or inferential framework.
> 

> A **pattern** is a **non-accidental regularity** in the structure, behavior, or distribution of elements within a domain.
> 

> A **pattern** exists when knowledge of some variables reduces uncertainty about others.
> 

## Index

## Pattern

> **The ontological nature of a pattern** is that it is a **non-ontic element**: it is **not an entity in itself**, but a **relational property** of a system, a dataset, or a model that constrains how partial descriptions may be completed.
> 

### Formulation

> What is a pattern? A **pattern** is a **stable, identifiable regularity** in relations, configurations, or behaviors across elements of a system or across observations of a system.
> 

> At its most **fundamental level**, a **pattern** is a **rule of completion**. Given a **partial description for a element**, a pattern specifies the **space of admissible completions**.
> 

> At its most abstract level, a **pattern** is a **constraint on degrees of freedom** such that **partial information determines (or restricts) missing information**.
> 

> A pattern exists when knowledge of some variables reduces uncertainty about others.
> 

> To identify a pattern is to know how to complete the incomplete.
> 

This is the ***completion principle***:

- If no completion is possible, there is no pattern.
- If multiple completions exist but are constrained, the pattern is probabilistic.
- If a unique completion exists, the pattern is deterministic.

### Pattern Space

> What is structure of patterns? What is the type of pattern? What is the structure of the space of patterns?
> 

| **Name** | **Pattern Form** | **Description** | **Instance(s)** |
| --- | --- | --- | --- |
| **Deterministic Rule** | Unique completion | Exactly one admissible continuation exists | Formal grammar rule, algorithmic sequence |
| **Probabilistic Schema** | Distribution over completions | Completions weighted by likelihood | Markov model, language model |
| **Constraint Satisfaction Pattern** | Feasible completion set | Any completion satisfying constraints is valid | Sudoku, conservation laws |
| **Optimization Pattern** | Extremal completion | Completion optimizes a criterion | Least action, loss minimization |
| **Generative Process Pattern** | Process-defined completion | A mechanism produces valid completions | L-systems, dynamical systems |
| **Associative Pattern** | Similarity-based completion | Completion via proximity in representation space | k-NN, analogical inference |
| **Emergent Interaction Pattern** | Collective completion | Completion arises from interacting components | Flocking, market equilibria |
| **Symmetry Pattern** | Invariant completion class | Completions equivalent under transformations | Crystallographic groups |
| **Hierarchical Pattern** | Multilevel completion | Completions constrained across scales | Grammars, organizational charts |

## Formalism

> How to formalize the concept of a pattern?
> 

> Across all formalisms, a pattern is a structured constraint that reduces the space of admissible completions of partial information.
> 

| **Underlying Method** | **Formalism** | **Description** | **Usage** |
| --- | --- | --- | --- |
| **Information Theory** | ( H(X \mid x_p) < H(X) ), ( I(x_p; X) > 0 ) | Pattern = uncertainty reduction enabling compression and prediction | Pattern detection, MDL, prediction, randomness testing |
| **Algorithmic Information Theory** | ( K(X \mid x_p) \ll K(X) ) | Pattern = low conditional complexity; compressible completion | Model induction, structure discovery |
| **Probability Theory** | ( P(X \mid x_p) \neq P(X) ) | Pattern = dependency between partial and complete | Bayesian inference, forecasting |
| **Constraint Satisfaction** | ( C(x) = \text{true} ) | Pattern = admissible set defined by constraints | Logic, CSPs, planning |
| **Optimization Theory** | ( x^* = \arg\min_x J(x) ) | Pattern = extremal completion under a criterion | Control, ML, physics |
| **Dynamical Systems** | ( x_{t+1} = F(x_t) ) | Pattern = lawful continuation governed by dynamics | Trajectory prediction, stability analysis |
| **Statistical Learning** | ( \hat{f} = \arg\min \mathcal{L}(f) ) | Pattern = learned mapping from partials to completions | Supervised / unsupervised learning |
| **Grammar & Formal Languages** | ( x \in L(G) ) | Pattern = syntactic admissibility of completions | Parsing, language modeling |
| **Symmetry & Group Theory** | ( T(x) \sim x ) | Pattern = invariance under transformations | Physics, geometry, crystallography |
| **Information Geometry** | Geodesics on ( \mathcal{P}(X) ) | Pattern = structured manifold of distributions | Model comparison, learning dynamics |
| **Category Theory** | Morphisms preserving structure | Pattern = compositional completion laws | System composition, abstraction |
| **Network Theory** | Motif recurrence | Pattern = recurring relational substructure | Social, biological networks |
| **Emergence / Complex Systems** | Macro-regularities from micro-rules | Pattern = collective completion | Markets, ecosystems |
| **Cognitive / Predictive Processing** | Prediction error minimization | Pattern = expectation-driven completion | Perception, reasoning |
| **Energy-Based Models** | ( E(x) \downarrow ) | Pattern = low-energy completion | Physics-inspired ML |

## Relation Notion(s)

| **Notion** | **Description** | **Relation** |
| --- | --- | --- |
| **Constraint** | A rule limiting admissible configurations or continuations | Defines what relations are *allowed* |
| **Dependency** | Variation in one element affects another | Couples elements informationally or causally |
| **Correlation** | Statistical co-variation without causal claim | Quantifies associative relation |
| **Causation** | Directed influence producing change | Orders relations temporally and directionally |
| **Invariance** | Property preserved under transformation | Defines equivalence across variations |
| **Symmetry** | Structured invariance under a transformation group | Constrains relational degrees of freedom |
| **Adjacency** | Proximity in space, time, or graph | Enables local interactions |
| **Ordering** | Partial or total arrangement of elements | Establishes precedence or hierarchy |
| **Hierarchy** | Nested relations across scales | Organizes relations recursively |
| **Composition** | Combination of relations into higher-order ones | Builds complex relational structures |
| **Equivalence** | Mutual substitutability under a criterion | Partitions elements into classes |
| **Similarity** | Degree of likeness under a metric | Supports associative completion |
| **Constraint Satisfaction** | Joint fulfillment of multiple relations | Intersects relational requirements |
| **Flow** | Transfer of quantity across relations | Connects states dynamically |
| **Feedback** | Output influences input | Enables regulation and stability |
| **Coupling** | Strength of interaction between elements | Modulates relational dependence |
| **Emergence** | Macro-relations from micro-relations | Generates higher-level patterns |
| **Closure** | Relations sufficient to sustain the system | Delimits relational boundaries |

## QA

### How can one test if a given dataset is random?

| **Category** | **Method (Test)** | **Assumption(s)** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| **Statistical Distribution** | **Chi-Square Test** | Observations are independent; expected frequency in each bin is sufficiently large (usually ≥5) | Compares the observed frequency of values in bins to the expected frequency under a uniform or other theoretical distribution. | Works best for categorical or binned numeric data. Sensitive to sample size and bin choice. |
| **Autocorrelation** | **Runs Test (Wald–Wolfowitz Test)** | Observations are independent under the null hypothesis; data is ordinal or binary (above/below median) | Measures the number and length of consecutive increasing/decreasing or above/below median sequences to detect non-randomness. | Detects serial correlation in sequences; simple to implement. |
| **Spectral / Frequency Analysis** | **Fourier Transform / Spectral Test** | Data is numeric and evenly spaced | Analyzes frequency components of numeric sequences; random data should have a flat spectrum. | Useful for detecting periodic patterns. |
| **Permutation / Resampling** | **Permutation Test / Randomness Simulation** | Observations are exchangeable under the null hypothesis | Compares dataset statistics to a distribution obtained by shuffling or resampling the data. | Computationally intensive but distribution-free. |
| **Entropy / Compression** | **Kolmogorov Complexity / Compression Test** | Data is representable as a finite string | Measures the compressibility of the dataset; highly random data is incompressible. | Exact Kolmogorov complexity is uncomputable; approximations use compression algorithms. |
| **Runs / Sequence Patterns** | **Gap / Serial Test** | Observations are independent; event probabilities are constant | Examines gaps between specific events or repeated patterns to see if sequences occur at expected frequencies. | Often used in RNG testing; sensitive to short-range dependencies. |
| **Randomness Batteries** | **NIST Statistical Test Suite (SP800-22)** | Depends on the specific test; generally assumes independence and sufficient sequence length | A collection of 15+ tests (frequency, runs, rank, spectral, etc.) specifically designed for evaluating RNGs. | Comprehensive and standardized for cryptographic and simulation purposes. |
| **Graphical / Visual** | **Histogram, Autocorrelation Plot, Scatter Plot** | Assumes no particular distribution; purely exploratory | Visual inspection for patterns or clustering that would indicate non-randomness. | Not definitive but useful for exploratory analysis. |

### Is the phrase “The Unreasonable Effectiveness of Mathematics in Physics” an example of being fooled by randomness?

> If physics selects problems that fit the available mathematical toolset—one that largely deals with simple, deterministic systems—then it is unsurprising that mathematics appears highly effective.
> 

> See [http://www.sci.brooklyn.cuny.edu/~noson/FindingOrder.pdf](http://www.sci.brooklyn.cuny.edu/~noson/FindingOrder.pdf) - One Can Always Find Order in Chaos - Disorder - If the Dataset is Large Enought.
> 

> This is an instance of a  cognitive bias called **Selection Bias -** we are not seeing  all the pset universe only a convenient subset - and we try something outside the subset - we tend to ignore the negative results and backtrack - which by consequences they will be less attemps to solve problems in the subset and outside it.
> 

This is a **well-known critique** of Wigner’s thesis and is commonly framed as:

- **Selection bias / survivorship bias** in problem choice
- **Model–phenomenon co-adaptation** (theory evolves toward what it can explain)
- **Retrospective sense-making** rather than genuine predictive miracle

## References

- https://en.wikipedia.org/wiki/Pattern
- https://en.wikipedia.org/wiki/Determinism
- https://en.wikipedia.org/wiki/Randomness
- https://en.wikipedia.org/wiki/Ramsey_theory
- [Ramsey Theory](https://app.notion.com/p/Ramsey-Theory-2ddc0f5171ec801c860dc73858791f35?pvs=21)
- https://giannirosato.com/blog/post/lossless-data-comp/
- [‣](https://app.notion.com/p/10e598edb790811ab17fda16133dc7d4?pvs=21)
- https://www.youtube.com/watch?v=7kqNNCywkV4&t=145s
