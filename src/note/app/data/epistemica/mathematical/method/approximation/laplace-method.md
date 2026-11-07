---
tags: [method, technique, analytical, mathematics]
---

# Laplace's Method

> **Laplace's method** evaluates an integral $\int g(x)e^{\lambda f(x)}dx$ for large $\lambda$ by concentrating it at the maximum of $f$: the exponential suppresses everything except a neighbourhood of the peak, and there the integrand is Gaussian.

## Formulation

> **What it is.** The real-exponent cousin of [stationary phase](stationary-phase.md). Where an oscillatory phase cancels away from its critical points, a growing real exponential *dominates* at its maximum; expanding $f$ to second order turns the integral into a Gaussian and the answer into $g(x_0)e^{\lambda f(x_0)}\sqrt{2\pi/(\lambda|f''(x_0)|)}$.
>
> **Type.** An `Epistemic Method`; together with saddle-point analysis it is the standard route to asymptotics of integrals and sums.
>
> **Boundary.** The maximum must be attained in the interior and be non-degenerate. A boundary maximum halves the Gaussian; a degenerate maximum changes the power of $\lambda$; and the expansion is asymptotic in $\lambda$, not convergent.

## Key results

- **Leading term.** $I(\lambda) \sim g(x_0)e^{\lambda f(x_0)}\sqrt{\frac{2\pi}{\lambda|f''(x_0)|}}$ — the Gaussian factor is the method's signature.
- **Stirling's formula.** Applying it to $\Gamma(n+1) = \int t^n e^{-t}dt$ yields $n! \sim \sqrt{2\pi n}(n/e)^n$ — the canonical application.
- **Saddle-point method.** In the complex plane the contour is deformed to pass through a saddle of the analytic continuation, where the same local Gaussian analysis applies; this evaluates oscillatory and contour integrals exactly.
- **Large deviations.** The exponential rate of a rare-event probability is a Legendre transform of a cumulant generating function — Laplace's method in probability form.
- **Generating functions.** Coefficient asymptotics of a [generating function](../transform/generating-function.md) come from the saddle point of its analytic continuation.

## References

- https://en.wikipedia.org/wiki/Laplace%27s_method
- https://en.wikipedia.org/wiki/Method_of_steepest_descent
- [Stationary Phase](stationary-phase.md) · [Asymptotic Analysis](asymptotic-analysis.md) · [Factorial](../../discrete/factorial.md) · [Generating Function](../transform/generating-function.md)
