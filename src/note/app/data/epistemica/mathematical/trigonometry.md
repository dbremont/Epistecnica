---
tags: [framework]
---

# Trigonometry

 : Geometry (Geometry%201acc0f5171ec809ab11ad964fbff6df1.md), Angle (Angle%20178c0f5171ec808fac84f62329514e7a.md), Euclidean  Geometry (Euclidean%20Geometry%20858b34433a204b55bb716919101bdcc6.md), Harmonic Analysis (Harmonic%20Analysis%201bbc0f5171ec8015a56bc2d92c1438a9.md), Complex Numbers (ℂ) (Complex%20Numbers%20(%E2%84%82)%20176c0f5171ec809eb4aff09a9448e3f1.md)

> **Trigonometry** is the **branch of mathematics** that studies the relationships between the **angles and sides of triangles**, particularly **right triangles**, and more generally, the properties of **periodic functions** related to angles. It provides **tools and formulas**—such as sine, cosine, tangent, their inverses, and related identities—to solve **geometric, algebraic, and analytic problems involving angles, distances, and periodic phenomena**.
> 

> **Trigonometry:** `Angle Problem * Technique → Result`.
> 

## Etymology

- **Origin:** The word *trigonometry* comes from the **Greek** words:
    - **τρίγωνον (trígonon)** meaning "**triangle**"
        
        — from **τρία (tría)** meaning "three"
        
        — and **γωνία (gōnía)** meaning "angle" or "corner"
        
    - **μετρία (metría)** meaning "**measurement**"
- **Literal meaning:**
    
    **"Measurement of triangles"**
    

## Formulation

> 

| **Method** | **Description** |
| --- | --- |
| **Geometric Definition** | Define trig functions as ratios of sides in a right triangle |
| **Unit Circle Definition** | Define trig functions as coordinates on the unit circle |
| **Series Definition** | Define trig functions via their Taylor or Maclaurin power series |
| **Differential Equation** | Define as solutions to certain ODEs |
| **Complex Exponential** | Define using Euler's formula linking exponentials to trig functions |
| **Integral Definition** | Define trig functions via integrals |
| **Functional Equations** | Define via identities and properties |
| **Limit Definition** | Define trig functions as limits of sequences or functions |

## Measure

> How angles are measure?
> 

| Measure | **Description** |
| --- | --- |
| Degrees | A unit of measurement for angles, where a full circle is divided into 360 equal parts. |
| Radians | A unit of measurement for angles based on the radius of a circle, where a full circle is \(2\pi\) radians. |
| Gradians | A unit of measurement for angles, where a full circle is divided into 400 equal parts. |
| Milliradians | A unit of angular measurement equal to one-thousandth of a radian, often used in military and engineering. |
| Turns | A unit of measurement where a full circle is one turn, often expressed as fractions or multiples of a turn. |
| Binary Degrees (brads) | A unit of angular measurement used in digital systems, dividing a circle into 256 equal parts. |
| Hours, Minutes, Seconds | Used primarily in astronomy, where angles are measured in terms of time with one full circle equal to 24 hours. |
| Compass Bearings | Angles measured clockwise from the north direction, used in navigation and mapping. |
| Azimuth | The angle between the north direction and the projection of the vector to the point of interest onto the horizontal plane. |
| Zenith Distance | The angle between the zenith direction (directly overhead) and the line to the object. |
| Altitude | The angle above the horizon, used in navigation and astronomy. |
| Slope Angle | The angle of inclination, often used in geology, civil engineering, and architecture. |

## Function

> **Trigonometric functions** are mathematical functions that relate the angles of a triangle to the lengths of its sides, commonly including sine, cosine, and tangent.
> 

> **Characterization:** Domain, Range, Periodicity, Symmetry, Phase Shift, …, etc.
> 

### Taxonomy

| **Type** | **Function** | **Name** | **Definition** |
| --- | --- | --- | --- |
| Circular | `sin(x)` | Sine | Opposite / Hypotenuse |
|  | `cos(x)` | Cosine | Adjacent / Hypotenuse |
|  | `tan(x)` | Tangent | `sin(x) / cos(x)` |
|  | `csc(x)` | Cosecant | `1 / sin(x)` |
|  | `sec(x)` | Secant | `1 / cos(x)` |
|  | `cot(x)` | Cotangent | `cos(x) / sin(x)` |
| Hyperbolic | `sinh(x)` | Hyperbolic Sine | `(e^x - e^-x)/2` |
|  | `cosh(x)` | Hyperbolic Cosine | `(e^x + e^-x)/2` |
|  | `tanh(x)` | Hyperbolic Tangent | `sinh(x) / cosh(x)` |
|  | `csch(x)` | Hyperbolic Cosecant | `1 / sinh(x)` |
|  | `sech(x)` | Hyperbolic Secant | `1 / cosh(x)` |
|  | `coth(x)` | Hyperbolic Cotangent | `cosh(x) / sinh(x)` |
| Inverse | `arcsin(x)` | Inverse Sine | — |
|  | `arccos(x)` | Inverse Cosine | — |
|  | `arctan(x)` | Inverse Tangent | — |
|  | `arccsc(x)` | Inverse Cosecant | — |
|  | `arcsec(x)` | Inverse Secant | — |
|  | `arccot(x)` | Inverse Cotangent | — |
| Inverse Hyperbolic | `arsinh(x)` | Inverse Hyperbolic Sine | `ln(x + √(x² + 1))` |
|  | `arcosh(x)` | Inverse Hyperbolic Cosine | `ln(x + √(x² - 1))` |
|  | `artanh(x)` | Inverse Hyperbolic Tangent | `0.5 * ln((1 + x) / (1 - x))` |
|  | `arcsch(x)` | Inverse Hyperbolic Cosecant | `ln(1/x + √(1 + x⁻²))` |
|  | `arsech(x)` | Inverse Hyperbolic Secant | `ln((1 + √(1 - x²))/x)` |
|  | `arcoth(x)` | Inverse Hyperbolic Cotangent | `0.5 * ln((x + 1)/(x - 1))` |
| Circular Derived | `versin(x)` | Versine | `1 - cos(x)` |
|  | `coversin(x)` | Coversine | `1 - sin(x)` |
|  | `vercosin(x)` | Vercosine | `1 + cos(x)` |
|  | `covercosin(x)` | Covercosine | `1 + sin(x)` |
|  | `haversin(x)` | Haversine | `(1 - cos(x)) / 2` |
|  | `hacoversin(x)` | Hacoversine | `(1 - sin(x)) / 2` |
|  | `exsec(x)` | Exsecant | `sec(x) - 1` |
|  | `excsc(x)` | Excosecant | `csc(x) - 1` |

### Identity

> Note: We need to prove each identity.
> 

| **Category** | **Identity** | **Expression** |
| --- | --- | --- |
| **Reciprocal Identities** | $csc(x)$ | $\frac{1}{\sin(x)}$ |
|  | $\sec(x)$ | $\frac{1}{\cos(x)}$ |
|  | $\cot(x)$ | $\frac{1}{\tan(x)} = \frac{\cos(x)}{\sin(x)}$ |
| **Pythagorean Identities** | $\sin^2(x) + \cos^2(x)$ | 11 |
|  | $1 + \tan^2(x)$ | $\sec^2(x)$ |
|  | $1 + \cot^2(x)$ | $\csc^2(x)$ |
| **Even–Odd Identities** | $\sin(-x)$ | $-\sin(x)$ |
|  | $\cos(-x)$ | $\cos(x)$ |
|  | $\tan(-x)$ | $-\tan(x)$ |
|  | $\csc(-x)$ | $-\csc(x)$ |
|  | $\sec(-x)$ | $\sec(x)$ |
|  | $\cot(-x)$ | $-\cot(x)$ |
| **Co-Function Identities** | $\sin\left(\frac{\pi}{2} - x\right)$ | $\cos(x)$ |
|  | $\cos\left(\frac{\pi}{2} - x\right)$ | $\sin(x)$ |
|  | $\tan\left(\frac{\pi}{2} - x\right)$ | $\cot(x)$ |
|  | $\csc\left(\frac{\pi}{2} - x\right)$ | $\sec(x)$ |
|  | $\sec\left(\frac{\pi}{2} - x\right)$ | $\csc(x)$ |
|  | $\cot\left(\frac{\pi}{2} - x\right)$ | $\tan(x)$ |
| **Sum & Difference** | $\sin(a \pm b)$ | $\sin(a)\cos(b) \pm \cos(a)\sin(b)$ |
|  | $\cos(a \pm b)$ | $\cos(a)\cos(b) \mp \sin(a)\sin(b)$ |
|  | $\tan(a \pm b)$ | $tan⁡(b)\frac{\tan(a) \pm \tan(b)}{1 \mp \tan(a)\tan(b)}$ |
| **Double Angle** | $\sin(2x)$ | $2\sin(x)\cos(x)$ |
|  | $\cos(2x)$ | $\cos^2(x) - \sin^2(x) = 2\cos^2(x) - 1 = 1 - 2\sin^2(x)$ |
|  | $\tan(2x)$ | $\frac{2\tan(x)}{1 - \tan^2(x)}$ |
|  | $cos(2x)$ | $cos(2θ)= \frac{e^{i2θ}+e^{−i2θ}}{2}$. |
| **Half-Angle** | $\sin^2(x)$ | $\frac{1 - \cos(2x)}{2}$ |
|  | $\cos^2(x)$ | $\frac{1 + \cos(2x)}{2}$ |
|  | $\tan\left(\frac{x}{2}\right)$ | $\frac{\sin(x)}{1 + \cos(x)} = \frac{1 - \cos(x)}{\sin(x)}$ |
| **Product-to-Sum** | $\sin(a)\sin(b)$ | $\frac{1}{2}[\cos(a - b) - \cos(a + b)]$ |
|  | $\cos(a)\cos(b)$ | $\frac{1}{2}[\cos(a - b) + \cos(a + b)]$ |
|  | $\sin(a)\cos(b)$ | $\frac{1}{2}[\sin(a + b) + \sin(a - b)]$ |
| **Sum-to-Product** | $\sin(a) + \sin(b)$ | $2\sin\left(\frac{a + b}{2}\right)\cos\left(\frac{a - b}{2}\right)$ |
|  | $\sin(a) - \sin(b)$ | $2\cos\left(\frac{a + b}{2}\right)\sin\left(\frac{a - b}{2}\right)$ |
|  | $\cos(a) + \cos(b)$ | $2\cos\left(\frac{a + b}{2}\right)\cos\left(\frac{a - b}{2}\right)$ |
|  | $\cos(a) - \cos(b)$ | $-2\sin\left(\frac{a + b}{2}\right)\sin\left(\frac{a - b}{2}\right)$ |
| **Euler's Formula** | $e^{ix}$ | $\cos(x) + i\sin(x)$ |
| **De Moivre’s Theorem** | $(\cos x + i \sin x)^n$ | $\cos(nx) + i \sin(nx)$ |
| **Tangent Sum of Arcs** | $\tan^{-1}(x) + \tan^{-1}(y)$ | $\tan^{-1}\left( \frac{x + y}{1 - xy} \right)$ |
| **Weierstrass Substitution** | $\tan\left(\frac{x}{2}\right) = t$ | $\sin x = \frac{2t}{1 + t^2},\ \cos x = \frac{1 - t^2}{1 + t^2}$ |
| **Chebyshev Identity** | $\cos(n\theta)$ | $T_n(\cos\theta)$ |
| **Napier’s Analogies** | $\tan\left(\frac{A \pm B}{2}\right)$ | $\frac{\sin(A \pm B)}{\cos A + \cos B}$ |
| **Trig Sum Formula (Complex)** | $\sum_{k=0}^{n-1} \cos\left(x + \frac{2\pi k}{n}\right)$ | 00 |
| **Sum of Sines** | $\sum_{k=1}^n \sin(kx)$ | $\frac{\sin\left(\frac{nx}{2}\right)\sin\left(\frac{(n+1)x}{2}\right)}{\sin\left(\frac{x}{2}\right)}$ |
| **Sum of Cosines** | $\sum_{k=1}^n \cos(kx)$ | $\frac{\sin\left(\frac{nx}{2}\right)\cos\left(\frac{(n+1)x}{2}\right)}{\sin\left(\frac{x}{2}\right)}$ |
| **Dirichlet Kernel (Fourier)** | $\sum_{k=-n}^{n} e^{ikx}$ | $\frac{\sin((n + \frac{1}{2})x)}{\sin(\frac{x}{2})}$ |
| **Triple Angle** | $\sin(3x)$ | $\sin(x) - 4\sin^3(x)$ |
|  | $\cos(3x)$ | $\cos^3(x) - 3\cos(x)$ |
| **Universal Identity** | $\sin^2(x) + \cos^2(x) = 1$ | $\Rightarrow \forall x,\ \exists t: \sin x = \frac{2t}{1 + t^2}$ |
| **Lagrange’s Identity** | $\tan^2 x + 1 = \sec^2 x$ | $\sin^2 x + \cos^2 x = 1$ |
| **Half-Angle Substitution** | $\sin(x)$ | $\frac{2\tan(x/2)}{1 + \tan^2(x/2)}$ |
|  | $\cos(x)$ | $\frac{1 - \tan^2(x/2)}{1 + \tan^2(x/2)}$ |
| **Ramanujan’s Identity** | $\cos(\pi/5)$ | $\frac{\sqrt{5} + 1}{4}$ |
| **Symmetry** | $\sin(n\pi + x)$ | $(-1)^n \sin(x)$ |

### Trigonometric Function Decomposition

> Other Ways to represent trigonometric functions.
> 

> See more in [**Polynomial**](polynomial.md), …
> 

| Representation | Formula | Use |
| --- | --- | --- |
| **Power series / binomial** | $\cos(x) = \sum (-1)^n x^{2n}/(2n)!$ | Exact series, combinatorial interpretation |
| **Binomial in multiple-angle** | $\cos(n\theta) = \sum (-1)^k \binom{n}{2k} \cos^{n-2k} \sin^{2k}$ | Multiple-angle expansion |
| **Chebyshev polynomials** | $\cos(n\theta) = T_n(\cos\theta)$ | Polynomial in cos⁡θ\cos\theta, numerical approximation |
| **Exponential / Euler** | $e^{i\theta} = \cos\theta + i \sin\theta$ | Simplifies sums/products of trig functions |
| **Hypergeometric** | $\cos(x) = {}_0F_1(;1/2;-x^2/4)$ | Advanced analytical representation |

## Representation Capacity

> aka .Use.
> 

| **Modeling Capacity** | **Abstract Description** | **Representative Domains** |
| --- | --- | --- |
| **Periodic Structure Modeling** | Representing cyclic, repeating patterns and oscillations | Signal processing, wave physics, biology |
| **Rotational & Angular Dynamics** | Modeling rotations, orientations, and angular relationships | Robotics, kinematics, computer graphics |
| **Spatial & Geometric Relations** | Encoding distances, angles, and shapes in various geometries | Surveying, architecture, computational geometry |
| **Harmonic Decomposition** | Decomposing complex phenomena into fundamental frequency components | Fourier analysis, communications, acoustics |
| **Curvature-Dependent Metrics** | Describing geometric properties on curved spaces | Spherical/hyperbolic geometry, cosmology |
| **Force & Motion Interaction** | Modeling vector forces and periodic motions | Mechanical engineering, dynamics |
| **Wavefunction Representation** | Expressing states and probabilities in wave-based systems | Quantum mechanics, optics |
| **Temporal Biological Cycles** | Capturing rhythmic physiological and ecological processes | Chronobiology, neuroscience |
| **Celestial and Orbital Mechanics** | Predicting positions and motions in gravitational fields | Astronomy, aerospace engineering |
| **Acoustic and Vibrational Patterns** | Modeling propagation and resonance of sound and vibrations | Acoustics, audio engineering |

## Case Study

| **Problem** | **Time Period & Person** | **Description & Significance** |
| --- | --- | --- |
| **Building the Great Pyramid of Giza** | ~2560 BCE, Ancient Egyptians | While not explicitly recorded, the pyramid’s precise slope angles imply early use of geometric and trig-like ratios to achieve architectural perfection. |
| **Measuring the Earth’s Circumference** | ~240 BCE, **Eratosthenes** | Using shadows and angles of sunlight in two cities, Eratosthenes estimated Earth’s circumference with remarkable accuracy, applying basic trig reasoning with angle measurement. |
| **Astronomical Models and Planetary Positions** | 2nd century CE, **Hipparchus** | Often called the “father of trigonometry,” Hipparchus created the first known trig table and used spherical trigonometry to model celestial motions and predict eclipses. |
| **Navigation and Latitude Determination** | 15th-16th century, Age of Exploration | Mariners used sextants and trig functions of measured angles between horizon and stars to find their latitude, enabling safer and more accurate ocean voyages. |
| **Surveying and Land Division** | Ancient and Medieval Times | Early cadastral surveys used triangles and trig ratios to measure land boundaries accurately — critical for taxation and property rights. |
| **Calculating Distances to the Moon and Sun** | 17th century, **Isaac Newton** & contemporaries | Using angular measurements and parallax, trigonometric calculations helped estimate astronomical distances, fundamental for celestial mechanics. |
| **Solving the “Lighthouse Problem”** | 18th century, Practical Navigation | Given the angle between two lighthouses as seen from a ship, trig laws help determine the ship’s position — an essential problem for coastal navigation. |
| **Sound and Wave Analysis** | 18th-19th centuries, **Joseph Fourier** | Fourier’s work decomposing complex vibrations into sine waves revolutionized physics, acoustics, and engineering by applying trigonometric series. |
| **Designing Telescopes and Optics** | 17th-19th centuries | Trig was used to calculate angles of reflection and refraction to design lenses and mirrors with precise curvatures for optimal focus. |
| **The Construction of the Panama Canal** | Early 20th century | Surveyors used trigonometric methods extensively to measure and level land, crucial for this massive engineering feat. |

## QA

- Can we define the notion of trigonometric functions in other spaces—such as non-Euclidean geometries?

### Can we define the notion of trigonometric functions in other spaces—such as non-Euclidean geometries?

> **Ttrigonometric functions can be defined and generalized in other geometric spaces**, including **non-Euclidean geometries**. The nature of these trig functions and their relationships change depending on the underlying geometry. Here’s a detailed explanation:
> 

| **Geometry Type** | **Key Idea** | **Trig Functions / Laws** | **Notes** |
| --- | --- | --- | --- |
| **Euclidean Geometry** | Flat plane with zero curvature | Classical trig functions | Standard trigonometry taught in school; angles and distances behave as expected. |
| **Spherical Geometry** (Positive curvature) | Geometry on the surface of a sphere | Spherical trig functions, e.g., spherical sine and cosine laws | Sides of triangles are arcs of great circles; angles sum to > 180°; laws modify classical trig (Napier’s rules). Used in astronomy, navigation. |
| **Hyperbolic Geometry** (Negative curvature) | Saddle-shaped geometry | Hyperbolic trig functions | Angles of triangles sum to < 180°; distance and angle relations involve hyperbolic functions. Crucial in modern geometry, relativity. |
| **Elliptic Geometry** (Closed, no parallel lines) | Like spherical but without antipodal points identified | Similar trig functions to spherical geometry, with variations | Used in some cosmological models and theoretical physics. |
| **General Riemannian Geometry** | Curved spaces with varying curvature | Trigonometric relations generalized using metric tensors | Trig functions generalized via Jacobi fields, comparison theorems, etc. |

## References

- https://en.wikipedia.org/wiki/Trigonometry
- https://en.wikipedia.org/wiki/Trigonometric_tables
- https://en.wikipedia.org/wiki/Trigonometric_functions
- https://en.wikipedia.org/wiki/Trigonometric_functions
- https://en.wikipedia.org/wiki/List_of_trigonometric_identities
- https://en.wikipedia.org/wiki/Trigonometric_series
- https://en.wikipedia.org/wiki/Trigonometric_substitution
- https://en.wikipedia.org/wiki/Generalized_trigonometry
- https://en.wikipedia.org/wiki/Trigonometric_tables
- https://en.wikipedia.org/wiki/Proofs_of_trigonometric_identities
- [Wave](https://app.notion.com/p/Wave-abe8be3df7354f11a8e84fa436de2e0b?pvs=21)
