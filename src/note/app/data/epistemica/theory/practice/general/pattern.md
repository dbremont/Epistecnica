# Pattern

> A **pattern** is a **non-accidental regularity** in the structure, behavior, or distribution of elements within a domain.
> 

> A **pattern** exists when knowledge of some variables reduces uncertainty about others.
> 

> An **explanation** is a connection between the phenomenon to be explained (explanandum) and the account that explains it (explanans).
> 

> **Randomness** is the **absence of exploitable pattern** relative to a given descriptive or inferential framework.
> 

> The notion of a pattern is one of the most fundamental concepts in the toolbox of a modeler.
> 

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
| **Information Theory** | $H(X \mid x_p) < H(X) ), ( I(x_p; X) > 0$ | Pattern = uncertainty reduction enabling compression and prediction | Pattern detection, MDL, prediction, randomness testing |
| **Algorithmic Information Theory** | $K(X \mid x_p) \ll K(X)$ | Pattern = low conditional complexity; compressible completion | Model induction, structure discovery |
| **Probability Theory** | $P(X \mid x_p) \neq P(X)$ | Pattern = dependency between partial and complete | Bayesian inference, forecasting |
| **Constraint Satisfaction** | $C(x) = \text{true}$ | Pattern = admissible set defined by constraints | Logic, CSPs, planning |
| **Optimization Theory** | $x^* = \arg\min_x J(x)$ | Pattern = extremal completion under a criterion | Control, ML, physics |
| **Dynamical Systems** | $x_{t+1} = F(x_t)$ | Pattern = lawful continuation governed by dynamics | Trajectory prediction, stability analysis |
| **Statistical Learning** | $\hat{f} = \arg\min \mathcal{L}(f)$ | Pattern = learned mapping from partials to completions | Supervised / unsupervised learning |
| **Grammar & Formal Languages** | $x \in L(G)$ | Pattern = syntactic admissibility of completions | Parsing, language modeling |
| **Symmetry & Group Theory** | $T(x) \sim x$ | Pattern = invariance under transformations | Physics, geometry, crystallography |
| **Information Geometry** | Geodesics on $\mathcal{P}(X)$ | Pattern = structured manifold of distributions | Model comparison, learning dynamics |
| **Category Theory** | Morphisms preserving structure | Pattern = compositional completion laws | System composition, abstraction |
| **Network Theory** | Motif recurrence | Pattern = recurring relational substructure | Social, biological networks |
| **Emergence / Complex Systems** | Macro-regularities from micro-rules | Pattern = collective completion | Markets, ecosystems |
| **Cognitive / Predictive Processing** | Prediction error minimization | Pattern = expectation-driven completion | Perception, reasoning |
| **Energy-Based Models** | $E(x) \downarrow$ | Pattern = low-energy completion | Physics-inspired ML |

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

- Can Every Type of Pattern Be Cast as Completion?
- …

## References

- https://en.wikipedia.org/wiki/Pattern
- https://en.wikipedia.org/wiki/Determinism
- https://en.wikipedia.org/wiki/Randomness
- An Essay on Pattern, Prediction, Randomness and Explanation
- Anderson, P. W. (1972). More is different. *Science, 177*(4047), 393–396. [https://doi.org/10.1126/science.177.4047.393](https://doi.org/10.1126/science.177.4047.393)
- Chaitin, G. J. (1975). Randomness and mathematical proof. *Scientific American, 232*(5), 47–52. [https://doi.org/10.1038/scientificamerican0575-47](https://doi.org/10.1038/scientificamerican0575-47)
- Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory, 2*(3), 113–124. [https://doi.org/10.1109/TIT.1956.1056813](https://doi.org/10.1109/TIT.1956.1056813)
- Clark, A. (2016). *Surfing uncertainty: Prediction, action, and the embodied mind*. Oxford University Press. [https://doi.org/10.1093/acprof:oso/9780190217013.001.0001](https://doi.org/10.1093/acprof:oso/9780190217013.001.0001)
- Cover, T. M., & Thomas, J. A. (2006). *Elements of information theory* (2nd ed.). Wiley-Interscience.
- Dechter, R. (2003). *Constraint processing*. Morgan Kaufmann.
- Dennett, D. C. (1991). Real patterns. *The Journal of Philosophy, 88*(1), 27–51. [https://doi.org/10.2307/2027085](https://doi.org/10.2307/2027085)
- French, S. (2014). *The structure of the world: Metaphysics and representation*. Oxford University Press. [https://doi.org/10.1093/acprof:oso/9780199684847.001.0001](https://doi.org/10.1093/acprof:oso/9780199684847.001.0001)
- Haken, H. (1983). *Synergetics: An introduction* (3rd ed.). Springer. [https://doi.org/10.1007/978-3-642-96469-5](https://doi.org/10.1007/978-3-642-96469-5)
- Helmholtz, H. von. (1867). Concerning the perceptions in general. In R. S. Cohen & Y. Elkana (Eds.), *Hermann von Helmholtz: Epistemological writings* (pp. 1–31). Reidel. (Original work published 1867)
- Hempel, C. G., & Oppenheim, P. (1948). Studies in the logic of explanation. *Philosophy of Science, 15*(2), 135–175. [https://doi.org/10.1086/286983](https://doi.org/10.1086/286983)
- Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. *Problems of Information Transmission, 1*(1), 1–7.
- Ladyman, J., & Ross, D. (2007). *Every thing must go: Metaphysics naturalized*. Oxford University Press.
- Li, M., & Vitányi, P. (2008). *An introduction to Kolmogorov complexity and its applications* (3rd ed.). Springer. [https://doi.org/10.1007/978-0-387-49820-1](https://doi.org/10.1007/978-0-387-49820-1)
- Martin-Löf, P. (1966). The definition of random sequences. *Information and Control, 9*(6), 602–619. [https://doi.org/10.1016/S0019-9958(66)80018-9](https://doi.org/10.1016/S0019-9958(66)80018-9)
- Noether, E. (1918). Invariant variation problems. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 235–257. (English translation published 1971)
- Prigogine, I. (1980). *From being to becoming: Time and complexity in the physical sciences*. W. H. Freeman.
- Rissanen, J. (1978). Modeling by shortest data description. *Automatica, 14*(5), 465–471. [https://doi.org/10.1016/0005-1098(78)90005-5](https://doi.org/10.1016/0005-1098(78)90005-5)
- Salmon, W. C. (1984). *Scientific explanation and the causal structure of the world*. Princeton University Press.
- Solomonoff, R. J. (1964). A formal theory of inductive inference. Part I. *Information and Control, 7*(1), 1–22. [https://doi.org/10.1016/S0019-9958(64)90223-2](https://doi.org/10.1016/S0019-9958(64)90223-2)
- Solomonoff, R. J. (1964). A formal theory of inductive inference. Part II. *Information and Control, 7*(2), 224–254. [https://doi.org/10.1016/S0019-9958(64)90231-1](https://doi.org/10.1016/S0019-9958(64)90231-1)
- Woodward, J. (2003). *Making things happen: A theory of causal explanation*. Oxford University Press.
- [Explanation](note.html?n=epistemica/theory/practice/explanation.md)
