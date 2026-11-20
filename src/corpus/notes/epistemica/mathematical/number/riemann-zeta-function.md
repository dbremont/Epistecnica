---
tags: [note, mathematics, number-theory, analytic-number-theory]
---

# Riemann Zeta Function

> The **Riemann zeta function** $\zeta(s)$ is the analytic function that encodes the distribution of the prime numbers: its Dirichlet series is the sum over the integers, its Euler product is the product over the primes, and its zeros are the frequencies of the primes' fluctuations.

## Definition

For a complex variable $s = \sigma + it$ with $\sigma > 1$, the series converges absolutely:

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}.$$

The same function has an **Euler product**, obtained by expanding each factor geometrically and using unique factorization:

$$\zeta(s) = \prod_{p \text{ prime}} \left(1 - p^{-s}\right)^{-1}.$$

The product is the bridge that makes the zeta function arithmetic: the sum ranges over all integers, the product only over primes, and the identity holds because every integer is a unique product of primes. Taking logarithms turns the product into a sum over primes weighted by $p^{-s}$, which is why the analytic behaviour of $\zeta$ controls the distribution of primes.

## Analytic continuation

The series diverges at $s = 1$ and defines $\zeta$ only for $\sigma > 1$. Riemann's 1859 memoir continued it to the whole complex plane as a meromorphic function with a single **simple pole at $s = 1$** (residue $1$), and proved the **functional equation**

$$\zeta(s) = 2^{s} \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s)\, \zeta(1-s),$$

or, in the symmetric form with the completed zeta $\xi(s) = \tfrac{1}{2} s(s-1) \pi^{-s/2} \Gamma(s/2) \zeta(s)$:

$$\xi(s) = \xi(1-s).$$

The functional equation forces **trivial zeros** at the negative even integers $s = -2, -4, -6, \dots$ (from the sine factor), and leaves all other zeros in the **critical strip** $0 < \sigma < 1$. The line $\sigma = 1/2$ is the **critical line**.

## The Riemann Hypothesis

> **Every non-trivial zero of $\zeta(s)$ lies on the critical line $\sigma = 1/2$.**

Riemann stated it in 1859 and checked the first few zeros; it remains unproved. What is known:

- **Hardy (1914)** — infinitely many zeros lie on the critical line.
- **Selberg (1942)** — a positive proportion of the zeros lie on the line.
- **Conrey (1989)** — at least two-fifths; later work has pushed the proportion above 41 per cent.
- **Numerically** — the first ten trillion zeros have been verified to lie on the line.
- **Function fields** — the analogue is a theorem: Weil proved it for curves over finite fields, and Deligne's proof of the Weil conjectures extended the method.

The hypothesis is equivalent to a sharp bound on the error term in the prime number theorem (see below), and it is one of the Clay Mathematics Institute's Millennium Prize Problems.

## QA

### Why is it so difficult?

The difficulty comes from the interaction between several mathematical structures:

1. **Complex analysis** — analytic continuation and the properties of complex functions: $\zeta$ is defined beyond its series by continuation, and its zeros live where the series does not converge.
2. **Number theory** — prime distribution and multiplicative arithmetic: the Euler product ties the function to unique factorization, so an analytic statement becomes a statement about primes.
3. **Spectral theory** — connections between zeros and eigenvalues of mathematical operators: the Hilbert–Pólya programme reads the zeros as the spectrum of an unknown self-adjoint operator, which would make the line a consequence of self-adjointness.
4. **Harmonic analysis** — oscillatory behaviour and transformations of functions: the explicit formula expresses the primes as a sum of oscillations whose frequencies are the zeros.

The problem sits at the intersection, and no one structure has proved sufficient: the analytic estimates are too weak at the critical line, the arithmetic input is too rigid, and the operator that would make the spectral picture literal has not been found.

### Why does this matter for prime numbers?

The **explicit formula** (von Mangoldt) writes the weighted prime-counting function $\psi(x) = \sum_{p^k \le x} \log p$ as

$$\psi(x) = x - \sum_{\rho} \frac{x^{\rho}}{\rho} - \log(2\pi) - \tfrac{1}{2}\log\left(1 - x^{-2}\right),$$

where $\rho$ runs over the non-trivial zeros. Each zero contributes an oscillation $x^{\rho} = x^{\sigma} e^{it \log x}$: the real part $\sigma$ is the **amplitude** of the oscillation and the imaginary part $t$ is its **frequency**.

- The **prime number theorem** $\pi(x) \sim x/\log x$ is equivalent to $\zeta(s) \neq 0$ on $\sigma = 1$ — no zero may sit on the edge of the strip and dominate the error.
- The **Riemann hypothesis** says every amplitude is exactly $\sqrt{x}$, so the error in $\pi(x)$ is as small as $O(\sqrt{x}\log x)$ — the best possible order.
- The zeros therefore control the **gaps, fluctuations and apparent randomness** of the primes: the primes look random because their error term is a sum of incommensurable oscillations.

### What would a proof look like?

- **Hilbert–Pólya** — exhibit a self-adjoint operator whose eigenvalues are the imaginary parts of the zeros; self-adjointness forces the real part to $1/2$.
- **Random matrix theory** — Montgomery's pair-correlation conjecture and Odlyzko's numerics match the zeros to the eigenvalues of large random Hermitian matrices (GUE); a proof would have to explain why.
- **Function-field analogue** — Weil and Deligne proved the analogue by algebraic geometry; the hope is a translation to number fields.
- **Langlands programme** — treat $\zeta$ as the first of a family of automorphic $L$-functions, with the hypothesis generalizing to the whole family.
- **Trace formulas** — Connes' spectral realization of the zeros as a absorption spectrum of a classical dynamical system.

### What would it change?

- Sharper bounds for $\pi(x)$, the $n$-th prime, and prime gaps.
- Deterministic complexity bounds: under the generalized Riemann hypothesis, Miller's primality test is deterministic polynomial time, and many algorithm analyses improve.
- It would **not** break RSA or any current cryptography: factoring does not become easy, and the practical security of the schemes does not rest on the hypothesis.

## References

- Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer gegebenen Größe. *Monatsberichte der Berliner Akademie*.
- Titchmarsh, E. C. (1986). *The theory of the Riemann zeta-function* (2nd ed., rev. D. R. Heath-Brown). Oxford University Press.
- Edwards, H. M. (1974). *Riemann's zeta function*. Academic Press.
- Conrey, J. B. (2003). The Riemann hypothesis. *Notices of the American Mathematical Society*, 50(3), 341–353.
- Bombieri, E. (2000). *Problems of the Millennium: The Riemann Hypothesis*. Clay Mathematics Institute.
- Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. *Proceedings of Symposia in Pure Mathematics*, 24, 181–193.
- Odlyzko, A. M. (1987). On the distribution of spacings between zeros of the zeta function. *Mathematics of Computation*, 48(177), 273–308.
- Hardy, G. H. (1914). Sur les zéros de la fonction ζ(s) de Riemann. *Comptes Rendus de l'Académie des Sciences*, 158, 1012–1014.
- Selberg, A. (1942). On the zeros of Riemann's zeta-function. *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo*.
- Weil, A. (1948). *Sur les courbes algébriques et les variétés qui s'en déduisent*. Hermann.
- Deligne, P. (1974). La conjecture de Weil. I. *Publications Mathématiques de l'IHÉS*, 43, 273–307.
- [Riemann zeta function — Wikipedia](https://en.wikipedia.org/wiki/Riemann_zeta_function)
- [Riemann hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis)
- [Riemann Hypothesis — Clay Mathematics Institute](https://www.claymath.org/millennium/riemann-hypothesis/)

## Read it with

- [Gamma Function](/view.html?p=notes/epistemica/mathematical/mapping/gamma-function.md) — the completed zeta and the functional equation.
- [Analytic Function](/view.html?p=notes/epistemica/mathematical/complex/analytic-function.md) — the class the continuation lives in.
- [Holomorphic Function](/view.html?p=notes/epistemica/mathematical/complex/holomorphic-function.md) — the local structure behind the zeros.
- [Elliptic Function](/view.html?p=notes/epistemica/mathematical/complex/elliptic-function.md) and [Modular Form](/view.html?p=notes/epistemica/mathematical/complex/modular-form.md) — the automorphic family the zeta function opens.
- [Number](/view.html?p=notes/epistemica/mathematical/number/number.md) — the integers the Euler product sums over.
