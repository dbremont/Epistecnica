---
tags: [note, mathematics, series, analysis]
qa:
 - Is a power series a function or a formal object — and which one is the corpus using when it writes $\sum a_k x^k$ for a generating function?
 - The radius of convergence is a property of the coefficients, but the boundary is not: what does the series do on the circle where every term is still defined?
 - Where does the polynomial stop and the series begin, given that a polynomial is a power series with all but finitely many coefficients zero?
---

# Power Series

> A **power series** is the object $\sum_{k\ge 0} a_k (x-a)^k$ read as a series in the variable $x$. It is neither a finite sum nor yet a function: whether it names anything at a point is a question about convergence, and the answer depends on the point. Where it converges it is a function; where it does not, it is only a formal expression.

$$S(x)=\sum_{k\ge 0} a_k (x-a)^k,
\qquad
S_n(x)=\sum_{k\le n} a_k (x-a)^k$$

> The series is the limit of its partial sums $S_n$, and the partial sums are [polynomials](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md). That is the whole construction: a power series is the completion of the polynomial ring in one variable, taken in the topological sense that makes the limit exist.

## 1. Convergence, and the radius

The set of points where a power series converges is not arbitrary — it is an interval in $\mathbb{R}$ or a disc in $\mathbb{C}$, centred at $a$, and its radius is computed from the coefficients alone:

$$\frac{1}{R}=\limsup_{k\to\infty} \lvert a_k\rvert^{1/k},
\qquad\text{equivalently}\qquad
R=\lim_{k\to\infty}\left\lvert\frac{a_k}{a_{k+1}}\right\rvert \ \text{when that limit exists.}$$

That is the **Cauchy–Hadamard formula**, and what it delivers has three parts:

| Region | Behaviour |
| --- | --- |
| $\lvert x-a\rvert<R$ | absolute convergence, and uniform convergence on every compact subinterval |
| $\lvert x-a\rvert>R$ | divergence — the terms do not tend to zero |
| $\lvert x-a\rvert=R$ | undecided by the formula: convergence at the boundary is a separate question, decided point by point |

The boundary is where the interesting failures live. $\sum x^k$ diverges at both ends; $\sum x^k/k^2$ converges at both; $\sum x^k/k$ converges at one and diverges at the other. The radius is a property of the coefficients; the boundary is a property of the series.

## 2. Analytic functions

Inside its disc a power series defines an analytic function, and it does so in the strongest available sense: the series can be differentiated and integrated term by term, with the same radius, and the result is again a power series. A function is **analytic at $a$** when it equals its own Taylor series in a neighbourhood — see [Taylor Representation](/view.html?p=notes/epistemica/mathematical/method/representation/taylor-representation.md) — so power series and analytic germs are the same objects described from two directions.

Two consequences carry the theory:

- **identity.** Two power series that agree on a set with an accumulation point inside the disc are the same series. Coefficients are therefore recoverable from values, which is what makes the representation faithful inside its radius.
- **maximality.** The radius is the distance to the nearest singularity of the function being represented, so a power series cannot be continued past it by rearranging coefficients; a different centre is required.

## 3. Formal power series, where convergence is not asked

Drop the question of convergence and the object survives intact. The **formal power series** over a ring $R$,

$$R[[x]]=\Bigl\{\textstyle\sum_{k\ge 0} a_k x^k \Bigr\},$$

with coefficientwise addition and convolution product, is a ring containing $R[x]$; the polynomial ring is the subring of series that terminate. In $R[[x]]$ there is no radius and no variable to evaluate — a series is a sequence of coefficients, and the operations are defined so that every formal manipulation of the analytic case remains valid.

That is not a lesser object but a different use:

- $1/(1-x)=\sum x^k$ is an identity of formal series, true without any hypothesis on $x$;
- a series is invertible exactly when its constant term is invertible in $R$, which is how formal division and hence [recurrence equations](recurrence-equation.md) are solved;
- composition is defined only when the inner series has zero constant term, since otherwise infinitely many terms contribute to each coefficient.

This is the setting of **generating functions**: the coefficients are the answer to a counting problem, the series is a bookkeeping device, and no value of $x$ is ever substituted. See the combinatorial families at [Discrete Structure](/view.html?p=notes/epistemica/mathematical/discrete/discrete-structure.md).

## 4. Where it sits

Three distinctions keep the object straight, and this corpus needs all three:

- **Power series vs polynomial.** The polynomial is a power series that terminates. The [polynomial ring](/view.html?p=notes/epistemica/mathematical/structure/algebra/polynomial-ring.md) is the subring; the series ring is its completion.
- **Power series vs Taylor representation.** A Taylor representation is the power series *of a given function at a given point*, with the coefficients fixed by the derivatives. A power series is the object, coefficient sequence first — it exists whether or not any function produces it, which is exactly the case for a generating function. The [representation table](/view.html?p=notes/epistemica/mathematical/method/representation.md) lists the power series row for this reason, and the [Taylor note](/view.html?p=notes/epistemica/mathematical/method/representation/taylor-representation.md) is about the case where a function supplies the coefficients.
- **Power series vs series.** A [series](series.md) is the sequence of partial sums of any terms; a power series is the special case whose terms are powers of a variable, so that its convergence set has the interval or disc structure above.

## References

- Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique* (1re partie: Analyse algébrique). Debure frères. — the first systematic treatment of convergence, and the series tests that follow from it
- Abel, N. H. (1826). Untersuchungen über die Reihe $1+\frac{m}{1}x+\frac{m(m-1)}{1\cdot 2}x^2+\cdots$. *Journal für die reine und angewandte Mathematik*, 1, 311–339. — the binomial series handled rigorously, and the first proof that convergence cannot be assumed from the coefficients' form
- Knopp, K. (1928). *Theorie und Anwendung der unendlichen Reihen*. Springer. — the classical treatise on series, where the radius and the boundary cases are catalogued
- Cartan, H. (1963). *Théorie élémentaire des fonctions analytiques d'une ou plusieurs variables complexes*. Hermann. — power series as analytic germs, in the form this note uses
- Rudin, W. (1976). *Principles of mathematical analysis* (3rd ed.). McGraw-Hill. — the radius, term-by-term operations and the identity theorem
- Ahlfors, L. V. (1979). *Complex analysis* (3rd ed.). McGraw-Hill.
- Wilf, H. S. (1990). *generatingfunctionology*. Academic Press. — formal power series as generating functions, with no convergence question asked
- Stanley, R. P. (1997). *Enumerative combinatorics* (Vol. 1, 2nd ed.). Cambridge University Press. — the combinatorial use of $R[[x]]$
- Krantz, S. G., & Parks, H. R. (2002). *A primer of real analytic functions* (2nd ed.). Birkhäuser. — analyticity, and the functions for which the series fails
- [Power series](https://en.wikipedia.org/wiki/Power_series)
- [Series](series.md) · [Sequence](sequence.md) · [Cauchy Sequence](cauchy-sequence.md) · [Convergence Modes](convergence-modes.md) · [Recurrence Equation](recurrence-equation.md)
- [Taylor Representation](/view.html?p=notes/epistemica/mathematical/method/representation/taylor-representation.md) · [Representation](/view.html?p=notes/epistemica/mathematical/method/representation.md)
- [Polynomial Ring](/view.html?p=notes/epistemica/mathematical/structure/algebra/polynomial-ring.md) · [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md)
