---
tags: [note, mathematics, representation, analysis, approximation]
qa:
 - Is the Padé approximant a representation of a function or of its power series — and what happens when the series converges nowhere?
 - A rational function is fixed by its poles and zeros. Which of those poles belong to the function, and which are artefacts of the matching?
 - The Taylor representation is exact and truncation is the approximation. Where does that separation go when the representation itself is a ratio of finite polynomials?
---

# Padé Representation

> The **Padé representation** writes a [function](/view.html?p=notes/epistemica/mathematical/mapping/function.md) as a ratio of two polynomials, with the coefficients fixed by matching its [Taylor series](/view.html?p=notes/epistemica/mathematical/change/power-series.md) to a chosen order. Its blocks are the rational functions; its coefficients are the solution of a linear system. Where the Taylor representation makes local behaviour a sequence of derivatives, the Padé representation makes it a pair of polynomials — and a pair of polynomials can have poles, which is the whole of its advantage and the whole of its danger.

$$\left[\frac{m}{n}\right]_f(x)=\frac{P_m(x)}{Q_n(x)}=\frac{p_0+p_1x+\cdots+p_mx^m}{1+q_1x+\cdots+q_nx^n},
\qquad
f(x)\,Q_n(x)-P_m(x)=\mathcal{O}\left(x^{m+n+1}\right)$$

> The matching condition is the definition: the rational function reproduces the series through order $m+n$ and says nothing about the terms beyond it. The $n$ equations for $q_1,\dots,q_n$ are linear, the $P_m$ then follow by convolution, and the object is unique when that system is non-singular. Introduced systematically by Henri Padé in his 1892 thesis; see [Padé approximant](https://en.wikipedia.org/wiki/Pad%C3%A9_approximant).

## 1. The representation

A representation is a choice of building blocks. The Taylor representation chooses the powers of $x-a$; the Padé representation chooses their ratios, and pays for the richer blocks with a nonlinear bookkeeping problem — the denominator's coefficients enter the matching equations, so the extraction is a solve, not a differentiation.

The family it belongs to, with each member's blocks and the way its coefficients are fixed:

| Representation | Building blocks | Coefficients fixed by |
| --- | --- | --- |
| [Taylor representation](/view.html?p=notes/epistemica/mathematical/method/representation/taylor-representation.md) | Powers of $x-a$ | Derivatives at $a$ |
| **Padé representation** | Ratios $P_m/Q_n$ | Series coefficients through order $m+n$, by a linear system |
| [Fourier representation](/view.html?p=notes/epistemica/signal/fourier-series.md) | Sines and cosines | Inner products against the basis |
| Laurent representation | Positive and negative integer powers | Contour integrals around the annulus |
| [Power series representation](/view.html?p=notes/epistemica/mathematical/change/power-series.md) | Integer powers of a variable | Derivatives at the centre, as a special case |
| [Chebyshev representation](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) | Chebyshev polynomials | Projection under the weight $1/\sqrt{1-x^2}$ |
| [Wavelet representation](/view.html?p=notes/epistemica/signal/wavelet.md) | Wavelets | Inner products at each scale and position |

Read down the table and two things distinguish the Padé row. Its blocks are not a basis — a sum of rational functions is not decomposed into them the way a Fourier series is decomposed into sines — so the representation is a *single* ratio chosen from a family, not an expansion in a fixed set. And its coefficients are extracted from the same data the Taylor representation uses, the series coefficients, but through a different operation: Taylor differentiates, Padé solves.

## 2. What the conversion buys

Three consequences follow, and they are what the representation is for.

**Poles become first-class.** A Taylor series cannot represent a pole: its radius of convergence stops at the nearest singularity and the series diverges there. A rational function carries poles explicitly, so a function whose behaviour is dominated by a nearby singularity — a resonance, a bound state, a critical point — is represented by the object that has the singularity in it, not by a polynomial that cannot.

**Analytic continuation.** The $[m/n]$ approximant is defined wherever its denominator does not vanish, which can be far outside the Taylor disc. For a Stieltjes or meromorphic function the diagonal sequence $[n/n]$ converges in capacity on the domain cut by the singularities, so the representation reconstructs the function from local data at a point — the precise sense in which it continues the series.

**Resummation.** Asymptotic and divergent series are the standard case: $\sum (-1)^k k!\,x^k$ has zero radius of convergence, yet its Padé approximants converge to the function the series was trying to describe. Perturbation expansions in quantum mechanics, critical phenomena and fluid dynamics are routinely resummed this way, which is why the Padé representation sits next to [Perturbation Method](/view.html?p=notes/epistemica/mathematical/method/approximation/perturbation-method.md) as well as next to Taylor.

## 3. Where the representation fails

The pole that makes the representation useful is also the artefact that makes it untrustworthy.

- **Spurious poles.** The matching fixes $m+n+1$ coefficients from $m+n+1$ conditions; a pole–zero pair can appear that has nothing to do with the function — a Froissart doublet — and moves or disappears as the order changes. Reading a physical pole off a single approximant is a mistake; reading it off a stable sequence is evidence.
- **Non-uniqueness and defects.** The linear system for $q_1,\dots,q_n$ can be singular, in which case the approximant is not unique and the matching order is not the nominal one. The defect is not an error in the arithmetic; it is a statement that the data do not determine the rational function.
- **No universal convergence.** Convergence holds under conditions — in capacity for functions with the appropriate singularity structure, such as meromorphic and Stieltjes functions — and there is no theorem for an arbitrary formal series. A well-behaved approximant is evidence, never proof.
- **Ill-conditioning.** The matching system is a Toeplitz system built from the series coefficients, and its condition number grows with the order. High-order approximants computed in floating point can be dominated by the conditioning rather than by the function.

## 4. Representation, approximant and sequence

> The Taylor note keeps the series and its truncation apart. The Padé representation needs the same discipline, with one further distinction: the *representation* is the family of rational functions admitted by the matching rule, the *approximant* is one member $[m/n]$, and the *sequence* is the ordered family $[0/0],[1/0],[0/1],[1/1],\dots$ whose limit is what the convergence theorems are about.

Three consequences:

- the approximant is exact on the data it matches and silent on everything else — a statement about order $m+n$, never about the function;
- the diagonal sequence is the object with the theory; a single off-diagonal entry has no convergence claim attached to it;
- the continued-fraction route — the same rational functions generated by a three-term recurrence from the series — is how the representation is computed stably, and it is where the connection to orthogonal polynomials and to the [Generating Function](/view.html?p=notes/epistemica/mathematical/method/transform/generating-function.md) lives.

## 5. Where it sits in the corpus

The Padé representation is the rational counterpart of the [Taylor representation](/view.html?p=notes/epistemica/mathematical/method/representation/taylor-representation.md): it reads the same coefficients and returns an object with poles instead of a polynomial. It is the resummation tool of [Perturbation Method](/view.html?p=notes/epistemica/mathematical/method/approximation/perturbation-method.md) and of asymptotic analysis, the representation behind the Padé entries in the [Differential Equation](/view.html?p=notes/epistemica/mathematical/change/differential-equation.md) method tables, and the reason a rational function is worth studying as a [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md) ratio rather than as a numerical convenience. The family it belongs to is [Representation](/view.html?p=notes/epistemica/mathematical/method/representation.md).

## References

- Padé, H. (1892). *Sur la représentation approchée d'une fonction par des fractions rationnelles*. Annales scientifiques de l'École Normale Supérieure, 9 (supplément), 3–93. — the thesis that fixed the matching rule and the table of approximants
- Baker, G. A. (1975). *Essentials of Padé approximants*. Academic Press. — the convergence theory and the numerical practice
- Baker, G. A., & Graves-Morris, P. (1996). *Padé approximants* (2nd ed.). Cambridge University Press. — the standard reference, including the spurious-pole and defect theory
- Bender, C. M., & Orszag, S. A. (1978). *Advanced mathematical methods for scientists and engineers*. McGraw-Hill. — resummation of divergent perturbation series
- [Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007). *Numerical recipes: The art of scientific computing* (3rd ed.). Cambridge University Press.](/view.html?p=documents/books/press-2007-numerical-recipes-edition-art-scientific.md) — the continued-fraction algorithm
- [Padé approximant](https://en.wikipedia.org/wiki/Pad%C3%A9_approximant)
- [Representation](/view.html?p=notes/epistemica/mathematical/method/representation.md) — the family, and the table of building blocks
- [Taylor Representation](/view.html?p=notes/epistemica/mathematical/method/representation/taylor-representation.md) · [Power Series](/view.html?p=notes/epistemica/mathematical/change/power-series.md) · [Perturbation Method](/view.html?p=notes/epistemica/mathematical/method/approximation/perturbation-method.md)
- Andraka, R. (1998). A survey of CORDIC algorithms for FPGA based computers. In *Proceedings of the 1998 ACM/SIGDA sixth international symposium on Field programmable gate arrays* (pp. 191–200). Association for Computing Machinery. https://doi.org/10.1145/275107.275139
- Meher, P. K., Valls, J., Juang, T. B., Sridharan, K., & Maharatna, K. (2009). 50 years of CORDIC: Algorithms, architectures, and applications. *IEEE Transactions on Circuits and Systems I: Regular Papers, 56*(9), 1893–1907. https://doi.org/10.1109/TCSI.2009.2025803
- Timmermann, D., Hahn, H., & Hosticka, B. J. (1992). Low latency time CORDIC algorithms. *IEEE Transactions on Computers*.
- Volder, J. E. (1959). The CORDIC trigonometric computing technique. *IRE Transactions on Electronic Computers, EC-8*(3), 330–334. https://doi.org/10.1109/TEC.1959.5222693
- Volder, J. E. (2000). The birth of CORDIC. *Journal of VLSI Signal Processing Systems for Signal, Image, and Video Technology, 25*, 101–105. https://doi.org/10.1023/A:1008110704586
- Walther, J. S. (1971). A unified algorithm for elementary functions. In *Proceedings of the May 18–20, 1971, Spring Joint Computer Conference* (pp. 379–385). Association for Computing Machinery. https://doi.org/10.1145/1478786.1478840
- Wang, C., Piuri, V., & Swartzlander, E. E. (1997). Hybrid CORDIC algorithms. *IEEE Transactions on Computers*.
- Hsiao, S. F., & Delosme, J. M. (1995). Householder CORDIC algorithms. *IEEE Transactions on Computers*.
