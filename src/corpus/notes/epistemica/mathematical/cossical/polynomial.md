---
tags: [note, mathematics, algebraic, function]
qa:
 - Which are the thoeiretical reulsts about polynomiasl?
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

## Descartes's Rule of Signs

> Take a polynomial - analye \[
P(x)=x^4-3x^3-2x^2+5x-1
\]

aanmd alyze the singn changes Its coefficient signs are:
\[
\boxed{+\quad -\quad -\quad +\quad -}
\]
There are three sign changes:
\[
+\rightarrow-,\qquad -\rightarrow+,\qquad +\rightarrow-
\]
Therefore, the polynomial has either:
\[
\boxed{3\text{ or }1\text{ positive real roots}}
\]
The number of positive real roots, counting multiplicities, differs from the number of sign changes by an even integer.

Thsi chnges boudn teh number of roots.

## To Be Work 

# The Role of Polynomials in Mathematical Modelling

Polynomials are mathematical representations used to describe, approximate, analyze, and predict the behavior of systems.

However, different polynomial families possess different mathematical properties. Those properties make some families particularly suitable for representing certain classes of systems, geometries, physical phenomena, and functional relationships.

The important question is therefore:

> **What mathematical properties make a particular polynomial family useful for representing a particular class of systems?**

To answer this, we need to distinguish three things:

1. **Representational properties:** What mathematical structures can the polynomials represent?
2. **Analytical properties:** What operations and mathematical analyses do they facilitate?
3. **Computational properties:** What makes them numerically efficient or stable?

## 1. Comparative table of polynomial families

| Polynomial family | Defining mathematical property | What makes it useful? | Typical modelling applications |
|---|---|---|---|
| **Chebyshev** | Orthogonality with weight \(1/\sqrt{1-x^2}\); strong minimax approximation properties | Minimizes approximation errors and provides efficient polynomial representations | Function approximation, numerical simulation, spectral methods |
| **Legendre** | Orthogonality under uniform weight on \([-1,1]\) | Provides an orthogonal basis without privileging particular interior regions of the interval | Spherical problems, potential theory, angular distributions, fluid dynamics |
| **Hermite** | Orthogonality under Gaussian weight \(e^{-x^2}\) | Naturally accommodates Gaussian-weighted functions and probability-related problems | Quantum mechanics, Gaussian processes, probability theory |
| **Laguerre** | Orthogonality under exponential weight \(e^{-x}\) on \([0,\infty)\) | Particularly suitable for representing functions over nonnegative, unbounded domains | Quantum mechanics, radial differential equations |
| **Jacobi** | Orthogonality under a general algebraic weight \((1-x)^\alpha(1+x)^\beta\) | Allows control over endpoint weighting and generalizes several classical families | Differential equations, numerical approximation, mathematical physics |
| **Gegenbauer** | Orthogonality under weight \((1-x^2)^{\lambda-1/2}\) | Captures structures associated with higher-dimensional spherical geometries | Harmonic analysis, spherical problems, mathematical physics |
| **Bernstein** | Positive basis functions that sum to one over \([0,1]\) | Provides positivity, convex-hull containment, and intuitive geometric control | Bézier curves, geometric modelling, shape representation |
| **Fourier-related Chebyshev representations** | Connection between polynomial evaluation and cosine expansions | Allows efficient transformation between polynomial and trigonometric representations | Signal approximation, spectral analysis, periodic and nonperiodic numerical problems |

## 2. Which mathematical properties matter for modelling?

The usefulness of a polynomial family is not determined simply by its degree. Several structural properties matter.

| Mathematical property | What does it mean? | Why does it matter in modelling? |
|---|---|---|
| **Orthogonality** | Different basis functions have zero inner product under a specified weight | Reduces interference between coefficients and facilitates decomposition |
| **Completeness** | The polynomial family can approximate a sufficiently broad class of functions | Determines whether a function can be represented to arbitrary accuracy |
| **Approximation error** | The difference between the original function and its polynomial representation | Determines representational accuracy |
| **Numerical stability** | Resistance to computational errors during evaluation | Important for large-scale numerical simulations |
| **Recurrence relations** | Higher-degree polynomials can be generated from lower-degree ones | Makes computation more efficient |
| **Domain compatibility** | The polynomial family is naturally defined or orthogonal over a particular domain | Makes it suitable for representing systems with specific domains |
| **Weight function** | Determines how different regions contribute to orthogonality | Allows the representation to reflect particular mathematical structures |
| **Boundary behavior** | Describes how the polynomials behave at domain boundaries | Important for systems with boundary conditions |
| **Symmetry** | Even, odd, or other structural symmetries | Simplifies representations of symmetric systems |
| **Differential properties** | Relationships between derivatives and other polynomials in the family | Useful for solving differential equations |
| **Convergence properties** | Describes how representations approach the target function as degree increases | Determines whether increasing model complexity improves accuracy |

## 3. Matching polynomial families to system characteristics

This is perhaps the most important perspective for modelling.

Rather than selecting a polynomial family arbitrarily, we can select it according to the mathematical characteristics of the system.

| System characteristic | Relevant mathematical property | Suitable polynomial family |
|---|---|---|
| Function defined over a finite interval | Minimax approximation | Chebyshev |
| Function defined over a finite interval with uniform weighting | Orthogonality under uniform weight | Legendre |
| Gaussian-weighted system | Gaussian orthogonality | Hermite |
| System defined over a nonnegative, unbounded domain | Exponential weighting | Laguerre |
| System with asymmetric endpoint behavior | Adjustable endpoint weighting | Jacobi |
| Spherical geometry | Compatibility with spherical harmonics | Legendre / Gegenbauer |
| Geometric curves and surfaces | Positive basis and convex-hull properties | Bernstein |
| Symmetric function | Even/odd polynomial structure | Chebyshev / Legendre |
| Differential equations with known boundary conditions | Differential operator compatibility | Depends on the equation; often Chebyshev, Legendre, or Jacobi |

## 4. A deeper distinction: representation versus approximation

It is important not to confuse two different roles.

**A. Representing a mathematical system**

A polynomial may arise naturally as part of the system's mathematical structure.

For example, Legendre polynomials appear in the separation of variables for Laplace's equation in spherical coordinates.

**B. Approximating a mathematical system**

A polynomial may instead be selected because it approximates a function efficiently, even when the original function is not polynomial.

For example, Chebyshev polynomials can approximate:

\[
f(x)=e^x
\]

over a finite interval:

\[
e^x \approx \sum_{k=0}^{n}a_kT_k(x)
\]

Here, the Chebyshev polynomials are not necessarily describing the underlying physical mechanism. They are providing a convenient mathematical representation of its behavior.

These are fundamentally different modelling situations.

## 5. General classification of their modelling roles

We can organize the uses of polynomial families into five broad categories:

| Role | Objective | Relevant properties |
|---|---|---|
| Functional approximation | Approximate arbitrary functions | Completeness, approximation error, convergence |
| Geometric representation | Represent curves and surfaces | Positivity, convex-hull property, basis structure |
| Differential equation representation | Solve mathematical descriptions of physical systems | Differential properties, orthogonality, boundary compatibility |
| Statistical representation | Represent probability-related functions and distributions | Weight functions, orthogonality, completeness |
| Numerical representation | Improve computational efficiency and stability | Recurrence relations, conditioning, convergence |

---

## 6. The central principle

A polynomial family is useful not simply because it can represent a function, but because its mathematical structure makes certain representations, operations, or computations particularly convenient.

For a modelling problem, the selection process should therefore consider:

\[
\boxed{
\text{System}
\rightarrow
\text{Mathematical properties}
\rightarrow
\text{Polynomial family}
\rightarrow
\text{Representation}
}
\]

One final distinction is worth emphasizing: **orthogonality is not inherently a property of a polynomial family alone; it is defined relative to an inner product, which includes a domain and a weight function.**

This is one of the most important reasons why different orthogonal polynomial families are useful for different mathematical problems.

### Which are the main questino gtaht guides theoiretical results about polynomails?

| Mathematical question | Principal results |
|---|---|
| How do we manipulate polynomials? | Division Algorithm, Remainder Theorem, Factor Theorem |
| How are roots related to coefficients? | Vieta's Formulas, Newton's Identities, Symmetric Polynomial Theorem |
| How many roots exist? | Fundamental Theorem of Algebra, Descartes's Rule of Signs, Sturm's Theorem |
| How do we find or characterize roots? | Rational Root Theorem, Multiplicity of Roots, Polynomial Interpolation |
| How do we factor polynomials? | Gauss's Lemma, Irreducibility Criteria, Euclidean Algorithm |
| How do we determine common roots? | Bézout's Identity, Resultant Theorem |
| How do we characterize repeated roots? | Discriminant |
| When can polynomial equations be solved algebraically? | Galois Theory |
| What is the general algebraic structure of polynomial rings? | Hilbert's Basis Theorem |

### What are the main theoretical results concerning polynomials?

> Some results concern the algebraic structure of polynomials themselves (division, factorization, irreducibility), others concern their roots (existence, number, multiplicity), and others establish connections with broader mathematical structures (fields, groups, rings, and geometry).

| Result | Description | Origin |
|---|---|---|
| **Polynomial Division Algorithm** | Given polynomials \(P(x)\) and \(D(x)\neq 0\), there exist unique polynomials \(Q(x)\) and \(R(x)\) such that \(P(x)=D(x)Q(x)+R(x)\), where \(\deg R<\deg D\). | Classical algebra; formalized in modern algebra by the 19th century. |
| **Remainder Theorem** | The remainder obtained by dividing \(P(x)\) by \(x-a\) is \(P(a)\). | Classical algebra; formalized in the 18th–19th centuries. |
| **Factor Theorem** | \(x-a\) is a factor of \(P(x)\) if and only if \(P(a)=0\). | Follows from polynomial division; classical algebra. |
| **Fundamental Theorem of Algebra** | Every nonconstant polynomial with complex coefficients has at least one complex root. Consequently, a polynomial of degree \(n\) has exactly \(n\) complex roots, counting multiplicities. | Carl Friedrich Gauss, 1799. |
| **Vieta's Formulas** | Establish relationships between polynomial coefficients and the elementary symmetric sums of its roots. | François Viète, 1591. |
| **Descartes's Rule of Signs** | The number of positive real roots of a polynomial, counted with multiplicity, is at most the number of sign changes in its coefficient sequence, differing from it by an even integer. | René Descartes, 1637. |
| **Rational Root Theorem** | For a polynomial with integer coefficients, any rational root \(p/q\), in lowest terms, must have \(p\) dividing the constant coefficient and \(q\) dividing the leading coefficient. | Classical number-theoretic result; established in early modern algebra. |
| **Multiplicity of Roots** | A root \(a\) has multiplicity \(m\) if \((x-a)^m\) divides the polynomial but \((x-a)^{m+1}\) does not. | Classical algebra; developed through polynomial factorization. |
| **Euclidean Algorithm for Polynomials** | Computes the greatest common divisor of two polynomials through successive divisions with remainders. | Classical Euclidean algorithm adapted to polynomials; formalized in modern algebra. |
| **Bézout's Identity for Polynomials** | For polynomials \(P,Q\), there exist polynomials \(A,B\) such that \(AP+BQ=\gcd(P,Q)\). | Étienne Bézout, 18th century. |
| **Gauss's Lemma** | The product of two primitive integer polynomials is primitive. It provides a fundamental connection between factorization over the integers and over the rationals. | Carl Friedrich Gauss, 1801. |
| **Irreducibility Criterion** | Establishes conditions under which a polynomial cannot be factored into lower-degree polynomials over a specified coefficient field. Important examples include Eisenstein's criterion. | Gottfried Wilhelm Leibniz and others; Eisenstein, 1850. |
| **Sturm's Theorem** | Determines the exact number of distinct real roots of a polynomial in a given interval using a sequence of polynomial divisions. | Jacques Charles François Sturm, 1829. |
| **Polynomial Interpolation Theorem** | Given \(n+1\) distinct points and their corresponding values, there exists a unique polynomial of degree at most \(n\) passing through all those points. | Classical interpolation; developed by Newton and others in the 17th century. |
| **Taylor's Theorem for Polynomials** | A polynomial can be expressed exactly as a finite Taylor expansion around any point, with coefficients determined by its derivatives. | [Brook Taylor](/view.html?p=notes/social/collective/actor/private/persona/brook-taylor.md), 1715a (title page 1717). |
| **Newton's Identities** | Relate the power sums of polynomial roots to the coefficients of the polynomial. | Isaac Newton, 17th century. |
| **Symmetric Polynomial Theorem** | Every symmetric polynomial can be expressed uniquely as a polynomial in the elementary symmetric polynomials. | Developed in 19th-century algebra; foundational work by Cauchy and others. |
| **Resultant Theorem** | The resultant of two polynomials vanishes if and only if they have a common root in the algebraic closure of their coefficient field. | Étienne Bézout, 1779; the determinant formulation by James Joseph Sylvester, 1853. |
| **Discriminant of a Polynomial** | Provides an algebraic expression in the coefficients that vanishes precisely when the polynomial has a repeated root. | 19th-century algebra; developed by Sylvester and others. |
| **Galois Theory** | Establishes a correspondence between field extensions and groups of automorphisms, providing criteria for whether polynomial equations can be solved by radicals. | Évariste Galois, 1830s. |
| **Hilbert's Basis Theorem** | Every ideal in a polynomial ring over a Noetherian ring is finitely generated. | David Hilbert, 1890 (proved 1888). |

## References

- Viète, F. (1591). *In artem analyticem isagoge*. Jamet Mettayer. — the relations between roots and coefficients, before the symbolic notation existed
- Descartes, R. (1637). *Discours de la méthode, plus La dioptrique, Les météores et La géométrie*. Ian Maire. — the rule of signs, in the *Géométrie*
- Tschirnhaus, E. W. von (1683). Methodus auferendi omnes terminos intermedios ex data aequatione. *Acta Eruditorum*, 2, 204–207.
- Newton, I. (1707). *Arithmetica universalis*. Cambridge University Press. — the identities relating power sums of roots to coefficients
- Bernoulli, J. (1713). *Ars conjectandi*. Thurnisius. — the Bernoulli numbers behind the Bernoulli polynomials
- [Taylor, B. (1715a). *Methodus incrementorum directa et inversa*. William Innys.](/view.html?p=documents/books/taylor-1715-methodus-incrementorum-directa-et-inversa-innys.md) — the finite Taylor expansion of a polynomial
- Euler, L. (1755). *Institutiones calculi differentialis*. Imperial Academy of Sciences. — the Eulerian polynomials and the power-sum generating function
- Bézout, É. (1779). *Théorie générale des équations algébriques*. Ph.-D. Pierres. — the identity $AP + BQ = \gcd(P,Q)$ and the elimination theory behind the resultant
- Legendre, A.-M. (1785). Recherches sur l'attraction des sphéroïdes homogènes. *Mémoires de mathématique et de physique présentés à l'Académie royale des sciences par divers savants*, 10, 411–434.
- Bring, E. S. (1786). *Meletemata quaedam mathematica circa transformationem aequationum algebraicarum*. Lund.
- Lagrange, J.-L. (1795). Leçons élémentaires sur les mathématiques. *Séances des Écoles Normales*, 2. — the interpolating basis that carries his name
- Gauss, C. F. (1799). *Demonstratio nova theorematis omnem functionem algebraicam rationalem integram unius variabilis in factores reales primi vel secundi gradus resolvi posse*. Fleckeisen. — the fundamental theorem of algebra
- Gauss, C. F. (1801). *Disquisitiones arithmeticae*. Fleischer. — the lemma on primitive polynomials, and the irreducibility of the cyclotomic polynomials
- Rodrigues, O. (1816). De l'attraction des sphéroïdes. *Correspondence sur l'École Impériale Polytechnique*, 3, 361–385.
- Abel, N. H. (1826a). Beweis eines Ausdrucks, von welchem die Binomial-Formel ein einzelner Fall ist. *Journal für die reine und angewandte Mathematik*, 1, 159–160.
- Abel, N. H. (1826b). Démonstration de l'impossibilité de la résolution algébrique des équations générales qui passent le quatrième degré. *Journal für die reine und angewandte Mathematik*, 1, 65–84.
- Jerrard, G. B. (1834). *An essay on the resolution of equations*. Taylor & Walton. — the reduction of the quintic to the Bring–Jerrard form
- Sturm, J. C. F. (1835). Mémoire sur la résolution des équations numériques. *Mémoires présentés par divers savants à l'Académie royale des sciences de l'Institut de France*, 6, 271–318. — the sequence that counts distinct real roots in an interval
- Galois, É. (1846). Mémoire sur les conditions de résolubilité des équations par radicaux. *Journal de mathématiques pures et appliquées*, 11, 417–433.
- Eisenstein, G. (1850). Über die Irreducibilität und einige andere Eigenschaften der Gleichung, von welcher die Theilung der ganzen Lemniscate abhängt. *Journal für die reine und angewandte Mathematik*, 39, 160–179. — the criterion on the coefficients
- Puiseux, V. (1850). Recherches sur les fonctions algébriques. *Journal de mathématiques pures et appliquées*, 15, 365–480. — the fractional-power series that resolve a branch at a singular point
- Sylvester, J. J. (1853). On a theory of the syzygetic relations of two rational integral functions, comprising an application to the theory of Sturm's functions, and that of the greatest algebraical common measure. *Philosophical Transactions of the Royal Society of London*, 143, 407–548. — the determinant whose vanishing is the common root: the resultant, and the discriminant
- Chebyshev, P. L. (1859). Sur les questions de minima qui se rattachent à la représentation approximative des fonctions. *Mémoires de l'Académie Impériale des Sciences de St.-Pétersbourg*, 7, 199–291. — the polynomial of least sup norm
- Hermite, C. (1864). Sur un nouveau développement en série des fonctions. *Comptes rendus de l'Académie des sciences*, 58, 93–100, 266–273.
- Lucas, É. (1878). Théorie des fonctions numériques simplement périodiques. *American Journal of Mathematics*, 1(2), 184–240. — the Fibonacci and Lucas polynomials
- Appell, P. (1880). Sur une classe de polynômes. *Annales scientifiques de l'École Normale Supérieure*, 9, 119–144. — the sequences whose derivative is the shifted sequence
- Hilbert, D. (1890). Über die Theorie der algebraischen Formen. *Mathematische Annalen*, 36, 473–534. — the basis theorem for ideals in a polynomial ring (proved 1888, published here)
- Weber, H. (1895). *Lehrbuch der Algebra* (Vol. 1). Vieweg. — the polynomial ring stated as an algebraic structure
- Charlier, C. V. L. (1905). Über die Darstellung willkürlicher Funktionen. *Arkiv för Matematik, Astronomi och Fysik*, 2(20), 1–35.
- Steinitz, E. (1910). Algebraische Theorie der Körper. *Journal für die reine und angewandte Mathematik*, 137, 167–309.
- Birkhoff, G. D. (1912). A determinant formula for the number of ways of coloring a map. *Annals of Mathematics*, 14(1), 42–46. — the chromatic polynomial
- Zhegalkin, I. I. (1927). On the technique of calculating propositions in symbolic logic. *Matematicheskii Sbornik*, 34, 9–28. — the algebraic normal form of a Boolean polynomial
- Alexander, J. W. (1928). Topological invariants of knots and links. *Transactions of the American Mathematical Society*, 30(2), 275–306.
- Krawtchouk, M. (1929). Sur une généralisation des polynômes d'Hermite. *Comptes rendus de l'Académie des sciences*, 189, 620–622.
- Funkhouser, H. G. (1930). A short account of the history of symmetric functions of roots of equations. *The American Mathematical Monthly*, 37(7), 357–365. https://doi.org/10.1080/00029890.1930.11987092 — the history behind Vieta's formulas, Newton's identities and the symmetric-polynomial theorem
- Bell, E. T. (1934). Exponential polynomials. *Annals of Mathematics*, 35(2), 258–277. https://doi.org/10.2307/1968431
- Meixner, J. (1934). Orthogonale Polynomsysteme mit einer besonderen Gestalt der erzeugenden Funktion. *Journal of the London Mathematical Society*, s1-9(1), 6–13. https://doi.org/10.1112/jlms/s1-9.1.6
- Zernike, F. (1934). Beugungstheorie des Schneidenverfahrens und seiner verbesserten Form, der Phasenkontrastmethode. *Physica*, 1(8), 689–704. https://doi.org/10.1016/S0031-8914(34)80259-5 — the polynomials orthogonal on the unit disk
- Szegő, G. (1939). *Orthogonal polynomials* (AMS Colloquium Publications No. 23). American Mathematical Society. — the standard account of the recurrence, the weights and the asymptotics
- Touchard, J. (1939). Sur les cycles des substitutions. *Acta Mathematica*, 70, 243–297. https://doi.org/10.1007/BF02547349
- Hahn, W. (1949). Über Orthogonalpolynome, die q-Differenzengleichungen genügen. *Mathematische Nachrichten*, 2(1), 4–34. https://doi.org/10.1002/mana.19490020103 — the general family of the lattice
- Krall, H. L., & Frink, O. (1949). A new class of orthogonal polynomials: The Bessel polynomials. *Transactions of the American Mathematical Society*, 65(1), 100–115.
- Tutte, W. T. (1954). A contribution to the theory of chromatic polynomials. *Canadian Journal of Mathematics*, 6, 80–91. https://doi.org/10.4153/CJM-1954-010-9 — deletion–contraction, and the two-variable polynomial that specializes to the rest
- Narayana, T. V. (1955). Sur les treillis formés par les partitions d'un entier et leurs applications à la théorie des probabilités. *Comptes rendus de l'Académie des sciences*, 240, 1188–1189.
- Ehrhart, E. (1962). Sur les polyèdres rationnels homothétiques à n dimensions. *Comptes rendus de l'Académie des sciences*, 254, 616–618. — lattice-point counting, where the quasi-polynomial appears
- Chihara, T. S. (1978). *An introduction to orthogonal polynomials*. Gordon and Breach.
- Gutman, I., & Harary, F. (1983). Generalizations of the matching polynomial. *Utilitas Mathematica*, 24, 97–106.
- Askey, R., & Wilson, J. (1985). *Some basic hypergeometric orthogonal polynomials that generalize Jacobi polynomials* (Memoirs of the American Mathematical Society No. 319). American Mathematical Society. — the top of the scheme
- Freyd, P., Yetter, D., Hoste, J., Lickorish, W. B. R., Millett, K., & Ocneanu, A. (1985). A new polynomial invariant of knots and links. *Bulletin of the American Mathematical Society*, 12(2), 239–246. https://doi.org/10.1090/S0273-0979-1985-15361-3 — the HOMFLY polynomial
- Jones, V. F. R. (1985). A polynomial invariant for knots via von Neumann algebras. *Bulletin of the American Mathematical Society*, 12(1), 103–111. https://doi.org/10.1090/S0273-0979-1985-15304-2
- Borwein, P., & Erdélyi, T. (1995). *Polynomials and polynomial inequalities*. Springer. — Chebyshev, Zolotarev and the extremal problems between them
- Lang, S. (2002). *Algebra* (3rd ed.). Springer.
- Rahman, Q. I., & Schmeisser, G. (2002). *Analytic theory of polynomials*. Oxford University Press.
- Sturmfels, B. (2002). *Solving systems of polynomial equations* (CBMS Regional Conference Series No. 97). American Mathematical Society.
- Dummit, D. S., & Foote, R. M. (2004). *Abstract algebra* (3rd ed.). Wiley.
- Gautschi, W. (2004). *Orthogonal polynomials: Computation and approximation*. Oxford University Press. — the three-term recurrence as an algorithm
- Prasolov, V. V. (2004). *Polynomials*. Springer. — the classical theory as a problem book
- Ismail, M. E. H. (2005). *Classical and quantum orthogonal polynomials in one variable*. Cambridge University Press.
- Simon, B. (2005). *Orthogonal polynomials on the unit circle* (Vols. 1–2; AMS Colloquium Publications No. 54). American Mathematical Society. — the Szegő recurrence and the Verblunsky coefficients
- Basu, S., Pollack, R., & Roy, M.-F. (2006). *Algorithms in real algebraic geometry* (2nd ed.). Springer. — Sturm, Descartes and the decision procedures built on them
- Koekoek, R., Lesky, P. A., & Swarttouw, R. F. (2010). *Hypergeometric orthogonal polynomials and their q-analogues*. Springer. — the Askey scheme as a table
- Cox, D. A. (2012). *Galois theory* (2nd ed.). Wiley.
- Cox, D., Little, J., & O'Shea, D. (2015). *Ideals, varieties, and algorithms* (4th ed.). Springer. — the basis theorem, resultants and the algorithms that use them
- Maclagan, D., & Sturmfels, B. (2015). *Introduction to tropical geometry* (Graduate Studies in Mathematics No. 161). American Mathematical Society. — the tropical polynomial and its breakpoints
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
- https://en.wikipedia.org/wiki/List_of_polynomial_topics
- https://en.wikipedia.org/wiki/Gauss%E2%80%93Lucas_theorem 
- https://en.wikipedia.org/wiki/Geometrical_properties_of_polynomial_roots 
- https://en.wikipedia.org/wiki/Rational_root_theorem
- https://en.wikipedia.org/wiki/Symmetric_polynomial 
- https://en.wikipedia.org/wiki/Newton's_identities
