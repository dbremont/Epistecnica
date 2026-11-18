---
tags: [note, mathematics, function, special-function, gamma]
qa:
 - Is the gamma function a factorial or an integral — and which definition survives the complex plane?
 - Why does the function have poles at the non-positive integers when the factorial is defined there?
 - What does the gamma function interpolate that the factorial does not?
---

# Gamma Function

> The **gamma function** $\Gamma(z)$ is the continuous interpolation of the factorial: $\Gamma(n) = (n-1)!$ for positive integers, and the function extends to the complex plane with poles at the non-positive integers. It is the analytic object that the factorial only samples.

$$\Gamma(z) = \int_0^\infty t^{z-1} e^{-t}\,dt, \qquad \Re(z) > 0.$$

> The integral converges only in the right half-plane; the function is then continued analytically to the rest of the complex plane, where the poles at $z = 0, -1, -2, \dots$ are the trace of the factorial's undefined values.

## The identities that do the work

| Identity | Statement | Use |
| --- | --- | --- |
| **Functional equation** | $\Gamma(z+1) = z\,\Gamma(z)$ | The factorial recurrence, continued |
| **Integer values** | $\Gamma(n) = (n-1)!$ | The bridge to combinatorics |
| **Half-integer** | $\Gamma(1/2) = \sqrt{\pi}$ | Gaussian integrals, the normal distribution |
| **Reflection** | $\Gamma(z)\Gamma(1-z) = \dfrac{\pi}{\sin \pi z}$ | Continues across the poles; gives the half-integer values |
| **Duplication** | $\Gamma(z)\Gamma\!\left(z+\tfrac12\right) = 2^{1-2z}\sqrt{\pi}\,\Gamma(2z)$ | Doubling arguments, beta integrals |
| **Beta relation** | $B(a,b) = \dfrac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$ | Integrals over the simplex, Bayesian conjugacy |
| **Stirling** | $\Gamma(z) \sim \sqrt{\dfrac{2\pi}{z}}\left(\dfrac{z}{e}\right)^z$ | Asymptotics of factorials and of large-parameter integrals |
| **Log-derivative** | $\psi(z) = \dfrac{\Gamma'(z)}{\Gamma(z)}$ (digamma) | Sums of harmonic type, maximum-likelihood equations |

> The reflection formula is the most useful single identity: it converts a value in the left half-plane into a value in the right half-plane, which is how the analytic continuation is actually computed. The poles are then not a defect of the definition but the image of the singularities of $\sin \pi z$ in the reflection.

## Where it appears

| Field | The appearance |
| --- | --- |
| **Combinatorics** | Factorials, binomial coefficients, the volume of the $n$-ball |
| **Probability** | The gamma, chi-square, beta and Dirichlet distributions; the normalising constants are gamma values |
| **Statistics** | The beta function in Bayesian conjugacy; the digamma in the likelihood equations of gamma-family models |
| **Analysis** | The Mellin transform, the zeta functional equation, the asymptotic expansion of integrals |
| **Physics** | Dimensional regularisation, the partition functions of ideal gases, the gamma-family special functions |
| **Number theory** | The functional equation of $\zeta(s)$, which pairs $\Gamma$ with the completed zeta |

> The distribution connection is the one most often met in applied work: if $X \sim \mathrm{Gamma}(k,\theta)$ then its density carries $1/\Gamma(k)$, and the moments are products of gamma ratios. The function is doing normalisation, not interpolation, in that context — and the two roles are the same object.

## The family

> The gamma function is the head of a family: the **beta** function (the ratio of gamma values), the **digamma** and **polygamma** (its logarithmic derivatives), the **incomplete gamma** (the integral to a finite limit, which is the cumulative distribution function of the gamma family), and the **multivariate gamma** (the complex Wishart normaliser). Each is a different question asked of the same integral.

## References

- [Gamma function](https://en.wikipedia.org/wiki/Gamma_function)
- Artin, E. (1964). *The gamma function*. Holt, Rinehart and Winston. — the classical short treatment
- Abramowitz, M., & Stegun, I. A. (1964). *Handbook of mathematical functions*. National Bureau of Standards. — the identities and tables
- [Beta Function](/view.html?p=notes/epistemica/mathematical/mapping/beta-function.md) — the ratio of gamma values
- [Bessel Function](/view.html?p=notes/epistemica/mathematical/mapping/bessel-function.md) — the sibling special function
- [Lambert W Function](/view.html?p=notes/epistemica/mathematical/mapping/lambert-w-function.md) — the other inverse-flavoured special function
- [Gamma Distribution](/view.html?p=notes/epistemica/observational/distribution/gamma-distribution.md) — the probabilistic reading of the normalising constant
