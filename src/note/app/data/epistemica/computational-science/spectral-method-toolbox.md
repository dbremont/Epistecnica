# Spectral Method Toolbox


> This **Spectral Method Toolbox** note describes the set of **epistemic tools** that leverage spectral representations—such as spectra, eigenvalues, eigenfunctions, and spectral decompositions—to analyze, represent, and solve problems. The toolbox encompasses both **spectral analysis** (for extracting and interpreting spectral information) and **spectral methods** (for solving mathematical and computational problems using spectral representations).
> 

> In this note, **spectrum** denotes the **structured decomposition** of an object into its fundamental components and their contributions. It is more than a range of values—it reveals the object's intrinsic structure. **Analogy:** Like identifying every ingredient in a plate of food and how much each contributes to its flavor.
> 

## Formulation

### What is the function of spectral methods?

> A spectral method changes the coordinate system of a problem from its original representation into one organized around its characteristic modes.
> 

> Spectral analysis uses spectral representations to understand structure; spectral methods use spectral representations to perform computation.
> 

| Function | What the spectral method does |
| --- | --- |
| **Representation** | Expresses an object in terms of modes or basis functions |
| **Decomposition** | Separates a complex object into simpler components |
| **Compression** | Retains dominant modes while discarding less important ones |
| **Approximation** | Represents a continuous or high-dimensional object with a finite number of modes |
| **Transformation** | Converts a problem into a representation where its structure is easier to manipulate |
| **Analysis** | Makes characteristic scales, frequencies, eigenmodes, or latent structures explicit |
| **Solution** | Converts mathematical problems, such as differential equations, into problems involving coefficients or modes |
| **Filtering** | Selects, suppresses, or reconstructs particular spectral components |
| **Model reduction** | Represents a high-dimensional system using a smaller set of dominant modes |
| **Pattern discovery** | Reveals recurring, dominant, or dynamically important structures |

### Spectral

A **spectral** representation describes an object in terms of a structured collection of **characteristic components or modes** and the characteristic values associated with them.

The central idea is:

> **An object can be represented or analyzed through the modes that constitute its structure and the characteristic values that describe those modes.**
> 

Depending on the domain, the modes may be frequencies, eigenvectors, singular vectors, wavelets, eigenfunctions, graph modes, or other basis-like components. The associated characteristic values may be frequencies, eigenvalues, singular values, scales, growth rates, or energy levels.

Thus, *spectral* does not refer to one particular mathematical technique. It denotes a family of representations and analyses organized around the decomposition of an object into characteristic modes.

### Spectrum

A **spectrum** is the structured collection of **characteristic values** associated with the modes of an object under a particular spectral representation or operator.

Formally, a spectral representation can be expressed abstractly as: $\mathcal{O}
;\longrightarrow;
{(m_i,\lambda_i)}_{i=1}^{n}$

where:

- $\mathcal{O}$ is the object being analyzed,
- $m_i$ is a component or mode,
- $\lambda_i$ is the characteristic value associated with that mode.

The spectrum is therefore not merely the numerical range occupied by the object. It describes **how the object's structure is distributed across characteristic modes**.

The precise meaning of a spectrum depends on the underlying transformation or operator:

- Fourier analysis → frequencies
- eigenvalue analysis → eigenvalues
- SVD → singular values
- graph spectral analysis → graph eigenvalues
- Koopman analysis → Koopman eigenvalues
- quantum mechanics → energy eigenvalues

In some contexts, the spectrum is formally defined as a set of characteristic values; in others, spectral representations additionally retain information about the associated modes, coefficients, multiplicities, or energy.

### Component

A **component** is a constituent element obtained by decomposing an object according to a particular representation.

In a spectral context, a component is typically a **mode** that captures a particular structural contribution of the object.

Examples include:

- a sinusoidal component in Fourier analysis,
- a wavelet component in wavelet analysis,
- an eigenvector in eigenvalue decomposition,
- a principal component in PCA,
- a singular vector in SVD,
- an eigenfunction in Koopman analysis,
- a graph eigenvector in spectral graph analysis.

A component is therefore **representation-dependent**. The same object may have different components under different spectral transformations.

### Characteristic Value

A **characteristic value** is a numerical quantity associated with a component or mode that describes a relevant property of that mode.

The characteristic value depends on the spectral construction.

Examples include:

| Spectral representation | Component | Characteristic value |
| --- | --- | --- |
| Fourier | Sinusoid | Frequency |
| Wavelet | Wavelet mode | Scale / frequency |
| Eigenvalue decomposition | Eigenvector | Eigenvalue |
| SVD | Singular vector | Singular value |
| PCA | Principal component | Eigenvalue / explained variance |
| DMD | Dynamic mode | Complex eigenvalue |
| Koopman analysis | Eigenfunction | Koopman eigenvalue |
| Quantum mechanics | Energy eigenstate | Energy |

The characteristic value provides a way of **ordering, comparing, or interpreting the modes**.

### Spectral Analysis

**Spectral analysis** is the epistemic activity of extracting, estimating, interpreting, or comparing the spectral structure of an object.

Its purpose is primarily **descriptive and inferential**: $\text{Object}
\rightarrow
\text{Spectral Representation}
\rightarrow
\text{Modes + Characteristic Values}
\rightarrow
\text{Interpretation}$

Spectral analysis can therefore be used to answer questions such as:

- Which frequencies dominate a signal?
- Which timescales contain the greatest energy?
- Which latent factors explain the greatest variance?
- Which eigenmodes dominate a dynamical system?
- Which network structures are represented by the leading graph modes?
- How does the spectral structure change through time?

Spectral analysis does not necessarily mean solving a differential equation or constructing a numerical approximation. Its primary function is to **discover and characterize structure through spectral representation**.

### Spectral Method

A **spectral method** is a computational or mathematical method that represents an object, function, or solution using a collection of basis functions, modes, eigenfunctions, or other spectral components and performs analysis or computation in that representation.

In numerical mathematics, spectral methods commonly approximate a function as: $f(x) \approx \sum_{k=0}^{N} a_k\phi_k(x)$

where:

- $\phi_k(x)$ are basis functions or modes,
- $a_k$ are coefficients,
- $N$ determines the truncation of the representation.

The computational problem is then transformed from operating directly on (f(x)) to operating on its spectral representation.

This distinguishes **spectral methods** from **spectral analysis**:

| Concept | Primary purpose |
| --- | --- |
| **Spectral analysis** | Discover and characterize spectral structure |
| **Spectral method** | Use spectral representation as a computational or mathematical method |

The distinction is not absolute: many techniques perform both spectral analysis and computation.

### Spectral Decomposition

A **spectral decomposition** expresses an object in terms of constituent modes under a specified mathematical structure.

Abstractly: $\mathcal{O}
\approx
\sum_i c_i m_i$

where $m_i$ are modes and $c_i$ describe their contribution.

Depending on the problem, the decomposition may be:

- Fourier decomposition,
- eigenvalue decomposition,
- singular-value decomposition,
- wavelet decomposition,
- modal decomposition,
- graph spectral decomposition,
- Koopman decomposition.

The decomposition provides the structural bridge between the original object and its spectral representation.

### Spectral Representation

A **spectral representation** is the representation of an object in terms of its spectral components and their associated coefficients or characteristic values.

It can be viewed as an epistemic interface: $\boxed{
\text{Object}
\rightarrow
\text{Transformation}
\rightarrow
\text{Spectral Representation}
\rightarrow
\text{Components}
+
\text{Characteristic Values}
}$

The representation makes properties that may be difficult to observe in the original representation explicit.

For example, a financial price series may appear irregular in the time domain while its spectral representation may reveal concentrations of variation around particular timescales.

### Spectral Toolbox

> The **Spectral Method Toolbox** is the collection of epistemic and computational tools that use **spectral representations** to expose, characterize, compare, model, or solve structures in objects and processes.
> 

> Transform an object into a representation in which its characteristic modes and their contributions become observable, measurable, and manipulable.
> 

> Its tools can be organized according to the kind of structure they expose:
> 

| Structural Domain | Spectral Tool — Method | Object | Components — (Modes) | Characteristic Values | Primary Use |
| --- | --- | --- | --- | --- | --- |
| **Harmonic structure** | Fourier Transform | Signal | Sinusoids | Frequency | Identify periodic and oscillatory structure |
| **Time-localized harmonic structure** | Short-Time Fourier Transform | Non-stationary signal | Windowed sinusoids | Frequency + time | Track changing frequency content |
| **Multiscale structure** | Wavelet Transform | Signal | Wavelets | Scale / frequency | Identify localized structures across timescales |
| **Adaptive oscillatory structure** | Empirical Mode Decomposition | Non-stationary signal | Intrinsic Mode Functions | Local / instantaneous frequency | Extract data-adaptive oscillatory modes |
| **Adaptive time-frequency structure** | Hilbert–Huang Transform | Non-stationary signal | Intrinsic Mode Functions | Instantaneous frequency | Analyze nonlinear and non-stationary oscillations |
| **Latent variance structure** | PCA | Multivariate data | Principal components | Eigenvalues / explained variance | Identify dominant directions of variation |
| **Matrix structure** | SVD | Matrix / data | Singular vectors | Singular values | Identify dominant low-rank structure |
| **Linear dynamical structure** | Dynamic Mode Decomposition | Time-evolving data | Dynamic modes | Complex eigenvalues | Identify spatial patterns and their dynamics |
| **Dynamical-system structure** | Koopman Spectral Analysis | Dynamical system | Koopman eigenfunctions | Koopman eigenvalues | Represent nonlinear dynamics through spectral modes |
| **Operator structure** | Spectral Decomposition | Linear operator | Eigenvectors / eigenfunctions | Eigenvalues | Characterize intrinsic operator modes |
| **Graph structure** | Spectral Graph Analysis | Graph / network | Graph eigenvectors | Graph eigenvalues | Identify network structure and diffusion modes |
| **Manifold structure** | Laplacian Eigenmaps | Data manifold / graph | Laplacian eigenvectors | Laplacian eigenvalues | Represent low-dimensional manifold structure |
| **Diffusion structure** | Diffusion Maps | Data manifold | Diffusion modes | Diffusion eigenvalues | Reveal geometric and connectivity structure |
| **Nonlinear feature structure** | Kernel PCA | Nonlinear data | Kernel principal components | Kernel eigenvalues | Extract nonlinear latent structure |
| **Tensor structure** | HOSVD / Tucker Decomposition | Tensor | Factor modes | Singular values / mode strengths | Decompose multidimensional structure |
| **Source structure** | ICA | Multivariate observations | Independent components | Component statistics / weights | Separate latent statistical sources |
| **Physical energy structure** | Quantum Spectral Decomposition | Hamiltonian / operator | Energy eigenstates | Energy eigenvalues | Characterize allowed physical states |
| **Numerical solution structure** | Spectral Methods | Differential equation / function | Basis functions | Expansion coefficients / modes | Approximate and solve mathematical problems |

## QA

### Which is the `difference` of the term **`Spectrum`  and a range of values?**

> This is an important distinction. A **`range`** and a **`spectrum`** are not the same thing, even though both involve collections of values.
> 

| **Aspect** | Range of values | Spectrum |
| --- | --- | --- |
| **Meaning** | The set of possible values a quantity can take | A set of characteristic modes or values obtained by decomposing an object |
| **Origin** | Direct measurement or definition | Result of a mathematical or physical transformation |
| **Structure** | Usually just an interval or set | Values associated with modes, often with weights or multiplicities |
| **Example** | Temperatures from 15°C to 35°C | Frequencies present in a recording |

### What is the history of the term `Spectra`?

| Period | Approx. Date | Primary Contributor(s) | Meaning of **Spectrum** | Conceptual Shift |
| --- | --- | --- | --- | --- |
| **Classical Latin** | Before 1st century CE | Roman writers | *Spectrum* = appearance, image, apparition, ghost, phantom | A visible manifestation or appearance |
| **Optics** | 1666–1672 | Isaac Newton | The band of colors produced when white light passes through a prism | White light is revealed as a composition of colors |
| **Spectroscopy** | Early–mid 19th century | Joseph von Fraunhofer, Gustav Kirchhoff, Robert Bunsen | The distribution of light intensity across wavelengths, including emission and absorption lines | The spectrum becomes a diagnostic fingerprint of matter |
| **Fourier Analysis** | Early 19th century | Joseph Fourier | The distribution of a signal's energy or amplitude across frequencies | Signals are understood as sums of frequency components |
| **Linear Algebra** | Late 19th–early 20th century | David Hilbert and others | The set of eigenvalues of a matrix or linear transformation | Operators are characterized by their intrinsic modes |
| **Functional Analysis** | Early–mid 20th century | David Hilbert, John von Neumann | The spectrum of an operator, including point, continuous, and residual spectra | Generalization from matrices to infinite-dimensional operators |
| **Quantum Mechanics** | 1920s onward | Werner Heisenberg, Erwin Schrödinger | The allowed energy levels (eigenvalues) of quantum operators | Physical observables are understood through operator spectra |
| **Modern Mathematics & Engineering** | Late 20th century–Present | Many contributors | Any structured decomposition into characteristic modes (eigenvalues, frequencies, singular values, graph modes, etc.) | **Spectrum** becomes a general concept for revealing the intrinsic components of a mathematical or physical object |

### Which are the related epistemic tools?

| Class of Method | Method | Object | Components (Modes) | Characteristic Values |
| --- | --- | --- | --- | --- |
| **Harmonic Spectral Analysis** | Fourier Transform | Signal | Sinusoids | Frequencies |
| **Harmonic Spectral Analysis** | Short-Time Fourier Transform | Signal | Windowed sinusoids | Frequency + time |
| **Multiresolution Spectral Analysis** | Wavelet Transform | Signal | Wavelets | Scale (frequency) |
| **Adaptive Time–Frequency Analysis** | Hilbert–Huang Transform | Signal | Intrinsic Mode Functions | Instantaneous frequency |
| **Adaptive Signal Decomposition** | Empirical Mode Decomposition | Signal | Adaptive modes | Local frequency |
| **Linear Algebraic Spectral Analysis** | Eigenvalue Decomposition | Matrix / Operator | Eigenvectors | Eigenvalues |
| **Linear Algebraic Spectral Analysis** | Singular Value Decomposition (SVD) | Matrix | Singular vectors | Singular values |
| **Statistical Spectral Analysis** | Principal Component Analysis (PCA) | Covariance matrix | Principal components | Eigenvalues |
| **Blind Source Separation** | Independent Component Analysis (ICA) | Data matrix | Independent components | No natural spectrum (component strength is often used) |
| **Dynamical Spectral Analysis** | Dynamic Mode Decomposition (DMD) | Time-evolving system | Dynamic modes | Complex eigenvalues |
| **Operator Spectral Analysis** | Koopman Spectral Analysis | Dynamical system | Koopman eigenfunctions | Koopman eigenvalues |
| **Reduced-Order Modeling** | Proper Orthogonal Decomposition (POD) | Field data | Orthogonal modes | Modal energy |
| **Graph Spectral Analysis** | Spectral Graph Decomposition | Graph | Graph eigenvectors | Graph eigenvalues |
| **Manifold Learning** | Laplacian Eigenmaps | Graph | Laplacian eigenvectors | Laplacian eigenvalues |
| **Manifold Learning** | Diffusion Maps | Data manifold | Diffusion modes | Diffusion eigenvalues |
| **Kernel Spectral Methods** | Kernel PCA | Nonlinear data | Kernel principal components | Kernel eigenvalues |
| **Tensor Spectral Methods** | Tensor Decompositions (HOSVD, Tucker) | Tensor | Factor matrices | Singular values |
| **Matrix Factorization** | Non-negative Matrix Factorization (NMF) | Matrix | Basis vectors | Component weights (not a true spectrum) |
| **Quantum Spectral Theory** | Quantum Spectral Decomposition | Hamiltonian | Energy eigenstates | Energy levels |

### How to apply spectral methods to market signals?

> Spectral methods analyze market signals by decomposing them into characteristic components, where each component is associated with a characteristic value (such as frequency, timescale, eigenvalue, singular value, or energy). This decomposition reveals structures that are difficult to observe in the original time-domain signal, including dominant cycles, trends, volatility regimes, correlations, and latent factors.
> 

> For financial markets, the notion of a "characteristic value" depends on the spectral method being used.
> 

| Spectral Method | Components | Characteristic Value | What it reveals |
| --- | --- | --- | --- |
| Fourier Transform | Sinusoidal modes | Frequency | Market cycles (daily, weekly, yearly, etc.) |
| Wavelet Transform | Localized wavelets | Scale (or frequency) | Time-varying cycles and transient events |
| Eigenvalue Decomposition | Eigenvectors | Eigenvalues | Dominant correlation modes and market factors |
| Singular Value Decomposition (SVD) | Singular vectors | Singular values | Dominant latent structures in return matrices |
| Principal Component Analysis (PCA) | Principal components | Eigenvalues | Systematic risk factors |
| Dynamic Mode Decomposition (DMD) | Dynamic modes | Complex eigenvalues | Growth/decay rates and oscillatory dynamics |
| Hilbert-Huang Transform | Intrinsic Mode Functions | Instantaneous frequency | Non-stationary oscillations |
| Spectral Graph Methods | Graph eigenvectors | Graph eigenvalues | Market network structure |

## References

- https://www.st-andrews.ac.uk/~wjh/dataview/tutorials/sonogram.html#spectral-analysis
- https://en.wikipedia.org/wiki/Spectral_method
- https://en.wikipedia.org/wiki/Spectrum
