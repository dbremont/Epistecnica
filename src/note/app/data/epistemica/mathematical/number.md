---
tags: [quantity]
---

# Number

 : Complex Numbers (ℂ) (Complex%20Numbers%20(%E2%84%82)%20176c0f5171ec809eb4aff09a9448e3f1.md), Quaternions (Quaternions%201e4c0f5171ec807ab0bdcdb8d0b798ec.md), Octonions (Octonions%201e4c0f5171ec80eca8beeba4c6e2d59c.md), Dual Number (Dual%20Number%201e4c0f5171ec8042a788dc7fe662fcda.md), Hyperreal Number (Hyperreal%20Number%201e4c0f5171ec8059b7a4c8e52b963740.md), Numeric System (Numeric%20System%201d6c0f5171ec80899160d6587a6a9e3e.md)

> In this note we will explore the powerful ideas of numbers — specially the **counting numbers**.
> 

> Numbers and numeral systems are **representational mechanisms**—similar to signs, symbols, and pictograms—that humans use to represent and reason about the **quantitative properties of reality**.
> 

> A **number** must not be conflated with the symbolic forms used to represent it (e.g., **V**, **5**, **|||||**, etc.). These are merely numerals—conventional notational systems—whereas the number itself is an abstract **epistemic object — abstracting a property (or representation mechanism)  of a segment of reality**.
> 

> (Co Boostraping, Co Evolution) Number concepts and their representations co-evolve: each provides the means through which the other is conceptualized, refined, and extended. A number is an abstract representation of a quantifiable property or abstraction of reality; yet what counts as quantifiable is itself partly determined by the possibility of representing that property through numerals. Thus, the concepts of number, quantification, and numeral representation develop through a recursive relationship in which each helps define and extend the others.
> 

```bash
Reality or (Symbolic World)
   ↓
Abstraction
   ↓
Representation Role: Quantitative Property, etc
   ├── Cardinality
   ├── Length
   ├── Mass
   ├── Duration
   ├── Area
   ├── Volume
   └── Magnitude
   └── Rotation
   ↓
Number (Abstract Quantitative Concept)
   ├── Natural Number
   ├── Integer
   ├── Rational Number
   ├── Irrational Number
   ├── Real Number
   ├── Complex Number
   ├── Quaternions
   └── etc
   ↓
Numeral  (Concrete Representation)
   ├── "5"        (Arabic numeral)
   ├── "V"        (Roman numeral)
   ├── "|||||"    (tally representation)
   └── "five"     (word representation)
```

## Formulation: Cardinality → Counting (Natural) Number

> Let us formalize the concept of **counting numbers**.
> 

> In this note, we will use cardinality—the property underlying counting—to develop an understanding of the concept of number.
> 

> A number is an abstract entity. In its most elementary form, an integer serves to represent the **cardinality** (size) of a set. That is, a number ( x ) can denote the size property shared by two distinct sets, provided those sets are equinumerous (i.e., they have the same number of elements).
> 

> A counting number represents the **cardinality** of a finite set. Two sets have the same cardinality if and only if there exists a **bijection** between them.
> 

> Cardinality can be understood via **equivalence classes**: we partition the class of all finite sets into equivalence classes under the relation of bijective correspondence. Each equivalence class contains all sets that have the same number of elements.
> 

> A counting number (e.g., 1, 2, 3, …) is then a **symbol assigned to one such equivalence class**. The numeral system used to represent that class—Indo-Arabic, Mayan, Roman, etc.—is merely a **conventional symbolic representation** of the same abstract cardinal number.
> 

> A **numeral** is a **symbolic** or **structural** entity within a formal system, representing an abstraction of quantity, order, or measure, and equipped with defined operations and relations. In fact, it is the operations that unify the concept of numbers, providing an underlying unifying perspective.
> 

Notes:

- The underlying concept (the cardinal number) is independent of the representation.
- A subtle technical point: the collection of all finite sets is a proper class, not a set, so the equivalence classes are also proper classes. In practice, this is handled by choosing a canonical representative from each class (e.g., the von Neumann ordinals) or by using a foundational trick (like Scott’s trick) to turn them into sets. But for an intuitive or introductory explanation, the description you gave is perfectly fine.

### Role

> A number is not primarily a concrete epistemic artifact or merely an epistemic blueprint.
> 

> It is better understood as an **epistemic operator - epistemic blueprint**: a symbolic mechanism that enables agents to perform **structured assignments** of quantitative identity, magnitude, relation, or order onto state, phenomena (reality) through **reproducible procedures**. That the procedure determines the type of numbers.
> 

> The numeral itself (e.g., “5”) is only the visible symbolic token. The deeper significance of number lies in the operational process that maps aspects of reality into a formal quantitative regime.
> 

> Note: The differences between numbers arise from what they denote—such as magnitude, order, count, or other properties—while still sharing a common underlying concept.
> 

### Why do humans use counting numbers instead of coarse-grained linguistic descriptions?

> Basically Resolution, Fine-Grained, and Precision.
> 
- One major epistemic advantage of numerical systems over qualitative linguistic terms such as “many,” “few,” or “large” is their effectively unbounded **discriminative granularity**.
- Linguistic quantifiers partition reality into coarse semantic categories. Numerical systems, by contrast, permit arbitrarily fine differentiation through scalable symbolic extension.

## **Numeric Cognition Development**

> See more in [Numerical Cognition](https://app.notion.com/p/Numerical-Cognition-176c0f5171ec801c954cd4c7e71c4004?pvs=21) and [Cognitive Development](https://app.notion.com/p/Cognitive-Development-24cc0f5171ec80859297ef1b49f84740?pvs=21).
> 

> **(aka Abstraction Path Dependency)**
> 

> aka. How the reference system has developed?
> 
- **Words (qualitative)**: Used to reference or characterize the size of collections (e.g., "many," "few," "some").
- **Specific Numbers (contextual numerals)**: Symbols typically associated with a particular type of collection or measurement (e.g., "3 apples," "7 days").
- **Abstract Numbers (decontextualized numerals)**: General numerical symbols not tied to any specific measurement system or type of collection. The significance of **symbols** for **numbers** lies primarily in their ability to embody the concept of an **abstract number** in a simple and general form.
- **Operations (relational abstraction)**: Mathematical operations are abstractions of real-world operations or relationships between **concrete collections** (e.g., combining, partitioning, comparing).

## How to conceptualize numbers?

Philosophically, numbers pose intriguing questions:

- **Platonism:** Views numbers as abstract, non-physical entities existing independently of human thought.
- **Formalism:** Treats numbers as symbols manipulated according to formal rules, devoid of inherent meaning.
- **Constructivism:** Asserts that numbers are mental constructions, only meaningful if they can be constructed or computed.

## Number Type

### Traditional

| **Type** | **Symbol** | **Description** | **Instance(s)  (Indo-Arabic Representation Form)** |
| --- | --- | --- | --- |
| **Natural Numbers** | $\mathbb{N}$ | Positive whole numbers (1, 2, 3, ...) | $1, 2, 3$ |
| **Whole Numbers** | - | Natural numbers including zero | $0, 1, 2, 3$ |
| **Integers** | $\mathbb{Z}$ | Whole numbers and their negatives | -3, -2, -1, 0, 1, 2, 3 |
| **Rational Numbers** | $\mathbb{Q}$ | Numbers that can be written as fractions | $\frac{1}{2}, 3, -\frac{4}{5}$ |
| **Irrational Numbers** | - | Numbers that cannot be written as fractions | $π,2,e\pi, \sqrt{2}, e$ |
| **Real Numbers** | $\mathbb{R}$ | All rational and irrational numbers | $π,2,−5\pi, 2, -5$ |
| **Complex Numbers** | $\mathbb{C}$ | Numbers of the form $a + bi$, where $i^2 = -1$ | $3+4i,−2−i3 + 4i, -2 - i$ |
| **Algebraic Numbers** | - | Roots of polynomials with integer coefficients | $\sqrt{2}, \omega$ |
| **Transcendental Numbers** | - | Numbers that are not algebraic | $π,e\pi, e$ |
| **Prime Numbers** | - | Natural numbers greater than 1, divisible only by 1 and itself | 2, 3, 5, 7 |
| **Composite Numbers** | - | Non-prime natural numbers | 4, 6, 8, 9, 10 |

### Extension

> The **real numbers** $(\mathbb{R})$ from the foundation of most everyday mathematics, representing quantities such as lengths, areas, and time. However, to model a wider range of mathematical and physical phenomena, the real number system is extended in several ways, introducing new types of numbers that go beyond the familiar realm of real numbers.
> 

| **Extension** | **Description** | **Useful In** | **Key Feature** |
| --- | --- | --- | --- |
| **Complex Numbers** | Extends real numbers to include a real part and an imaginary part. | Algebra, physics, signals | Imaginary unit i |
| **Quaternions** | Extends complex numbers to four dimensions with one real part and three imaginary parts. | 3D geometry, graphics, control systems | 4D + rotation |
| **Octonions** | Extends quaternions to eight dimensions, including one real part and seven imaginary parts. | Theoretical physics | 8D + exotic symmetry |
| **p-adic Numbers** | Extends rational numbers using a different norm based on prime numbers. | Number theory, cryptography | Prime-based arithmetic |
| **Dual Numbers** | Extends real numbers with an element ϵ\epsilon where $\epsilon^2 = 0$. | Automatic differentiation | Infinitesimal changes |
| **Hyperreals** | Extends real numbers to include infinitesimals and infinite numbers used in non-standard analysis. | Nonstandard calculus | Infinitesimals and infinities |
| **Surreal Numbers** | A generalization of real numbers that includes infinitesimal and infinite quantities. | Game theory, ordinal analysis | Ultimate generalization |
| **Gaussian Integers** | Complex numbers where both real and imaginary parts are integers. | Number theory, lattice theory | Integer real and imaginary parts |
| **Eisenstein Integers** | Complex numbers of the form $a + b\omega$ where $\omega$ is a cube root of unity. | Number theory, algebraic geometry | Cube roots of unity |
| **Sedenions** | Extends octonions to sixteen dimensions, losing both commutativity and associativity. | Theoretical physics, algebra | 16D + non-associativity |
| **Superreal Numbers** | Extends the real numbers to include additional infinitesimal and infinite elements. | Nonstandard analysis, logic | Infinitesimals and infinities |
| **Hypercomplex Numbers** | General term for extensions of complex numbers, including quaternions and octonions. | Algebra, physics, computer science | Higher-dimensional extensions |
| **Geometric Algebra** | A combination of algebra and geometry used to express rotations and transformations. | Physics, robotics, graphics | Algebra + geometry |

## Numeral Representation System

> Which types of numeral systems are used to represent different types of numbers?
> 

> See more in [Numeric System](numeric-system.md).
> 

| **Symbol System / Numeral System** | **Number Type(s)** | **Description** |
| --- | --- | --- |
| **Unary numerals** | Natural numbers | Represents a number by repeating one symbol: ` |
| **Decimal positional system** | Natural, integer, rational, real numbers | Base-10 positional notation using `0–9`; e.g. `125`, `−12`, `3.75`. |
| **Binary positional system** | Natural, integer, rational, real numbers | Base-2 notation using `0,1`; fundamental for digital computation: `1011₂ = 11`. |
| **Octal positional system** | Natural, integer, rational numbers | Base-8 notation using `0–7`; historically/common in computing. |
| **Hexadecimal positional system** | Natural, integer, rational numbers | Base-16 notation using `0–9,A–F`; common in computing. |
| **Other positional systems (base-*b*)** | Natural, integer, rational, real numbers | General positional representation in any base `b ≥ 2`. |
| **Signed numeral system** | Integers | Extends magnitude notation with a sign, e.g. `+7`, `−7`. |
| **Fractional notation** | Rational numbers | Represents a rational number as a ratio of integers: `3/4`, `−7/2`. |
| **Decimal-fraction notation** | Rational, real numbers | Represents fractions using a decimal point: `0.75`, `−2.125`. |
| **Repeating-decimal notation** | Rational numbers | Represents rational numbers whose decimal expansion repeats: `1/3 = 0.333…`. |
| **Scientific notation** | Real numbers | Represents numbers as `a × 10ⁿ`, e.g. `6.02 × 10²³`. |
| **Engineering notation** | Real numbers | Scientific notation constrained to powers of 10 that are multiples of 3. |
| **Mixed-radix notation** | Integers, rational quantities, measurements | Uses different bases at different positions; e.g. time `2 h 37 min 15 s`. |
| **Roman numerals** | Natural numbers, some integers | Non-positional symbolic system: `I, V, X, L, C, D, M`. |
| **Egyptian numerals** | Natural numbers, rational numbers | Ancient additive/hieroglyphic system; fractions had specialized forms. |
| **Mayan numerals** | Natural numbers | Base-20 positional system with specialized symbols. |
| **Babylonian numerals** | Integers, rational numbers | Ancient sexagesimal (base-60) positional system. |
| **Complex Cartesian notation** | Complex numbers | Represents a complex number as `a + bi`. |
| **Complex polar notation** | Complex numbers | Represents a complex number as `r(cos θ + i sin θ)` or `re^{iθ}`. |
| **Vector / coordinate notation** | Tuples, vectors, geometric quantities | Represents numerical objects by ordered components, e.g. `(3,4)`. |
| **Matrix notation** | Matrices / numerical arrays | Represents collections of numbers as rectangular arrays. |
| **Interval notation** | Sets of real numbers | Represents ranges of real numbers: `[a,b]`, `(a,b)`. |
| **Set notation** | Natural, integer, rational, real, complex numbers | Represents numbers as elements of explicitly defined sets, e.g. `x ∈ ℝ`. |
| **Algebraic/radical notation** | Algebraic real/complex numbers | Represents numbers through algebraic expressions, e.g. `√2`, `∛5`. |
| **Root / algebraic-number notation** | Algebraic numbers | Represents numbers as roots of polynomials, e.g. `x² − 2 = 0`. |
| **Continued fractions** | Rational, irrational real numbers | Represents real numbers through nested fractions, e.g. `[1;2,2,2,…]`. |
| **Numeral systems for algebraic structures** | Modular integers, finite fields, etc. | Specialized representations such as `ℤ/nℤ` or finite-field elements. |
| **p-adic notation** | p-adic numbers | Represents numbers using expansions in powers of a prime `p`, e.g. `a₀ + a₁p + a₂p² + …`. |

## Number Line

> A **number line** is a **one-dimensional visual representation of real numbers** as points on a straight line.
> 

## Theory

> See [Arithmetic Formalism](arithmetic.md), etc.
> 

| **Theory** | **Type of Numbers** | **Core Idea** | **Purpose** |
| --- | --- | --- | --- |
| Dedekind’s Theory of Real Numbers | Real numbers ($\mathbb{R}$) | Define reals as *Dedekind cuts* of rationals: partitions of $\mathbb{Q}$ into two sets $A, B$ with all $a \in A < b \in B$ | Rigorous foundation for the continuum; completeness of $\mathbb{R}$ |
| Cantor’s Set-Theoretic Construction | Natural, integers, rationals, reals | Construct numbers entirely as sets: 0 = ∅, 1 = {0}, 2 = {0,1}, rationals as pairs, reals via cuts or Cauchy sequences | Unified, axiomatic set-theoretic foundation for all numbers |
| Von Neumann Ordinals | Natural numbers ($\mathbb{N}$) | Each number is the set of all smaller numbers: 0=∅, 1={0}, 2={0,1}, 3={0,1,2}, … | Elegant set-theoretic model; links natural numbers and ordinals |
| Cauchy Sequences of Rationals | Real numbers ($\mathbb{R}$) | Real numbers as equivalence classes of Cauchy sequences of rationals; two sequences are equivalent if their difference → 0 | Constructs reals, emphasizing limits and completeness |

## QA

### Is the Cardinality of a set a Property?

> This is largely a matter of language, but **cardinality** is best understood as a *property type*. The property type is *cardinality*, and a specific value—such as **3** (in the Indo-Arabic numeral system)—is the particular value that instantiates that property for a given set.
> 

### What is the representational role of numbers in the description of reality?

| Abstraction Type / Representation Role | Description | Role in describing reality | Typical Numeral |
| --- | --- | --- | --- |
| **Cardinality** | Number of distinct objects in a collection | Represents **how many** | `7` |
| **Ordinality** | Position of an object in an ordered sequence | Represents **which position** | `3rd` / `3` |
| **Length** | Spatial extent between points | Represents **how long** | `2.5 m` |
| **Area** | Extent of a two-dimensional region | Represents **how much surface** | `12 m²` |
| **Volume** | Extent of a three-dimensional region | Represents **how much space** | `4 m³` |
| **Mass** | Amount of matter / inertial quantity | Represents **how much mass** | `5 kg` |
| **Duration** | Extent of time between events | Represents **how long** | `30 s` |
| **Magnitude** | Quantitative size of a measurable property | Represents **how much / how large** | `8.4` |
| **Ratio** | Multiplicative relationship between quantities | Represents **relative magnitude** | `3:2` / `1.5` |
| **Rate** | Quantity relative to another quantity, often time | Represents **change or quantity per unit** | `60 km/h` |
| **Probability** | Degree of possibility associated with an event | Represents **uncertainty / likelihood** | `0.75` |
| **Frequency** | Number of occurrences relative to an interval | Represents **how often** | `10 Hz` |
| **Temperature** | Quantitative representation of thermal state | Represents **thermal condition** | `25 °C` |
| **Value (Amount)** | Quantified economic magnitude | Represents **economic quantity** | `$100` |
| **Coordinate / Position** | Numerical specification of location in a space | Represents **where** | `(3, 5)` |
| **Index** | Numerical identifier or position within a system | Represents **identity/location within an ordered structure** | `i = 7` |

## References

- https://en.wikipedia.org/wiki/Number
- https://en.wikipedia.org/wiki/Number_line
- [Object](https://app.notion.com/p/Object-065fa34e929c49cb8204bdd35b255b6e?pvs=21)
- [Property](https://app.notion.com/p/Property-271c0f5171ec80498865e3db652beafb?pvs=21)
- [Cardinality](cardinality.md)
- [‣](https://app.notion.com/p/10e598edb79081b8820fe8d8bed966e9?pvs=21)
- [‣](https://app.notion.com/p/362598edb7908042b237ed2d3b5b32c0?pvs=21)
- https://en.wikipedia.org/wiki/Triangle_of_reference
