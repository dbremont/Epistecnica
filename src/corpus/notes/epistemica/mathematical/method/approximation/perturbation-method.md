---
tags: [note, mathematics, method, technique, analytical]
---

# Perturbation Method

> A **perturbation method** solves a problem that has no closed form by expanding its solution in a small parameter, order by order: the unperturbed problem is solved exactly, and each correction solves a linear problem built from the previous orders.

## Formulation

> **What it is.** The routine of the small parameter. Write the solution as $x = x_0 + \varepsilon x_1 + \varepsilon^2 x_2 + \cdots$, substitute, and equate powers of $\varepsilon$; each order is a problem one step easier than the last.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** The expansion is asymptotic, not convergent: it approximates for small $\varepsilon$ and may diverge for any fixed $\varepsilon$. A *singular* perturbation — where the small parameter multiplies the highest derivative — breaks the naive expansion and needs boundary layers.

## Key results

- **Regular perturbation.** The expansion is uniformly valid; the error is $O(\varepsilon^{N+1})$ after $N$ orders.
- **Singular perturbation.** The limit $\varepsilon \to 0$ changes the order of the equation, so the solution develops a boundary layer; matched asymptotic expansions patch an inner and an outer solution.
- **Secular terms.** Naive expansion of an oscillator produces terms growing without bound; multiple-scale analysis removes them by letting the amplitude depend on a slow time.
- **WKB.** For $\varepsilon y'' + q(x)y = 0$ the expansion is exponential, not polynomial — the method's most important variant.
- **Adjoint solvability.** At each order, solvability requires the correction to be orthogonal to the null space of the adjoint — the Fredholm alternative appearing inside the routine.

## References

- Strutt, J. W. (1877). *The theory of sound* (Vol. 1). Macmillan. — the perturbation of a frequency, before the method had a name
- Lindstedt, A. (1882). Beitrag zur Integration der Differentialgleichungen der Störungstheorie. *Astronomische Nachrichten*, 100, 137–150. — the strained coordinate that removes secular terms
- Poincaré, H. (1892–1899). *Les méthodes nouvelles de la mécanique céleste* (Vols. 1–3). Gauthier-Villars. — the asymptotic series made an object of analysis
- Fredholm, I. (1903). Sur une classe d'équations fonctionnelles. *Acta Mathematica*, 27, 365–390. — the alternative that governs solvability at each order
- Jeffreys, H. (1925). On certain approximate solutions of linear differential equations of the second order. *Proceedings of the London Mathematical Society*, s2-23(1), 428–436. — the exponential ansatz behind WKB
- van der Pol, B. (1926). On relaxation-oscillations. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 2(11), 978–992. — the oscillator that made nonlinear perturbation a subject
- Krylov, N., & Bogolyubov, N. (1943). *Introduction to non-linear mechanics* (S. Lefschetz, Trans.). Princeton University Press. (Original work published 1937) — averaging, stated as a method
- Stoker, J. J. (1950). *Nonlinear vibrations in mechanical and electrical systems*. Interscience. — the engineering statement of the same techniques
- Friedrichs, K. O. (1955). Asymptotic phenomena in mathematical physics. *Bulletin of the American Mathematical Society*, 61(6), 485–504. — the singular case stated as a general problem
- Erdélyi, A. (1956). *Asymptotic expansions*. Dover. — the analysis the expansions rest on
- Kaplun, S. (1957). Low Reynolds number flow past a circular cylinder. *Journal of Mathematics and Mechanics*, 6(5), 595–603. — the matched expansion and the inner-outer split
- Proudman, I., & Pearson, J. R. A. (1957). Expansions at small Reynolds numbers for the flow past a sphere and a circular cylinder. *Journal of Fluid Mechanics*, 2(3), 237–262. — the same boundary layer, worked out
- Bogoliubov, N. N., & Mitropolsky, Y. A. (1961). *Asymptotic methods in the theory of non-linear oscillations*. Gordon and Breach. — averaging and multiple scales systematised
- Van Dyke, M. (1964). *Perturbation methods in fluid mechanics*. Academic Press. — the matching rules as a working manual
- Wasow, W. (1965). *Asymptotic expansions for ordinary differential equations*. Interscience. — what the expansions are, as mathematics
- Cole, J. D. (1968). *Perturbation methods in applied mathematics*. Blaisdell. — the strained coordinate made general
- Nayfeh, A. H. (1973). *Perturbation methods*. Wiley. — the earlier of the two Nayfeh texts: a catalogue by technique
- Olver, F. W. J. (1974). *Asymptotics and special functions*. Academic Press. — the asymptotics of the special functions the expansions produce
- Bender, C. M., & Orszag, S. A. (1978). *Advanced mathematical methods for scientists and engineers*. McGraw-Hill. — the textbook that taught the generation after 1978
- de Bruijn, N. G. (1981). *Asymptotic methods in analysis*. Dover. (Original work published 1958) — the analysis of asymptotics, rather than the recipes
- [Nayfeh, A. H. (1981). *Introduction to perturbation techniques*. Wiley.](/view.html?p=documents/books/nayfeh-1981-introduction-to-perturbation-techniques-wiley.md) — the techniques catalogue: strained coordinates, multiple scales, averaging, matched expansions
- Hinch, E. J. (1991). *Perturbation methods*. Cambridge University Press. — the modern short course, matching included
- O'Malley, R. E. (1991). *Singular perturbation methods for ordinary differential equations*. Springer. — the initial-layer and boundary-layer theory
- Holmes, M. H. (1995). *Introduction to perturbation methods*. Springer. — the graduate text, with the worked cases
- Kevorkian, J., & Cole, J. D. (1996). *Multiple scale and singular perturbation methods*. Springer. — multiple scales in full
- Verhulst, F. (2005). *Methods and applications of singular perturbations*. Springer. — the boundary-layer method as a coherent account
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos* (2nd ed.). Westview Press. — averaging and multiple scales in the dynamical-systems idiom
- https://en.wikipedia.org/wiki/Perturbation_theory
- [Asymptotic Analysis](asymptotic-analysis.md) · [Linearization](../reduction/linearization.md) · [Stationary Phase](stationary-phase.md) · [Differential Equation](../../change/differential-equation.md)
- [Asymptotics and perturbation methods - Prof. Steven Strogatz](https://www.youtube.com/playlist?list=PL5EH0ZJ7V0jV7kMYvPcZ7F9oaf_YAlfbI)
- [Perturbation Methods](https://www.youtube.com/playlist?list=PLcYq2buGaQDma0UeqiM860DxRSS7b0jOm)

