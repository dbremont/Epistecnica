---
tags: [note, mathematics, geometry]
---

# Fractal

> A **fractal** is a point set whose dimension exceeds its topological dimension: a curve that is not one-dimensional, a region that is not flat, a body that is not solid. Mandelbrot's definition is dimensional, not pictorial — the set is a fractal because measuring it demands a fractional exponent, not because it looks busy.

> What produces fractals is a different property: **self-similarity**, the set repeating its own form under magnification. Every exactly self-similar construction has a computable dimension, but not every self-similar set is a fractal — the straight line and the space-filling curve are the two ends that fall outside.

## Formulation

> **What it is.** The scale-invariant shape. A smooth curve resolves into a straight line under magnification; a fractal does not — magnify it and the same structure reappears, so no scale exists at which the detail is exhausted.
>
> **Type.** A `Concept` — a predicate on a point set, stated in the vocabulary of [measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md). It is not a figure kind: the rows that file fractal curves, regions and solids under [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md) are figures that *carry* the property, and the same set can be read as a smooth curve at one magnification and as a fractal at another.
>
> **Boundary.** The dimensional definition and the self-similar generator are not the same test, and sets pass one while failing the other. A space-filling curve — Hilbert's, Peano's, Moore's — is exactly self-similar and has integer dimension $2$, so it is not a fractal by the definition, yet the shape atlas files it among the fractal curves. A coastline is statistically self-similar but exhibits no exact copy of itself at any scale. The word is used for both, which is why "fractal" names a family of readings rather than a closed class.

## Defining properties

| Test | What it asserts | Satisfied by | Failed by |
| --- | --- | --- | --- |
| **Excess dimension** | the Hausdorff dimension is strictly greater than the topological dimension | Koch curve ($\log 4/\log 3$), Cantor dust, Sierpiński triangle, Menger sponge | a smooth curve, a disk, a ball; the space-filling curves, whose dimension is exactly $2$ |
| **Exact self-similarity** | the set is a finite union of copies of itself, each scaled by a fixed ratio | Koch curve, Cantor dust, Sierpiński triangle and carpet, Menger sponge | a coastline, a river network, the boundary of the Mandelbrot set |
| **Statistical self-similarity** | the distribution of form over a window is invariant in scale | coastlines, river networks, turbulence, diffusion-limited aggregation | any set that resolves under magnification |
| **No rectification** | no tangent at any point, so no finite length | Koch curve, Weierstrass function, Brownian path | any piecewise-smooth curve |

The last three are the ways a set becomes fractal; the first is what makes it one. A set is self-similar because of a rule that builds it, and fractal because of what that rule does to its measure — the two are linked by construction, not by definition.

## How they arise

| Mechanism | Rule | Instances |
| --- | --- | --- |
| **Recursive replacement** | every segment, triangle or cube is replaced by scaled copies of itself | Koch curve, Cantor dust, Sierpiński triangle and carpet, Menger sponge |
| **Iterated function system** | the attractor of a finite set of contractions | Cantor dust, Sierpiński triangle, dragon curve, Barnsley fern |
| **Escape-time iteration** | the parameter set for which an orbit stays bounded | [Mandelbrot set](/view.html?p=notes/epistemica/mathematical/change/mandelbrot-set.md), its [Julia sets](/view.html?p=notes/epistemica/mathematical/change/mandelbrot-set.md) |
| **Random growth** | a stochastic rule with no exact copy of the whole | diffusion-limited aggregation, Brownian trail, river networks |

The first two are the same object: an iterated function system is the rewriting rule stated in the language of maps, and its attractor is the limit of the replacement. Escape-time sets are different in kind — the fractal is a set of *parameters* or *initial conditions*, not a shape traced by the iteration, which is why the Mandelbrot set's own boundary is not a self-similar construction.

## Dimension

For an exactly self-similar set built from $N$ copies of itself, each scaled by the ratio $r$,

$$D = \frac{\log N}{\log(1/r)},$$

the exponent that makes the number of copies grow like the inverse scale raised to $D$. The formula is the exact computation; the Hausdorff dimension of an arbitrary set is defined by the measures that vanish or diverge at that exponent, and it coincides with the box-counting dimension for self-similar sets satisfying the open set condition.

| Set | Construction | Dimension |
| --- | --- | --- |
| Cantor dust | two copies at ratio $1/3$ | $\log 2/\log 3 \approx 0.631$ |
| Koch curve | four copies at ratio $1/3$ | $\log 4/\log 3 \approx 1.262$ |
| Sierpiński triangle | three copies at ratio $1/2$ | $\log 3/\log 2 \approx 1.585$ |
| Sierpiński carpet | eight copies at ratio $1/3$ | $\log 8/\log 3 \approx 1.893$ |
| Menger sponge | twenty copies at ratio $1/3$ | $\log 20/\log 3 \approx 2.727$ |

The values are what the dimension means: the Koch curve is more than a line but less than a plane, and the Cantor dust is more than a point and less than a line. The dimension is a *quantity* only because the [Hausdorff measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) turns it into one — the measure at exponent $D$ is finite and positive, and every other exponent gives zero or infinity.

Not every fractal dimension is fractional: the boundary of the Mandelbrot set has Hausdorff dimension $2$, and the Julia set of $z \mapsto z^2$ is the unit circle, dimension $1$. The definition asks for excess over the topological dimension, not for a fraction.

## Where they appear

- **In nature.** A coastline has no finite length — the measured length grows as the ruler shrinks, and the growth exponent is a fractal dimension. River networks, fracture surfaces, clouds and diffusion-limited aggregation are the same reading: a structure whose [power law](/view.html?p=notes/nature/construction/power-law.md) over scales is the signature of self-similarity. The constructions behind them are the stochastic processes of [Cellular Automata](/view.html?p=notes/epistemica/mathematical/change/cellular-automata.md).
- **In time series.** A persistent or anti-persistent series has a fractal dimension estimate, and the Hurst exponent — with detrended fluctuation analysis beside it — measures the same self-similarity in the time domain rather than in space ([Statistical Function](/view.html?p=notes/epistemica/observational/statistical-function.md)).
- **In networks.** A network is fractal when its box-counting over renormalised neighbourhoods follows a power law, which is how hierarchical, self-similar topologies are distinguished from random ones ([Network Science](/view.html?p=notes/epistemica/network/network-science.md)).

## References

- https://en.wikipedia.org/wiki/Fractal
- Mandelbrot, B. *How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension* (1967) — the paper that made the dimension measurable in nature.
- Falconer, K. *Fractal Geometry: Mathematical Foundations and Applications* — the standard treatment of Hausdorff and box dimension.
- [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md) — the figure rows that carry the property · [Dimension](/view.html?p=notes/epistemica/mathematical/structure/linear/dimension.md) — the overloaded word, and the vector-space sense this note does not use · [Hausdorff Measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) · [Mandelbrot Set](/view.html?p=notes/epistemica/mathematical/change/mandelbrot-set.md)
