---
tags: [note, mathematics]
---

# Mathematical Construction

> A **mathematical construction** is an artifact mathematics leaves behind: a stated result carried by a representational system and standing about a target — a theorem, an inequality, a representation, or a fixed-point condition.

## Formulation

### What is this epistemic instance?

> The construction scope of the mathematical domain: the named results the corpus states, gathered as one catalogue. A construction is what the domain *produces*; the routine that produced it lives in the [method scope](../method/method.md), and the rules it was written with live in the representational systems it is written in.

### What epistemic element type does this epistemic instance belong to?

> An `Aggregate` over `Epistemic Construction`s — chiefly `Theory` and `Model` instances, each stated about a class of targets and evaluated by proof. The schema is owned by the canonical
> [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

### Is the type of this `epistemic element instance` ambiguous?

> One boundary is worth stating. A named *law* or *theorem* is a construction, not a target: Navier–Stokes is a model of a flow, not the flow. The target itself is parsed in the naturalis grammar, never here.

### What is the recursive instance decomposition of this epistemic instance?

> The members are grouped by the obligation the construction discharges.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Mathematical Construction | The catalogue of stated mathematical results. |
| `Aggregate` → Mathematical Construction → Ordering Construction | Grouping: results that bound one quantity by another. |
| `Aggregate` → Mathematical Construction → Ordering Construction → AM–GM Inequality | The arithmetic mean bounds the geometric mean. |
| `Aggregate` → Mathematical Construction → Ordering Construction → Cauchy–Schwarz Inequality | An inner product is bounded by the product of the norms. |
| `Aggregate` → Mathematical Construction → Ordering Construction → Chebyshev's Inequality | Order statistics bound deviations from the mean. |
| `Aggregate` → Mathematical Construction → Ordering Construction → Jensen's Inequality | A convex function bounds the mean of its values. |
| `Aggregate` → Mathematical Construction → Limit Construction | Grouping: results that exchange a limit with another operation. |
| `Aggregate` → Mathematical Construction → Limit Construction → Intermediate Value Theorem | A continuous function on an interval attains every value between its endpoints. |
| `Aggregate` → Mathematical Construction → Limit Construction → Mean Value Theorem | A differentiable function's average slope is attained somewhere. |
| `Aggregate` → Mathematical Construction → Limit Construction → Taylor's Theorem | A function is reconstructed from its derivatives at a point plus a remainder. |
| `Aggregate` → Mathematical Construction → Limit Construction → Fundamental Theorem of Calculus | Differentiation and integration are inverse operations. |
| `Aggregate` → Mathematical Construction → Integral Construction | Grouping: results that move an integral across a boundary or a limit. |
| `Aggregate` → Mathematical Construction → Integral Construction → Green's Theorem | A planar integral is exchanged for a boundary integral. |
| `Aggregate` → Mathematical Construction → Integral Construction → Stokes' Theorem | The circulation of a field equals the flux of its curl. |
| `Aggregate` → Mathematical Construction → Integral Construction → Divergence Theorem | The flux through a closed surface equals the divergence inside. |
| `Aggregate` → Mathematical Construction → Integral Construction → Fubini's Theorem | A multiple integral may be iterated. |
| `Aggregate` → Mathematical Construction → Integral Construction → Lebesgue's Dominated Convergence Theorem | A dominated sequence of integrable functions may be integrated term by term. |
| `Aggregate` → Mathematical Construction → Algebraic Construction | Grouping: results about the structure of algebraic systems. |
| `Aggregate` → Mathematical Construction → Algebraic Construction → Cayley–Hamilton Theorem | A matrix satisfies its own characteristic polynomial. |
| `Aggregate` → Mathematical Construction → Algebraic Construction → Fundamental Theory of Algebra | Every non-constant complex polynomial has a root. |
| `Aggregate` → Mathematical Construction → Algebraic Construction → De Moivre's Theorem | Powers of a complex number are a rotation in the complex plane. |
| `Aggregate` → Mathematical Construction → Fixed-Point Construction | Grouping: conditions under which an iteration has a limit. |
| `Aggregate` → Mathematical Construction → Fixed-Point Construction → Banach Fixed-Point Theorem | A contraction on a complete metric space has a unique fixed point. |
| `Aggregate` → Mathematical Construction → Fixed-Point Construction → Brouwer Fixed-Point Theorem | A continuous map of a compact convex set into itself has a fixed point. |
| `Aggregate` → Mathematical Construction → Approximation Construction | Grouping: how well one class of functions represents another. |
| `Aggregate` → Mathematical Construction → Approximation Construction → Weierstrass Approximation Theorem | Continuous functions on a closed interval are uniformly approximated by polynomials. |
| `Aggregate` → Mathematical Construction → Approximation Construction → Universal Approximation Theorem | A single hidden layer approximates a continuous function on a compact set. |
| `Aggregate` → Mathematical Construction → Representation Construction | Grouping: results that identify an object with another class of objects. |
| `Aggregate` → Mathematical Construction → Representation Construction → Riesz–Fréchet Representation Theorem | A continuous linear functional is an inner product with a fixed vector. |
| `Aggregate` → Mathematical Construction → Representation Construction → Hahn–Banach Theorem | A bounded functional on a subspace extends without increasing its norm. |
| `Aggregate` → Mathematical Construction → Geometry Construction | Grouping: results about figures and their invariants. |
| `Aggregate` → Mathematical Construction → Geometry Construction → Euclid's Theorem | The primes are infinite. |
| `Aggregate` → Mathematical Construction → Geometry Construction → Pythagorean Theorem | The square on the hypotenuse is the sum of the squares on the legs. |
| `Aggregate` → Mathematical Construction → Symmetry Construction | Grouping: results deriving conservation from invariance. |
| `Aggregate` → Mathematical Construction → Symmetry Construction → Noether's Theorem | Every continuous symmetry of an action yields a conserved quantity. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- [Philosophia Artium Lectionis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-lectionis-et-operis.md) (extraction grammar)
