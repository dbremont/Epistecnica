---
tags: [operator]
---

# Operator

 : Function (Function%20049537a4fd564eaaac4bae443839b0c0.md), Integral Transform (Integral%20Transform%205c5fd9afa97942dca93d67c594f6ebe2.md), Integral Operator (Integral%20Operator%20100c0f5171ec804e8f36d1066c3679d2.md), Functional (Functional%201d6c0f5171ec80b19358d228c3cf04a6.md), Convolution Operator (Convolution%20Operator%201d6c0f5171ec8057b135f9b4b10cbe31.md), Polynomial (Polynomial%20c29542c4a2ce4a0e887db0a00b61e977.md), Representation (Representation%20262c0f5171ec8021a535fc9111fd1ed5.md)

> The term is **context-dependent**: in linear algebra, an operator might be a matrix; in calculus, it might be a differential operator.
> 

> Mathematics **does have terms** for “operations on functions”—they’re just **distributed across several precise concepts**, not unified under a single everyday label like “higher-order function.”
> 

> **Function**: Map an object (domain) to another object in a range.
> 

> **Functional**: Map a function to a  real number.
> 

> **Operator**:  Maps a functional space to another.
> 

> The **domain** of an operator can be numbers, vectors, functions, or even **functionals** (functions of functions).
> 

> Operators are central in many fields: differential equations (differential operators), quantum mechanics (Hermitian operators), signal processing (convolution operators), etc.
> 

## Definition

An **operator** is a special kind of function that acts on elements of **structured spaces**, often vector spaces or function spaces: $T: V \to W$

- When $V$ and $W$ are **function spaces**, the operator maps **functions to functions**.
- Operators can also act on general vectors (not necessarily functions), especially in finite-dimensional contexts.

## List of Operators

| **Category** | **Operator** | **Description** |
| --- | --- | --- |
| **Algebraic & Linear** | **Identity Operator** | Maps a function to itself. |
|  | **Multiplication Operator** | Multiplies input by a fixed function: $g(x)f(x)$. |
|  | **Addition Operator** | Pointwise sum: $(f + g)(x)$. |
|  | **Scaling Operator** | Scales function by a scalar. |
|  | **Composition** | $y =   f (g(x))$ |
| **Polynomial Transformation** | … | … |
| **Differential & Pseudo-diff.** | **Differential Operator** | Applies derivatives: $\frac{d^n f}{dx^n}$. |
|  | **Gradient / Divergence / Curl** | Vector calculus operators. |
|  | **Laplace Operator** | $\Delta f = \nabla \cdot \nabla f$, measures diffusion. |
|  | **Pseudo-differential Operator** | Defined via Fourier symbols, generalizes differentiation. |
| **Integral & Transform** | **Integral Operator** | Integration against a kernel:  $\int K(x,t)f(t)dt$. |
|  | **Convolution Operator** | Weighted shift-integral:  $(f * g)(x)$. |
|  | **Fourier Transform** | Converts to frequency domain. |
|  | **Laplace Transform** | Converts to complex frequency domain. |
|  | **Hilbert Transform** | Principal value integral, phase shift. |
| **Geometric & Symmetry** | **Translation Operator** | Shifts input: $f(x - h)$. |
|  | **Dilation (Scaling) Operator** | Rescales input:  $f(ax)$. |
|  | **Rotation Operator** | Rotates input space. |
|  | **Reflection Operator** | Reflects input: $f(-x)$. |
| **Spectral & Functional Analysis** | **Projection Operator** | Projects function onto a subspace. |
|  | **Compact Operator** | Maps bounded sets to relatively compact ones. |
|  | **Bounded/Unbounded Operator** | Maps bounded inputs to bounded/unbounded outputs. |
|  | **Self-Adjoint Operator** | Operator equal to its adjoint. |
|  | **Eigen-Operator** | Acts by scaling eigenfunctions: $(f) = \lambda f$. |
| **Nonlinear & Functional** | **Composition Operator** | Composes functions: $f(\phi(x))$. |
|  | **Max/Min Operator** | Returns max/min over domain or between functions. |
|  | **Norm Operator** | Assigns norm value (e.g., $\|f\|_{L^p}$ ). |
|  | **Activation Functions** | Nonlinear scalar functions: ReLU, sigmoid, etc. |
| **Applied Mathematics** | **Green’s Operator** | Inverts a differential operator using Green's function. |
|  | **Dirichlet-to-Neumann Map** | Maps boundary values to flux (PDEs). |
|  | **Sampling Operator** | Evaluates function at discrete points. |
|  | **Integral Transforms** | Mellin, Radon, Hankel, etc. |
| **Others** |  |  |
|  | **Kernel Operator** | Applies a kernel function to map a function to another function in functional analysis. |
|  | **Sobolev Embedding Operator** | An operator that embeds functions from one Sobolev space into another (function space with derivatives). |
|  | **Neural Operator** | … |

## References

- [Operator](https://en.wikipedia.org/wiki/Operator_(mathematics))
- [Operator theory](https://en.wikipedia.org/wiki/Operator_theory)
- [Neural Operators](https://en.wikipedia.org/wiki/Neural_operators)
- [Bounded Operator](https://en.wikipedia.org/wiki/Bounded_operator)
- [Hahn–Banach theorem](https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem)
- https://en.wikipedia.org/wiki/Operator_theory
- http://www.mathphysics.com/opthy/OpHistory.html
- https://en.wikipedia.org/wiki/Operator_(physics)
- https://en.wikipedia.org/wiki/Operator_(mathematics)
- https://en.wikipedia.org/wiki/Laplace%E2%80%93Beltrami_operator
- https://mathworld.wolfram.com/topics/OperatorTheory.html
