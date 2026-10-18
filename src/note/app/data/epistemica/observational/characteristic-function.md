# Characteristic Function


> A **characteristic function** is a complex-valued function that **uniquely encodes the probability distribution of a random variable**.
> 

> A characteristic function is a **representation of a random variable’s probability distribution** in the complex exponential domain that enables analysis, manipulation, and reconstruction of the distribution, particularly for studying sums of independent variables, convergence in distribution, and moment extraction.
> 

## Formulation

For a random variable ($X$), its characteristic function $\phi_X(t)$ is defined as: $\phi_X(t) = \mathbb{E}[e^{itX}] = \int_{-\infty}^{\infty} e^{itx} , dF_X(x)$

where:

- $i = \sqrt{-1}$ is the imaginary unit,
- $t \in \mathbb{R}$ is a real parameter,
- $F_X(x)$ is the cumulative distribution function of ($X$),
- $\mathbb{E}[\cdot]$ denotes the expectation.

## Property

1. **Uniqueness:** Each probability distribution has a unique characteristic function.
2. **Inversion:** The probability distribution can be recovered from the characteristic function via an inverse Fourier transform.
3. **Moments:** If they exist, the (n)-th moment of (X) can be obtained by differentiating $\phi_X(t)$ (n) times at (t=0).
4. **Convergence:** Useful in studying convergence in distribution (via Lévy’s continuity theorem).

## References

- https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory)
