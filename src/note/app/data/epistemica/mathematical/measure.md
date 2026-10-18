---
tags: [analytical, measure-theory]
---

# Measure

 : Set (Set%20176c0f5171ec800f8b41f66b6d8cc5b3.md), σ-algebra (%CF%83-algebra%2015fc0f5171ec80f392e8ffbf11d4cf84.md), Function Space (Function%20Space%201d6c0f5171ec80b5b311fe52e4fa23b8.md), Metric Space (Metric%20Space%20a96a5c7274d445188d654c88e86e43a0.md), Vitali Set (Vitali%20Set%20273c0f5171ec80b89ebbf64e1c55fa26.md)

> In this note, we explore the abstract concept of a **measure**, unifying it into a single powerful idea that brings together notions of  **size, probability, and integration - of objects.**
> 

> A **measure** is an abstract concept that provides a systematic way to assign a “size” or “weight” to objects, formalized as subsets of a given space, generalizing familiar notions such as **length, area, volume, or probability**.
> 

> This note will be organized around a key concept in theory called the **“Measure Space.”**
> 

> **Note:** The concept of a **measure** can be extended to more abstract notions—such as “distance,” “complexity,” or other generalized sizes—but here we focus on the simpler idea of **assigning a measure to an object or a class of objects**.
> 

## Measure Space

> In everyday life and mathematics, we often want to **quantify “how big” a set is**, whether it’s the length of an interval, the area of a region, or the probability of an event. At first glance, this seems easy for simple sets like intervals or rectangles. But as sets become more complicated, or when we work with infinite collections, these intuitive notions break down.
> 

A **measure space** provides a rigorous framework to handle this. It allows us to:

- **Assign size consistently** to very general sets, not just simple shapes.
- **Integrate functions** overcomplicated domains, which is the backbone of calculus and probability.
- **Develop probability theory** formally, by treating probabilities as measures.
- **Handle limits and convergence** carefully, which is crucial in analysis and applications like physics, statistics, and engineering.

### Formulation

A **measure space** is a triple $(X, \mathcal{F}, \mu)$ where:

- $X$ – a set (the *space*).
- $\mathcal{F}$ – a σ-algebra of subsets of $X$ (the *measurable sets*).
- $\mu: \mathcal{F} \to [0, \infty]$ – a measure (the *size* of sets), satisfying:
    1. **Non-negativity:** $\mu(A) \ge 0$ for all $A \in \mathcal{F}$.
    2. **Null empty set:** $\mu(\emptyset) = 0$.
    3. **Countable additivity (σ-additivity):** For any countable collection $\{A_n\} \subseteq \mathcal{F}$ of disjoint sets: $\mu\Big(\bigcup_{n=1}^\infty A_n\Big) = \sum_{n=1}^\infty \mu(A_n)$/

### Instances(s)

> See more in [**Integral Operator**](integral-operator.md).
> 

| Space | Measure | Description |
| --- | --- | --- |
| **Finite Set** (e.g., $X = \{a, b, c\}$) | **Counting Measure** ($\mu$) | The measure of a subset is the number of elements in it. Example: $\mu(\{a, c\}) = 2$. This is the fundamental concept of "size" for discrete spaces. |
| **Power Set** ($\mathcal{P}(\mathbb{N})$) | **Counting Measure** ($\mu$) | Extends the counting measure to infinite sets. The measure of a set is its cardinality (e.g., $\mu(\text{even numbers}) = \aleph_0$). |
| $\mathbb{R}$ (Real Line) | **Lebesgue Measure** ($\lambda$) | The standard generalization of "length." For an interval $[a, b]$, $\lambda([a, b]) = b - a$. Measures all sets in the Lebesgue $\sigma$-algebra, which is much larger than just intervals. |
| $\mathbb{R}^n$ (n-dimensional Euclidean space) | **Lebesgue Measure** ($\lambda^n$) | Generalizes length ($n=1$), area ($n=2$), and volume ($n=3$). For an $n$-dimensional rectangle, its measure is the product of its side lengths. |
| **Any Measurable Space** $(X, \Sigma)$ | **Dirac Measure** ($\delta_x$) | A "point mass" concentrated at $x \in X$. For any set $A \in \Sigma$, $\delta_x(A) = 1$ if $x \in A$, and $0$ otherwise. |
| **Any Measurable Space** $(X, \Sigma)$ | **Probability Measure** ($\mathbb{P}$) | A measure where $\mathbb{P}(X) = 1$. The measure of any event (measurable set) is between 0 and 1, representing its probability. |
| **Set of Outcomes** (e.g., $\{H, T\}$) | **Probability Measure** ($\mathbb{P}$) | For a fair coin: $\mathbb{P}(\{H\}) = 0.5$, $\mathbb{P}(\{T\}) = 0.5$, $\mathbb{P}(\{H, T\}) = 1$. A concrete example of a probability measure. |
| **Arbitrary Set** $X$ | **Zero Measure** ($\mu$) | Defined by $\mu(A) = 0$ for all $A \in \Sigma$. A trivial but theoretically important example. |
| **Function Space** | **Wiener Measure** | A probability measure on the space of continuous functions. Describes the probability distribution of Brownian motion, fundamental in stochastic calculus. |
|  | **Haar Measure** |  |

## Zero Measure Set

> A **zero measure set** (or null set) is a set $A \subset X$ such that $\mu(A) = 0$.
> 

> These sets are often “ignored” in measure-theoretic statements, leading to concepts like “almost everywhere.”
> 

## Measurable Set

> A **measurable set** is any set $A \subset X$ that belongs to the $\sigma$-algebra $\Sigma$.
> 

> Only measurable sets can be assigned a measure $\mu(A)$.
> 

## Non-Measurable Set

> A **non-measurable set** is a set that does **not** belong to the $\sigma$-algebra $\Sigma$.
> 

> Such sets cannot be assigned a consistent measure.
> 

## Measurable Function

> A measurable function $f: X \to \mathbb{R}$ is a function such that for every Borel set $B \subset \mathbb{R}$, the preimage $f^{-1}(B)$ is measurable: $f^{-1}(B) \in \Sigma$.
> 

> **Measurable functions** allow us to define integrals and expectations in **measure theory**.
> 

## Result

| **Result** | **Note** | **Description** |
| --- | --- | --- |
| **Monotonicity of Measures** | Measures are monotone | If $A \subseteq B$, then $\mu(A) \le \mu(B)$. This ensures that larger sets cannot have smaller measure. |
| **Countable Additivity** | Core property of measures | For a countable sequence of disjoint measurable sets $(A_n)$, $\mu\big(\bigcup_{n=1}^{\infty} A_n\big) = \sum_{n=1}^{\infty} \mu(A_n)$. |
| **Continuity from Below** | Increasing sequences | If $A_1 \subseteq A_2 \subseteq \dots$, then $\mu\big(\bigcup_n A_n\big) = \lim_{n\to\infty} \mu(A_n)$. |
| **Continuity from Above** | Decreasing sequences | If $A_1 \supseteq A_2 \supseteq \dots$ and $\mu(A_1)<\infty$, then $\mu\big(\bigcap_n A_n\big) = \lim_{n\to\infty} \mu(A_n)$. |
| **Null Sets** | Zero measure sets | A set $N$ with $\mu(N)=0$ is negligible; adding or removing it does not affect the measure of other sets. |
| **Carathéodory Extension Theorem** | Measure extension | Any pre-measure on an algebra can be uniquely extended to a complete measure on the generated σ-algebra. |
| **Fatou’s Lemma** | Limit inferior of integrals | For non-negative measurable functions $f_n$, $\int \liminf f_n \le \liminf \int f_n$. |
| **Monotone Convergence Theorem (MCT)** | Increasing sequences | If $f_n \uparrow f$, then $\lim_{n\to\infty} \int f_n = \int f$. |
| **Dominated Convergence Theorem (DCT)** | Convergence under domination |  |
| **Non-Measurable Sets Exist** | Vitali set example | Not all subsets of $\mathbb{R}$ are Lebesgue-measurable; shows limits of measure theory. |
| **Measure of Cartesian Product** | Fubini-Tonelli | For σ-finite measures, $\int_{X\times Y} f d(\mu\times\nu) = \int_X \int_Y f(x,y) d\nu(y) d\mu(x)$. |

## QA

- What is the relationship between measure theory and topology?
- Which is the relation of measure theory and functional analysis?
- Which is the relation of measure theory and Geometry?

## References

- [Set Theory](https://app.notion.com/p/Set-Theory-7f150c9c26fe407fbc9f40f810600d3f?pvs=21)
- https://en.wikipedia.org/wiki/Measurable_space
- https://en.wikipedia.org/wiki/Measurable_function
- https://en.wikipedia.org/wiki/Measure_(mathematics)
- https://en.wikipedia.org/wiki/Category_of_measurable_spaces
- [‣](https://app.notion.com/p/10e598edb79081089cd8fed69a3303c9?pvs=21)
- [‣](https://app.notion.com/p/272598edb790807d9d73d6a2b3dcba1e?pvs=21)
- [‣](https://app.notion.com/p/113598edb79080618a61f83cdcce36fb?pvs=21)
- [https://www.notion.so/Axler-S-2020-Measure-integration-real-analysis-Springer-Nature-273598edb7908035a918e6059e5fb3f3?v=10e598edb7908185b165000c521c82a8&source=copy_link](https://www.notion.so/Axler-S-2020-Measure-integration-real-analysis-Springer-Nature-273598edb7908035a918e6059e5fb3f3?v=10e598edb7908185b165000c521c82a8&source=copy_link)
- https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/
- [‣](https://app.notion.com/p/273598edb79080a5bf02f50f392b9b98?pvs=21)
- [https://web.math.princeton.edu/~js129/PDFs/teaching/MAT425_spring_2025/MAT425_Lecture_Notes.pdf](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT425_spring_2025/MAT425_Lecture_Notes.pdf)
- https://www.youtube.com/playlist?list=PLo4jXE-LdDTQq8ZyA8F8reSQHej3F6RFX
- https://www.youtube.com/playlist?list=PLLyj1Zd4UWrO6VtBSiQLsNlo9QBm30nxC
- https://www.youtube.com/playlist?list=PLBh2i93oe2qvMVqAzsX1Kuv6-4fjazZ8j
- https://www.youtube.com/playlist?list=PL0vEWJI_pj7RZ51zecINlzWxpFv83r8RE
- https://www.youtube.com/playlist?list=PLgMDNELGJ1CYKDzKdGcM1-kuH_a1NCfQA
- https://en.wikipedia.org/wiki/Category_of_measurable_spaces
