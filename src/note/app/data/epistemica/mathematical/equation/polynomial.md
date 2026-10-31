---
tags: [algebraic, function]
---

# Polynomial

 : Polynomial System (Polynomial%20System%2018bc0f5171ec800d991ce7d700be4698.md), Function (Function%20049537a4fd564eaaac4bae443839b0c0.md), Level Set (Level%20Set%20abc64f35e19d40b4b78a62ab147a58e4.md), Diophantine Equation (Diophantine%20Equation%201bbc0f5171ec80bdb421dd2d9bf3f204.md), Operator (Operator%2096b9329acc2b493388cda715c8e66caa.md), Fundamental Theory of Algebra (Fundamental%20Theory%20of%20Algebra%201dec0f5171ec80bfaa59ce50e1098e7f.md), Complex Numbers (ℂ) (Complex%20Numbers%20(%E2%84%82)%20176c0f5171ec809eb4aff09a9448e3f1.md)

> A **polynomial** is an algebraic expression consisting of one or more terms, each with non-negative integer exponents, and coefficients that are real or complex numbers.
> 

## Definition

A **polynomial** is a mathematical expression of the form:

$P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$

where:

- $P(x)$ is the polynomial function,
- $x$ is the indeterminate (a variable),
- $a_n, a_{n-1}, \dots, a_1, a_0$ are **coefficients** from a ring, typically the field of real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$,
- $n$ is a non-negative integer, representing the degree of the polynomial, and
- the coefficients $a_n, a_{n-1}, \dots, a_1, a_0$ are typically chosen from a commutative ring (commonly $\mathbb{R}$ or $\mathbb{C}$).

## Taxonomy

> Note: This is an attempt to classify polynomials.
> 

| Category | **Type** | **Definition** |
| --- | --- | --- |
| By Number of Terms | **Monomial** | A polynomial with a single term: $f(x) = a_n x^n$, where $a_n$ is a constant and $n$ is a non-negative integer. |
|  | **Binomial** | A polynomial with two terms: $f(x) = ax^n + b$, where $a$ and $b$ are constants. |
| By Degree | **Linear Polynomial** | polynomial of degree 1: $f(x)=ax+b$. Simplest non-constant polynomial, representing a straight line. |
|  | **Quadratic** | A polynomial of degree 2: $f(x)=ax^2+bx+c$. |
|  | **Cubic** | A polynomial of degree 3: $f(x) = ax^3 + bx^2 + cx + d$. |
|  | **Quartic** | A polynomial of degree 4: $f(x) = ax^4 + bx^3 + cx^2 + dx + e$. |
| By Structural Property | **Symmetric Polynomial** | A polynomial where the variables appear symmetrically. |
|  | Homogeneous Polynomial | A polynomial in several variables where all terms have the same total degree (e.g., $x^2y + xy^2$). |
|  | Multivariate Polynomial | A polynomial in more than one variable (e.g., $f(x,y) = x^2 + xy + y^2$). |
|  | **Quasi-Polynomial** | A function of the form $f(n) = c_k(n)n^k + \dots + c_0(n)$, where coefficients $c_i(n)$ are periodic. Appears in combinatorics and number theory. |
| Classical Orthogonal Polynomials | **Chebyshev Polynomial** | A specific set of **orthogonal polynomials** defined by the recurrence relation $T_n(x) = 2xT_{n-1}(x) - T_{n-2}(x)$. |
|  | **Legendre Polynomial** | Solutions to Legendre's differential equation, defined on the interval $[-1,1]$: $P_n(x)$. |
|  | **Hermite Polynomial** | Defined by $H_n(x) = (-1)^n e^{x^2/2} \frac{d^n}{dx^n} e^{-x^2/2}$ and satisfy a recurrence relation. |
|  | **Laguerre Polynomial** | Solutions to Laguerre's differential equation, defined as $L_n(x) = \frac{e^x}{n!} \frac{d^n}{dx^n} (x^n e^{-x})$. |
|  | **Jacobi Polynomial** | Solutions to the Jacobi differential equation, denoted as $P_n^{(\alpha,\beta)}(x)$. |
|  | Gegenbauer Polynomial | Generalization of Legendre polynomials, orthogonal with weight $w(x)=(1-x^2)^{\lambda-1/2}$. |
|  | Ultraspherical Polynomials | Another name for Gegenbauer polynomials; arise in expansions on spheres. |
|  | Zernike Polynomials | Orthogonal on the unit disk, used in optics and wavefront analysis. Defined as $R_n^m(\rho) = \rho^m \sum_{s=0}^{(n-m)/2} (-1)^s \frac{(n-s)!}{s!((n+m)/2-s)!((n-m)/2-s)!} \rho^{2s}$. |
| Special Polynomial Families | **Bernoulli Polynomial** | Defined using the Bernoulli numbers $B_n(x)$, used to express certain sums and series. |
|  | **Bessel Polynomial** | Solutions to Bessel's equation, defined as $y_n(x)$. |
|  | **Pell Polynomial** | A recursive sequence of polynomials defined by the recurrence relation $P_n(x) = 2xP_{n-1}(x) + P_{n-2}(x)$. |
|  | Euler Polynomial | Defined using the Euler numbers $E_n(x)$, related to Bernoulli polynomials and used in number theory. |
|  | Appell Polynomial | A sequence of polynomials satisfying $\frac{d}{dx} P_n(x) = n P_{n-1}(x)$ for all n. |
|  | **Orthogonal Polynomial on the Unit Circle (OPUC)** | A set of orthogonal polynomials on the unit circle in the complex plane, important in signal processing and moment problems. |
| Series Representation | **Taylor Series (Polynomial)** | An infinite polynomial expansion of a function about a point $a$: $f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$. |
|  | Laurent Polynomial | A polynomial that may include terms with negative exponents, of the form $f(z) = \sum_{n=-m}^{\infty} a_n z^n$. |
|  | **Cyclotomic Polynomial** | A polynomial whose roots are the primitive n-th roots of unity. |
| Knot Polynomial |  | Polynomial invariants (e.g., Jones, Alexander, HOMFLY) used in knot theory to distinguish knots and links. These are associated with knots and can help determine if two knots are equivalent. |

## Property

| **Property** | **Description** |
| --- | --- |
| **Orthogonality** | A set of polynomials is orthogonal over an interval with respect to a weight function if the inner product of any two distinct polynomials in the set is zero. Common in approximation theory and spectral methods. |
| **Degree** | The highest power of the variable in the polynomial. Determines the polynomial’s growth, shape, and the maximum number of roots it can have. |
| **Zeros** | The values of the variable for which the polynomial evaluates to zero. Also called roots; a polynomial of degree $n$ has at most $n$ zeros. |
| **Symmetry** | Refers to whether the polynomial is even ($p(-x) = p(x)$), odd ($p(-x) = -p(x)$), or has other symmetric properties. Important in simplifying computations and understanding function behavior. |
| **Coefficient Pattern** | Some polynomials have coefficients with special structures (e.g., binomial coefficients in $(x+1)^n$, Fibonacci polynomials, or Chebyshev coefficients). These patterns are often exploited in combinatorics and numerical methods. |
| **Leading Coefficient** | The coefficient of the highest-degree term. Influences end behavior of the polynomial as $x \to \pm\infty$. |

## **Vieta's Relation**

> **Vieta's Formulas** (also known as Vieta's relations) are a set of equations that relate the coefficients of a polynomial to sums and products of its roots. Let $p(x)$ be a polynomial of degree $n$ over a field $\mathbb{K}$, given by:   $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$
> 

> Assuming that $\alpha_1, \alpha_2, \dots, \alpha_n$ are the roots of the polynomial $p(x) = 0$ (with appropriate multiplicities, if necessary), Vieta's Formulas express the coefficients $a_k$ in terms of the elementary symmetric polynomials of the roots $\alpha_i$ (for $i = 1, 2, \dots, n$).
> 

The general form of Vieta's formulas for a polynomial of degree nn is:

1. **Sum of roots**: The sum of the roots, taken one at a time, is related to the coefficient of $x^{n-1}$: $\sum_{i=1}^n \alpha_i = -\frac{a_{n-1}}{a_n}$
2. **Sum of products of roots taken two at a time**: The sum of the products of the roots, taken two at a time, is related to the coefficient of $x^{n-2}$: $\sum_{1 \leq i < j \leq n} \alpha_i \alpha_j = \frac{a_{n-2}}{a_n}$
3. **Sum of products of roots taken three at a time**: The sum of the products of the roots, taken three at a time, is related to the coefficient of $x^{n-3}$: $\sum_{1 \leq i < j < k \leq n} \alpha_i \alpha_j \alpha_k = -\frac{a_{n-3}}{a_n}$
4. **Continuing this pattern**: For the sum of products of the roots taken $k$ at a time, the relation is given by: $\sum_{1 \leq i_1 < i_2 < \dots < i_k \leq n} \prod_{j=1}^k \alpha_{i_j} = (-1)^k \frac{a_{n-k}}{a_n}$
5. **Product of all roots**: The product of all the roots, taken with the appropriate sign, is related to the constant term: $\prod_{i=1}^n \alpha_i = (-1)^n \frac{a_0}{a_n}$

## Polynomial Transformation

> **Polynomial transformations** refer to a mapping of a polynomial to another.
> 

> **Note**: The resulting polynomial may or may not be the same as the original polynomial in terms of its form, but it typically represents a transformed version with equivalent or adjusted properties.
> 

### Tschirnhaus Transformation

> The Tschirnhaus transformation is a change of variables that aims to eliminate certain terms from a polynomial equation, typically the higher-degree terms, to make the equation simpler to solve or analyze. It is commonly used to simplify the form of a given polynomial, especially quartic or higher-degree polynomials, by removing certain terms like the cubic term in a general polynomial.
> 

**General Form:**

Consider a polynomial of degree $n$ in the variable $x$:  $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$.

The Tschirnhaus transformation replaces the variable $x$ with a new variable $y$ via a substitution of the form: $x = y + \alpha$; Where $\alpha$ is a constant that is chosen in such a way as to eliminate specific terms (often the cubic term) in the expanded polynomial expression. The goal is to choose $\alpha$ such that the transformed polynomial has a simpler structure.

**Example:**

For example, for a quartic equation: $x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0 = 0$

The Tschirnhaus transformation would attempt to eliminate the cubic term by making the substitution $x = y + \alpha$. Expanding the equation in terms of $y$ and choosing α\alpha such that the coefficient of $y^3$ is zero leads to a simplified equation in terms of $y$.

### **Completing the Square**

> It’s a polynomial transformation on 2-degree polynomials.
> 

> **Completing the square** is a mathematical technique used to rewrite a quadratic expression in a way that makes it easier to solve or analyze.
> 

> Completing the square is a technique for converting a quadratic polynomial of the form $ax^2 + bx + c$ to the form $a(x - h)^2 + k$ for some values of $h$ and $k$.
> 

## Homogeneous Polynomial

> A **homogeneous polynomial** (also called a **form**) is a polynomial in several variables where **all terms have the same total degree**.
> 
- **Total degree**: sum of the exponents of all variables in a term.
- **Homogeneous** means each term has the same total degree.
- **Case:**
    - Homogeneous: $f(x,y)=3x^2y+5xy$
    - Non-Homogeneous: $g(x,y)=x^2+xy+y$

## **Characteristic Polynomial**

> The characteristic polynomial of a square matrix $A \in \mathbb{C}^{n \times n}$ (or $\mathbb{R}^{n \times n}$) is a polynomial that encodes information about the eigenvalues of $A$. It is defined as: $p_A(\lambda) = \det(A - \lambda I)$
where:
> 
- $\lambda$ is a scalar (the variable of the polynomial),
- $I$ is the $n \times n$ identity matrix,
- $\det$ denotes the determinant.

**Properties**

1. **Degree**: The characteristic polynomial is of degree $n$ for a $n \times n$ matrix.
2. **Eigenvalues**: The roots of $p_A(\lambda)$ are exactly the eigenvalues of $A$.
3. **Coefficients**: The sum of the eigenvalues equals the trace of $A$, and the product of the eigenvalues equals $\det(A)$.

## References

- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- https://en.wikipedia.org/wiki/Delta_operator
- https://en.wikipedia.org/wiki/Polynomial_ring
- https://en.wikipedia.org/wiki/Zero_of_a_function
- https://en.wikipedia.org/wiki/Theory_of_equations
- https://en.wikipedia.org/wiki/Irreducible_polynomial
- https://en.wikipedia.org/wiki/Vieta's_formulas
- https://en.wikipedia.org/wiki/Completing_the_square
- https://en.wikipedia.org/wiki/Degree_of_a_polynomial
- https://en.wikipedia.org/wiki/Polynomial_transformation
- https://en.wikipedia.org/wiki/Characteristic_polynomial
- https://en.wikipedia.org/wiki/Intermediate_value_theorem
- https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra
- https://mathworld.wolfram.com/topics/Polynomials.html
- https://en.wikipedia.org/wiki/Homogeneous_polynomial
- https://en.wikipedia.org/wiki/Quadratic_form
