---
tags: [mathematics, method, technique, analytical]
---

# Separation of Variables

> **Separation of variables** looks for a solution of a partial differential equation as a product $u(x,t) = X(x)T(t)$, turning one PDE into two ordinary differential equations joined by a constant.

## Formulation

> **What it is.** The standard entrance to linear PDEs. Substituting the product and dividing by it leaves a function of $x$ equated to a function of $t$; both must equal the same constant, and the problem splits.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** It works when the operator is a sum of one-variable operators and the domain is a product — rectangles, cylinders, spheres. For coupled or non-separable domains it fails, and one needs a [variational method](variational-method.md) or numerical treatment.

## Key results

- **The heat and wave equations.** Each mode decays or oscillates independently; the general solution is a superposition of modes, i.e. a [Fourier series](../../mapping/fourier-series.md).
- **Eigenvalue problems.** The separated spatial equation is a Sturm–Liouville problem, so separation is the source of the orthonormal eigenfunction expansion.
- **Boundary conditions.** Separation respects the boundary conditions through the eigenvalue choice: only discrete frequencies fit a bounded domain.
- **Laplace's equation.** In rectangular, cylindrical and spherical domains separation gives the classical harmonic functions and Legendre polynomials.
- **Limits.** Non-homogeneous or non-linear equations break the product ansatz; the reduction then proceeds by eigenfunction expansion instead.

## References

- https://en.wikipedia.org/wiki/Separation_of_variables
- [Change of Variables](change-of-variables.md) · [Fourier Series](../../mapping/fourier-series.md) · [Differential Equation](../../change/differential-equation.md) · [Variational Method](variational-method.md)
