---
tags: [note, mathematics, method, technique, analytical]
---

# Green's Function Method

> The **Green's function method** solves a linear equation by first solving it for a point source: once $G$ with $LG = \delta$ is known, the solution for any source is the convolution $u = G * f$.

## Formulation

> **What it is.** The inversion routine for linear operators. The Green's function is the response to a unit impulse at one point; by linearity and superposition, the response to any source is the integral of responses.
>
> **Type.** An `Epistemic Method`. The Green's function itself is an object — often a [distribution](/view.html?p=notes/epistemica/mathematical/mapping/distribution/distribution.md), and in the constant-coefficient case the response to a [Dirac delta](/view.html?p=notes/epistemica/mathematical/mapping/distribution/dirac-delta-function.md) — while the method is the reduction of a boundary-value problem to an integral equation.
>
> **Boundary.** The method requires linearity, a known operator, and boundary conditions encoded in $G$. For nonlinear problems the impulse response does not superpose, and the Green's function survives only as a linearization.

## Key results

- **Representation.** $u(x) = \int G(x,y)f(y)\,dy$ solves $Lu = f$ with homogeneous boundary conditions; the boundary terms are the ones the Green's function is built to kill.
- **Reciprocity.** For self-adjoint operators $G(x,y) = G(y,x)$ — the symmetry that makes the method practical.
- **Canonical cases.** The heat kernel, the free-space Laplace kernel $1/4\pi r$, and the wave equation's retarded kernel are the three archetypes.
- **Integral equations.** A boundary-value problem becomes a Fredholm equation of the second kind, which is where spectral and [compactness](../reduction/compactness-argument.md) arguments apply.
- **Physics reading.** The Green's function is the propagator; Feynman diagrams are a perturbative expansion of exactly this object.

## References

- https://en.wikipedia.org/wiki/Green%27s_function
- [Distribution](/view.html?p=notes/epistemica/mathematical/mapping/distribution/distribution.md) · [Generalized Function](/view.html?p=notes/epistemica/mathematical/mapping/generalized-function.md) · [Differential Equation](/view.html?p=notes/epistemica/mathematical/change/differential-equation.md) · [Variational Method](/view.html?p=notes/epistemica/mathematical/method/reduction/variational-method.md) · [Feynman Diagram](/view.html?p=notes/epistemica/singular/feynman-diagram.md)
