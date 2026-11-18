---
tags: [note, mathematics, analysis, functional-analysis]
---

# Schwartz Space

> The **Schwartz space** $\mathcal{S}(\mathbb{R}^n)$ is the space of smooth functions that, together with every derivative, decay faster than any polynomial. It is the smallest natural home in which **differentiation and the Fourier transform are both everywhere defined and continuous** — which is why it is the standard test space of distribution theory.

## Definition

> A smooth function $f \in C^\infty(\mathbb{R}^n)$ belongs to $\mathcal{S}$ when every seminorm
> $$p_{\alpha,\beta}(f) = \sup_{x \in \mathbb{R}^n} \left| x^\alpha \, \partial^\beta f(x) \right|$$
> is finite, for all multi-indices $\alpha, \beta$. The family $\{p_{\alpha,\beta}\}$ gives the topology: a **countably normed** space, hence a Fréchet space, not a Banach space.

> Two equivalent characterisations are worth having. $\mathcal{S}$ is the intersection of the weighted Sobolev spaces $\bigcap_{k,m} H^{k,m}$, and it is the space on which the operator $(1+|x|^2)^{m}(1-\Delta)^{k}$ is bounded for every $m,k$. The first is useful for proofs of completeness; the second for the intuition that decay and smoothness trade against each other.

## Properties

| Property | Statement |
| --- | --- |
| **Closure** | Closed under differentiation, under multiplication by polynomials, and under convolution with $\mathcal{S}$ functions |
| **Density** | Dense in $L^p(\mathbb{R}^n)$ for every $1 \le p < \infty$ |
| **Inclusions** | Continuously included in $L^p$, in $C_0$ (vanishing at infinity), and in every weighted $L^p$ |
| **Fourier** | $\mathcal{F}: \mathcal{S} \to \mathcal{S}$ is a homeomorphism, with $\mathcal{F}^{-1}$ of the same form |
| **Duals** | $\mathcal{S}'$, the tempered distributions, contains $L^p$, $C_0'$, the delta, and the derivatives of bounded functions |

> The Fourier property is the one that matters. On $L^1$ the transform exists but does not map back; on $L^2$ it is an isometry but differentiation is not internal; on $\mathcal{S}$ both operations are defined everywhere and continuous, and they exchange: $\mathcal{F}(\partial_j f) = i\xi_j \mathcal{F}(f)$, $\mathcal{F}(x_j f) = i\partial_j \mathcal{F}(f)$. That exchange is the whole reason the space is used.

## What is in, and what is not

| Function | In $\mathcal{S}$? | Why |
| --- | --- | --- |
| $e^{-x^2}$ (Gaussian) | **Yes** | Smooth, decays faster than any polynomial |
| $x^k e^{-x^2}$ | **Yes** | Polynomial growth is dominated by the decay |
| $\phi \in C_c^\infty$ (test functions) | **Yes** | Compact support is the strongest decay |
| $e^{-|x|}$ | **No** | Not smooth at the origin |
| $\frac{1}{1+x^2}$ | **No** | Decays like $x^{-2}$, slower than every polynomial asks |
| A polynomial | **No** | Does not decay |
| $\sin(x^2)$ | **No** | Bounded but oscillating: the derivative grows without bound, so a seminorm diverges |

> The table is the definition read backwards: membership is a statement about the **product of growth and decay**, and the space is arranged so that functions are neither too big at infinity nor too rough anywhere.

## Why the space exists

> The Schwartz space is the technical answer to a trust problem in analysis. Classical analysis wants to differentiate functions, integrate them, and Fourier-transform them, and no single classical function space supports all three without caveats — differentiability is too strong for $L^p$, integrability too weak for derivatives, and the Fourier transform is an isometry only on $L^2$. $\mathcal{S}$ is the **compromise space** where all three are internal, and the dual $\mathcal{S}'$ is the space where the operations are then extended by continuity.

> This is the pattern of a good test space, and it is worth naming because it recurs: the space must be **small** enough that its dual is **large** (every tempered distribution is a continuous functional on it, including the delta and the derivatives of non-differentiable functions), and **large** enough that the operations one wants to distribute are defined inside it. The Schwartz space is the canonical example, and the reason the theory of distributions does not need a case analysis for each operation.

## References

- [Schwartz space — Wikipedia](https://en.wikipedia.org/wiki/Schwartz_space)
- [Tempered Distribution](/view.html?p=notes/epistemica/mathematical/mapping/distribution/tempered-distribution.md) — the dual, and the reason the space is defined
- [Test Function](/view.html?p=notes/epistemica/mathematical/mapping/distribution/test-function.md) — the compactly supported subspace
- [Distribution](/view.html?p=notes/epistemica/mathematical/mapping/distribution/distribution.md) — the general theory
- [Dirac Delta Function](/view.html?p=notes/epistemica/mathematical/mapping/distribution/dirac-delta-function.md) — the tempered distribution that motivates the construction
- [Function Space](/view.html?p=notes/epistemica/mathematical/space/function-space.md) — the family this space belongs to
- [Hilbert Space](/view.html?p=notes/epistemica/mathematical/space/hilbert-space.md) — the completion, where the Fourier transform becomes an isometry
