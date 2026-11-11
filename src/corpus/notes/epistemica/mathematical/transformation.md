---
tags: [note, mathematics]
---

# Transformation Rule

> A **transformation rule** is a constituting element of a representational system: the licence that rewrites one well-formed expression into another well-formed expression. It is not the act that fires it, not the method that orders acts, and not the glyph that marks it.

## Formulation

### What is this epistemic instance?

> The catalogue of the rewrite licences carried by the mathematical representational systems — the rules of the numeral, algebraic, differential, and equational systems, gathered in one place because they cut across every branch of the domain.

### What epistemic element type does this epistemic instance belong to?

> An `Aggregate` over `Transformation Rule`s, each a `Constitutive Element` of the `Constitutive Substrate` of a `Representational System`. The schema is owned by the canonical
> [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md), whose Arithmetic case is the worked reference.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in three directions, and the guide settles all three. An operation specifies a result, never an order of acts, so it is **not** an `Epistemic Act` — the act is the `Computation` that fires the rule. It is **not** an `Epistemic Method` — a method is the reproducible order of acts, which is why *Shift-And-Add Multiplication*, *Lattice Multiplication*, and *Russian Peasant Multiplication* are methods while multiplication is not. It is **not** a glyph — the `Operator Glyph` `×` is inert, marks which rule fires, and is itself never transformed. Filing a rule under an "operator" theme would merge a rule, a glyph, and an act into one row.

### What is the recursive instance decomposition of this epistemic instance?

> The path below is the guide's Arithmetic case verbatim: the rule is reached from the practice through the representation lane, and it lives nowhere else. The Arithmetic system is itself one of the dynamical representational systems catalogued by the [change scope](change/dynamical-system.md).

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic | The practice whose notation the rule constitutes. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` | The representation lane of the practice. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System | The numeral system the rules are written in. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` | The rules and structures constituting the system. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Multiplication Rule | Rewrite licence: `a × 0 ↦ 0` and `a × S(b) ↦ (a × b) + a`; the rule `Presburger Arithmetic` lacks. |

## Rules by representational system

| Representational system | Rules | Note |
| --- | --- | --- |
| Numeral system | addition, subtraction, multiplication, division, exponentiation, logarithm | [Multiplication](number/multiplication.md) · [Division](number/division.md) · [Exponentiation](number/exponentiation.md) · [Logarithm](number/logarithm.md) |
| Algebraic system | composition, substitution, normalization | [Normalization](equation/normalization.md) · [Composition Operator](mapping/composition-operator.md) |
| Differential system | differentiation, integration | [Derivative Operator](change/derivative-operator.md) · [Differential Operator](change/differential-operator.md) · [Partial Derivative Operator](change/partial-derivative-operator.md) |
| Field representation | gradient, divergence, curl, laplacian | [Gradient Operator](change/gradient-operator.md) · [Divergence Operator](change/divergence-operator.md) · [Curl Operator](change/curl-operator.md) · [Nabla Operator](change/nabla-operator.md) |
| Equational system | factorization, canonical form, solving | [Factorization](equation/factorization.md) · [Canonical Form](equation/canonical-form.md) · [Equation](equation/equation.md) |

> The glyphs that mark these rules live with the notes that use them; the methods that order them live in the [method scope](method/method.md); the acts that fire them are `Computation`s, not notes. A rule is not a map: the kinds of map — function, functional, operator, transformation, morphism, relation — are catalogued in [Map](mapping/map.md).

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) — §QA "Is multiplication an `Epistemic Act`, an `Epistemic Method`, or a constituent of the representation?" and §QA "(Case Study) What is the recursively decomposed instance tree of Arithmetic?"
