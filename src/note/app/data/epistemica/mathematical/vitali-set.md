# Vitali Set

 : Measure (Measure%20273c0f5171ec80ae812dc3c73aad95dc.md), Set (Set%20176c0f5171ec800f8b41f66b6d8cc5b3.md)

> The construction of the Vitali set was [Giuseppe Vitali’s](https://en.wikipedia.org/wiki/Giuseppe_Vitali) answer to a challenge posed by [Henri Lebesgue](https://en.wikipedia.org/wiki/Henri_Lebesgue): is there a subset of the real numbers that cannot be measured?
> 

## Problem Formulation

> The problem is to determine whether such a measure $\lambda$ can be consistently defined on **all** subsets of $\mathbb{R}$.
> 

> Let us define a measure $\lambda: \mathcal{P}(\mathbb{R}) \to [0,\infty]$  on subsets of $\mathbb{R}$ with the following properties:
> 

 $\lambda$: P($\mathbb{R}$) →  on subsets of $\mathbb{R}$ with the following properties:

1. **Non-negativity:** $\lambda(A) \geq 0$ for all $A \subseteq \mathbb{R}$.
2. **Normalization:** $\lambda([0,1]) = 1$.
3. **Countable additivity:** If $\{A_n\}$ are pairwise disjoint subsets, then $\lambda\!\Big(\bigcup_{n=1}^\infty A_n\Big) = \sum_{n=1}^\infty \lambda(A_n).$
4. **Translation invariance:** For all $t \in \mathbb{R}$ and $A \subseteq \mathbb{R}$, $\lambda(A+t) = \lambda(A)$,
    
    where $A+t = \{x+t : x \in A\}$.
    

## Vitali Proof

> **The Vitali Strategy:** This is a proof by **contradiction**. We start by assuming that a certain set is measurable and attempt to assign it a measure. Although the set is bounded, applying the properties of a measure leads to a value that is either too large or too small—outside the bounds of the interval. Therefore, our assumption must be false, and the set is **not measurable**.
> 

> A key idea in designing a non-measurable set is to create an **infinite partition** of the interval $[0,1]$. In the Vitali construction, this is done by considering the equivalence relation $x \sim y \quad \text{if and only if} \quad x - y \in \mathbb{Q}.$ This partitions $[0,1]$ into **uncountably many equivalence classes**. By selecting exactly one representative from each class (using the axiom of choice), we obtain a set $V$ — the **Vitali set**.
> 

> The crucial point is that the rational shifts of $V$, $V + q$ for $q \in \mathbb{Q} \cap [0,1]$, attempt to form an **infinite collection of disjoint “equal-measure pieces”** inside a bounded interval. If $V$ were measurable, countable additivity would force the total measure of these pieces to be either $0$ or infinite, both of which are impossible since they lie inside $[0,1]$.
> 

> Thus, the **infinite partition via rational equivalence** directly leads to the conclusion that $V$ is **not measurable**.
> 

> These sets evade measurability because the measure axioms + translation invariance + infinite partition don’t allow such pathological choices to be consistently measured.
> 

## References

- https://en.wikipedia.org/wiki/Vitali_set
- Vitali Set → [https://ocw.mit.edu/courses/24-118-paradox-and-infinity-spring-2019/09d491697f75ff86fe2fb226e199331a_MIT24_118S19_LecNote14.pdf](https://ocw.mit.edu/courses/24-118-paradox-and-infinity-spring-2019/09d491697f75ff86fe2fb226e199331a_MIT24_118S19_LecNote14.pdf)
- https://www.youtube.com/watch?v=hs3eDa3_DzU
- https://en.wikipedia.org/wiki/Giuseppe_Vitali
- https://www.youtube.com/watch?v=llnNaRzuvd4&list=PLo4jXE-LdDTQq8ZyA8F8reSQHej3F6RFX
- https://en.wikipedia.org/wiki/Sigma-additive_set_function
- https://en.wikipedia.org/wiki/Non-measurable_set
