---
tags: [mathematics, analytical, function, representation]
---

# Fourier Series

> A **Fourier series** expands a periodic function into a sum of sines and cosines: $f(x) = a_0 + \sum_{n\ge1}\big(a_n\cos nx + b_n\sin nx\big)$, with the coefficients obtained by projecting onto each harmonic.

## Formulation

> **What it is.** The periodic case of the Fourier transform, and the oldest instance of an orthonormal expansion: the functions $e^{inx}$ form an orthogonal basis of $L^2$ on a period, so a function is its list of coefficients in that basis.
>
> **Type.** A `Concept` — a representational construction. The [Fourier transform](note.html?n=epistemica/singular/fourier-transform.md) is its non-periodic limit; the [integral transform](integral-transform.md) is the general frame.
>
> **Boundary.** Pointwise convergence is delicate (Gibbs phenomenon, Dirichlet conditions); $L^2$ convergence is the clean statement, because there the harmonics really are a basis of a [Hilbert space](../space/hilbert-space.md).

## Key results

- **Orthogonality.** $\int_0^{2\pi} e^{inx} e^{-imx} dx = 2\pi\delta_{nm}$ — the inner product that makes the expansion a projection.
- **Parseval.** $\sum |c_n|^2 = \frac{1}{2\pi}\int |f|^2$ — energy is conserved by the transform, which is why the Hilbert-space reading is the right one.
- **Convolution.** Multiplying coefficients convolves functions and vice versa — the reason Fourier analysis diagonalizes linear time-invariant operators.
- **Smoothness.** The faster the coefficients decay, the smoother the function; a jump forces $c_n \sim 1/n$ and the Gibbs overshoot.

## References

- https://en.wikipedia.org/wiki/Fourier_series
- [Fourier Transform](note.html?n=epistemica/singular/fourier-transform.md) · [Harmonic Analysis](harmonic-analysis.md) · [Hilbert Space](../space/hilbert-space.md) · [Wavelet](wavelet.md)
