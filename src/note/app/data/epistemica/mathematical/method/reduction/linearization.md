---
tags: [mathematics, method, technique, dynamical-system]
---

# Linearization

> **Linearization** replaces a nonlinear problem by its first-order approximation near a point: the derivative (or Jacobian) at that point captures the local behaviour, and the linear theory answers the local question.

## Formulation

> **What it is.** The routine that turns an intractable nonlinear object into a matrix. Around an equilibrium, $\dot x = f(x)$ becomes $\dot{\xi} = J\xi$ with $J = Df(x_0)$, and the [eigenvalues](../../structure/linear/eigenvalue.md) of $J$ classify the behaviour.
>
> **Type.** An `Epistemic Method`; the approximation is a [change of variables](change-of-variables.md) to deviation coordinates plus a truncation.
>
> **Boundary.** Linearization is local and generic. At a hyperbolic point (no eigenvalue on the imaginary axis) it is valid — Hartman–Grobman; at a non-hyperbolic point it says nothing and one needs centre-manifold or normal-form analysis.

## Key results

- **Stability.** $\operatorname{Re}\lambda < 0$ for all eigenvalues gives asymptotic stability; any positive real part gives instability.
- **Hartman–Grobman.** Near a hyperbolic equilibrium the nonlinear flow is topologically conjugate to the linear one — the theorem that licenses the method.
- **Oscillation.** Imaginary eigenvalues give a centre: the linear part predicts oscillation, but the nonlinear terms decide whether the orbit spirals in, out, or closes.
- **Iteration.** Newton's method is linearization of a root-finding problem; each step solves the linearized equation exactly.
- **Failure modes.** A saddle-node, a Hopf bifurcation and a homoclinic tangency are all non-hyperbolic — linearization is blind exactly where the interesting dynamics lives.

## References

- https://en.wikipedia.org/wiki/Linearization
- [Dynamical System](../../change/dynamical-system.md) · [Fixed Point](../../change/fixed-point.md) · [Stability Theory](../../change/stability-theory.md) · [Eigenvalue](../../structure/linear/eigenvalue.md)
