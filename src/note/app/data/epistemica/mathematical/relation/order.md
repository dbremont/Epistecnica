---
tags: [relation]
---

# Order

 : Set (Set%20176c0f5171ec800f8b41f66b6d8cc5b3.md), Relation (Relation%20185c0f5171ec80a4beeccf2fce06871c.md)

> In **mathematics**, the concept of **order** is formalized as a **relation** that organizes elements of a set according to a specific structure. It captures the idea of “which element comes before or after another” or “how elements are comparable” in a rigorous way.
> 

> **Order captures the deep idea of structured comparability under constraint**: it specifies when elements can be meaningfully related, in which direction, and with what logical consequences (such as hierarchy, succession, or extremality).
> 

> `A` can account for `B` - it’s but not `B` for `A`.   Extends Equality - trying to … Information Increasing in one direction, covers,  *subsumes.*
> 

## Taxonomy

| **Type** | **Definition** | Case |
| --- | --- | --- |
| **Partial Order** | A relation $\leq$ on $S$ that is **reflexive** ($a \le a$), **antisymmetric** ($a \le b \land b \le a \implies a = b$), and **transitive** ($a \le b \land b \le c \implies a \le c$). Not all elements need to be comparable. | Subsets under inclusion ($\subseteq$), divisibility of integers |
| **Total (Linear) Order** | A partial order where every pair of elements is **comparable**: for all $a, b \in S$, either $a \le b$ or $b \le a$. | Natural numbers $\mathbb{N}$ with $\le$, real numbers $\mathbb{R}$ with $\le$ |
| **Well-Order** | A total order where every **non-empty subset has a least element**. | $\mathbb{N}$ with $\le$ |
| **Lexicographic Order** | Order on tuples where comparison is done component-wise in sequence. | Dictionary order on words, tuples $(x,y)$ with $(a,b)<(c,d)$ if $a<c$ or $a=c$ and $b<d$ |
| **Partial Order in Graphs (Posets)** | Elements of a partially ordered set can be represented as nodes, with edges indicating order. | Task scheduling, dependency graphs |
| **Causal  (Topological Order)** | Ordering respecting a dependency or causality relation in a directed acyclic graph (DAG). | Job sequences, topological sorting |

## Ordered Set

> 

## Representation

> How to represent an ordered set?
> 

## Related

> Which are the related concepts?
> 

| **Concept** | **Definition** | **Case** |
| --- | --- | --- |
| **Monotonicity** | Property of a function between ordered sets where the order is preserved: $x \le y \Rightarrow f(x) \le f(y)$. | Increasing sequences, order-preserving maps in algorithms, cumulative distribution functions. |
| **Chain** | A totally ordered subset of a partially ordered set. | Subset of numbers $\{1,2,3\}$ in a partially ordered set; sequences in task scheduling. |
| **Filtration** | A nested sequence of substructures (e.g., subspaces or subgroups) ordered by inclusion. | Filtration of vector spaces in algebraic topology or signal processing. |
| **Dominance** | Ordering of elements (often vectors) based on aggregated or cumulative criteria. | Majorization of probability distributions; Pareto efficiency in economics. |
| **Lattice** | A partially ordered set where every pair of elements has a **least upper bound** (join) and **greatest lower bound** (meet). | Boolean algebra, set inclusion lattice, hierarchical clustering structures. |

## References

- https://en.wikipedia.org/wiki/Order_theory
- https://en.wikipedia.org/wiki/Partially_ordered_set
