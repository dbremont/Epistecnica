---
tags: [measure-theory, structure]
---

# σ-algebra

 : Set (Set%20176c0f5171ec800f8b41f66b6d8cc5b3.md), Boolean Algebra (Boolean%20Algebra%2029a6a469a6714ad89edc85c8ffbe2d57.md), Measure (Measure%20273c0f5171ec80ae812dc3c73aad95dc.md)

> Note: This is not an “algebraic structure / aka algebra”; is a **“set algebra”**.
> 

QA:

- …

## Formulation

A **σ-algebra** (or **sigma-algebra**) is a collection $\mathcal{F}$ of subsets of  $\mathcal{P} (\mathbb{\Omega})$  that satisfies the following properties:

- **Contains the Sample Space**: $\Omega \in \mathcal{F}$.
- **Closed under Complements**: If $A \in \mathcal{F}$, then $A^c \in \mathcal{F}$.
- **Closed under Countable Unions**: If $A_1, A_2, A_3, \dots \in \mathcal{F}$, then $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$.

## Uses

> 📊 **Goals of the Sigma-Algebra Abstraction**
> 

| 🏷️ **Goal** | 🎯 **Purpose / Why it Matters** |
| --- | --- |
| 📐 **Define measurable sets** | Ensures only "well-behaved" subsets are included—excludes paradoxical or undefined sets. |
| 🧩 **Avoid paradoxes** | Prevents contradictions like the Banach–Tarski paradox by avoiding “too wild” subsets. |
| 🎲 **Support probability theory** | Enables assigning probabilities to complex events (unions, intersections, complements). |
| ∫ **Enable integration theory** | Forms the foundation for **Lebesgue integration** by defining domains and measurable functions. |
| ➕ **Ensure countable additivity** | Guarantees that the measure (or probability) behaves consistently under countable operations. |

## References

- https://en.wikipedia.org/wiki/%CE%A3-algebra
