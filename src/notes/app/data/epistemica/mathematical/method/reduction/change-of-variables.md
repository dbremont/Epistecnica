---
tags: [note, mathematics, method, technique, analytical]
---

# Change of Variables

> A **change of variables** rewrites a problem in new coordinates in which it becomes simpler: the operator, the domain, or the expression takes a standard form, and the transformation is undone at the end.

## Formulation

> **What it is.** The most reused reduction in mathematics. Substitution in an integral, a linear change of basis, a normal form, a dimensionless rescaling — all are the same routine: choose coordinates adapted to the problem, solve there, transport the answer back.
>
> **Type.** An `Epistemic Method`. What it operates on is a [coordinate system](../../coordinate-system.md) and the [transformation rules](../../transformation.md) of the representational system.
>
> **Boundary.** The transport is where the error lives: integrals acquire a Jacobian, differential equations acquire transformed operators, and a coordinate change that is not a diffeomorphism can silently merge or lose solutions.

## Key results

- **Integration.** $\int f(x)\,dx = \int f(\varphi(u))|\varphi'(u)|\,du$ — the Jacobian determinant is the price of the change (see [determinant](../../structure/linear/determinant.md)).
- **Linear change of basis.** $A \mapsto P^{-1}AP$ turns a matrix into one whose structure is visible; diagonalization is the extreme case.
- **Normal forms.** Bring an equation to a canonical form and the classification follows — this is how second-order PDEs are sorted into elliptic, parabolic and hyperbolic.
- **Rescaling.** Removing units by nondimensionalization reduces a problem's parameter count; the [Pi theorem](dimensional-analysis.md) is its theory.
- **Polar, cylindrical, spherical.** Coordinates chosen to the symmetry of the domain turn a boundary-value problem into a separable one.

## References

- https://en.wikipedia.org/wiki/Change_of_variables
- [Coordinate System](../../coordinate-system.md) · [Dimensional Analysis](dimensional-analysis.md) · [Separation of Variables](separation-of-variables.md) · [Linearization](linearization.md)
