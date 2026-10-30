# Functional Decomposition


> **Functional Decomposition** is the process of breaking down a complex function, signal, or system into simpler, constituent parts—often in terms of well-understood *basis functions* or *components*—to analyze, manipulate, or understand its structure, behavior, or properties.
> 

> Decompose something **complex** into **meaningful, interpretable, and manipulable parts**, often for **analysis**, **simplification**, or **computational efficiency**.
> 

## Methods

| Toolkit Area / Family | Tools / Methods Inside It | Core Use |
| --- | --- | --- |
| **Fourier Methods** | Fourier Series, Fourier Transform, DFT, FFT, STFT, FrFT, Windowed FT | Global and local frequency decomposition |
| **Wavelet Methods** | Continuous Wavelet Transform, Discrete Wavelet Transform, Multiresolution Analysis | Multi-scale, localized signal analysis |
| **Time-Frequency Methods** | STFT, Gabor Transform, Wavelets, Hilbert–Huang Transform, EMD | Joint time–frequency representations |
| **Integral Transforms** | Laplace Transform, Z-Transform, Hilbert Transform, Fourier Integral Operators | System analysis, stability, analytic continuation |
| **Microlocal/Geometric** | Fourier–Bros–Iagolnitzer Transform, FIOs, Pseudodifferential Operators | Singularity tracking, PDEs, geometric optics |
| **Adaptive/Nonlinear Methods** | EMD, Variational Mode Decomposition, Matching Pursuit, Synchrosqueezing | Data-driven decomposition of nonstationary or nonlinear signals |
| **Computational Enhancements** | FFT, CZT, Multi-resolution FFT, Sparse FFT | Fast computation and focused spectrum analysis |

## Common Types of Functional Decomposition

| Method | Basis Functions | Domain | Decomposes Into |
| --- | --- | --- | --- |
| **Fourier Series/Transform** | Sines and cosines | Time, space | Frequencies |
| **Wavelet Transform** | Scaled & shifted wavelets | Time-scale | Local features at multiple resolutions |
| **Eigenfunction Expansion** | Problem-specific eigenfunctions | Differential operators | Normal modes or harmonics |
| **Principal Component Analysis (PCA)** | Orthogonal vectors (data-derived) | Multivariate data space | Maximal variance directions |
| **Singular Value Decomposition (SVD)** | Orthogonal vector triples | Linear operators/matrices | Rank-ordered mode components |

## 📤  **Interpretations & Representations**

> 

| Representation Type | Description | Interpretation Contexts |
| --- | --- | --- |
| **Frequency Spectrum** | ( | \hat{f}(\omega) |
| **Time–Frequency Representation** | F(t,ω)F(t, \omega) via STFT or wavelet | How signal changes over time |
| **Energy Distribution** | ( \int | c_k |
| **Amplitude–Phase Spectrum** | ( | c_k |
| **Mode Shape or Eigenfunction** | In PDEs: spatial pattern of a vibration or field | Physical geometry (e.g., drumhead modes) |
| **Sparse Coefficients** | Most ckc_k small → compressible | Useful for compression, noise removal |
| **Feature Embedding** | In ML: decomposition as embedding of structure | Feature extraction, dimensionality reduction |
| **Component Signal** | Reconstructed parts: ckϕk(x)c_k \phi_k(x) | Local structure, layers of signal |

## 🎨 Visual Representation

| Tool | Visual Output | Used In |
| --- | --- | --- |
| **Spectrogram** | Heatmap of frequency vs time | Audio, speech, bio-signals |
| **Phase Space Trajectory** | Time evolution of components | Dynamical systems |
| **Modal Plot** | Spatial shape of eigenmodes | Structural engineering, acoustics |
| **Coefficient Heatmap** | Energy across basis index (e.g. ckc_k) | Compression analysis, filtering |
| **Wavelet Scalogram** | Energy at each scale and time | Edge and anomaly detection |
| **Time–Reconstruction Layers** | Each basis function’s contribution | Multi-layer analysis (EMD, DWT) |

## Limits

> What Kinds of Functions Can’t Be Decomposed by Any Method?
> 

> Most practical or physical functions can be decomposed.
But when functions become non-measurable, non-integrable, non-approximable, or non-computable, no known decomposition method applies.
> 

## Uses

| Domain | Purpose | Example |
| --- | --- | --- |
| **Signal Processing** | Analyze frequency content | Fourier or Wavelet Transform |
| **Numerical Methods** | Solve PDEs using basis expansions | Finite Element Methods (FEM) |
| **Control Systems** | Break systems into subsystems | Block diagrams |
| **Software Engineering** | Divide complex systems into modules/functions | Functional abstraction |
| **Physics & Engineering** | Mode decomposition, resonance analysis | Normal mode analysis |

## References

- https://en.wikipedia.org/wiki/Functional_decomposition
- [Function Space](../mathematical/space/function-space.md)
- http://bactra.org/notebooks/basis-selection-in-function-decomposition.html
