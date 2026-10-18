---
tags: [analytical]
---

# Function

 : Operator (Operator%2096b9329acc2b493388cda715c8e66caa.md), Wavelet (Wavelet%207b19eaee77db4a42bf9c1c9027f158c2.md), Polynomial (Polynomial%20c29542c4a2ce4a0e887db0a00b61e977.md), Logistic Function (Logistic%20Function%201cec0f5171ec80c0bdc1dc3a00517092.md), Expression (Expression%201d1c0f5171ec8015bae8d3fc820709ca.md), Functional (Functional%201d6c0f5171ec80b19358d228c3cf04a6.md), Knot (Knot%201d6c0f5171ec80a09a74d226b53f7ee3.md), Bijective Method (Bijective%20Method%20258c0f5171ec805191e3ea620c687525.md), Pigeonhole Principle (Pigeonhole%20Principle%20258c0f5171ec80558fbbd3e50222f26a.md), Harmonic Analysis (Harmonic%20Analysis%201bbc0f5171ec8015a56bc2d92c1438a9.md), Representation (Representation%20262c0f5171ec8021a535fc9111fd1ed5.md)

> A **function** is a relation between two sets of values, where each input value (also called the independent variable) corresponds to exactly one output value (also called the dependent variable).
> 

> A **function** can be thought of as a rule or a machine that takes an input value and produces a corresponding output value.
> 

> **Other names** include Mapping (mapeo), Transformation (transformación), Correspondence (correspondencia), Relation (relación), Dependence (dependencia), Rule (regla), and others.
> 

## Property

| **Property** | **Description** |
| --- | --- |
| **Domain** | The set of all possible input values for which the function is defined. |
| **Range** | The set of all possible output values of the function. |
| **Injective (One-to-One)** | A function is injective if each element of the domain maps to a unique element in the range. |
| **Surjective (Onto)** | A function is surjective if every element in the codomain is mapped by at least one element in the domain. |
| **Bijective** | A function is bijective if it is both injective and surjective. |
| **Even** | A function $f(x)$ is even if $f(-x)=f(x)$. |
| **Odd** | A function $f(x)$ is odd if $f(-x)=-f(x)$. |
| **Periodic** | A function is periodic if $f(x+T)=f(x)$ for some $T > 0$ (the period). |
| **Continuous** | A function is continuous if there are no abrupt changes or breaks in its graph. |
| **Differentiable** | A function is differentiable if it has a defined derivative at every point in its domain. |
| **Bounded** | A function is bounded if its range is contained within a finite interval. |
| **Monotonic** | A function is monotonic if it is either entirely non-increasing or non-decreasing. |
| **Convex** | A function $f(x)$ is convex if $f(\lambda x_1+(1-\lambda)x_2)\leq \lambda f(x_1)+(1-\lambda)f(x_2)$ for all $x_1,x_2$ and $\lambda\in[0,1]$. |
| **Concave** | A function $f(x)$ is concave if $f(\lambda x_1+(1-\lambda)x_2)\geq \lambda f(x_1)+(1-\lambda)f(x_2)$ for all $x_1,x_2$ and $\lambda\in[0,1]$. |
| **Lipschitz Continuous** | A function is Lipschitz continuous if there exists a constant \(L\) such that \( |
| **Injective at Points** | A function is locally injective if it is injective within a neighborhood around each point. |
| **Idempotent** | A function $f(x)$ is idempotent if $f(f(x))=f(x)$. |

## Signature

> Signatures describe the type of mapping, emphasizing the domain (input) and codomain (output), without tying to a specific field. They can be **functional** (producing numbers, vectors, distributions, labels, or functions) or **operator** (producing transformations or evolving other entities).
> 

> **Note:** Do not take this terminology as fixed or authoritative; it is intended only to help us understand the structure of certain types of functions.
> 

| Name | **Signature** | Description |
| --- | --- | --- |
| Functional | **Set → Scalar** | Maps a set of elements to a single numeric value summarizing some property. |
| Functional | **Set → Vector** | Maps a set of elements to a vector, capturing multiple aggregated properties. |
| Functional | **Set → Tag (Label)** | Maps a set of elements to a qualitative label or category. |
| Functional | **Set → Distribution** | Maps a set of elements to a full distribution or function describing variation across the set. |
| Operator | **Set → Operator** | Produces an operator or transformation acting on the system or set. |
| Operator | **Operator → Operator** | Evolves or modifies an operator according to a rule or process. |
| Functional | **Function → Scalar / Vector** | Evaluates a property from a function, e.g., extracting summary measures. |
| Operator / Functional | **Set → Function** | Maps a set of elements to a function capturing relationships, correlations, or behaviors. |
| Functional | **Function → Distribution** | Converts a function into a distribution-like representation. |
| Operator | **Function → Function** | Evolves a function over a domain, e.g., transformation or propagation. |
| Functional | **Scalar / Vector → Scalar / Vector** | Maps numeric summaries to other summaries, e.g., aggregations, transformations, or feature mappings. |

## Taxonomy

| **Category** | **Function** | **Expression** | **Applications** |
| --- | --- | --- | --- |
| **Algebraic Functions** | Polynomial | $f(x) = a_nx^n + \cdots + a_0$ | Algebra, modeling, curve fitting |
|  | Rational | $f(x) = \frac{P(x)}{Q(x)}$ | Engineering, control theory |
|  | Radical | $f(x) = \sqrt{x}, \sqrt[n]{x}$ | Geometry, physics |
| **Transcendental Functions** | Exponential | $f(x) = a^x, exe^x$ | Growth/decay, finance |
|  | Logarithmic | $f(x) = \log_a x, ln⁡x\ln x$ | Information theory, complexity |
|  | Trigonometric | $\sin x, \cos x, \tan x$ | Waves, mechanics, signal processing |
|  | Inverse Trigonometric | $\arcsin x, \arccos x$ | Geometry, calculus |
|  | Hyperbolic | $\sinh x, \cosh x$ | Relativity, PDEs |
|  | Inverse Hyperbolic | $\text{arsinh}(x), \text{arcosh}(x)$ | Special integrals, geometry |
| **Sigmoid-like Functions** | **Logistic function** | $f(x) = \frac{1}{1 + e^{-x}}$ | Machine learning, population dynamics |
|  | Hyperbolic tangent | $\tanh x$ | Activation functions, signal compression |
|  | Arctangent function | $\arctan x$ | Neural networks, control systems |
|  | General sigmoid | Any S-shaped function | Classification, smooth thresholding |
| **Piecewise Functions** | Absolute value | … | … |
|  | Sign function | $\text{sgn}(x)$ | Directional control, classification |
|  | Step / Heaviside | $H(x) = \begin{cases} 0 & x < 0 \\ 1 & x \ge 0 \end{cases}$ | Signal processing, switching functions |
|  | Ramp function | $\max(0, x)$ | ReLU in neural nets |
|  | Dirichlet function | Discontinuous everywhere | Real analysis, counterexamples |
| **Special Functions** | Gamma function | $\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$ | Extensions of factorials, statistics |
|  | Beta function | Related to Gamma; used in statistics | Bayesian statistics |
|  | Error function (erf) | Related to normal distribution | Probability, heat equations |
|  | Bessel functions | Solutions to Bessel’s differential equation | Wave propagation, engineering |
|  | Legendre / Hermite / Laguerre | Orthogonal polynomials | Quantum mechanics, numerical methods |
| **Set-theoretic Functions** | Indicator function | $\mathbf{1}_A(x)$ | Probability, integration |
|  | Kronecker delta | $\delta_{ij}$ | Discrete math, tensors |
|  | Dirac delta (generalized) | $\delta(x)$ (distribution) | Physics, signal processing |
| **Boolean Functions** | AND, OR, XOR | Logical binary functions | Logic, circuits, computer science |
| **Multivariable Functions** | Scalar fields | $f(x, y), f(x, y, z)$ | Thermodynamics, economics |
|  | Vector fields | $\vec{F}(x, y, z)$ | Electromagnetism, fluid dynamics |
|  | Gradient, Divergence, Curl | Derived vector-valued operations | Differential geometry, physics |
| **Implicit Functions** | Defined by relation | $x^2 + y^2 = 1$ | Geometry, multivariable analysis |
| **Parametric Functions** | Parametric curves/surfaces | $x(t), y(t)$ | Graphics, physics |
| **Stochastic Functions** | Random variables, Processes | $X(\omega), B(t)$ | Statistics, stochastic modeling |

### Activation Function

> See more here ([Activation Function](activation-function.md)).
> 

## Representation

> aka. Decomposition.
> 

| **Concept** | **Definition** | **Example** |
| --- | --- | --- |
| **Function Decomposition** | Breaking down a complex function into simpler, smaller functions. | Decomposing $f(x) = 3x^2 + 2x + 1$ into $f(x) = g(x) + h(x)$ where$g(x) = 3x^2$ and $h(x) = 2x + 1$. |
| **Composite Functions** | A function formed by combining two functions, $f(g(x))$. | If $f(x) = x^2$ and $g(x) = x + 1$, then $f(g(x)) = (x + 1)^2$. |
| **Linear Decomposition** | Expressing a function as a sum of linear components. | $f(x) = 2x^2 + 3x + 1$ can be decomposed into linear functions like$g(x) = 2x^2$ and $h(x) = 3x + 1$. |
| **Polynomial Decomposition** | Breaking down a polynomial into simpler polynomials or factors. | Decomposing$f(x) = x^3 - 3x^2 + 4$ into$g(x) = (x - 1)(x^2 - 2x - 4)$. |
| **Partial Fraction Decomposition** | Expressing a rational function as a sum of simpler fractions. | $f(x) = \frac{2x + 3}{(x - 1)(x + 2)}$ can be decomposed into $\frac{A}{x - 1} + \frac{B}{x + 2}$. |
| **Trigonometric Decomposition** | Breaking down trigonometric functions into simpler components. | $f(x) = \sin^2(x) + \cos^2(x)$ can be recognized as $1$ (Pythagorean identity). |
| **Fourier Decomposition** | Expressing a function as a sum of sinusoidal functions. | $f(t) = A \sin(kt) + B \cos(kt)$, where$A$ and $B$are coefficients. |
| **Harmonic Analysis** | Analyzing functions in terms of sinusoidal components and their frequencies. | Decomposing a function $f(x)$ using its Fourier series:$f(x) = \sum_{n=0}^{\infty} a_n \cos(nx) + b_n \sin(nx)$. |
| **Wavelet Decomposition** | Breaking down a function into wavelets, which are localized oscillations. | Representing a signal as a linear combination of wavelets: $f(t) = \sum_{j,k} c_{j,k} \psi_{j,k}(t)$, where $\psi$ are wavelet functions. |
| **Spectral Analysis** | Examining functions in terms of their frequency components and energy distribution. | Analyzing the spectrum of a signal to find dominant frequencies and their amplitudes. |
| **Power Series** | A series of the form $f(x) = \sum_{n=0}^{\infty} a_n (x - c)^n$ that represents a function as an infinite polynomial. | The Taylor series for $e^x$ is$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$. |
| **Taylor Series** | A specific power series that approximates a function near a point $c$. | For $f(x) = \sin(x)$, the Taylor series around $0$ is $\sin(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n + 1)!}$. |
| **Laurent Series** | An extension of the Taylor series that includes negative powers, useful for functions with singularities. | For $f(z) = \frac{1}{z} + z$, the Laurent series around $0$ is $f(z) = \sum_{n=-1}^{\infty} a_n z^n$. |
| **Fourier Series** | Represents a periodic function as a sum of sines and cosines. | The Fourier series of a square wave function is represented as $f(x) = \sum_{n=1, \text{ odd}}^{\infty} \frac{4}{n\pi} \sin(nx)$. |
| **Vector** |  |  |

### Rpr[Vector(Function)]

> Representation of using vectors.
> 

## Operator

> 

## Functional

> 

## References

- https://en.wikipedia.org/wiki/Function_(mathematics)
- [Superposition Principle](https://en.wikipedia.org/wiki/Superposition_principle)
- [Linear Map](https://en.wikipedia.org/wiki/Linear_map)
- https://en.wikipedia.org/wiki/Function_of_several_real_variables
- [Linear form](https://en.wikipedia.org/wiki/Linear_form)
- [Functional](https://en.wikipedia.org/wiki/Functional_(mathematics))
- https://en.wikipedia.org/wiki/Transformation_(function)
- [Formal System](https://app.notion.com/p/Formal-System-41d02881d0544314b0e7ad3e6ada608a?pvs=21) [Relation, …]
- https://en.wikipedia.org/wiki/Zero_of_a_function
- https://en.wikipedia.org/wiki/Geometrical_properties_of_polynomial_roots
- https://en.wikipedia.org/wiki/Function_composition
- https://jakubtomsu.github.io/posts/fixed_timestep_without_interpolation/
- https://en.wikipedia.org/wiki/Continuous_function
- http://web1.eng.famu.fsu.edu/~dommelen/quantum/style_a/funcvec.html
- https://en.wikipedia.org/wiki/Infinite-dimensional_vector_function
- https://thenumb.at/Functions-are-Vectors/
