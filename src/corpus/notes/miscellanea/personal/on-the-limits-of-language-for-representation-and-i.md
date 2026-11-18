---
tags: [note, essay]
---

# On the Limits of Language for Representation and Inference

**Contains:** [A Guide to Language and Cognition](/view.html?p=notes/miscellanea/personal/a-guide-to-language-and-cognition.md)

> An Essay on “On the Limits of Language for Representation and Inference”.
> 

Guiding Questions:

- Why formalization is useful?
- Why is mathematical so useful?
- What value does a formal language adds?
- What epistemic problems motivate formalization?
- Which representational and inferential limits are intrinsic to natural language?
- What kinds of errors or failures emerge when formal structure is absent but precision is required?
- How does formalization transform vague or open-ended descriptions into tractable object spaces?
- What are the limits of using language (or linguistic representations) for representation and inference?
- What additional structure does a formal language introduce beyond linguistic expression?
- Why do mathematical and logical formalisms enable forms of reasoning that natural language cannot?

## Index

## Formulation

### Evaluation

- **How can a description of reality be evaluated?**
- **By which criteria can we assess the adequacy of a representation of reality?**
- **What makes a description faithful, informative, or operationally useful?**

| **Category** | **Criteria** | **Description** |
| --- | --- | --- |
| Ontic Adequacy | Referential fidelity | Degree to which the description correctly maps to real entities, properties, relations, and processes. |
| Structural Fidelity | Isomorphism / homomorphism | Extent to which the structure of the description preserves the structure of the underlying reality (e.g., causal, relational, topological). |
| Precision | Unambiguity | Whether the description minimizes vagueness and underspecification. |
| Completeness | Coverage | Whether all relevant variables, boundary conditions, and constraints are represented. |
| Consistency | Internal coherence | Absence of contradictions within the description. |
| Explanatory Power | Causal intelligibility | Ability to account for why phenomena occur, not merely that they occur. |
| Predictive Power | Forecast accuracy | Ability to generate empirically testable and reliable predictions. |
| Inferential Power | Derivability | What non-trivial conclusions can be logically or computationally derived from the description. |
| Operationality | Actionability | Whether the description can be used for control, intervention, or decision-making. |
| Robustness | Stability under perturbation | Sensitivity of conclusions to noise, parameter changes, or modeling assumptions. |
| Parsimony | Minimality | Degree to which unnecessary entities or assumptions are avoided. |
| Epistemic Transparency | Interpretability | Ease with which agents can understand, inspect, and reason about the description. |

### Comparison

- **How can different mechanisms for describing reality be compared?**
- **On what dimensions can representational frameworks be contrasted (expressiveness, precision, inferential power, etc.)?**
- **How do alternative descriptive mechanisms trade off realism, tractability, and explanatory power?**

| **Mechanism(s)** | **Description** | **Evaluation** |
| --- | --- | --- |
| Natural Language | Informal, context-dependent symbolic system | High expressiveness; low precision and inferential rigor; weak reproducibility. |
| Formal Logic (FOL, Modal, Temporal) | Axiomatic symbolic representations | High precision and inferential soundness; limited scalability and realism. |
| Mathematical Models | Quantitative functional or structural relations | Strong predictive and explanatory power; abstraction-dependent. |
| Statistical Models | Probabilistic descriptions of observed data | Empirically grounded; weak causal semantics unless augmented. |
| Computational Models (Simulations) | Algorithmic process representations | Captures dynamics and emergence; validation can be difficult. |
| Ontologies | Explicit conceptual and relational schemas | High semantic clarity; limited dynamics and causality. |
| Dynamical Systems | State-space evolution models | Strong for temporal and causal analysis; may oversimplify structure. |
| Agent-Based Models | Micro-level interacting agents | Captures emergence; parameter sensitivity and interpretability issues. |
| Machine Learning Models | Data-driven functional approximations | High predictive accuracy; low epistemic transparency and causal grounding. |
| Hybrid Models | Integrated symbolic–numeric systems | Balanced trade-offs; increased complexity and design burden. |

### Precision (Lack of Ambiguity)

> What is Precision? How to detect Precision? Which does Precision entails?
> 

**Precision** is the degree to which a representation **uniquely determines its intended interpretation** with respect to:

- referents (what entities are being talked about),
- structure (how those entities are related),
- conditions (when and where the description applies),
- consequences (what follows from the description).

Formally, a description is precise if the **mapping from representation → interpretation is narrow and stable**, i.e., it admits **few admissible models**.

> Precision is not truth.
> 
> 
> Precision is not accuracy.
> 
> Precision is *determinacy of meaning and inference*.
> 

### How do I know that interpretation *Y* is an *admissible* (or allowable) interpretation of description *X*?

> When does an interpretation *satisfy* a description?
> 

> A very deep question that needs introduction of some **model-theoretic and interpretive criteria.**
> 

1. **Ontological Compatibility**  An interpretation *Y* is ontologically compatible with a description *X* iff the domain, categories, and primitive relations presupposed by *Y* are homomorphic to—or at least embeddable within—the ontic commitments implicitly or explicitly licensed by *X*.
2. **Referential Assignment** *Y* provides an admissible referential assignment for *X* iff every referring expression in *X* is mapped, under *Y*, to a well-defined element, class, or relation in the interpretation domain such that identity, scope, and type constraints are preserved.
3. **Structural Satisfaction** An interpretation *Y* structurally satisfies *X* iff the relational structure induced by *Y* constitutes a model in which the formal (or implicit) relational patterns, dependencies, and compositional constraints expressed by *X* are preserved up to isomorphism or permitted weakening.
4. **Constraint Satisfaction** *Y* is admissible relative to *X* only if all explicit and implicit constraints encoded in *X*—logical, algebraic, causal, temporal, or normative—are satisfied in *Y* without violation or compensatory reinterpretation.
5. **Boundary Conditions** An interpretation *Y* satisfies the boundary conditions of *X* iff it respects the intended domain limits, contextual scope, and exclusion criteria of *X*, preventing overgeneration, category leakage, or unintended model extension.
6. **Inferential Closure** *Y* is inferentially adequate for *X* iff the set of inferences licensed by *X* is closed under the interpretive rules of *Y*, such that no sanctioned inference becomes invalid and no invalid inference is introduced.

## Language

Natural language is inherently **underspecified**, **context-dependent**, and **structurally weak** for rigorous representation and inference.

Linguistic expressions do not uniquely determine their referents, boundary conditions, or inferential rules; instead, they rely on shared background knowledge, pragmatic cues, and interpretive conventions. As a result, the same statement may correspond to multiple, mutually incompatible possible worlds.

This makes language suitable for **exploration, communication, and heuristic reasoning**, but insufficient for **exhaustive case specification**, **formal consistency**, or **systematic inference**. Without an explicit formal structure, language cannot delimit the full space of possibilities, nor can it reliably identify the conditions under which a statement is true, false, or indeterminate.

Consequently, linguistic representations must be supplemented by **formal systems** (e.g., mathematics, logic, computational models) when precision, completeness, and tractable inference are required.

## On Communication

> A **writer, teacher, or communicator** has internal mental representations, which are **serialized into material structures** (e.g., text, audio). The reader’s task is to **map those material structures onto the representations the writer intended**. The **level of communication** is therefore defined by the **degree to which the reader can successfully decode and reconstruct the writer’s intended mental representation**.
> 

## References

- [Writing](https://app.notion.com/p/Writing-28cc0f5171ec800c9ef4e1db31532c40?pvs=21)
- [Language](https://app.notion.com/p/Language-275c0f5171ec80feb2f0c4a393a4af6b?pvs=21)
- [A Guide to Reading](/view.html?p=notes/miscellanea/personal/a-guide-to-reading.md)
- https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html
- Priest, G. "Limits of Language." *278 Future Tense and Future Time Reference* (2006): 365.
