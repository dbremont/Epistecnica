---
tags: [note, mathematics, statistics]
---

# Construction

> A **construction** is a result an inquiry leaves behind: a statement carried by a representational system and discharged by proof about a class of targets — a theorem, an inequality, a limit or convergence result, or a fixed-point condition.

## Formulation

### What is this epistemic instance?

> The construction scope: the named results the corpus states in the mathematical and observational domains, gathered as one catalogue. A construction is what an inquiry *produces* by derivation; the routine that produced it lives in the [method scope](../../mathematical/method/method.md), and the rules it was written with live in the representational systems it is written in.

### What epistemic element type does this epistemic instance belong to?

> An `Aggregate` over `Epistemic Construction`s — `Theory` instances each stated about a class of targets and evaluated by proof. The schema is owned by the canonical
> [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

### Is the type of this `epistemic element instance` ambiguous?

> One boundary is worth stating. A construction is a result *discharged by proof* — a theorem, an inequality, a limit or convergence result. A named *theory*, *law*, or *model* of a particular system is a theoretical result rather than a construction: Navier–Stokes is the theory of a flow, not a theorem about one, and it is filed with its system in [the science scope](../../singular/science.md). The target itself is parsed in the naturalis grammar, never here.

### What is the recursive instance decomposition of this epistemic instance?

> The members are grouped by the obligation the construction discharges.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Construction | The catalogue of stated results, mathematical and observational. |
| `Aggregate` → Construction → Ordering Construction | Grouping: results that bound one quantity by another. |
| `Aggregate` → Construction → Ordering Construction → AM–GM Inequality | The arithmetic mean bounds the geometric mean. |
| `Aggregate` → Construction → Ordering Construction → Cauchy–Schwarz Inequality | An inner product is bounded by the product of the norms. |
| `Aggregate` → Construction → Ordering Construction → Chebyshev's Inequality | Order statistics bound deviations from the mean. |
| `Aggregate` → Construction → Ordering Construction → Jensen's Inequality | A convex function bounds the mean of its values. |
| `Aggregate` → Construction → Limit Construction | Grouping: results that exchange a limit with another operation. |
| `Aggregate` → Construction → Limit Construction → Intermediate Value Theorem | A continuous function on an interval attains every value between its endpoints. |
| `Aggregate` → Construction → Limit Construction → Mean Value Theorem | A differentiable function's average slope is attained somewhere. |
| `Aggregate` → Construction → Limit Construction → Taylor's Theorem | A function is reconstructed from its derivatives at a point plus a remainder. |
| `Aggregate` → Construction → Limit Construction → Fundamental Theorem of Calculus | Differentiation and integration are inverse operations. |
| `Aggregate` → Construction → Integral Construction | Grouping: results that move an integral across a boundary or a limit. |
| `Aggregate` → Construction → Integral Construction → Green's Theorem | A planar integral is exchanged for a boundary integral. |
| `Aggregate` → Construction → Integral Construction → Stokes' Theorem | The circulation of a field equals the flux of its curl. |
| `Aggregate` → Construction → Integral Construction → Divergence Theorem | The flux through a closed surface equals the divergence inside. |
| `Aggregate` → Construction → Integral Construction → Fubini's Theorem | A multiple integral may be iterated. |
| `Aggregate` → Construction → Integral Construction → Lebesgue's Dominated Convergence Theorem | A dominated sequence of integrable functions may be integrated term by term. |
| `Aggregate` → Construction → Algebraic Construction | Grouping: results about the structure of algebraic systems. |
| `Aggregate` → Construction → Algebraic Construction → Cayley–Hamilton Theorem | A matrix satisfies its own characteristic polynomial. |
| `Aggregate` → Construction → Algebraic Construction → Fundamental Theory of Algebra | Every non-constant complex polynomial has a root. |
| `Aggregate` → Construction → Algebraic Construction → De Moivre's Theorem | Powers of a complex number are a rotation in the complex plane. |
| `Aggregate` → Construction → Fixed-Point Construction | Grouping: conditions under which an iteration has a limit. |
| `Aggregate` → Construction → Fixed-Point Construction → Banach Fixed-Point Theorem | A contraction on a complete metric space has a unique fixed point. |
| `Aggregate` → Construction → Fixed-Point Construction → Brouwer Fixed-Point Theorem | A continuous map of a compact convex set into itself has a fixed point. |
| `Aggregate` → Construction → Approximation Construction | Grouping: how well one class of functions represents another. |
| `Aggregate` → Construction → Approximation Construction → Weierstrass Approximation Theorem | Continuous functions on a closed interval are uniformly approximated by polynomials. |
| `Aggregate` → Construction → Approximation Construction → Universal Approximation Theorem | A single hidden layer approximates a continuous function on a compact set. |
| `Aggregate` → Construction → Representation Construction | Grouping: results that identify an object with another class of objects. |
| `Aggregate` → Construction → Representation Construction → Riesz–Fréchet Representation Theorem | A continuous linear functional is an inner product with a fixed vector. |
| `Aggregate` → Construction → Representation Construction → Hahn–Banach Theorem | A bounded functional on a subspace extends without increasing its norm. |
| `Aggregate` → Construction → Geometry Construction | Grouping: results about figures and their invariants. |
| `Aggregate` → Construction → Geometry Construction → Euclid's Theorem | The primes are infinite. |
| `Aggregate` → Construction → Geometry Construction → Pythagorean Theorem | The square on the hypotenuse is the sum of the squares on the legs. |
| `Aggregate` → Construction → Symmetry Construction | Grouping: results deriving conservation from invariance. |
| `Aggregate` → Construction → Symmetry Construction → Noether's Theorem | Every continuous symmetry of an action yields a conserved quantity. |

| `Aggregate` → Construction → Asymptotic Construction | Grouping: results about how a statistic behaves as the sample grows. |
| `Aggregate` → Construction → Asymptotic Construction → Central Limit Theorem | A sum of independent terms approaches the normal law. |
| `Aggregate` → Construction → Asymptotic Construction → Crámer–Rao Lower Bound | The variance of an unbiased estimator is bounded below by the information. |
| `Aggregate` → Construction → Asymptotic Construction → Glivenko–Cantelli Theorem | The empirical distribution converges uniformly to the true one. |
| `Aggregate` → Construction → Asymptotic Construction → Law of Large Numbers | The sample mean converges to the expectation. |
| `Aggregate` → Construction → Asymptotic Construction → Law of the Iterated Logarithm | The scaled fluctuation of a sum is bounded almost surely. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- [Philosophia Artium Lectionis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-lectionis-et-operis.md) (extraction grammar)
