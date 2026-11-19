---
tags: [note, mathematics, representation, analysis, series]
qa:
 - Is the Taylor representation a representation of the function or of its germ at the point — and where does the difference bite when the function is smooth but not analytic?
 - The series is exact and the truncation is the approximation; which of the two does a numerical method actually use, and what does it inherit from the other?
 - Every representation turns operations into algebra. What does the Taylor representation make algebraic that the Fourier representation does not — and what does it lose in exchange?
---

# Taylor Representation

> The **Taylor representation** writes a [function](/view.html?p=notes/epistemica/mathematical/mapping/function.md) as a combination of the powers of $x-a$, with the coefficients fixed by the derivatives of the function at the point $a$. Its blocks are the powers of $x-a$; its coefficients are the derivatives. That conversion — local behaviour at a point becoming a sequence of numbers — is the whole of the representation, and everything it is useful for follows from it.

$$f(x)=\sum_{k\ge 0}\frac{f^{(k)}(a)}{k!}\,(x-a)^k
\qquad\text{with}\qquad
f^{(k)}(a)=\left.\frac{d^k f}{dx^k}\right|_{x=a}$$

> The same expansion is taken for a [map](/view.html?p=notes/epistemica/mathematical/mapping/map.md) between spaces where a derivative and a power make sense — in a Banach space, in several variables, and in the formal setting of a polynomial ring. Published by [Brook Taylor](/view.html?p=notes/social/actor/private/persona/brook-taylor.md) in the *Methodus incrementorum* (1715a; title page 1717); see [Taylor series](https://en.wikipedia.org/wiki/Taylor_series).

## 1. The representation

A representation is a choice of building blocks, and the Taylor representation is the choice of the powers of $x-a$. The choice fixes the coefficients: if $f$ is to be a combination of those blocks, the $k$-th coefficient must be $f^{(k)}(a)/k!$, because the blocks are linearly independent and the derivatives read them off one at a time. Nothing else is available to vary — the point $a$ is the only other parameter, and it selects *where* the local description is taken rather than what the description is made of.

The family it belongs to, with each member's blocks:

| Representation | Building blocks | Coefficients fixed by |
| --- | --- | --- |
| **Taylor representation** | Powers of $x-a$ | Derivatives at $a$ |
| [Fourier representation](/view.html?p=notes/epistemica/signal/fourier-series.md) | Sines and cosines | Inner products against the basis |
| Laurent representation | Positive and negative integer powers | Contour integrals around the annulus |
| [Power series representation](/view.html?p=notes/epistemica/mathematical/change/power-series.md) | Integer powers of a variable | Derivatives at the centre, as a special case |
| [Chebyshev representation](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) | Chebyshev polynomials | Projection under the weight $1/\sqrt{1-x^2}$ |
| [Wavelet representation](/view.html?p=notes/epistemica/signal/wavelet.md) | Wavelets | Inner products at each scale and position |

Read down the table and the representations differ in exactly two things: what the blocks are, and how the coefficients are extracted. The Taylor representation is the one whose extraction is purely local — no integral, no weight, no scale — which is why it is the cheapest to compute where the derivatives are known and the most fragile where they are not.

## 2. What the conversion buys

Three consequences follow from the conversion, and they are what the representation is for.

**Local data becomes a sequence.** The function near $a$ is replaced by the list $f(a), f'(a), f''(a),\dots$ Two functions with the same list are indistinguishable in a neighbourhood of $a$ — they have the same *germ*. That is a gain where the question is local (a maximum, a stability, a linearisation) and a loss where it is not: the sequence says nothing about the function a domain away.

**Operations become algebra.** Differentiation multiplies the $k$-th coefficient by $k$ and shifts the index down; integration divides by $k$ and shifts it up; sum, product and composition are the ring operations on formal power series in $R[[x]]$. A differential problem becomes an algebraic one, which is the sense in which this is a *representation* and not merely an expansion: the structure is transported, not approximated.

**Truncation becomes an approximation.** Cutting the sequence at degree $n$ leaves a polynomial, and the error is controlled by Taylor's theorem with remainder — the Lagrange, Cauchy or integral form according to what regularity is available. The magnitude of the remainder, not the size of the coefficients, is what says whether the truncation is usable.

## 3. The germ, and where the representation fails

The representation is of the **germ**, and a germ is not a function. The series converges on a disc whose radius is the distance from $a$ to the nearest singularity of $f$, and inside that disc it sums to $f$ if $f$ is analytic there. Two failures are worth keeping apart:

- **Convergence.** The series may have a finite radius — $1/(1-x)$ at $a=0$ has radius $1$ — so the representation is local in a second sense, bounded by the nearest obstruction.
- **Summation.** A smooth function need not be analytic: $f(x)=e^{-1/x^2}$ with $f(0)=0$ has $f^{(k)}(0)=0$ for every $k$, so its Taylor representation at $0$ is the zero series. The sequence is faithful to the germ and the germ is not the function. Smoothness is not enough; analyticity is exactly the condition under which the representation determines its object.

This is the precise content of the note's first QA question, and the reason the Taylor representation is the standard counterexample to "a representation loses nothing": it can lose everything, silently, on a set of functions that looks no different from the analytic ones.

## 4. Series and truncation are different objects

The infinite series is the representation. The finite Taylor polynomial is an *approximation* in that representation. They are so often conflated that the polynomial is called the series, and the conflation has consequences:

- the series may converge where no truncation is accurate, and a truncation may be useful well outside the radius of convergence (asymptotic expansions, where the series diverges but the early terms are excellent);
- a truncation inherits the local character of the representation — it describes $f$ near $a$ — but not its exactness, so error analysis is about the remainder and never about the coefficients alone;
- the truncation is a polynomial, so it lives in the ring this corpus treats under [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md); the representation lives in the ring of formal power series, and the passage between them is where the approximation theory sits.

## 5. Where it sits in the corpus

The Taylor representation is the linearisation used everywhere in these notes: [Differential Operator](/view.html?p=notes/epistemica/mathematical/change/differential-operator.md) is its infinitesimal form, [Perturbation Method](/view.html?p=notes/epistemica/mathematical/method/approximation/perturbation-method.md) approximates in this representation and then asks when the result is uniform, [Integral Operator](/view.html?p=notes/epistemica/mathematical/change/integral-operator.md) is its continuous counterpart — the sum over powers of $x-a$ replaced by an integral over a continuum, and the inverse of the difference where the Taylor representation is the inverse of a derivative. The family it belongs to is [Representation](/view.html?p=notes/epistemica/mathematical/method/representation.md).

## References

- [Taylor, B. (1715a). *Methodus incrementorum directa et inversa*. William Innys.](/view.html?p=documents/books/taylor-1715-methodus-incrementorum-directa-et-inversa-innys.md) — the theorem stated, in the book that also created the calculus of finite differences
- Rudin, W. (1976). *Principles of mathematical analysis* (3rd ed.). McGraw-Hill. — Taylor's theorem with remainder, in the form the truncation argument uses
- Feigenbaum, L. (1985). Brook Taylor and the method of increments. *Archive for History of Exact Sciences*, 34(1–2), 1–140. https://doi.org/10.1007/BF00329903 — the reception: why the theorem waited until Lagrange for its importance to be recognised
- Krantz, S. G., & Parks, H. R. (2002). *A primer of real analytic functions* (2nd ed.). Birkhäuser. — the germ, and the smooth-but-not-analytic counterexamples
- [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)
- [Representation](/view.html?p=notes/epistemica/mathematical/method/representation.md) — the family, and the table of building blocks
- [Function](/view.html?p=notes/epistemica/mathematical/mapping/function.md) · [Map](/view.html?p=notes/epistemica/mathematical/mapping/map.md) · [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md)
- [Brook Taylor](/view.html?p=notes/social/actor/private/persona/brook-taylor.md) — the persona
