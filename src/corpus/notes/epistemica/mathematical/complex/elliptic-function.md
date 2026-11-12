---
tags: [note, mathematics, analytical, complex]
---

# Elliptic Function

> An **elliptic function** is a doubly periodic meromorphic function on the complex plane: two independent complex periods $\omega_1, \omega_2$ with $\omega_1/\omega_2 \notin \mathbb{R}$ such that
> $$f(z + \omega_1) = f(z + \omega_2) = f(z)$$
> for every $z$. Equivalently — and more usefully — an elliptic function is a **meromorphic function on a torus**, the quotient $\mathbb{C}/\Lambda$ where $\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ is the lattice of periods. Everything the functions can do is a statement about that torus.

## Definition

The period lattice $\Lambda$ tiles the plane, so the fundamental parallelogram $\{a + s\omega_1 + t\omega_2 : 0 \le s, t < 1\}$ contains exactly one representative of each point of the torus. An elliptic function is a meromorphic function on $\mathbb{C}$ invariant under translation by $\Lambda$, hence a function on the compact surface $\mathbb{C}/\Lambda$ — a genus-1 Riemann surface.

Two consequences follow immediately and fix the shape of the whole subject:

- **No non-constant holomorphic elliptic function exists.** A doubly periodic entire function is bounded on the fundamental parallelogram, hence bounded on $\mathbb{C}$, hence constant (Liouville). So every non-constant elliptic function has **poles**.
- **The order is well defined.** Counting poles and zeros with multiplicity in the fundamental parallelogram, the numbers are equal, and that common number is the **order** of the function. The residues of the poles sum to zero — which is why the simplest non-constant example has a double pole, not a simple one.

## The Weierstrass ℘ Function

The canonical elliptic function, built for a given lattice so that nothing is assumed about it:

$$\wp(z) = \frac{1}{z^{2}} + \sum_{\omega \in \Lambda \setminus \{0\}} \left( \frac{1}{(z - \omega)^{2}} - \frac{1}{\omega^{2}} \right)$$

It is **even**, doubly periodic, and of order two: a double pole at every lattice point and nowhere else. Subtracting $1/\omega^2$ from each term is what makes the sum converge, and it is why ℘ is not simply $\sum (z-\omega)^{-2}$.

℘ satisfies a differential equation whose coefficients are constants of the lattice,

$$\wp'(z)^{2} = 4\wp(z)^{3} - g_{2}\wp(z) - g_{3},$$

with the invariants $g_2, g_3$ built from $\Lambda$. That is the bridge between the two meanings of *elliptic*: the point $(\wp(z), \wp'(z))$ traces an **elliptic curve** $y^2 = 4x^3 - g_2x - g_3$, and the uniformisation is exact — every complex elliptic curve is a torus, reached this way.

## Jacobi's Functions

The older construction, from the elliptic integral. For the modulus $k \in (0, 1)$ define $u = \int_0^\phi \frac{d\theta}{\sqrt{1 - k^2\sin^2\theta}}$; then

$$\mathrm{sn}(u) = \sin\phi, \qquad \mathrm{cn}(u) = \cos\phi, \qquad \mathrm{dn}(u) = \sqrt{1 - k^2\sin^2\phi},$$

doubly periodic in $u$ with the identity $\mathrm{sn}^2 + \mathrm{cn}^2 = 1$ on every branch. Jacobi's functions are rational functions of $\wp$ and $\wp'$ for the right lattice — the two constructions describe the same objects, told from the integral side rather than the lattice side.

## Where They Arise

- **The exact pendulum.** For a swing of amplitude $\theta_0$, the motion is $\theta(t) = 2\arcsin\!\left(k\,\mathrm{sn}(\,\cdot\,)\right)$ with $k = \sin(\theta_0/2)$; the small-angle approximation $\sin\theta \approx \theta$ is what turns the elliptic function into an ordinary sine.
- **The perimeter of an ellipse.** The arc length of $x^2/a^2 + y^2/b^2 = 1$ is an elliptic integral, and inverting it gives the functions — *this is where the name comes from*, not from the ellipse being a curve of genus one.
- **Addition theorems.** Elliptic functions admit addition formulas structurally like $\sin(\alpha+\beta)$, which is what makes them the natural generalisation of the trigonometric functions to a torus.
- **Modular forms.** As functions of the period ratio $\tau = \omega_2/\omega_1$, the invariants $g_2, g_3$ belong to [Modular Form](/view.html?p=notes/epistemica/mathematical/complex/modular-form.md).

## The Three Elliptics

The word names four different objects; the corpus should not let them blur.

| Term | What it is | Note |
| --- | --- | --- |
| **Elliptic function** | doubly periodic meromorphic function on $\mathbb{C}/\Lambda$ | this note |
| **Elliptic integral** | an integral $\int R(x, \sqrt{P(x)})\,dx$ with $P$ cubic or quartic; not elementary | the object the functions invert |
| **Elliptic curve** | a projective curve of genus 1, e.g. $y^2 = x^3 + ax + b$ | the image of the torus under $(\wp, \wp')$ |
| **Elliptic equation** | a linear second-order PDE, $a u_{xx} + 2b u_{xy} + c u_{yy} + \dots = 0$ with $b^2 - ac < 0$ | unrelated to the above; cf. [Ultrahyperbolic Equation](/view.html?p=notes/epistemica/mathematical/equation/ultrahyperbolic-equation.md) |

## References

- https://en.wikipedia.org/wiki/Elliptic_function
- https://en.wikipedia.org/wiki/Weierstrass_elliptic_function
- https://en.wikipedia.org/wiki/Jacobi_elliptic_functions
- https://en.wikipedia.org/wiki/Elliptic_curve
- https://en.wikipedia.org/wiki/Elliptic_integral
- [Complex Function](/view.html?p=notes/epistemica/mathematical/complex/complex-function.md) — the class of functions this one refines
- [Holomorphic Function](/view.html?p=notes/epistemica/mathematical/complex/holomorphic-function.md) — what a doubly periodic function cannot be (unless constant)
- [Modular Form](/view.html?p=notes/epistemica/mathematical/complex/modular-form.md) — what the lattice invariants become as functions of $\tau$
- [Conformal Map](/view.html?p=notes/epistemica/mathematical/complex/conformal-map.md) — the local behaviour every meromorphic function shares
- [Trigonometry](/view.html?p=notes/epistemica/mathematical/geometry/trigonometry.md) — the circular counterpart, of which these are the elliptic generalisation
- Whittaker, E. T., and Watson, G. N. *A Course of Modern Analysis*, 4th ed., ch. 20–22.
- McKean, H., and Moll, V. *Elliptic Curves: Function Theory, Geometry, Arithmetic*.
