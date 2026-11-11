---
tags: [note, mathematics, operator]
---

# Operator

> An **operator** is a map between function spaces: it takes a function and returns a function. It is one of the kinds of [map](map.md), alongside the [function](function.md), the [functional](functional.md), the transformation, the morphism, and the relation.

> The term is **context-dependent**: in linear algebra an operator may name a matrix; in calculus it may name a differential operator. This note keeps the strict sense — both domain and codomain are function spaces. A map between finite-dimensional vector spaces is a [linear map](../structure/linear/linear-map.md), and a map to a scalar field is a [functional](functional.md).

## Definition

An **operator** is a map $T: \mathcal{F} \to \mathcal{G}$ whose domain and codomain are **function spaces**: $T$ sends a function to a function. The classification is the one drawn in [Map](map.md):

| Domain | Codomain | Classification |
|---|---|---|
| Non-map object | Non-map object | Object-valued function |
| Non-map object | Map object | Map-valued function |
| Map object | Non-map object | Functional |
| Map object | Map object | **Operator** |

A [functional](functional.md) returns a scalar; an operator returns a function. A map between finite-dimensional vector spaces is a [linear map](../structure/linear/linear-map.md) or a matrix, not an operator in the strict sense.

## Where operator content lives

The operator-kind definition lives here; the operator instances stay in the branch that owns the object they act on.

| Branch | Operator content |
|---|---|
| mapping | [Convolution Operator](convolution-operator.md) · [Composition Operator](composition-operator.md) · [Identity Operator](identity-operator.md) · [Non-linear Operator](non-linear-operator.md) |
| structure/linear | [Linear Operator](../structure/linear/linear-operator.md) · [Adjoint Operator](../structure/linear/adjoint-operator.md) · [Self-adjoint Operator](../structure/linear/self-adjoint-operator.md) · [Compact Operator](../structure/linear/compact-operator.md) · [Shift Operator](../structure/linear/shift-operator.md) |
| structure/algebra | [Operator Algebra](../structure/algebra/operator-algebra.md) — the algebra of operators, not an operator instance |

The `change/` notes named `*-operator.md` — [Derivative Operator](../change/derivative-operator.md), [Differential Operator](../change/differential-operator.md), [Partial Derivative Operator](../change/partial-derivative-operator.md), [Gradient Operator](../change/gradient-operator.md), [Divergence Operator](../change/divergence-operator.md), [Curl Operator](../change/curl-operator.md), [Nabla Operator](../change/nabla-operator.md), [Laplace Operator](../change/nabla-laplace-operator.md) — are **transformation rules** of the differential and field representational systems, not operator-kind instances. They are catalogued in [Transformation Rule](../transformation.md); the [Integral Operator](../change/integral-operator.md) is the integration-side note.

## References

- [Operator](https://en.wikipedia.org/wiki/Operator_(mathematics))
- [Operator theory](https://en.wikipedia.org/wiki/Operator_theory)
- [Bounded operator](https://en.wikipedia.org/wiki/Bounded_operator)
- [Map](map.md) · [Function](function.md) · [Functional](functional.md) · [Transformation Rule](../transformation.md)
