---
tags: [relation]
---

# Equivalence Relation

 : Knot (Knot%201d6c0f5171ec80a09a74d226b53f7ee3.md), Foliation (Foliation%20207c0f5171ec80c8a718cb55a1213e9d.md)

> An **equivalence relation** is a relation $\sim$ on a set $S$ that groups elements into classes based on a notion of “sameness” or equivalence.
> 

## Formulation

Formally, a relation $\sim$ is an equivalence relation if it satisfies three **properties**:

1. **Reflexive:** Every element is related to itself. $\forall a \in S, \quad a \sim a$
2. **Symmetric:** If one element is related to another, the reverse is also true. $\forall a,b \in S, \quad a \sim b \implies b \sim a$
3. **Transitive:** If an element is related to a second, and the second to a third, then the first is related to the third. $\forall a,b,c \in S, \quad a \sim b \ \text{and} \ b \sim c \implies a \sim c$

## **Equivalence Class**

> Given a set $S$ and an equivalence relation $\sim$ on $S$, the **equivalence class** of an element $a \in S$ is the subset of all elements in $S$ that are equivalent to $a$.
> 

> Think of **equivalence classes** as **piles of objects that are “the same kind”** according to your chosen rule.
> 

Formally: $[a] = \{ x \in S \mid x \sim a \}$

- **Notation:** $[a]$ denotes the equivalence class of $a$.
    - Note: [a] is not specially - but a instance of the equivalence class  - any instance will do. An equivalence class is not “owned” by a particular element.  It is a **set of mutually equivalent elements**, and every member generates the same class.
- **Properties:**
    1. Each element of $S$ belongs to exactly **one equivalence class**.
    2. Equivalence classes **partition the set** $S$ into disjoint subsets.
    3. If $[a] \cap [b] \neq \emptyset$, then $[a] = [b]$.

## Case

| Set $S$ | Equivalence Relation $\sim$ | Equivalence Classes |
| --- | --- | --- |
| Integers $\mathbb{Z}$ | $a \sim b$ if $a - b$ is divisible by 3 | $[0] = \{..., -3,0,3,...\}$, $[1] = \{..., -2,1,4,...\}$ |
| Strings | $a \sim b$ if $a$ and $b$ have the same length | $[“cat”] = \{“dog”, “sun”, …\}$ |
| Real numbers $\mathbb{R}$ | $a \sim b$ if $\lfloor a \rfloor = \lfloor b \rfloor$ | $[2.3] = [2,2.5,2.9] = \{ x \in \mathbb{R} : 2 \le x < 3\}$  |

## References

- https://en.wikipedia.org/wiki/Equivalence_class
- https://en.wikipedia.org/wiki/Equivalence_relation
