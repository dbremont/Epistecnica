# Subshift

 : Subshift of Finite Type (Subshift%20of%20Finite%20Type%20273c370f795e4ba8a79b6fd9cf33f4ab.md)

> A **subshift** captures the idea of **global behavior constrained by local rules**, by forbidding certain patterns from ever appearing in infinite configurations.
> 

## Breviarium

A **subshift** is a set of bi-infinite sequences (or configurations) over a finite alphabet that is:

- **Shift-invariant** (stable under the shift map), and
- **Closed** in the product topology.

In Essence:

- You start with **all possible infinite sequences** over some alphabet.
- Then, you **forbid some finite patterns** from appearing **anywhere** in those sequences.
- The set of sequences that **never** contain those forbidden patterns forms the **subshift**.

This concept allows us to:

- **Model systems with local constraints** (e.g., no two cars next to each other, no illegal symbols, no conflicting states).
- **Study dynamical systems** defined over symbolic sequences (symbolic dynamics).
- Formally describe the **state space** of systems like **cellular automata**, **tilings**, or **grammar-based systems**.

## Formal Definition

Let:

- $A$ be a finite **alphabet** (e.g., $A = \{0,1\}$),
- $A^{\mathbb{Z}}$ be the set of all **bi-infinite sequences** over $A$: $x = (\dots, x_{-2}, x_{-1}, x_0, x_1, x_2, \dots), \quad x_i \in A$
- The **shift map** $\sigma : A^{\mathbb{Z}} \to A^{\mathbb{Z}}$ is defined by:  $(\sigma(x))_n = x_{n+1}$
- (it shifts every element one position to the left).

A **subshift** $X \subseteq A^{\mathbb{Z}}$ is a set such that:

- $\sigma(X) = X$ (**shift-invariant**), and
- $X$ is **closed** in the product topology (i.e., limits of sequences in $X$ also belong to $X$).

## 🔹 Types of Subshifts

| Type | Description |
| --- | --- |
| **Full shift** | All sequences in $A^{\mathbb{Z}}$ (no forbidden patterns) |
| **Subshift of finite type (SFT)** | Defined by a **finite** set of forbidden patterns |
| **Sofic shift** | Image of an SFT under a sliding block code |

## References

- …
