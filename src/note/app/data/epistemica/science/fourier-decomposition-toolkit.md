# Fourier Decomposition Toolkit


> aka. Fourier Analysis.
> 

> **Fourier analysis** is a branch of mathematics that studies how functions or signals can be represented as a combination of simple waves, specifically sine and cosine functions (or complex exponentials). It allows us to **break down complex patterns into basic frequency components**, making it easier to analyze, understand, and manipulate data or phenomena that vary over time or space.
> 

## Toolkit

### 🧱 **Mathematical Core**

| Component | Description |
| --- | --- |
| **Function Spaces** | $L^2(\mathbb{R}),  L^2([0, T]),  \mathcal{S}(\mathbb{R})$, etc. |
| **Basis Functions** | Sines and cosines, or complex exponentials $e^{i\omega x}$ |
| **Inner Product** | $\langle f, g \rangle = \int f(x)\overline{g(x)}\,dx$ |
| **Orthogonality** | $\langle \phi_k, \phi_j \rangle = \delta_{kj}$ |
| **Completeness** | Any $f \in L^2$ can be expressed via basis expansion |

### 🛠 **Decomposition Tool**

| Tool | Input | Output | Domain |
| --- | --- | --- | --- |
| **Fourier Series** | Periodic function $f(x)$ | Harmonic coefficients $c_n$ | $L^2([0,T])$ |
| **Fourier Transform (FT)** | $f(x) \in L^1 \cap L^2$ | $\hat{f}(\omega)$ | $\mathbb{R}$ |
| **Discrete Fourier Transform (DFT)** | Sampled data $f[n]$ | $\hat{f}[k]$ | $\mathbb{Z}_N$ |
| **Fast Fourier Transform (FFT)** | DFT input | Efficient computation of DFT | Computational |
| **Short-Time Fourier Transform (STFT)** | $f(t)$, window $g(t)$ | Time-localized spectra $F(t,\omega)$ | Time-frequency |
| **Fractional Fourier Transform (FrFT)** | $f(x)$ | Projection onto rotated time-freq axes | Mixed domain |

### 🔍 **Processing Tool**

| Module | Operation | Uses |
| --- | --- | --- |
| **Convolution Engine** | $f * g \leftrightarrow \hat{f} \cdot \hat{g}$ | Signal filtering, system response |
| **Spectral Analysis** | .. | $\hat{f}(\omega)$ |
| **Filter Design** | Apply band-pass, low-pass, etc. in freq domain | DSP, control, imaging |
| **Windowing / Smoothing** | Multiply by window before FFT | Reduce spectral leakage |
| **Inverse Transforms** | Recover original signal | Reconstruction, synthesis |

### 📤 **Outputs (Interpretations & Representations)**

| Output Type | Meaning | Application |
| --- | --- | --- |
| **Spectrum (Freq Domain)** | Frequency content and strength | Signal diagnostics, audio/image |
| **Phase Spectrum** | Phase relationships between harmonics | Interference patterns, carrier phase |
| **Spectrogram (STFT)** | Time-evolving frequency content | Speech, music, vibration monitoring |
| **Filtered Signal** | Signal cleaned or modified in freq | Noise reduction, signal shaping |

[Fourier Transform](fourier-transform.md)

[Fast Fourier Transform (FFT)](fast-fourier-transform-fft.md)

## Capacity & Limitation

| Capability | Description | Fourier Tool(s) | Limitations |
| --- | --- | --- | --- |
| **Frequency Extraction** | Decomposes signal into pure frequency components | Fourier Transform, DFT | Poor time localization |
| **Periodic Signal Analysis** | Exact decomposition of periodic functions into harmonics | Fourier Series | Only works for periodic or quasi-periodic signals |
| **Spectral Analysis** | Reveals energy distribution across frequencies | FFT, Power Spectral Density | Assumes stationarity |
| **System Identification** | Models linear time-invariant systems via frequency response | Transfer Functions, Bode Plots | Not suitable for nonlinear or time-varying systems |
| **Convolution Simplification** | Converts convolution to multiplication in frequency domain | FT Convolution Theorem | Requires zero-padding and assumptions on boundaries |
| **Differential Equation Solving** | Transforms linear PDEs/ODEs into algebraic equations in frequency space | Fourier Transform, Eigenfunction Exp | Requires suitable boundary conditions |
| **Compression (Sparse Representation)** | Sparse representation for smooth signals | Truncated Fourier Series / FFT | Not efficient for sharp transitions or transients |
| **Filter Design** | Design and analyze frequency-selective filters | Ideal/Windowed Filters | Gibbs phenomenon; window design affects accuracy |
| **Phase and Amplitude Analysis** | Access to magnitude and phase spectrum | Complex Fourier Transform | Phase unwrapping is often needed |
| **Symmetry Detection** | Detect even/odd, real/imaginary properties | Fourier coefficient structure | Needs interpretation |
| **Global Structure Analysis** | Captures overall signal structure (not local behavior) | Full Fourier Transform | Not localized in time (non-adaptive) |

## Related Method

> See [Functional Decomposition](functional-decomposition.md).
> 

## References

- https://en.wikipedia.org/wiki/Fourier_analysis
- [Wave](https://app.notion.com/p/Wave-abe8be3df7354f11a8e84fa436de2e0b?pvs=21)
- [Trigonometry](note.html?n=epistemica/mathematical/geometry/trigonometry.md)
- 
- [Functional Decomposition](functional-decomposition.md)
