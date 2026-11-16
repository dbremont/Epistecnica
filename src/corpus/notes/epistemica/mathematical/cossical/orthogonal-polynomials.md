---
tags: [note, mathematics, algebraic, approximation]
qa:
 - Why are orthogonal polynomials useful — what does orthogonality buy that the monomial basis does not?
 - When do they arise — which problems generate the weight rather than presuppose it?
 - Is orthogonality a property of the family or of the measure, and what survives when the measure changes?
 - Why must every orthogonal family satisfy a three-term recurrence, and why is that the fact computation depends on?
 - Why do the Gaussian-quadrature nodes fall exactly on the roots?
 - Do Bochner's theorem and the Askey scheme classify the orthogonal families, or only the classical ones?
---

# Orthogonal Polynomials

> A **sequence of orthogonal polynomials** is a polynomial basis chosen so that the coefficients of a projection are read off one at a time — no linear system, no matrix to invert. The price is a weight, and the reward is larger than the arithmetic it saves: in that basis the operator *multiplication by $x$* becomes a symmetric tridiagonal matrix, and the whole spectral theory of the family is the spectral theory of that matrix.

## 1. Definition

Fix a positive measure $\mu$ on an interval (or a finite set, or the unit circle), and the inner product it induces,

\[
\langle f, g \rangle = \int f(x)\,g(x)\,d\mu(x).
\]

A sequence $\{p_n\}_{n\ge 0}$ is **orthogonal with respect to $\mu$** when

\[
\deg p_n = n
\qquad\text{and}\qquad
\langle p_m, p_n \rangle = h_n\,\delta_{mn},
\quad h_n > 0 .
\]

Equivalently: $p_n$ is orthogonal to every polynomial of degree $< n$. The family is determined by $\mu$ only **up to scaling**, so it is fixed by a normalization convention — **monic** ($p_n = x^n + \dots$) or **orthonormal** ($h_n = 1$). The two conventions give the same polynomials divided by constants, and the choice changes the form of every formula below.

Existence is Gram–Schmidt applied to $1, x, x^2, \dots$: each $p_n$ is the component of $x^n$ orthogonal to the span of the previous ones. Writing the condition out in moments $m_k = \int x^k\,d\mu$ gives $p_n$ as a ratio of Hankel determinants of the $m_k$, so the family exists exactly while those determinants stay nonzero — which holds for every measure of infinite support, and fails for a measure supported on finitely many points (there $p_n$ vanishes identically past the support size).

## 2. Why orthogonality is worth the trouble

The vector space of polynomials of degree $\le n$ is the same whatever basis is used. What changes is the *cost of the operations one actually performs on it*, and orthogonality changes three of them at once.

**The coefficients are independent.** For $f \in L^2(\mu)$, the expansion $f \approx \sum_k c_k p_k$ has

\[
c_k = \frac{\langle f, p_k\rangle}{h_k},
\]

one inner product per coefficient. In a non-orthogonal basis the same coefficients solve the **normal equations**, a dense linear system whose matrix is the Gram matrix of the basis.

**Every truncation is optimal.** $S_n f = \sum_{k\le n} c_k p_k$ is the best approximation to $f$ in the $L^2(\mu)$ norm among all polynomials of degree $\le n$, and the error is exactly the tail:

\[
\|f - S_n f\|^2 = \sum_{k>n} |c_k|^2 h_k .
\]

Orthogonality is what makes "best" computable: the residual is orthogonal to the whole space, so no minimization is performed — the answer falls out of the projection.

**The monomial basis is the counter-example.** For $\mu$ the Lebesgue measure on $[0,1]$, the Gram matrix of $1, x, x^2, \dots$ is the **Hilbert matrix** $H_{ij} = 1/(i+j+1)$, whose condition number grows like $(1+\sqrt2)^{4n}$ — at $n = 20$ it exceeds $10^{18}$, past the resolution of double precision. The projection is exact in theory and meaningless in floating point. The orthogonal basis is not a convenience: it is what makes the same theory numerically executable.

**Multiplication by $x$ becomes tridiagonal.** This is the structural reason the families matter beyond approximation. In an orthogonal basis the operator $M_x : f \mapsto xf$ is represented by a symmetric tridiagonal matrix — zeros everywhere except the diagonal $\alpha_n$ and the off-diagonal $\sqrt{\beta_n}$. Approximation theory, quadrature and spectral theory of the family are then all statements about one tridiagonal matrix, which is why the same objects reappear in numerical analysis, in physics and in random matrix theory.

## 3. The recurrence

Orthogonality forces a **three-term recurrence**. For the monic normalization,

\[
p_{n+1}(x) = (x - \alpha_n)\,p_n(x) - \beta_n\,p_{n-1}(x),
\qquad \beta_n = \frac{h_n}{h_{n-1}} > 0 ,
\]

with $\alpha_n = \langle x p_n, p_n\rangle / h_n$. The proof is one line: $x p_n$ has degree $n+1$, so it is a combination of $p_0,\dots,p_{n+1}$, and orthogonality kills every coefficient except three.

The coefficients $(\alpha_n, \beta_n)$ — Gautschi's **recurrence coefficients** — are the canonical data of the family. Legendre, Chebyshev, Hermite and every other named case are a particular sequence of these numbers, and a numerical library stores the sequence, not the polynomials: from it everything else is computed.

- **Evaluation.** Clenshaw's algorithm evaluates $\sum c_k p_k(x)$ in $O(n)$ using the recurrence, with no coefficients of the expanded polynomial ever formed. Expanding into monomials first would reintroduce the conditioning problem.
- **Roots.** The zeros of $p_n$ are the eigenvalues of the $n \times n$ leading block of the **Jacobi matrix** — the symmetric tridiagonal matrix with $\alpha_0,\dots,\alpha_{n-1}$ on the diagonal and $\sqrt{\beta_1},\dots,\sqrt{\beta_{n-1}}$ off it (Golub–Welsch, 1969). Root-finding becomes symmetric eigenvalue computation, which is the most stable routine in the field.
- **The reproducing kernel.** The **Christoffel–Darboux kernel** $K_n(x,y) = \sum_{k\le n} p_k(x)p_k(y)/h_k$ is the kernel of the orthogonal projection onto degree $\le n$; it is the object that reappears as the correlation kernel of determinantal point processes and of random-matrix eigenvalue statistics.

## 4. Where they arise

The family is never chosen for its own sake. Five different mechanisms produce one, and it is worth keeping them apart, because each explains a different part of the literature.

**Sturm–Liouville eigenfunctions.** This is the general mechanism. A self-adjoint second-order operator $(p\,y')' + (\lambda w - q)y = 0$ has a complete set of eigenfunctions orthogonal with respect to $w$. When the eigenfunctions happen to be polynomials, the operator's coefficients satisfy a **Pearson equation** $(\sigma w)' = \tau w$ with $\sigma$ of degree $\le 2$ and $\tau$ of degree $\le 1$ — and that is exactly the condition under which the eigenfunctions are polynomial. Orthogonality is inherited from self-adjointness; the polynomial case is the degenerate, solvable end of it.

**The physical problems those operators carry.** The weights are not invented: they are the domains and boundary conditions of the classical equations. Legendre on $[-1,1]$ is the angular equation of the sphere (zonal harmonics); Hermite with weight $e^{-x^2}$ is the stationary Schrödinger equation of the harmonic oscillator; Laguerre with $e^{-x}$ is the radial equation of the hydrogen atom; Jacobi with $(1-x)^\alpha(1+x)^\beta$ is the hypergeometric equation, and hence the sphere in $d$ dimensions.

**Quadrature.** Gauss quadrature places its $n$ nodes at the roots of $p_n$ and is exact for every polynomial of degree $\le 2n-1$ — the maximum any $n$-point rule can achieve. The weights are $w_i = h_{n-1}/(p_{n-1}(x_i)\,p_n'(x_i))$ and are all positive, which is what makes the rule stable and convergent. This is the sharpest answer to *when do they arise*: whenever a weighted integral must be evaluated exactly on a finite budget, the weight generates its own polynomial family.

**Approximation and filtering.** Chebyshev expansions are the standard basis for minimax approximation — $T_n$ is the monic polynomial of least sup norm, so the Chebyshev truncation is near-best in the uniform norm too. The same families design filters: Chebyshev filters for equiripple passband, Zolotarev (elliptic) filters for equiripple in both bands, Bessel for maximally flat delay.

**Probability, statistics and combinatorics.** On a discrete support the distribution *is* the weight: binomial gives Krawtchouk, Poisson gives Charlier, negative binomial gives Meixner, hypergeometric gives Hahn. In the continuous case the orthogonality is the natural language of moments (Hermite for the Gram–Charlier expansion), and of random matrices: the Hermite, Laguerre and Jacobi weights are the Gaussian, Wishart and MANOVA ensembles, and the Christoffel–Darboux kernel is the eigenvalue correlation kernel.

## 5. The classification

Two theorems organise the zoo, and they answer different questions.

**Bochner's theorem (1929)** classifies the families that satisfy a second-order *differential* equation with polynomial coefficients: up to scaling there are exactly four — **Jacobi, Laguerre, Hermite, Bessel**. Everything classical is a degeneration of Jacobi: Legendre ($\alpha=\beta=0$), Chebyshev of either kind ($\alpha=\beta=\mp\frac12$), Gegenbauer/ultraspherical (equal $\alpha=\beta$), Zernike and the spherical harmonics by a change of variable. The discrete families satisfy the *difference*-equation analogue, and are classified the same way: Hahn, Meixner, Krawtchouk, Charlier.

**The Askey scheme** arranges those families in a hierarchy of limits, from the top down: **Askey–Wilson** (four parameters, basic hypergeometric) contains the continuous dual Hahn, Wilson and continuous Hahn families; those degenerate to Meixner–Pollaczek, Jacobi, Laguerre and Hermite; those to the Hahn and dual Hahn branches, and to Meixner, Krawtchouk and Charlier. Each arrow is a parameter limit. The scheme is a classification of *classical* families — the ones with a hypergeometric representation — not of orthogonal polynomials in general, which is a far larger class.

## 6. What orthogonality is not

- **Not a property of a single polynomial.** A polynomial is orthogonal only *to a family*, in a *measure*. The same $x^2-1$ is $P_2$ for Legendre and a scaled $T_2$ for Chebyshev, and is not orthogonal to anything in the monomial basis.
- **Not unique.** The measure fixes the family only up to scaling; monic, orthonormal and "leading coefficient 1" conventions produce different constants in every formula.
- **Not a statement that the polynomials are small or well-behaved.** Orthogonal polynomials of high degree have roots spread over the support and coefficients that grow; what is well conditioned is the *basis*, not the individual coefficient vectors.
- **Not independent of the measure.** Change the measure and the "best approximation" changes with it: the least-squares problem in $L^2(\mu)$ has a different answer for every $\mu$, and the family is the index of which problem is being solved.
- **Not the same as the discrete families being a different concept.** Krawtchouk and Charlier are the same definition on a finite or countable support; what changes is that the recurrence's spectral measure is now a sum of atoms, and the integral is a weighted sum.

## References

- Szegő, G. (1939/1975). *Orthogonal Polynomials*. AMS Colloquium Publications 23.
- Gautschi, W. (2004). *Orthogonal Polynomials: Computation and Approximation*. Oxford University Press. — recurrence coefficients, quadrature, and the algorithms used above
- Chihara, T. S. (1978). *An Introduction to Orthogonal Polynomials*. Gordon and Breach.
- Askey, R. & Wilson, J. (1985). *Some Basic Hypergeometric Orthogonal Polynomials That Generalize Jacobi Polynomials*. Memoirs of the AMS 319.
- Golub, G. H. & Welsch, J. H. (1969). Calculation of Gauss quadrature rules. *Mathematics of Computation* 23, 221–230. — roots as Jacobi-matrix eigenvalues
- Bochner, S. (1929). Über Sturm–Liouvillesche Polynomsysteme. *Mathematische Zeitschrift* 29, 730–736.
- [Orthogonal polynomials — Wikipedia](https://en.wikipedia.org/wiki/Orthogonal_polynomials)
- [Gaussian quadrature — Wikipedia](https://en.wikipedia.org/wiki/Gaussian_quadrature)
- [Askey scheme — Wikipedia](https://en.wikipedia.org/wiki/Askey_scheme)
- [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) — the taxonomy these families sit in
- [Root](/view.html?p=notes/epistemica/mathematical/mapping/root.md) — the roots of $p_n$ are the quadrature nodes
- [Eigenvalue](/view.html?p=notes/epistemica/mathematical/structure/linear/eigenvalue.md) — the Golub–Welsch correspondence
- [Inner Product](/view.html?p=notes/epistemica/mathematical/structure/linear/inner-product.md) — the form orthogonality is stated in
- [Measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) — the weight as a measure
- [Separation of Variables](/view.html?p=notes/epistemica/mathematical/method/reduction/separation-of-variables.md) — how the physical weights are produced
