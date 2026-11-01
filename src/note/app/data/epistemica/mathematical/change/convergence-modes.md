---
tags: [analytical, dynamical-system]
---

# Modes of Convergence

> A sequence of random quantities can converge in several inequivalent senses — almost surely, in probability, in $L^p$, and in distribution — and the differences between them are the substance of probability theory.

## Formulation

> **What it is.** The taxonomy of "approaches a limit" once the objects are random. Each mode weakens or strengthens another, and most of probability's machinery exists to move between them.
>
> **Type.** A `Concept` — a discriminator of limit behaviour, extending the deterministic [convergence](convergent.md) of real analysis.
>
> **Boundary.** Deterministic [limits](limit.md) are one notion; with randomness the question "how close" must be paired with "in what sense", and the answers differ. Confusing the modes is the standard error in applied work.

## The ladder

| Mode | Statement | Implies |
| --- | --- | --- |
| **Almost sure** | $P(X_n \to X) = 1$ | convergence in probability |
| **In $L^p$** | $E|X_n - X|^p \to 0$ | convergence in probability |
| **In probability** | $P(|X_n - X| > \varepsilon) \to 0$ | convergence in distribution |
| **In distribution** | $F_n(x) \to F(x)$ at continuity points | — (weakest) |

## Key results

- **Implications.** $L^p \Rightarrow$ in probability $\Rightarrow$ in distribution; almost sure $\Rightarrow$ in probability. None of the reverse implications holds in general.
- **Borel–Cantelli.** Links almost-sure convergence to summability of tail probabilities — the standard proof technique.
- **Slutsky.** Convergence in distribution survives addition and multiplication by sequences converging in probability — the workhorse of asymptotic statistics.
- **Tightness.** Convergence in distribution is compactness in the space of measures; Prokhorov's theorem is the bridge to the analytic notion of [weak convergence](../space/weak-convergence.md).

## References

- https://en.wikipedia.org/wiki/Convergence_of_random_variables
- [Limit](limit.md) · [Convergent](convergent.md) · [Weak Convergence](../space/weak-convergence.md) · [Random Variable](../../observational/probability/random-variable.md)
