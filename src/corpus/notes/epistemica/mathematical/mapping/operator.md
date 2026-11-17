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

## Which properties can be associated with operators in operator theory?

| **Property** | **Description** |
|---|---|
| **Linearity** | An operator \(T\) satisfies \(T(\alpha x+\beta y)=\alpha T(x)+\beta T(y)\) for scalars \(\alpha,\beta\) and vectors \(x,y\). |
| **Boundedness** | An operator \(T\) is bounded if there exists \(C\geq 0\) such that \(\|Tx\|\leq C\|x\|\) for every \(x\) in its domain. |
| **Continuity** | An operator is continuous if small changes in its input produce small changes in its output. |
| **Compactness** | An operator maps bounded sets into relatively compact sets (sets whose closures are compact). |
| **Self-Adjointness** | An operator satisfies \(T=T^*\), where \(T^*\) is its adjoint. |
| **Symmetry** | An operator satisfies \(\langle Tx,y\rangle=\langle x,Ty\rangle\) for all vectors in its domain. |
| **Normality** | An operator satisfies \(T^*T=TT^*\). |
| **Unitarity** | An operator satisfies \(T^*T=TT^*=I\), preserving inner products and norms. |
| **Isometry** | An operator preserves norms: \(\|Tx\|=\|x\|\). |
| **Orthogonality Preservation** | An operator preserves orthogonality: \(\langle x,y\rangle=0\implies\langle Tx,Ty\rangle=0\). |
| **Positivity** | An operator satisfies \(\langle Tx,x\rangle\geq 0\) for every \(x\) in its domain. |
| **Positive Definiteness** | An operator satisfies \(\langle Tx,x\rangle>0\) for every nonzero \(x\). |
| **Idempotence** | An operator satisfies \(T^2=T\). |
| **Involutivity** | An operator satisfies \(T^2=I\). |
| **Nilpotency** | An operator satisfies \(T^n=0\) for some positive integer \(n\). |
| **Invertibility** | An operator has an inverse \(T^{-1}\) satisfying \(T^{-1}T=TT^{-1}=I\). |
| **Injectivity** | An operator maps distinct inputs to distinct outputs; equivalently, \(\ker(T)=\{0\}\). |
| **Surjectivity** | Every element of the codomain is the image of at least one element in the domain. |
| **Density of Range** | The closure of the operator's range is the entire codomain. |
| **Spectral Properties** | Properties concerning the spectrum, eigenvalues, and spectral structure of an operator. |
| **Diagonalizability** | An operator admits a representation as a diagonal operator under a suitable basis or transformation. |
| **Trace-Class** | An operator is compact and has summable singular values. |
| **Hilbert-Schmidt** | An operator has square-summable singular values. |
| **Finite Rank** | An operator has a finite-dimensional range. |
| **Fredholm Property** | An operator has a finite-dimensional kernel, closed range, and finite-dimensional cokernel. |
| **Contraction** | An operator satisfies \(\|T\|\leq 1\). |
| **Expansiveness** | An operator satisfies \(\|Tx\|\geq\|x\|\) for every vector in its domain. |
| **Accretivity** | An operator satisfies \(\operatorname{Re}\langle Tx,x\rangle\geq 0\). |
| **Dissipativity** | An operator satisfies \(\operatorname{Re}\langle Tx,x\rangle\leq 0\). |
| **Commutativity** | Two operators satisfy \(ST=TS\). |

## References

- [Operator](https://en.wikipedia.org/wiki/Operator_(mathematics))
- [Operator theory](https://en.wikipedia.org/wiki/Operator_theory)
- [Bounded operator](https://en.wikipedia.org/wiki/Bounded_operator)
- [Map](map.md) · [Function](function.md) · [Functional](functional.md) · [Transformation Rule](../transformation.md)
