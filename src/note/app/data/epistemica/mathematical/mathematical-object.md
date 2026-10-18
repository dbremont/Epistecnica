---
tags: [building-block]
---

# Mathematical Object

 : Expression (Expression%201d1c0f5171ec8015bae8d3fc820709ca.md)

> **Mathematical Object**: A mathematical object is an abstract concept arising in mathematics. In the usual language of mathematics, an object is anything that has been (or could be) formally defined, and with which one may do deductive reasoning and mathematical proofs. Typically, a mathematical object can be a value that can be assigned to a variable, and therefore can be involved in formulas. Commonly encountered mathematical objects include numbers, sets, functions, expressions, geometric objects, transformations of other mathematical objects, and spaces. Mathematical objects can be very complex; for example, theorems, proofs, and even theories are considered as mathematical objects in proof theory. It’s coalesced types and data structures.
> 

## Type System

> 

> **A taxonomy & ontology of  Mathematical Expressions.**
> 

> **Scalar**: Atomic symbols often representing magnitude.
> 

> **Compound Expression**: …
> 

> Number: …
> 

> **Operator**: An **operator** is a mathematical object that acts on elements (often vectors or functions) from a particular space, and produces elements of potentially the same or another space. Operators are typically used to describe transformations, mappings, or actions in various fields such as functional analysis, linear algebra, and differential equations.
> 

> Functional:  A **functional** is a specific type of mapping that maps elements from a vector space (or a more general set) to a scalar (typically an element of the real or complex numbers). Functionals are often used in functional analysis to study properties of vector spaces, particularly infinite-dimensional spaces.
> 

> Function: …
> 

> A **set** is the most general and fundamental mathematical object. It is simply a collection of distinct elements, which can be anything: numbers, functions, vectors, or even other sets.
> 

> Space: A **space** is a set that is equipped with additional structure. Spaces can be classified into various types depending on the structure they inherit, such as topological spaces, vector spaces, metric spaces, etc.
> 

> **Relation:** A **relation** is a more general concept than a function, representing a set of ordered pairs (or tuples). Unlike functions, relations do not have to assign exactly one output to each input.  Examples “Inequality, Equation, …”
> 

> An **algebra** is a mathematical structure that generalizes the arithmetic operations of addition, subtraction, multiplication, and division.
> 

> **Equations** are fundamental mathematical objects that describe relationships between variables, typically expressed in terms of equality.
> 

| **Category** | **Subcategory** | **Examples** | **Description** |
| --- | --- | --- | --- |
| **Numbers** | **Natural Numbers (ℕ)** | 0, 1, 2, 3, ... | Counting numbers starting from 0 or 1. |
|  | **Integers (ℤ)** | ..., -2, -1, 0, 1, 2, ... | Whole numbers, including negatives. |
|  | **Rational Numbers (ℚ)** | 1/2, -3/4, 0.75 | Numbers expressible as fractions of integers. |
|  | **Real Numbers (ℝ)** | √2, π, 3.14 | Numbers representing continuous quantities, including irrationals. |
|  | **Complex Numbers (ℂ)** | 1 + 2i, -3i | Numbers of the form a + bi, where a, b ∈ ℝ and i = √(-1). |
| **Algebraic Structures** | **Groups** | (ℤ, +), (S₃, ∘) | Sets equipped with a single associative operation, an identity element, and inverses. |
|  | **Rings** | (ℤ, +, ×), (ℤₙ, +, ×) | Sets equipped with two operations (addition and multiplication) satisfying distributive laws. |
|  | **Fields** | (ℚ, +, ×), (ℝ, +, ×) | Commutative rings where every non-zero element has a multiplicative inverse. |
|  | **Vector Spaces** | ℝⁿ, ℂⁿ | Sets of vectors closed under addition and scalar multiplication. |
|  | **Algebras** | Matrix algebras, Lie algebras | Vector spaces equipped with a bilinear product. |
| **Geometric Objects** | **Points** | (x, y) ∈ ℝ² | Zero-dimensional objects representing locations. |
|  | **Lines** | y = mx + b | One-dimensional objects extending infinitely in both directions. |
|  | **Planes** | ax + by + cz = d | Two-dimensional flat surfaces extending infinitely. |
|  | **Curves** | Circles, ellipses, parabolas | One-dimensional objects that may be curved. |
|  | **Surfaces** | Spheres, tori, planes | Two-dimensional manifolds embedded in higher-dimensional spaces. |
|  | **Manifolds** | ℝⁿ, Sⁿ (n-sphere) | Spaces that locally resemble Euclidean space. |
| **Functions** | **Real-Valued Functions** | f : ℝ → ℝ, f(x) = x² | Functions mapping real numbers to real numbers. |
|  | **Complex-Valued Functions** | f : ℂ → ℂ, f(z) = z² | Functions mapping complex numbers to complex numbers. |
|  | **Multivariate Functions** | f : ℝⁿ → ℝ, f(x₁, ..., xₙ) = x₁² + ... + xₙ² | Functions of multiple variables. |
|  | **Function Spaces** | L²(ℝ), C([a, b]) | Spaces of functions with specific properties (e.g., integrability, continuity). |
|  | **Metric** |  |  |
|  | **Vector Function** |  |  |
|  | **Polynomial** |  |  |
| Relation |  |  |  |
|  | Inequality |  |  |
|  | Equation |  |  |
|  | System of Equation |  |  |
| Matroid |  |  |  |
| Quaternion |  |  |  |
| Sequence |  |  |  |
| Tensor |  |  |  |
| Serie |  |  |  |
| **Sets** | **Finite Sets** | {1, 2, 3}, {a, b, c} | Sets with a finite number of elements. |
|  | **Infinite Sets** | ℕ, ℝ | Sets with infinitely many elements. |
|  | **Power Sets** | P({1, 2}) = {∅, {1}, {2}, {1, 2}} | The set of all subsets of a given set. |
|  | **Product Sets** | {1, 2} × {a, b} = {(1, a), (1, b), (2, a), (2, b)} | Sets formed by the Cartesian product of two or more sets. |
| **Spaces** | **Metric Spaces** | (ℝⁿ, d), where d(x, y) = √∑(xᵢ - yᵢ)² | Sets equipped with a distance function. |
|  | **Topological Spaces** | (ℝ, standard topology) | Sets equipped with a collection of open sets satisfying certain axioms. |
|  | **Hilbert Spaces** | L²(ℝ), ℓ² | Complete vector spaces with an inner product. |
|  | **Banach Spaces** | Lᵖ(ℝ), C([a, b]) | Complete normed vector spaces. |
| **Matrices** | **Square Matrices** | 2×2 matrices, 3×3 matrices | Matrices with the same number of rows and columns. |
|  | **Diagonal Matrices** | diag(1, 2, 3) | Matrices with non-zero entries only on the diagonal. |
|  | **Symmetric Matrices** | A = Aᵀ | Matrices equal to their transpose. |
|  | **Orthogonal Matrices** | QᵀQ = I | Matrices whose columns and rows are orthonormal vectors. |
| **Graphs** | **Directed Graphs** | Graphs with directed edges. | Graphs where edges have a direction. |
|  | **Undirected Graphs** | Graphs with undirected edges. | Graphs where edges have no direction. |
|  | **Weighted Graphs** | Graphs with weights assigned to edges. | Graphs used in optimization problems (e.g., shortest path). |
|  | **Trees** | Connected graphs with no cycles. | Graphs used in computer science (e.g., binary trees). |
| **Categories** | **Objects** | Sets, groups, topological spaces | The entities in a category. |
|  | **Morphisms** | Functions, homomorphisms, continuous maps | The arrows between objects in a category. |
|  | **Functors** | Forgetful functors, hom functors | Maps between categories preserving structure. |
|  | **Natural Transformations** | Transformations between functors. | Morphisms between functors. |
| **Probability Objects** | **Random Variables** | X : Ω → ℝ | Functions assigning real numbers to outcomes of a random experiment. |
| **Operators** | **Linear Operators** | Matrix multiplication, differentiation | Operators satisfying \( T(ax + by) = aT(x) + bT(y) \). |
|  | **Probability Distributions** | Normal distribution, binomial distribution | Functions describing the probabilities of random variables. |
|  | **Stochastic Processes** | Brownian motion, Markov chains | Collections of random variables indexed by time or space. |
|  | **Nonlinear Operators** | Exponentiation, composition of nonlinear functions | Operators that do not satisfy linearity. |
|  | **Bounded Operators** | Finite-dimensional linear operators | Operators with \( |T(x)| \leq C|x| \) for some constant \( C \). |
|  | **Unbounded Operators** | Differentiation on \( L^2(\mathbb{R}) \) | Operators that are not bounded. |
|  | **Self-Adjoint Operators** | The Hamiltonian operator, real symmetric matrices | Operators satisfying \( T = T^* \). |
|  | **Compact Operators** | Integral operators with continuous kernels | Operators mapping bounded sets to relatively compact sets. |
|  | **Differential Operators** | Laplacian \( \Delta \), gradient \( \nabla \) | Operators involving derivatives. |
|  | **Integral Operators** | Fredholm and Volterra integral operators | Operators defined by integrals. |
|  | **Projection Operators** | Orthogonal projections in Hilbert spaces | Operators satisfying \( P^2 = P \). |
|  | **Unitary Operators** | Fourier transform, rotation matrices | Operators preserving the inner product: \( \langle Ux, Uy \rangle = \langle x, y \rangle \). |
|  | **Positive Operators** | Positive definite matrices | Operators satisfying \( \langle Tx, x \rangle \geq 0 \). |
|  | **Spectral Operators** | Laplacian, Schrödinger operator | Operators analyzed using spectral theory. |
| Functional |  |  |  |
|  | Linear Functional |  | A mapping from a vector space VVV to a scalar field (R\mathbb{R}R or C\mathbb{C}C) that satisfies linearity: F(αf+βg)=αF(f)+βF(g)F(\alpha f + \beta g) = \alpha F(f) + \beta F(g)F(αf+βg)=αF(f)+βF(g). |
|  | Inner Product Functional |  | A specific linear functional that is associated with an inner product, where F(f)=⟨f,g⟩F(f) = \langle f, g \rangleF(f)=⟨f,g⟩. |
|  | Dual Functional (Dual Space) |  | A linear functional from the dual space of a vector space VVV, denoted as V∗V^*V∗, to the scalar field. |
|  | Norm Functional |  | A functional that returns the norm of a vector: F(f)=∥f∥F(f) = \|f\|F(f)=∥f∥. |
|  | Continuous Functional |  | A functional that is continuous with respect to the topology of the space VVV, i.e., if fn→ff_n \to ffn→f, then F(fn)→F(f)F(f_n) \to F(f)F(fn)→F(f). |
|  | Action Functional |  | A functional in variational calculus, representing the action of a physical system (often the integral of a Lagrangian or Hamiltonian). |
|  | Energy Functional |  | A functional representing the energy of a system, often used in mechanics and physics. |
|  | Nonlinear Functional |  | A functional that does not satisfy the property of linearity; often used in nonlinear analysis. |
|  | Differential Functional |  | A functional involving derivatives of a function, often used in calculus of variations. |
|  | Functional of Probability Measure |  | A functional that operates on probability measures, often used in stochastic processes. |
|  | Reproducing Kernel Functional |  | A special type of functional associated with reproducing kernel Hilbert spaces (RKHS). |
|  | Integral Functional |  |  |

## Syntax

| **Production** | **Definition** | **Example** |
| --- | --- | --- |
| **Equation** | A statement asserting the equality of two expressions. | $3x + 2 = 11$ |
| **Inequality** | Statement expressing the relative size or order of two values. | $x + 5 > 10$ |
| **Identity** | Equation that is true for all values of the variables involved. | $(a + b)^2 = a^2 + 2ab + b^2$ |
| **Expression** | A combination of numbers, variables, and operators represents a value. | $4x^2 + 7x - 3$ |
| **Statement (Proposition)** | Sentence that is either true or false. | "All prime numbers greater than 2 are odd." |
| **Theorem** | This statement has been proven based on previously established statements. | Pythagorean Theorem: $a^2 + b^2 = c^2$ |
| **Axiom/Postulate** | Statement accepted without proof as a basis for argument. | Through any two points, there is exactly one straight line. |
| **Corollary** | A statement that follows readily from a previously proven statement. | A corollary to the Pythagorean Theorem: In a right triangle, the altitude to the hypotenuse divides the triangle into two similar triangles. |
| **Lemma** | The proven statement is used as a stepping-stone to prove other statements. | Euclid's Lemma states that if a prime divides the product of two numbers, it must divide at least one of those numbers. |
| **Proof** | Logical argument that establishes the truth of a theorem or statement. | Proof of the infinitude of prime numbers. |
| **Conjecture** | Based on observations, the statement is believed to be accurate but has yet to be proven. | The Goldbach Conjecture: Every even integer greater than 2 can be expressed as the sum of two primes. |

## References

- [Mathematical object](https://en.wikipedia.org/wiki/Mathematical_object)
- Hussey, Edward. "Aristotle on mathematical objects." *Apeiron* 24.4 (1991): 105-134.
- Milton, G. W., & Mattei, O. (2017). Field patterns: a new mathematical object.
