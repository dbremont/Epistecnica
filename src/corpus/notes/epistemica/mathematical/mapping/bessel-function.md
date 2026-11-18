---
tags: [note, mathematics, function, special-function, bessel]
qa:
 - Why do Bessel functions appear whenever the domain is a cylinder?
 - What is the difference between the ordinary and the modified Bessel functions?
 - Why does the Bessel function decay like a cosine divided by the square root of the argument?
---

# Bessel Function

> **Bessel functions** are the solutions of Bessel's differential equation,
> $$x^2 y'' + x y' + (x^2 - \nu^2)\,y = 0,$$
> and the functions that appear whenever a problem is solved in **cylindrical coordinates**. They are the radial counterpart of the sine and cosine: the oscillation is the same, the amplitude decays as $1/\sqrt{x}$.

> The equation arises from separating the Laplacian in a cylinder. The angular part gives Fourier modes, the axial part gives exponentials, and the radial part gives Bessel's equation — which is why the function is unavoidable in heat conduction in rods, vibrations of a drumhead, electromagnetic waveguides and acoustic scattering.

## The four functions

| Function | Equation | Behaviour | Use |
| --- | --- | --- | --- |
| **$J_\nu(x)$** (Bessel, first kind) | Ordinary | Oscillatory, finite at the origin for $\nu \ge 0$ | The radial mode inside a cylinder |
| **$Y_\nu(x)$** (Bessel, second kind, Neumann) | Ordinary | Oscillatory, singular at the origin | The outward or exterior solution |
| **$I_\nu(x)$** (modified, first kind) | Modified | Growing, no oscillation | Diffusion and screening in cylindrical geometry |
| **$K_\nu(x)$** (modified, second kind, Macdonald) | Modified | Decaying, singular at the origin | Evanescent modes, Green's functions in cylinders |

> The ordinary pair solves the oscillatory problem (waves, vibrations); the modified pair solves the equation with a sign change, $x^2y''+xy'-(x^2+\nu^2)y=0$, which is the diffusive or evanescent problem. The substitution $x \mapsto ix$ carries one pair to the other.

## The series and the asymptotics

> For the first kind,
> $$J_\nu(x) = \sum_{k=0}^{\infty} \frac{(-1)^k}{k!\,\Gamma(k+\nu+1)}\left(\frac{x}{2}\right)^{2k+\nu},$$
> with the gamma function in the denominator — the first place the two special functions meet. For integer order the negative-order relation $J_{-n} = (-1)^n J_n$ holds; for non-integer order $J_\nu$ and $J_{-\nu}$ are independent.

> For large argument,
> $$J_\nu(x) \sim \sqrt{\frac{2}{\pi x}}\cos\left(x - \frac{\nu\pi}{2} - \frac{\pi}{4}\right), \qquad I_\nu(x) \sim \frac{e^{x}}{\sqrt{2\pi x}}.$$
> The $1/\sqrt{x}$ envelope is the cylindrical counterpart of the constant amplitude of a plane wave: the energy spreads over a growing circumference.

## Properties

| Property | Statement |
| --- | --- |
| **Generating function** | $e^{(x/2)(t - 1/t)} = \sum_{n=-\infty}^{\infty} J_n(x)\,t^n$ |
| **Recurrence** | $J_{\nu-1}(x) + J_{\nu+1}(x) = \dfrac{2\nu}{x}J_\nu(x)$ |
| **Orthogonality** | $J_\nu$ with the weight $x$ on the interval set by the zeros — the Fourier–Bessel series |
| **Zeros** | The boundary conditions of a cylinder are expressed as zeros of $J_\nu$; the roots of $J_0$ are the drumhead modes |
| **Half-integer order** | $J_{1/2}(x) = \sqrt{2/(\pi x)}\sin x$ — spherical Bessel functions are elementary |

> The orthogonality and the zeros are what make the function useful: a function on a disc is expanded in $J_\nu$, and the boundary condition "the membrane is fixed at the rim" becomes "the radial function vanishes at a zero of $J_0$".

## Where it appears

| Field | The problem |
| --- | --- |
| **Heat conduction** | Temperature in a cylindrical rod or a cylinder with convective boundary |
| **Vibrations** | The modes of a circular membrane — the drumhead — and of a cylindrical shell |
| **Electromagnetics** | Waveguide modes, the field in a coaxial line, diffraction by a circular aperture |
| **Acoustics** | Radiation from a circular piston, scattering by a cylinder |
| **Quantum mechanics** | Partial-wave expansion, the spherical Bessel functions in scattering |
| **Fluid dynamics** | Stability of cylindrical flows, the Lamb–Oseen vortex profile in modified form |
| **Signal processing** | The Kaiser window and the Fourier–Bessel series |

## References

- [Bessel function](https://en.wikipedia.org/wiki/Bessel_function)
- Abramowitz, M., & Stegun, I. A. (1964). *Handbook of mathematical functions*. National Bureau of Standards. — series, asymptotics and tables
- Watson, G. N. (1922). *A treatise on the theory of Bessel functions*. Cambridge University Press. — the classical monograph
- [Gamma Function](/view.html?p=notes/epistemica/mathematical/mapping/gamma-function.md) — in the series coefficients
- [Lambert W Function](/view.html?p=notes/epistemica/mathematical/mapping/lambert-w-function.md) — the sibling inverse-flavoured special function
- [Logarithm](/view.html?p=notes/epistemica/mathematical/number/logarithm.md) — the elementary inverse the series builds on
