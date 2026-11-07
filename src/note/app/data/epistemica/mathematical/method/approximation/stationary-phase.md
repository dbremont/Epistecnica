---
tags: [mathematics, method, technique, analytical]
---

# Stationary Phase

> **Stationary phase** evaluates an oscillatory integral $\int g(x)e^{i\lambda f(x)}dx$ by noting that the contributions cancel everywhere except where the phase is stationary: the integral localizes to the critical points of $f$.

## Formulation

> **What it is.** The asymptotic evaluation of exponentials of a large parameter. Away from a critical point the integrand oscillates fast and cancels; at a critical point the phase is flat, the oscillation stops, and the integral picks up a contribution there.
>
> **Type.** An `Epistemic Method`, the frequency-domain sibling of [Laplace's method](laplace-method.md) (where the exponent is real and the maximum dominates).
>
> **Boundary.** It gives an asymptotic expansion in $\lambda$, valid for $\lambda \to \infty$; it says nothing at finite $\lambda$. Degenerate critical points change the power law and require a different scaling.

## Key results

- **Leading term.** A non-degenerate critical point contributes $\propto \lambda^{-1/2}$ with a phase factor of $\pm i\pi/4$ — the reason stationary-phase asymptotics carry a universal $\sqrt{2\pi/\lambda}$.
- **Laplace's method.** For real $f$, the maximum of $f$ dominates and the same Gaussian local analysis gives the leading exponential term — the route to [Stirling's formula](../../discrete/factorial.md) and large-deviation estimates.
- **Saddle-point / steepest descent.** Deform the contour to pass through a saddle of the analytic continuation, where the integrand is real and sharply peaked; this handles Bessel, Airy and the gamma asymptotics.
- **Fourier asymptotics.** The decay of a Fourier transform of a singular function is read off the stationary points and endpoint contributions.
- **Combinatorics.** Saddle-point analysis of a [generating function](../transform/generating-function.md) yields coefficient asymptotics — the analytic half of enumerative combinatorics.

## References

- https://en.wikipedia.org/wiki/Stationary_phase_approximation
- https://en.wikipedia.org/wiki/Laplace%27s_method
- [Asymptotic Analysis](asymptotic-analysis.md) · [Perturbation Method](perturbation-method.md) · [Generating Function](../transform/generating-function.md) · [Fourier Transform](note.html?n=epistemica/singular/fourier-transform.md)
