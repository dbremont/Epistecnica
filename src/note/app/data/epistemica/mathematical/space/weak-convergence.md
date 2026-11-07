---
tags: [analytical, space, mathematics]
---

# Weak Convergence

> A sequence $x_n$ **converges weakly** to $x$ in a normed space when every continuous linear functional sees it converge: $\varphi(x_n) \to \varphi(x)$ for all $\varphi \in X^*$. Norm convergence implies it; the converse fails in infinite dimension.

## Formulation

> **What it is.** The topology a space inherits from its [dual](../structure/duality.md): points are indistinguishable when no functional can tell them apart. It exists because the norm topology is too strong for compactness in infinite dimension.
>
> **Type.** A `Concept` — a topology on a vector space, defined by a pairing.
>
> **Boundary.** Weak convergence is not convergence of the objects themselves: an orthonormal basis converges weakly to zero while its norm stays $1$. That gap is the content of the notion, not a defect.

## Key results

- **Banach–Alaoglu.** The closed unit ball of a dual space is weak-* compact — the compactness theorem that makes existence proofs in the calculus of variations work.
- **Eberlein–Šmulian.** In a Banach space, weak compactness is equivalent to weak sequential compactness.
- **Reflexivity.** In a reflexive space the unit ball is weakly compact; $L^p$ with $1<p<\infty$ and Hilbert spaces are reflexive, $L^1$ and $L^\infty$ are not.
- **Variational use.** A minimizing sequence that is bounded has a weakly convergent subsequence, and lower semicontinuity passes the limit to the infimum — the standard direct method.

## References

- https://en.wikipedia.org/wiki/Weak_convergence_(Hilbert_space)
- https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem
- [Banach Space](banach-space.md) · [Hilbert Space](hilbert-space.md) · [Duality](../structure/duality.md) · [Modes of Convergence](../change/convergence-modes.md)
