# Sobolev Space

 : Linear Space (Linear%20Space%20b935942a1a064729b3f2be42d174923a.md)

> A **Sobolev space** is a **functional space** that extends the concept of differentiability and integrability to a weak (distributional) framework, allowing the rigorous treatment of partial differential equations (PDEs) where classical differentiability may not hold.
> 

QA:

- What is $L^2$ means?
- …

## Formulation

Let $\Omega \subseteq \mathbb{R}^n$ be an open subset. For $k \in \mathbb{N} \cup \{0\}$ and $1 \leq p \leq \infty$, the **Sobolev space** $W^{k,p}(\Omega)$ is defined as:

$W^{k,p}(\Omega) := \left\{ u \in L^p(\Omega) \;\middle|\; D^\alpha u \in L^p(\Omega) \text{ for all multi-indices } \alpha \text{ with } |\alpha| \leq k \right\}$

where:

- $L^p(\Omega)$ is the usual Lebesgue space of $p$-integrable functions.
- $D^\alpha$ denotes the **distributional derivative** of order $\alpha \in \mathbb{N}_0^n$, i.e., $D^\alpha u$ is defined via: 
$\int_\Omega u(x) D^\alpha \varphi(x) \, dx = (-1)^{|\alpha|} \int_\Omega D^\alpha u(x) \varphi(x) \, dx, \quad \forall \varphi \in C_c^\infty(\Omega)$

## What is $L^2(0,1)$?

The space $L^2(0,1)$ is the set of all **square-integrable functions** on the interval $(0,1)$.

Formally:  $L^2(0,1) := \left\{ f : (0,1) \to \mathbb{R} \;\middle|\; \int_0^1 |f(x)|^2 \, dx < \infty \right\}$

### Intuition

- You're looking at all functions where the **square of the function is integrable**.
- The integral $\int_0^1 |f(x)|^2 \, dx$ can be thought of as a kind of "energy" or "length squared" of the function.
- The square integrability ensures that the function doesn't blow up too badly—e.g., you can't have vertical asymptotes with infinite area under the square.

### Properties

- It’s a **vector space**: you can add functions and multiply by scalars.
- It’s a **Hilbert space**, meaning it has an inner product:  $\langle f, g \rangle = \int_0^1 f(x) g(x) \, dx$
and corresponding norm:  $\|f\|_{L^2} := \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}$
- You can think of $L^2$ functions as **generalized functions** — even if they're not continuous, they’re still “tame” in the sense of being energetically bounded.

## Special Cases

- **Hilbert-Sobolev spaces**
- **Fractional Sobolev spaces**

## Distributional Framework

> The key insight is that **weak derivatives** $D^\alpha u$ are not defined pointwise but as distributions, making Sobolev spaces suitable for functions that are not classically differentiable. For example, the Heaviside function $H(x)$ belongs to $W^{1,p}_{\text{loc}}(\mathbb{R})$ for $p < \infty$, even though it is not classically differentiable at $x = 0$.
> 

## Embedding and Compactness Theorems

Sobolev spaces have deep analytical structure:

- **Sobolev Embedding Theorem**: Under suitable conditions on $\Omega$, there exists a continuous embedding: $W^{k,p}(\Omega) \hookrightarrow L^q(\Omega) \quad \text{for certain } q > p$ and even into spaces of continuous functions for high regularity.
- **Rellich–Kondrachov Compactness Theorem**: Under compactness assumptions on $\Omega$, the embedding $W^{k,p}(\Omega) \hookrightarrow L^q(\Omega)$ is compact for appropriate $q$, enabling variational techniques.

## Applications

Sobolev spaces form the **natural functional setting** for:

- Weak formulations of **elliptic PDEs** (e.g., variational solutions of the Poisson or Laplace equations).
- **Functional analysis of PDEs** via **Lax–Milgram lemma**, **Galerkin methods**, and **energy estimates**.
- **Calculus of variations**, where admissible function spaces are often Sobolev spaces.

## Case Study

> 

### $W^{1,2}(0,1)$ — also known as $H^1(0,1)$

> $H^1(0,1) = \{ u \in L^2(0,1) \mid u' \in L^2(0,1) \text{ (in the weak sense)} \}$
> 

This is the set of all real-valued functions $u: (0,1) \to \mathbb{R}$ such that:

1. $u \in L^2(0,1)$ (i.e., square-integrable),

2. the **weak derivative** $u' \in L^2(0,1)$ (i.e., the derivative in the distributional sense is also square-integrable).

## References

- https://en.wikipedia.org/wiki/Sobolev_space
