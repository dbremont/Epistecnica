---
tags: [note, mathematics, method, technique, numerical]
---

# Iterative Method

> An **iterative method** computes a solution by repeated correction: from an initial guess $x_0$ it generates $x_{n+1} = \Phi(x_n)$, converging to a fixed point of $\Phi$ — the solution.

## Formulation

> **What it is.** The computational form of the fixed-point routine. Instead of solving an equation directly, one designs a map whose fixed point is the answer and whose iteration converges; the design (and the proof) is the method.
>
> **Type.** An `Epistemic Method`; it needs a convergence argument, usually a [contraction](../reduction/contraction-mapping.md) or a spectral radius condition.
>
> **Boundary.** An iteration can diverge, cycle, or converge to the wrong fixed point. Convergence is local unless the map is globally contracting, and the rate decides whether the method is usable at all.

## Key results

- **Rate.** Linear convergence ($\|e_{n+1}\| \le q\|e_n\|$), superlinear, and quadratic (Newton) are the standard grades; each order of magnitude costs a known number of steps.
- **Newton's method.** $x_{n+1} = x_n - f(x_n)/f'(x_n)$ converges quadratically near a simple root, and fails at a multiple root or a zero derivative.
- **Stationary iterations.** Jacobi, Gauss–Seidel and SOR for linear systems; convergence is governed by the spectral radius of the iteration matrix.
- **Krylov methods.** Conjugate gradients and GMRES build the iterate in a Krylov subspace — the modern replacement for stationary iterations at scale.
- **Multigrid.** Iterating on a hierarchy of grids removes error at every frequency — the reason it is $O(n)$ where simpler iterations are $O(n^2)$.

## References

- https://en.wikipedia.org/wiki/Iterative_method
- [Contraction Mapping](../reduction/contraction-mapping.md) · [Discretization](discretization.md) · [Newton–Raphson Method](/note.html?p=notes/epistemica/singular/newton-raphson-method.md) · [Fixed Point](../../change/fixed-point.md)
