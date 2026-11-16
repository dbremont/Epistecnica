---
tags: [note, mathematics, algebra]
qa:
 - Is a root a property of the equation, of the function, or of the pair (equation, domain) — and does the answer change when the domain widens from ℝ to ℂ?
 - "Root" and "solution" are used interchangeably for one equation in one unknown; where do they come apart, and does the corpus need both words?
 - Every named special case below is the general notion restricted to a smaller family of equations — is there a case that is genuinely a different concept wearing the same word?
---

# Root

> A **root** is a value that makes a relation vanish: for the equation `f(x) = g(x)` it is a value of the unknown for which the equality holds, and for the function `f` it is a point at which `f` takes the value zero. The equation side and the function side name one fact; what changes is which of the two is the object and which is the residue.

## 1. Definition

Let `f` be a function from a domain `D` into a set carrying a distinguished zero `0` — a field, a ring, the complex numbers.

\[
a \text{ is a root of } f(x) = 0 \quad\iff\quad f(a) = 0
\]

An equation `f(x) = g(x)` is never read on its own terms: it is first rewritten as `f(x) − g(x) = 0`, and its roots are the zeros of the difference. Three words name the same object, and each names the side it is read from:

- a **root** is the value, read from the equation — *what value satisfies this?*
- a **zero** is the value, read from the function — *where does this vanish?*
- a **solution** is the value, read from the problem — *what answers the question posed?*

The set of all of them is the **zero set** `{a ∈ D : f(a) = 0}` — the level `0` of `f`, one member of the family of [level sets](/view.html?p=notes/epistemica/mathematical/mapping/level-set.md). See [Zero Set](/view.html?p=notes/epistemica/mathematical/mapping/zero-set.md) for the set-theoretic reading.

Three claims hold of the general notion, before any family is named:

- a root **need not exist** — `x² + 1` has none over ℝ;
- it **need not be unique** — `sin x` has infinitely many;
- it **need not be nameable** — a root may exist and admit no closed expression.

Existence is therefore not a property of the equation alone but of the **pair** (equation, domain): widen ℝ to ℂ and every nonconstant polynomial acquires a root. That widening is the fundamental theorem of algebra, and it is the clearest statement that the domain is half of the concept.

## 2. The polynomial case

For `f ∈ K[x]` the concept sharpens, because roots and factors are the same data:

\[
a \text{ is a root of } f \quad\iff\quad (x - a) \text{ divides } f
\]

This is the factor theorem, and it is what makes roots algebraic objects rather than numerical accidents: extracting a root is exactly factoring off a linear term. Iterating gives the **multiplicity** `k` — the largest power such that `(x − a)^k` divides `f` — and the count `Σ k ≤ deg f`, with equality over ℂ. The coefficients are then the elementary symmetric functions of the roots in multiplicities ([Vieta's relations](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md)).

**The zero root.** The value `a = 0` is a root exactly when the constant term vanishes, and then `f = x^k g` with `g(0) ≠ 0` and `k` the multiplicity. The root at the origin is therefore the number of times `x` factors out — which is why a vanishing constant term lowers the *effective* degree of an equation without changing its nominal one, and why the exceptional case in every formula (Cardano's, the resolvent, a Tschirnhaus substitution) is a coefficient that has fallen to zero with `x` standing in front of what remains.

## 3. The senses of the word

Each named family below is the general notion restricted — a smaller class of equations, or a named subset of the roots. Nothing is redefined; a case is named.

| Sense | What is solved | Where it is owned |
| --- | --- | --- |
| **Root of an equation** | `f(x) = g(x)` in one unknown | this note; [Equation](/view.html?p=notes/epistemica/mathematical/equation/equation.md) |
| **Zero of a function / zero set** | `f(x) = 0` over a stated domain | [Zero Set](/view.html?p=notes/epistemica/mathematical/mapping/zero-set.md), [Level Set](/view.html?p=notes/epistemica/mathematical/mapping/level-set.md) |
| **Root of a polynomial** | `f ∈ K[x]`: factor theorem, multiplicity, the fundamental theorem of algebra | [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) |
| **Zero root** | `a = 0`: constant term vanishes, `f = x^k g` | [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) |
| **n-th root / radical** | `x^n = a`: the inverse of the power map, principal versus all roots | [Exponentiation](/view.html?p=notes/epistemica/mathematical/number/exponentiation.md) — no dedicated note yet |
| **Root of unity** | `z^n = 1`: primitive roots, cyclotomic polynomials, the discrete Fourier transform | [Complex Numbers](/view.html?p=notes/epistemica/mathematical/complex/complex-numbers-c.md), [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) |
| **Unit root** | algebraic: a root with \|α\| = 1; time series: an autoregressive characteristic root on the unit circle, i.e. non-stationarity | [ARIMA](/view.html?p=notes/epistemica/observational/computational/autoregressive-integrated-moving-average-arima-model.md) |
| **Algebraic number** | a root of a nonzero polynomial over ℚ | [Number](/view.html?p=notes/epistemica/mathematical/number/number.md) |
| **Eigenvalue** | a root of the characteristic polynomial `det(A − λI)` | [Eigenvalue](/view.html?p=notes/epistemica/mathematical/structure/linear/eigenvalue.md) |

The restrictions are visible one at a time: the **radical** fixes `f` to `x^n − a`; the **root of unity** further fixes `a = 1`; the **unit root** keeps only roots on the circle `|z| = 1`; the **algebraic number** restricts the coefficients to ℚ and reads the root as a number rather than as a solution; the **eigenvalue** fixes the function to a determinant. The **zero root** is not a family at all — it is the case `a = 0` of the general definition, made visible because so many formulas degenerate there.

"Root" also names a structural position — the origin of a tree, the base of a dependency graph — in the technical corpus. That is a different concept with the same word, and it is not a mathematical root.

## 4. What a root is not

- **Not the factor.** `(x − a)` is a polynomial; the root is the value `a`. The factor theorem states an equivalence, not an identity of the two objects.
- **Not a solution of a system.** There the unknown is a vector and the object is a common zero of several functions; a single root is the one-dimensional case.
- **Not a property of the equation alone.** `x² + 1 = 0` has no real root and two complex ones; without the domain the sentence has no truth value.
- **Not a closed form.** A root can exist and be unwritable by radicals — [Abel–Ruffini and Galois](/view.html?p=notes/epistemica/mathematical/cossical/classical-algebra.md) establish exactly this for the general quintic and above.

## 5. Finding a root is a different question

The concept above is exact and needs no procedure. *Locating* a root is a technique family, filed elsewhere:

- **Closed forms** — the quadratic formula, [Cardano's and Ferrari's methods](/view.html?p=notes/epistemica/mathematical/cossical/classical-algebra.md) for the cubic and quartic;
- **Re-posing** — [Lagrange resolvents](/view.html?p=notes/epistemica/mathematical/cossical/lagrange-resolvent.md) and [Tschirnhaus transformations](/view.html?p=notes/epistemica/mathematical/cossical/tschirnhaus-transformation.md), which rewrite the equation so that an existing method applies;
- **Rational root extraction** — candidate roots from the divisors of the extreme coefficients, then factorization;
- **Numerical iteration** — [Newton–Raphson](/view.html?p=notes/epistemica/singular/newton-raphson-method.md), bisection, and their convergence analysis.

Insolubility is a statement about a *family* of equations, not about any one root: the general quintic has roots in ℂ, and none of them can be written in radicals from its coefficients.

## References

- [Zero of a function — Wikipedia](https://en.wikipedia.org/wiki/Zero_of_a_function)
- [nth root — Wikipedia](https://en.wikipedia.org/wiki/Nth_root)
- [Root of unity — Wikipedia](https://en.wikipedia.org/wiki/Root_of_unity)
- [Unit root — Wikipedia](https://en.wikipedia.org/wiki/Unit_root)
- [Multiplicity (mathematics) — Wikipedia](https://en.wikipedia.org/wiki/Multiplicity_(mathematics))
- [Algebraic number — Wikipedia](https://en.wikipedia.org/wiki/Algebraic_number)
- [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) — the factor theorem, Vieta's relations, cyclotomic polynomials
- [Classical Algebra](/view.html?p=notes/epistemica/mathematical/cossical/classical-algebra.md) — the radical techniques and their limits
- [Equation](/view.html?p=notes/epistemica/mathematical/equation/equation.md) — the equation the root satisfies
- [Function](/view.html?p=notes/epistemica/mathematical/mapping/function.md) — the function the zero set is read off
