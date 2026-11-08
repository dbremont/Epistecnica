---
tags: [note, mathematics, method, technique, numerical]
---

# Discretization

> **Discretization** replaces a continuous problem by a finite one: the domain becomes a mesh, the functions become values at nodes, and the operators become algebraic operations on those values.

## Formulation

> **What it is.** The bridge from a PDE or an integral equation to a linear system a computer can solve. The choice of scheme — finite difference, finite element, finite volume, spectral — decides accuracy, stability and conservation properties.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** Discretization introduces two errors that must be separated: *truncation* (the scheme approximates the operator) and *round-off* (floating point). Refining the mesh reduces the first and eventually increases the second; the balance is the method's practical limit.

## Key results

- **Consistency and convergence.** A scheme is consistent if the truncation error vanishes with the step, and convergent if the discrete solution approaches the continuous one; Lax equivalence adds stability as the missing hypothesis.
- **Stability.** The CFL condition for explicit schemes, and von Neumann analysis for linear ones — the reason time steps cannot be chosen freely.
- **Finite differences.** Derivatives become differences; accuracy follows from Taylor expansion, and the [Taylor theorem](../../construction/taylors-theorem.md) is the error analysis.
- **Finite elements.** The domain is partitioned and the solution approximated by basis functions; the variational form gives the linear system, and [Galerkin methods](/view.html?p=notes/epistemica/singular/galerkin-method.md) are the general frame.
- **Conservation.** Finite-volume schemes conserve fluxes by construction — the reason they dominate fluid dynamics.

## References

- https://en.wikipedia.org/wiki/Discretization
- [Finite Difference Method](/view.html?p=notes/epistemica/singular/finite-difference-method-fdm.md) · [Finite Element Method](/view.html?p=notes/epistemica/singular/finite-element-method-fem.md) · [Galerkin Method](/view.html?p=notes/epistemica/singular/galerkin-method.md) · [Runge–Kutta Toolbox](/view.html?p=notes/epistemica/singular/runge-kutta-toolbox.md)
