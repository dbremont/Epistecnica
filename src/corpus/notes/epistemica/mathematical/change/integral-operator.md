---
tags: [note, mathematics, analytical, operator]
---

# Integral Operator

Related: [Operator](../mapping/operator.md) · [Differential Operator](differential-operator.md) · [Green's Function](../method/transform/green-s-function.md) · [Differential Form](../differential-form.md)

> This note explore a powerful model of accumulation in mathematics, the **Integral Operator**. Knowing the **history of changes in a state system**; reconstruct the **state history of the system**.

## History of the Integral

> **The integral did not begin as an operation.** For two thousand years it was a method of measuring — how much area, how much volume, how much arc — and each measurement was a construction, not a computation. It became an *operation* when Newton and Leibniz made it the inverse of differentiation, and it became an *object* — the operator this note is about — only in the twentieth century, when Volterra, Fredholm and Hilbert turned the integral equation into a subject and the kernel into something that can be composed, inverted and diagonalised.

**Antiquity — exhaustion.** Eudoxus (c. 370 BCE) introduced the method of exhaustion: enclose the figure between inscribed and circumscribed polygons and show that the difference can be made smaller than any assigned magnitude. Archimedes (c. 250 BCE) used it to measure the parabolic segment, the sphere and the spiral, and his *Method of Mechanical Theorems* — a palimpsest rediscovered in 1906 — shows that he first found the results by weighing them mechanically and then proved them by exhaustion. The essential point is what is **absent**: no general procedure, no symbol, no inverse problem. Each quadrature is a bespoke construction, and the infinite process is a proof device rather than a calculation.

**The seventeenth century — indivisibles and quadratures.** Cavalieri (1635) treated a figure as the sum of "all its lines", which turns an area into a sum of infinitely many parallel segments. Wallis (1656) arithmetised the idea, computing $\int_0^1 x^n dx$ for fractional $n$ by infinite series and so producing the first genuinely algebraic quadrature. Fermat (c. 1636) obtained the same for the parabola and the hyperbola, and Barrow (1670) proved geometrically what everyone had noticed: the tangent problem and the area problem are inverse to one another. Still, the sums are summed by ingenuity — a series per curve — and the inverse relation is a theorem about pictures.

**1675–1686 — the algorithm and the sign.** Leibniz first wrote $\int$ — an elongated *s*, for *summa* — in a manuscript of 29 October 1675, and published the calculus of differentials in the *Nova methodus* (1684) and the integral notation in *De geometria recondita* (1686). Newton had reached the same inverse relation a decade earlier through fluxions and fluents, and published it late. What the two inventions share is decisive: the integral stops being a measurement and becomes the **inverse of a rule**. From then on one integrates by knowing derivatives, and the table of integrals replaces the series.

**The eighteenth century — integrals as functions.** Euler (1748) treats the integral as a function in its own right rather than a number attached to a figure: the Beta and Gamma integrals, the elliptic integrals, the whole catalogue of special functions. Lagrange's remark of 1772 that a derivative of fractional order might be defined by an integral formula is the seed of the fractional integrals in the table below.

**1823–1875 — the integral becomes a definition.** Cauchy (1823) defines the definite integral as the limit of a sum over a partition of the interval, which makes it a statement that can be proved rather than a picture that can be seen. Riemann (1854, published 1868) asks the question Cauchy had left implicit — *when* does that limit exist? — and exhibits integrable functions with infinitely many discontinuities, separating integrability from continuity for good. Darboux (1875) supplies the upper and lower sums that make the criterion usable, and Stieltjes (1894) generalises the weight: $\int f\,dg$ replaces $\int f\,dx$, and the differential begins to look like a measure.

**1902–1918 — measure, and the integral as a functional.** Lebesgue (1902, 1904) partitions the *range* rather than the domain: measure the sets where the function takes its values, and the integral becomes a sum over level sets. The gain is not generality for its own sake — it is the theorems that follow: the integral of a limit, dominated convergence, and a fundamental theorem of calculus for exactly the functions (absolutely continuous ones) for which it can hold. Radon (1913) and Nikodym (1930) carry the construction to abstract measures. Daniell (1918) then inverts the whole order: start from a linear functional on functions, assume a continuity property, and *recover* the measure from it. That is the moment the integral is treated as an operator first and a measure second — the view this note takes.

**1896–1912 — the integral equation, and the operator is born.** Volterra (1896) and Fredholm (1903) study equations in which the unknown sits *under* the integral sign: $f(x) = g(x) + \lambda\int K(x,y)f(y)\,dy$. Hilbert (1904–1912) shows that for a symmetric kernel the operator behaves exactly like a symmetric matrix — real eigenvalues, orthogonal eigenfunctions, a spectral decomposition — which is the spectral theorem arriving in analysis through an integral. Schmidt (1907) supplies the singular values, Riesz (1910) proves that every positive linear functional on continuous functions *is* integration against a measure, and Riesz–Schauder extends the theory to compact operators. This is where the note's own subject appears: an integral operator is a linear operator whose matrix has become a kernel $K(x,y)$, and the questions one asks of matrices — compose, invert, diagonalise, bound the norm — become questions about kernels.

**1923–1961 — beyond the real line.** Wiener (1923) constructs a measure on paths, and Feynman (1948) writes the quantum amplitude as an integral over them. Itô (1944) defines an integral against Brownian motion, where the integrand need not have bounded variation and the ordinary Stieltjes reading fails. Bochner (1933) integrates functions taking values in a Banach space. Kurzweil (1957) and Henstock (1961) give a gauge integral that integrates *every* derivative, restoring the fundamental theorem that Lebesgue's integral had to qualify.

| Stage | Who | What changed | What it left behind |
| --- | --- | --- | --- |
| Exhaustion, c. 370–250 BCE | Eudoxus, Archimedes | The infinite process as a proof device | The area results, and the absence of a method |
| Indivisibles, 1635–1670 | Cavalieri, Wallis, Fermat, Barrow | Figures as sums; quadrature by series | The inverse relation between tangents and areas |
| The calculus, 1675–1686 | Newton, Leibniz | The integral as the inverse of $d$; the sign $\int$ | An algorithm, a notation, and a table |
| Integrals as functions, 1748 | Euler | The integral as a function, not a number | Special functions; the Beta and Gamma integrals |
| Rigour, 1823–1875 | Cauchy, Riemann, Darboux | The integral as a limit of sums | Integrability as a property to be characterised |
| Weight and measure, 1894–1918 | Stieltjes, Lebesgue, Radon, Daniell | $\int f\,dg$; measure; the functional first | Convergence theorems; the integral as a functional |
| Integral equations, 1896–1912 | Volterra, Fredholm, Hilbert, Schmidt, Riesz | The kernel; the spectral theorem for integral operators | The operator this note is about |
| Beyond the line, 1923–1961 | Wiener, Feynman, Itô, Bochner, Kurzweil | Paths, noise, Banach spaces, gauges | Integrals that the Riemann and Lebesgue readings cannot reach |

> **Why the operator reading matters.** Once the kernel is the object, the family in this note stops being a list of procedures and becomes one kind of thing: [convolution](../../signal/convolution-operator.md) is an integral operator with $K(x,y) = g(x-y)$; the [Fourier](../../signal/fourier-transform.md) and [Laplace](../../signal/integral-transform.md) transforms are integral operators whose kernels are exponentials; the [Green's function](../method/transform/green-s-function.md) is the kernel that *inverts* a differential operator; a fractional integral is an operator whose kernel has a power singularity. The [Lebesgue integral](../mapping/lebesgue-integral.md) is the domain on which all of them are defined, and the [differential operator](differential-operator.md) is the object they invert. That is why these notes belong together and why this one is filed as an operator rather than as a technique.

## Breviarium

> A comprehensive exploration of the topic.

> **Nucleus (🧬)** → The integral operator essentially encapsulates the process **of summing or accumulating values over a given range**, typically for functions. The deepest essence of the integral operator is its role in transforming functions into scalar values (in definite integrals) or other functions (in indefinite integrals). It is rooted in the concept of accumulation or totalization.

> **Telos (🎯)** → The intent of the integral operator is to compute the area under a curve (for definite integrals), to solve differential equations, or to **represent** various physical phenomena like work, charge, or energy. It is directed toward understanding the cumulative behavior of a function over a specified domain.

> **Techne (🛠️)** → The integral operator works by taking a function and integrating it over a certain interval. Mathematically, this is done by evaluating the limit of a sum (Riemann sum) as the partition of the interval becomes infinitely small. It is used in calculus, physics, engineering, economics, and various other fields to model accumulations and continuous processes.

> **Idoneitas (📏)** → The integral operator is highly suitable for a wide range of applications, from simple geometric problems to complex scientific simulations. Its capability to model accumulation, area, and other integrative properties makes it indispensable. However, its suitability is tied to the function's continuity and the ability to define the limits properly.

> **Limites** (🚧) → The operation of the integral operator is limited by the nature of the function being integrated. For instance, the function must often be continuous (or piecewise continuous) over the interval. Discontinuities or singularities can complicate the process, requiring specialized methods such as improper integrals. Additionally, computational limitations, such as numerical methods for approximation, may impose further boundaries.

> **Contextus (🌐)** → The integral operator emerged from the need to solve problems in physics, especially in calculating areas, volumes, and other accumulations. Historically, it evolved from the work of ancient mathematicians like Archimedes and was formalized through the work of Newton and Leibniz in the development of calculus. Its applications have grown to span fields such as economics (to calculate total cost, revenue), biology (to model growth), and even finance (in risk assessment).

## Formulation

> What is the `deep nature` of the integral operator? What is the function of the operator?

> Which are the techniques used to perform integration (implement the operator)?

> Which is the role of the operator? What is the function of the operator?

## **∫** Integral Operator

| **Context** | **Operator** | **Symbol(s)** | **Description** |
| --- | --- | --- | --- |
| **Real Analysis (ℝ)** | Indefinite Integral | $\int f(x) \, dx$ | Antiderivative of a function. |
|  | Definite Integral | $\int_a^b f(x) \, dx$ | Area under the curve of $f$ from $a$ to $b$. |
|  | Line Integral (Scalar) | $\int_C f \, ds$ | Integral of a scalar field along a curve. |
|  | Line Integral (Vector) | $\int_C \mathbf{F} \cdot d\mathbf{r}$ | Work done by a vector field along a curve. |
| **Multivariable Calculus** | Double Integral | $\iint_D f(x,y) \, dA$ | Integral over a 2D region. |
|  | Triple Integral | $\iiint_V f(x,y,z) \, dV$ | Integral over a 3D volume. |
|  | Surface Integral (Scalar) | $\iint_S f \, dS$ | Integral of a scalar field over a surface. |
|  | Surface Integral (Vector) | $\iint_S \mathbf{F} \cdot d\mathbf{S}$ | Flux of a vector field through a surface. |
| **Complex Analysis (ℂ)** | Complex Line Integral | $\oint_\gamma f(z) \, dz$ | Integral of a holomorphic function along a path. |
|  | Contour Integral | $\oint_C f(z) \, dz$ | Integral around a closed loop (residue theorem). |
| **Functional Analysis** | [Lebesgue Integral](../mapping/lebesgue-integral.md) | $\int_X f \, d\mu$ | Generalization of the integral for measurable functions. |
|  | Bochner Integral | $\int_X f \, d\mu$ | Extension of Lebesgue integral to Banach spaces. |
| **Differential Geometry** | [Integration on Manifolds](../differential-form.md) | $\int_M \omega$ | Integral of a differential form over a manifold. |
|  | Stokes’ Theorem | $\int_{\partial M} \omega = \int_M d\omega$ | Relates boundary and interior integrals. |
| **Fourier & Transforms** | [Fourier Transform](../../signal/fourier-transform.md) | $\mathcal{F}\{f\}(\xi) = \int_{-\infty}^\infty f(x) e^{-i\xi x} dx$ | Transforms a function to frequency domain. |
|  | [Laplace Transform](../../signal/integral-transform.md) | $\mathcal{L}\{f\}(s) = \int_0^\infty f(t) e^{-st} dt$ | Converts time-domain functions to complex frequency. |
| **Distributions & PDEs** | [Convolution](../../signal/convolution-operator.md) | $(f * g)(x) = \int_{-\infty}^\infty f(y)g(x-y) \, dy$ | Combines two functions via integral. |
|  | [Green’s Function](../method/transform/green-s-function.md) | $G(x,y)$ (solves $\mathcal{L}G = \delta$) | **Integral kernel** for solving PDEs. |
| **Specialized Operators** | Fractional Integral | $I^\alpha f$ | Non-integer-order integral (e.g., Riemann-Liouville). |
|  | [Path Integral (QFT)](../../singular/path-integral.md) | $\int \mathcal{D}\phi \, e^{iS[\phi]}$ | Functional integral in quantum field theory. |
|  | **…** | **…** | **…** |

## Integrability

> What makes a function non-integrable? What makes a function hard to integrate?

- Continous
- Lebesgue Measurable Function
- Local
- Function Must Be Defined at the Point
- Continuity at the Point
- Smooth at the point
- Stable Local Behavior
- Bounded Variation in the Neighborhood
- Absence of Discontinuities in Higher-Order Oscillations
- Local Linear Approximability

## ❓ QA

### How can we evaluate the original function at a point \(x\), using only its derivative and the integration operation?

> Let us consider the function \(f(x)=x^2\), whose derivative is \(f'(x)=2x\).

Suppose we know the derivative \(f'(x)\), but want to recover the value of the original function at \(x=2\).

- How can integration be used to recover \(f(2)\) from \(f'(x)\)?
- Why must we specify a starting point where the value of the original function is known?
- Why can we choose different starting points and still obtain the same value of \(f(2)\)?
- What is the mathematical relationship between the accumulated change of a function over an interval and the difference between its values at the endpoints?

The value of the function at any point \(x\) is its value at a known starting point \(a\), plus the accumulated change between \(a\) and \(x\):

\[
\boxed{f(x)=f(a)+\int_a^x f'(t)\,dt}
\]

Where:
- \(f(a)\): known function value at the starting point.
- \(f'(t)\): derivative, representing the instantaneous rate of change.
- \(\int_a^x f'(t)\,dt\): accumulated change from \(a\) to \(x\).

**In essence:**

\[
\text{Function value}=\text{Initial value}+\text{Accumulated change}
\]

Note:

- The value of the original function at a **known starting** point must be provided to recover its value at another point using definite integration.

### What makes a function hard to integrate?

- Non-Elementary Integral
- Elliptic Integral
- Irregularity (Non-Stable Local Behavior)
- High-Dimensional Integral
- Pathological behavior (e.g., infinite oscillations, discontinuities).
- Transcendental Functions (Non Algebraic)
- Topological Obstruction

### How to Integrate Seemingly Impossible Functions?

- **Special Functions**: Express answers using special functions.
- **Numerical Methods**: Quadrature, Monte Carlo, adaptive sampling.
- **Symbolic Algorithms**: Risch algorithm (determines if elementary antiderivative exists).

### In which cases are integral equations a more suitable representation than differential equations, and why? What types of systems or processes benefit from being described by integral equations rather than differential equations, and for what reasons?

| **Case** | **Why Integral Equations Are Suitable** | **Example** |
| --- | --- | --- |
| **Systems with Memory Effects** | Integral equations naturally model systems where the current state depends on past states or events. | Viscoelastic materials, biological systems, Volterra integral equations. |
| **Nonlocal Interactions** | When interactions span a region or history, integral equations describe the cumulative effects better than differential equations. | Electromagnetic field theory (electric and magnetic field integral equations). |
| **Boundary Integral Methods (BEM)** | They simplify problems with complex geometries or infinite domains by reducing the problem to a boundary. | Acoustics, electromagnetics, fluid dynamics using boundary integral methods. |
| **Nonlinear Systems** | Nonlinearities that involve historical or spatially spread-out effects are captured better by integral equations. | Nonlinear optics, fluid dynamics, systems with nonlinear memory effects. |
| **Fractional Systems** | For systems exhibiting memory or nonlocal behavior, fractional derivatives are often replaced by integrals. | Anomalous diffusion, viscoelastic materials, fractional calculus problems. |
| **Inverse Problems** | Inverse problems often involve determining causes from effects, naturally leading to integral equations. | Medical imaging (tomography), conductivity reconstruction. |

## 📚 References

- Abramowitz, M., & Stegun, I. A. (Eds.). (1964). *Handbook of mathematical functions with formulas, graphs, and mathematical tables* (Applied Mathematics Series No. 55). National Bureau of Standards. — the scan the QA points at
- Archimedes. (1897). *The works of Archimedes* (T. L. Heath, Ed. & Trans.). Cambridge University Press. — the *Quadrature of the Parabola* and the *Method*
- Barrow, I. (1670). *Lectiones geometricae*. London. — the geometric inverse relation between tangents and areas
- Bochner, S. (1933). Integration von Funktionen, deren Werte die Elemente eines Vektorraumes sind. *Fundamenta Mathematicae*, 20, 262–276.
- Cauchy, A.-L. (1823). *Résumé des leçons données à l'École Royale Polytechnique sur le calcul infinitésimal*. Imprimerie Royale. — the definite integral as a limit of sums
- Cavalieri, B. (1635). *Geometria indivisibilibus continuorum nova quadam ratione promota*. Bologna.
- Courant, R., & Hilbert, D. (1953). *Methods of mathematical physics* (Vol. 1). Interscience.
- Daniell, P. J. (1918). A general form of integral. *Annals of Mathematics*, 19(4), 279–294. — the functional first, the measure after
- Darboux, G. (1875). Mémoire sur les fonctions discontinues. *Annales scientifiques de l'École Normale Supérieure*, 2e série, 4, 57–112.
- Euler, L. (1748). *Introductio in analysin infinitorum* (Vol. 1). Lausanne. — the integral as a function
- Feynman, R. P. (1948). Space-time approach to non-relativistic quantum mechanics. *Reviews of Modern Physics*, 20(2), 367–387.
- Folland, G. B. (1999). *Real analysis: Modern techniques and their applications* (2nd ed.). Wiley.
- Fredholm, I. (1903). Sur une classe d'équations fonctionnelles. *Acta Mathematica*, 27, 365–390.
- Gradshteyn, I. S., & Ryzhik, I. M. (2014). *Table of integrals, series, and products* (8th ed.). Academic Press.
- Henstock, R. (1963). *Theory of integration*. Butterworths. — the gauge integral, which integrates every derivative
- Hilbert, D. (1912). *Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen*. Teubner.
- Hochstadt, H. (1973). *Integral equations*. Wiley.
- Itô, K. (1944). Stochastic integral. *Proceedings of the Imperial Academy (Tokyo)*, 20(8), 519–524.
- Kanwal, R. P. (2013). *Linear integral equations* (3rd ed.). Birkhäuser.
- Kurzweil, J. (1957). Generalized ordinary differential equations and continuous dependence on a parameter. *Czechoslovak Mathematical Journal*, 7(82), 418–449.
- Lebesgue, H. (1904). *Leçons sur l'intégration et la recherche des fonctions primitives*. Gauthier-Villars.
- Leibniz, G. W. (1686). De geometria recondita et analysi indivisibilium atque infinitorum. *Acta Eruditorum*, 5, 292–300. — where the sign $\int$ was published
- Newton, I. (1736). *The method of fluxions and infinite series* (J. Colson, Trans.). Henry Woodfall. (Original work written 1671)
- Olver, F. W. J., Olde Daalhuis, A. B., Lozier, D. W., Schneider, B. I., Boisvert, R. F., Clark, C. W., Miller, B. R., Saunders, B. V., Cohl, H. S., & McClain, M. A. (Eds.). (2024). *NIST digital library of mathematical functions*. https://dlmf.nist.gov/
- Polyanin, A. D., & Manzhirov, A. V. (2008). *Handbook of integral equations* (2nd ed.). Chapman & Hall/CRC.
- Reed, M., & Simon, B. (1980). *Methods of modern mathematical physics I: Functional analysis*. Academic Press.
- Riemann, B. (1868). Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe. *Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, 13, 87–132.
- Riesz, F. (1910). Untersuchungen über Systeme integrierbarer Funktionen. *Mathematische Annalen*, 69, 449–497. — the representation of functionals as integrals
- Riesz, F., & Sz.-Nagy, B. (1990). *Functional analysis*. Dover.
- Risch, R. H. (1969). The problem of integration in finite terms. *Transactions of the American Mathematical Society*, 139, 167–189.
- Ritt, J. F. (1948). *Integration in finite terms: Liouville's theory of elementary methods*. Columbia University Press.
- Rudin, W. (1987). *Real and complex analysis* (3rd ed.). McGraw-Hill.
- Samko, S. G., Kilbas, A. A., & Marichev, O. I. (1993). *Fractional integrals and derivatives: Theory and applications*. Gordon and Breach.
- Schmidt, E. (1907). Zur Theorie der linearen und nichtlinearen Integralgleichungen. *Mathematische Annalen*, 63, 433–476.
- Stieltjes, T.-J. (1894). Recherches sur les fractions continues. *Annales de la Faculté des Sciences de Toulouse*, 8, J1–J122.
- Tricomi, F. G. (1957). *Integral equations*. Interscience.
- Volterra, V. (1896). Sulla inversione degli integrali definiti. *Atti della Reale Accademia delle Scienze di Torino*, 31, 311–324.
- Wallis, J. (1656). *Arithmetica infinitorum*. Oxford. — the arithmetisation of indivisibles
- Wiener, N. (1923). Differential-space. *Journal of Mathematics and Physics*, 2, 131–174.
- Yosida, K. (1980). *Functional analysis* (6th ed.). Springer.

**Lookup pages**

- [Integral symbol](https://en.wikipedia.org/wiki/Integral_symbol) · [Integral](https://en.wikipedia.org/wiki/Integral) · [Riemann integral](https://en.wikipedia.org/wiki/Riemann_integral) · [Lebesgue integral](https://en.wikipedia.org/wiki/Lebesgue_integral) · [Antiderivative](https://en.wikipedia.org/wiki/Antiderivative) · [Integral linear operator](https://en.wikipedia.org/wiki/Integral_linear_operator)
- [Lists of integrals](https://en.wikipedia.org/wiki/Lists_of_integrals) · [Special functions](https://en.wikipedia.org/wiki/Special_functions) · [Elementary function](https://en.wikipedia.org/wiki/Elementary_function) · [Risch algorithm](https://en.wikipedia.org/wiki/Risch_algorithm)
- [Integral kernel — Wolfram MathWorld](https://mathworld.wolfram.com/IntegralKernel.html)

**Corpus**

- [Equation](../../../nature/result/equation.md) — why an equation travels between fields, and where the differential and integral forms of the same law diverge
- [Lebesgue Integral](../mapping/lebesgue-integral.md) — the domain on which the kernels are defined
- [Differential Operator](differential-operator.md) — the object an integral operator inverts
- [Green's Function](../method/transform/green-s-function.md) — the kernel that inverts a differential operator
- [Convolution Operator](../../signal/convolution-operator.md) — an integral operator with a translation kernel
- [Fourier Transform](../../signal/fourier-transform.md) · [Integral Transform](../../signal/integral-transform.md) — the transform family as integral operators
- [Path Integral](../../singular/path-integral.md) — the functional integral the table reaches
- [Signal Processing](../../signal/signal-processing.md) — the practice in which most of these kernels are used
