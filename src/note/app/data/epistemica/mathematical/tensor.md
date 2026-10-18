---
tags: [analytical, type]
---

# Tensor

 : Vector (Vector%20171c0f5171ec80ad8609e882652c59be.md), Indo-Arabic Numeral (Indo-Arabic%20Numeral%20a3d9c8f22c444f89a7daf097cc1d29d3.md), Matrix (Matrix%20171c0f5171ec80c58898c4e26151fbb8.md), Multilinear Map (Multilinear%20Map%208989cd621d7a407d9137711e88aac9d1.md)

> **Note:** The definition of a tensor can be confusing. In computer science, it is often treated simply as a generalization of an n-dimensional data structure. In mathematics, tensors are sometimes described similarly, but this is often mixed with their use as multilinear maps or bilinear forms. In this note, we aim to be as precise as possible.
> 

> In this note, the word `m-tensor`  denotes the concept of tensor used in mathematics,  not the Computer Science  one.
> 

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | … |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | … |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | What is the deepest essence? |
| **Evidentia (Evidence) 📊** | What proofs, data, or logical arguments support it? How can its claims or performance be verified? |
| **Telos (Intent) 🎯** | What is it for? Toward what end is it directed? What tools does it offer, if any? What outcomes does it aim to achieve? |
| **Gnosis (Understanding) 🧠** | How to grow a **mental represented** (compress, fluid,  hierarchical (depth, abstraction), meta-awareness, flexibility, minimal sensitivity, well-connected) that capture this topic both its declarative aspects and procedural aspects?  How can we develop an **explicit representation & organization** of this topic that supports the growth of a strong **mental representation**? What **previous structure**  must be in place in order to make the growth of the new representation feasible? |
| **Epignosis (Application) 🛠️** | How is this knowledge applied in practice? What advanced skills or insights emerge from mastery? What real-world problems does it solve? |
| **Relatio (Connections) 🔗** | How does this topic relate to other subjects or fields? What are the interdisciplinary connections? |
| **Idoneitas (Suitability) 📐** | How effectively does it achieve its purpose? What metrics prove its value? |
| **Limites (Limits) ⛔** | What are its boundaries? What constraints define its operation? |
| **Contextus (Context) 🌍** | What is the historical, cultural, or situational context in which this study occurs? |
| **Dynamis (Evolution) 🌱** | How might it transform? What emerging influences could redefine it? |
| **Critica (Critique) 🔍** | What are the common criticisms or challenges associated with this topic? How have these been addressed or debated? |
| **Verbum Usus (Language Use) 🗣️** | How is the word/concept used in language and discourse? What are the typical semantic, pragmatic, and stylistic patterns surrounding its use? How do people’s usage contexts, connotations, and variations influence understanding? What shifts or trends in language use reflect its evolving meaning or social significance? |

### 🧠 Mental Representation

> How should we think about x?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Terminology

> Note: Many constructs are called tensors, such as the Ricci tensor; however, in this case, it is actually a tensor field.
> 

## Formulation

> How can we represent a tensor? How can we formalize the notion of a tensor?
> 

### Multilinear Map

A tensor of type $(m, n)$ is a function  

$T: \underbrace{V^* \times \dots \times V^*}{m \text{ times}} \times \underbrace{V \times \dots \times V}{n \text{ times}} \to \mathbb{R}$ that is **linear in each argument separately**.

- Here, $V$ is a vector space and $V^*$ its dual (space of linear functionals).
- $m$ = number of covariant indices, $n$ = number of contravariant indices.
- This is the most general, **coordinate-free** definition.

### Computer Science Tensor

Given a basis $\{e_i\}$ of $V$ and dual basis $\{e^i\}$ of $V^*$, the tensor can be written in components:
$T = T^{i_1 \dots i_n}{j_1 \dots j_m} \, e{i_1} \otimes \dots \otimes e_{i_n} \otimes e^{j_1} \otimes \dots \otimes e^{j_m}$

- $T^{i_1 \dots i_n}_{j_1 \dots j_m}$ are **numbers** (components) that encode the tensor in this basis.
- The **number of indices** corresponds to the rank of the tensor:
    - Rank 0 → scalar
    - Rank 1 → vector or covector
    - Rank 2 → matrix
    - Rank ≥ 3 → higher-dimensional array

This is the form most commonly used in computations, physics, and machine learning.

### Transformation Rule

A tensor can also be **defined by how its components change under a change of basis**:
$\tilde{T}^{i_1 \dots i_n}{j_1 \dots j_m} =
A^{i_1}{k_1} \dots A^{i_n}{k_n} (A^{-1})^{l_1}{j_1} \dots (A^{-1})^{l_m}{j_m} T^{k_1 \dots k_n}{l_1 \dots l_m}$

## Interpretation

| **Interpretation** | **Description** | **Case Study** |
| --- | --- | --- |
| **Geometric** | Encodes relationships between directions and magnitudes in space. | Metric tensor in general relativity: defines distances and angles in curved spacetime. |
| **Multilinear map** | Function that takes vectors and covectors and outputs a scalar; linear in each argument. | Bilinear form $B(v, w)$ representing work done by a force along a displacement. |
| **Data Structure** | Structured array of numbers indexed by rank; transforms predictably under coordinate changes. | Tensor in ML frameworks: 3D array representing RGB image data. |
| **Physical** | Represents measurable quantities independent of **coordinates**. | Stress tensor in mechanics: describes internal forces acting in all directions within a material. |
| **Abstract** | Generalizes scalars and vectors to multi-directional, multi-linear relationships; describes interactions in linear spaces. | Moment of inertia tensor in physics: encodes resistance to rotation along different axes. |

## Tensor Field

> A **tensor field** is a mathematical object that **assigns a tensor to every point in a space or manifold**.
> 

> Note: Seems the tensors in the field are usually of the same structure; in physics they just called it tensor - which is a terminology abused - like  Electromagnetic Field Tensor,  Elasticity Tensor, Riemann Curvature Tensor, Ricci Tensor and Stress-Energy Tensor, …
> 

## ❓ QA

> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- [Tensor](https://en.wikipedia.org/wiki/Tensor)
- [What, Exactly, Is a Tensor?](https://math.stackexchange.com/questions/657494/what-exactly-is-a-tensor)
- [Norm](norm.md)
- [**Representation Problem: Tensor**](https://app.notion.com/p/Representation-Problem-Tensor-3bf10e509aeb46088ba27c4a17cd31d9?pvs=21)
