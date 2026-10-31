---
tags: [framework]
---

# Harmonic Analysis

 : Wavelet (Wavelet%207b19eaee77db4a42bf9c1c9027f158c2.md), Function (Function%20049537a4fd564eaaac4bae443839b0c0.md), Trigonometry (Trigonometry%201d6c0f5171ec80529c03fd3d402539db.md)

> **Why "Harmonic"?** The term originates from **acoustics**, where higher-frequency integer multiples of a fundamental tone are called "harmonics." In analysis, this generalizes to any setting where functions are built from sinusoidal modes.
> 

> A **harmonic** is a **pure sinusoidal component** (e.g., a sine or cosine wave) that arises in the **Fourier decomposition** of a function or signal.
> 

 Specifically:

- Given a function$f$ (real- or complex-valued) defined on a domain $\Omega$(e.g., $\mathbb{R}^n$, the torus $\mathbb{T}$, or a discrete set), a harmonic is an **eigenfunction** of a differential or difference operator associated with the domain.
- In classical **Fourier analysis**, harmonics are the **trigonometric functions** `$e^{2\pi i k \cdot x}$`(for $k \in \mathbb{Z}^n$) that form an orthonormal basis for $L^2$-spaces on periodic domains.
- In the context of **spectral theory**, harmonics generalize to **eigenfunctions of the Laplacian** $\Delta$, satisfying $\Delta \phi = -\lambda \phi$ for some eigenvalue $\lambda \geq 0$.

## **Key Properties**

1. **Frequency Domain Representation**:
    - A harmonic has a **single frequency** $\xi$(or wavenumber $k$), making it a **pure tone** in signal processing.
    - In $\mathbb{R}^n$, harmonics take the form $e^{i \xi \cdot x}$.
2. **Orthogonality & Completeness**:
    - Harmonics are often **mutually orthogonal** (e.g., Fourier basis on $L^2([0,1]$), allowing unique signal decomposition.
    - They provide a **complete basis** for function spaces under certain conditions (e.g., Fourier series on compact domains).
3. **Generalizations**:
    - In **non-Euclidean settings** (e.g., manifolds, graphs), harmonics are eigenfunctions of the **Laplace-Beltrami operator** or graph Laplacian.
    - In **time-frequency analysis**, wavelets and other bases extend harmonic concepts to localized oscillations.

## Field

| **Branch** | **Core Idea** | **Key Techniques** | **Applications** |
| --- | --- | --- | --- |
| **Classical Harmonic Analysis** | Decomposition of functions into sines, cosines, or exponentials | Fourier series, Fourier transforms, convolution, Parseval/Plancherel identities | Signal analysis, PDEs, physics |
| **Modern Harmonic Analysis** | Extension to groups, manifolds, and general spaces | Representation theory, characters, dual groups, spectral decomposition | Group theory, analysis on manifolds, number theory |
| **Operator-Theoretic Harmonic Analysis** | Study of operators via their spectral properties | Singular integrals, Calderón-Zygmund operators, Littlewood-Paley theory | PDE regularity, functional analysis |
| **Signal-Oriented Harmonic Analysis** | Time/frequency localization of signals | Short-time Fourier transform (STFT), wavelets, Gabor analysis | Signal processing, image analysis, data compression |
| **Nonlinear / Geometric Harmonic Analysis** | Harmonic analysis with geometric or nonlinear constraints | Restriction estimates, oscillatory integrals, Kakeya problems | Analysis, combinatorics, PDEs, geometric measure theory |

## References

- https://en.wikipedia.org/wiki/Harmonic
