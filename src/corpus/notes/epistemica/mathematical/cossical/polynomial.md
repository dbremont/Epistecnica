---
tags: [note, mathematics, algebraic, function]
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

> Note: This is an attempt to classify polynomials — by how they are written, by the property that defines them, and by the named family they belong to. A row is one family or one property; the named families are not mutually exclusive.

| Category | **Type** | **Definition** |
| --- | --- | --- |
| By Number of Terms | **Monomial** | A polynomial with a single term: $f(x) = a_n x^n$, where $a_n$ is a constant and $n$ is a non-negative integer. |
|  | **Binomial** | A polynomial with two terms: $f(x) = ax^n + b$, where $a$ and $b$ are constants. |
|  | **Trinomial** | A polynomial with three terms. The form $x^n + ax + b$ is the target of the Bring–Jerrard reduction, and the trinomials $x^n \pm x \pm 1$ are the classical family for irreducibility tests. |
| By Degree | **Linear Polynomial** | Polynomial of degree 1: $f(x)=ax+b$. Simplest non-constant polynomial, representing a straight line. |
|  | **Quadratic** | A polynomial of degree 2: $f(x)=ax^2+bx+c$. |
|  | **Cubic** | A polynomial of degree 3: $f(x) = ax^3 + bx^2 + cx + d$. |
|  | **Quartic** | A polynomial of degree 4: $f(x) = ax^4 + bx^3 + cx^2 + dx + e$. |
| By Structure | **Symmetric Polynomial** | A polynomial invariant under every permutation of its variables; by the fundamental theorem it is a polynomial in the elementary symmetric functions. |
|  | Homogeneous Polynomial | A polynomial in several variables where all terms have the same total degree (e.g., $x^2y + xy^2$). |
|  | Multivariate Polynomial | A polynomial in more than one variable (e.g., $f(x,y) = x^2 + xy + y^2$). |
|  | **Quasi-Polynomial** | A sequence of the form $f(n) = c_k(n)n^k + \dots + c_0(n)$ with periodic coefficients $c_i(n)$. It is **not** a polynomial in $n$ — it is the form solutions of linear recurrences take, and the near-polynomial that appears in Ehrhart and lattice-point counting. |
| By Algebraic Property | **Monic Polynomial** | A polynomial whose leading coefficient is $1$. Monicity is what makes the division algorithm and the minimal polynomial well defined. |
|  | **Irreducible Polynomial** | A polynomial that admits no factorization into two non-constant factors of lower degree **over the stated field**. Irreducibility is a property of (polynomial, field): $x^2+1$ is irreducible over $\mathbb{R}$ and splits over $\mathbb{C}$. |
|  | **Primitive Polynomial** | Over $\mathbb{Z}$: a polynomial whose coefficients have greatest common divisor $1$ (Gauss's lemma makes primitivity the right invariant for factorization over $\mathbb{Q}$). The word is also used, in a different sense, for a polynomial whose root generates the multiplicative group of $\mathbb{F}_{p^n}$. |
|  | **Minimal Polynomial** | For an algebraic element $\alpha$ over a field $K$: the monic polynomial of least degree in $K[x]$ having $\alpha$ as a root. It is unique, irreducible, and its degree is the degree of the extension $K(\alpha)/K$. See [Root](/view.html?p=notes/epistemica/mathematical/mapping/root.md) and [Number](/view.html?p=notes/epistemica/mathematical/number/number.md). |
|  | **Square-Free (Separable) Polynomial** | A polynomial with no repeated root in an algebraic closure — equivalently $\gcd(f, f') = 1$. Over a perfect field this is the condition for separability. |
|  | **Reciprocal (Palindromic) Polynomial** | A polynomial whose coefficients read the same forwards and backwards: $a_k = a_{n-k}$, i.e. $x^n p(1/x) = p(x)$. The substitution $y = x + 1/x$ halves the degree, which is why reciprocal equations are solvable by radicals to higher degree than general ones. |
|  | **Cyclotomic Polynomial** | The monic polynomial $\Phi_n$ whose roots are exactly the primitive $n$-th roots of unity; it is irreducible over $\mathbb{Q}$ and satisfies $x^n - 1 = \prod_{d \mid n} \Phi_d(x)$. |
| Classical Orthogonal Polynomials | **Chebyshev Polynomial (First Kind)** | $T_n(\cos\theta) = \cos(n\theta)$, weight $1/\sqrt{1-x^2}$ on $[-1,1]$; the polynomial of least sup norm with leading coefficient fixed, which makes it the reference for minimax approximation. |
|  | **Chebyshev Polynomial (Second Kind)** | $U_n(\cos\theta) = \sin((n+1)\theta)/\sin\theta$, weight $\sqrt{1-x^2}$ on $[-1,1]$; the sibling of $T_n$, with $U_n = T_n'/(n+1)$. |
|  | **Legendre Polynomial** | Solutions to Legendre's differential equation, defined on the interval $[-1,1]$: $P_n(x)$, with weight $1$; the $n$-th Legendre polynomial is the $n$-th derivative of $(x^2-1)^n$ (Rodrigues). |
|  | **Hermite Polynomial** | Probabilists' form $He_n(x) = (-1)^n e^{x^2/2} \frac{d^n}{dx^n} e^{-x^2/2}$, physicists' form $H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}$. Orthogonal with weight $e^{-x^2/2}$ respectively $e^{-x^2}$; the eigenfunctions of the quantum harmonic oscillator. |
|  | **Laguerre Polynomial** | Solutions to Laguerre's differential equation, defined as $L_n(x) = \frac{e^x}{n!} \frac{d^n}{dx^n} (x^n e^{-x})$, orthogonal on $[0,\infty)$ with weight $e^{-x}$. |
|  | **Jacobi Polynomial** | Solutions to the Jacobi differential equation, denoted $P_n^{(\alpha,\beta)}(x)$, orthogonal on $[-1,1]$ with weight $(1-x)^\alpha (1+x)^\beta$. The family is the general one: Legendre, Chebyshev and Gegenbauer are its degenerate cases. |
|  | Gegenbauer Polynomial | Generalization of Legendre polynomials, orthogonal with weight $w(x)=(1-x^2)^{\lambda-1/2}$. |
|  | Ultraspherical Polynomials | Another name for Gegenbauer polynomials; arise in expansions on spheres. |
|  | Zernike Polynomials | Orthogonal on the unit disk, used in optics and wavefront analysis. Defined as $R_n^m(\rho) = \rho^m \sum_{s=0}^{(n-m)/2} (-1)^s \frac{(n-s)!}{s!((n+m)/2-s)!((n-m)/2-s)!} \rho^{2s}$. |
|  | **Zolotarev (Solotarev) Polynomial** | For fixed degree $n$, leading coefficient $1$ and a prescribed second coefficient, the polynomial on $[-1,1]$ of least sup norm under that constraint. Chebyshev $T_n$ is the case with second coefficient $0$; the off-centre cases are expressed through elliptic functions of the parameter, and they are the polynomials behind elliptic (Zolotarev–Cauer) filter design. |
|  | **Askey–Wilson Polynomial** | The four-parameter family $p_n(x; a,b,c,d \mid q)$ with $x = (z + z^{-1})/2$, orthogonal with respect to a $q$-weight on $[-1,1]$. It sits at the top of the Askey scheme: every classical and discrete orthogonal family above is a limit of it. |
| Discrete Orthogonal Polynomials | **Hahn Polynomial** | Orthogonal on the finite set $\{0,\dots,N\}$ with the weight $\binom{x+\alpha}{x}\binom{N-x+\beta}{N-x}$. It is the general family of the lattice: Krawtchouk, Meixner and Charlier are its limits. |
|  | **Krawtchouk Polynomial** | Orthogonal on $\{0,\dots,N\}$ with the binomial weight $\binom{N}{x} p^x (1-p)^{N-x}$. They are the eigenfunctions of the Fourier transform on the hypercube, and appear in coding theory and in the Krawtchouk (binary Fourier) transform. |
|  | **Meixner Polynomial** | Orthogonal on $\mathbb{N}$ with a negative-binomial weight; the lattice analogue of the Jacobi family. |
|  | **Charlier Polynomial** | Orthogonal on $\mathbb{N}$ with the Poisson weight $e^{-a}a^x/x!$; the lattice analogue of the Laguerre family. |
| Interpolation and Approximation | **Bernstein Polynomial** | $B_i^n(x) = \binom{n}{i} x^i (1-x)^{n-i}$ on $[0,1]$. The basis of Bézier curves; the family is a partition of unity, and Bernstein's proof of the Weierstrass approximation theorem expands any continuous function in it. |
|  | **Lagrange Basis Polynomial** | $\ell_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}$, equal to $1$ at the node $x_i$ and $0$ at every other node; the interpolant through $n+1$ points is $\sum y_i \ell_i(x)$. |
|  | **Newton Polynomial** | The divided-difference form $N(x) = \sum_{k} a_k \prod_{j<k} (x - x_j)$, the same interpolant as Lagrange's, written so that one more node costs one more term. |
| Combinatorial | **Fibonacci Polynomial** | $F_1 = 1$, $F_2 = x$, $F_n = x F_{n-1} + F_{n-2}$; evaluates at $x = 1$ to the Fibonacci numbers, and its roots are $2i\cos(k\pi/(n+1))$. |
|  | **Lucas Polynomial** | $L_0 = 2$, $L_1 = x$, $L_n = x L_{n-1} + L_{n-2}$; the companion sequence to the Fibonacci polynomials, evaluating to the Lucas numbers at $x = 1$. |
|  | **Pell Polynomial** | A recursive sequence of polynomials defined by $P_n(x) = 2xP_{n-1}(x) + P_{n-2}(x)$; at $x = 1$ it gives the Pell numbers. |
|  | **Abel Polynomial** | $A_n(x) = x(x - an)^{n-1}$. An Appell sequence whose binomial-type identity is Abel's binomial theorem; it counts rooted forests, and its coefficients are the tree numbers of Cayley. |
|  | **Bell (Touchard) Polynomial** | The partial Bell polynomials $B_{n,k}$ sum over the partitions of an $n$-set into $k$ blocks; the complete Bell polynomial $Y_n$ composes them, and the Touchard polynomial $T_n(x) = \sum_k S(n,k)x^k$ gives the moments of a Poisson variable. |
|  | **Eulerian Polynomial** | $A_n(x) = \sum_k \left\langle {n \atop k} \right\rangle x^k$, whose coefficients count the permutations of $n$ elements by number of descents; the generating function is $\sum_{m \geq 0} m^n x^m = A_n(x)/(1-x)^{n+1}$. |
|  | **Narayana Polynomial** | $N_n(x) = \frac{1}{n}\sum_{k} \binom{n}{k}\binom{n}{k-1} x^k$, counting Dyck paths by number of peaks; it is the $h$-polynomial of the associahedron. |
| Graph and Knot | **Chromatic Polynomial** | $P(G,k)$: the number of proper $k$-colourings of a graph $G$. It is a polynomial in $k$ for every finite graph, and its values at negative integers carry combinatorial meaning ($P(G,-1)$ counts acyclic orientations). |
|  | **Tutte Polynomial** | $T(G;x,y)$, defined by deletion–contraction; the chromatic polynomial, the flow polynomial, the reliability polynomial and the spanning-tree count are all specializations of it. |
|  | **Independence Polynomial** | $I(G;x) = \sum_k i_k x^k$, where $i_k$ is the number of independent sets of size $k$; evaluating at $2$ counts all independent sets, and the family is the matching polynomial's close relative. |
|  | Knot Polynomial | Polynomial invariants (e.g., Jones, Alexander, HOMFLY) used in knot theory to distinguish knots and links. They are Laurent polynomials in a variable, not functions of a numerical unknown: the variable records the skein relation, and equality of two polynomials is a theorem about the knots. |
| Named Special Families | **Bernoulli Polynomial** | Defined by $\frac{t e^{xt}}{e^t - 1} = \sum_n B_n(x)\frac{t^n}{n!}$; the Bernoulli numbers are $B_n = B_n(0)$, and the polynomials give the closed form of $\sum_{k=1}^{m} k^p$ (Faulhaber). |
|  | Euler Polynomial | Defined by $\frac{2 e^{xt}}{e^t + 1} = \sum_n E_n(x)\frac{t^n}{n!}$, giving the alternating power sums; the Euler numbers are $E_n = 2^n E_n(1/2)$. |
|  | **Reverse Bessel Polynomial** | $\theta_n(x) = \sum_{k=0}^{n} \frac{(n+k)!}{(n-k)!\,k!}\left(\frac{x}{2}\right)^{k}$. Not a solution of Bessel's equation — it is the polynomial whose roots define the maximally flat delay of a Bessel filter, and the Bessel *functions* are a different object. |
|  | Appell Polynomial | A sequence of polynomials satisfying $\frac{d}{dx} P_n(x) = n P_{n-1}(x)$ for all $n$; Bernoulli, Euler, Hermite and Abel polynomials are Appell sequences. |
|  | **Orthogonal Polynomial on the Unit Circle (OPUC)** | A set of orthogonal polynomials on the unit circle in the complex plane, important in signal processing and moment problems; generated by the Szegő recurrence and encoded by the Verblunsky coefficients, the circle analogue of the Jacobi parameters. |
| Coefficient Domain | **Boolean Polynomial** | A polynomial over $\mathbb{F}_2$ in variables satisfying $x_i^2 = x_i$. Every Boolean function has exactly one such multilinear representative — its algebraic normal form — and this is the polynomial system solved in algebraic cryptanalysis. |
|  | **Tropical Polynomial** | A polynomial read in the max-plus semiring: $+$ becomes $\max$ and $\times$ becomes $+$. The result is a piecewise-linear convex function, and its roots — the breakpoints — are the object of tropical geometry. |
|  | **Puiseux Polynomial** | A polynomial in fractional powers, $\sum_k a_k x^{k/n}$. The field of Puiseux series is the algebraic closure of the Laurent series, so every branch of an algebraic curve has a Puiseux expansion at a singular point. |
| Series Representation | **Taylor Polynomial** | The truncation $T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k$ of the Taylor series. The series is not a polynomial; the truncations are, and they are the polynomials that approximate $f$ near $a$. |
|  | Laurent Polynomial | A polynomial that may include terms with negative exponents: $f(z) = \sum_{k=-m}^{n} a_k z^k$. A Laurent polynomial is a polynomial in $z$ and $z^{-1}$; it is a polynomial only when the negative part vanishes. |

## Property

| **Property** | **Description** |
| --- | --- |
| **Orthogonality** | A set of polynomials is orthogonal over an interval with respect to a weight function if the inner product of any two distinct polynomials in the set is zero. Common in approximation theory and spectral methods. The families themselves, the recurrence that generates them and the reason the basis is worth having are in [Orthogonal Polynomials](/view.html?p=notes/epistemica/mathematical/cossical/orthogonal-polynomials.md). |
| **Degree** | The highest power of the variable in the polynomial. Determines the polynomial’s growth, shape, and the maximum number of roots it can have. |
| **Zeros** | The values of the variable for which the polynomial evaluates to zero. Also called roots; a polynomial of degree $n$ has at most $n$ zeros. The general concept — the factor theorem, multiplicity, the zero root and the named special cases — is [Root](/view.html?p=notes/epistemica/mathematical/mapping/root.md). |
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

> **Survey entry.** What follows is the shape of the transformation. The technique itself — the substitution, the coefficient conditions, the auxiliary system they require, and why the method stops at the quintic — has [its own note](/view.html?p=notes/epistemica/mathematical/cossical/tschirnhaus-transformation.md).

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
- https://en.wikipedia.org/wiki/System_of_polynomial_equations
- https://en.wikipedia.org/wiki/Rodrigues%27_formula
