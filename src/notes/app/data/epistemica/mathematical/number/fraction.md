---
tags: [note, mathematics, arithmetic, quantity]
qa:
  - "Which are the types of fractions: proper, improper, mixed, unit, decimal, complex, continued, algebraic?"
  - "Is a fraction a number or an expression?"
  - "Why can the denominator never be zero?"
---

# Fraction

> A **fraction** is the written form that carries a rational magnitude as an ordered pair of terms under a fraction bar — $\frac{a}{b}$, read as *a out of b*, *a divided by b*, or *a per b* — with $b \neq 0$.

> The glyph does not fix one inscription: $\frac{3}{4}$, $\frac{6}{8}$, and $0.75$ are three writings of one magnitude. The fraction fixes the **class** $\{(ka, kb) : k \neq 0\}$, and its lowest-terms member is only the canonical representative of that class.

## Formulation

### What is this epistemic instance?

> The **fraction instance** is the representational construct by which a rational quantity is written as a quotient of two terms. Given terms $a$ and $b$ with $b \neq 0$, the fraction $a/b$ denotes the single number
>
> $$\frac{a}{b} \;=\; a \cdot b^{-1},$$
>
> and equality of fractions is equality of their classes: $a/b = c/d$ exactly when $a d = b c$. The numerator and the denominator are not quantities in their own right until interpreted; they are the two inscriptions the bar binds.

> Three readings are routinely conflated and must be kept apart: the **notation** ($3/4$ as a written form), the **value** (the rational number $0.75$), and the **act** (the division $3 \div 4$ that produces it). Only the first is the representation this note decomposes.

> A fraction is not its neighbours, and the distinctions are load-bearing:

| Construct | What it carries | Result |
| --- | --- | --- |
| **Fraction** | a rational magnitude, written as a quotient of two terms | a written form (a number in fractional notation) |
| **Ratio** | a comparison of two like-kind quantities | a dimensionless relation, not a single written number |
| **Quotient (division)** | the arithmetic result of dividing one number by another | a number; the act that produces the fraction's value |
| **Decimal** | a rational number written in place-value notation | a written form with a finite or repeating expansion |
| **Percentage** | a fraction rescaled so the denominator is 100 | a written form per hundred |
| **Rational number** | any number expressible as a quotient of integers | the concept the fraction denotes |
| **Rate** | a comparison of unlike-kind quantities | a number carrying a unit |

> The same operation underlies all seven: division. What differs is what the quotient is *taken to represent* — a written number (fraction), a relation between like quantities (ratio), an act (quotient), a place-value form (decimal), a normalized share (percentage), a concept (rational number), or a unit-bearing comparison (rate).

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the **Fraction Representation**: the notational construct through which rational magnitude is encoded, interpreted, and manipulated. A fraction is not a segment of reality, an agent, nor an act; it is a representational construct of the arithmetic–algebraic system, with a written form, constitutive rules, and readings.

> `readable as` an **`Epistemic Construction`** (→ Kind `Concept`) when attention falls on the rational number the form denotes — the constructed discriminator of quotient magnitude, taught and extended alongside number and ratio. The operation reading is not a second type: the act of *taking* a fraction is the `Computation` that fires the division rule, and the licences that rewrite one fraction into an equivalent one are `Transformation Rule`s of the same substrate. `Epistemic Operation` is a type the guide retires, and it is not used here.

> The magnitudes the numerator and denominator count are read in the **Ontic Order**; the fraction that carries their quotient is epistemic.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in three ways the decomposition keeps apart. First, **aspect**: "fraction" names the notation ($3/4$), the value ($0.75$), and the act ($3 \div 4$); only the notation is the representation, and the value is a concept. Second, **kind of terms**: the terms may be integers (an arithmetic fraction), measured quantities (three-quarters of a metre), or algebraic expressions (the *algebraic* fraction $\frac{x+1}{x-1}$); the last reuses the notation for a different construct, and the boundary is set by what the terms range over. Third, **scope**: *proper*, *improper*, and *mixed* are all well-formed fractions — "improper" marks a relation between numerator and denominator, never an error, and a magnitude larger than one is not a defect of the notation.

> The ambiguity is resolved by declaring `Epistemic Representation` primary and typing the forms under `Representational System`: proper, improper, mixed, unit, decimal, complex, continued, and algebraic. The act and concept readings stay prose rather than becoming a second tree. Collapsing the fraction into its value would erase the notation; collapsing it into the division would erase the difference between the written form and the computation that produced it. The typology of fractions is a set of classification axes over one construct, not a partition into sub-constructs; see [QA](#sec-which-are-the-types-of-fractions).

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the fraction as a representational construct — into its written forms, its combinable elements, its rules and conventions, and its readings.
>
> **Stopping rule.** A row is terminal when it names a concrete form, element, rule, convention, or reading; the arithmetic of division itself is not decomposed here (see [Division](note.html?n=epistemica/mathematical/number/division.md)).
>
> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique.
>
> **Typing.** The root type is `Epistemic Representation`, declared once; the forms hang under `Representational System`, the elements under `Representation Element`, and the rules and readings under its `Constitutive Substrate`.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Representation` → Fraction | The representational construct writing a rational magnitude as an ordered pair of terms under a fraction bar. |
| `Epistemic Representation` → Fraction → `Representational System` | Grouping: the sign system in which a fraction is written. |
| `Epistemic Representation` → Fraction → `Representational System` → Proper Fraction | Numerator smaller in magnitude than the denominator; the value lies strictly inside the unit interval. |
| `Epistemic Representation` → Fraction → `Representational System` → Improper Fraction | Numerator at least as large in magnitude as the denominator; a well-formed fraction, not an error. |
| `Epistemic Representation` → Fraction → `Representational System` → Mixed Number | A whole-number part beside a proper fraction ($2\frac{3}{4}$) — one value in a two-part inscription. |
| `Epistemic Representation` → Fraction → `Representational System` → Unit Fraction | Numerator equal to one ($1/n$) — the form the Egyptian and continued-fraction systems build from. |
| `Epistemic Representation` → Fraction → `Representational System` → Decimal Fraction | Denominator a power of ten ($\frac{75}{100}$) — the bridge to place-value notation. |
| `Epistemic Representation` → Fraction → `Representational System` → Complex Fraction | A fraction whose numerator or denominator is itself a fraction. |
| `Epistemic Representation` → Fraction → `Representational System` → Continued Fraction | A nested chain of unit fractions, $a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cdots}}$. |
| `Epistemic Representation` → Fraction → `Representational System` → Algebraic Fraction | A quotient of two algebraic expressions ($\frac{x+1}{x-1}$) — the notation reused where the terms are not integers. |
| `Epistemic Representation` → Fraction → `Representational System` → `Representation Element` | Grouping: combinable constituents of the written form. |
| `Epistemic Representation` → Fraction → `Representational System` → `Representation Element` → Numerator | The upper term — what is taken, divided, or compared. |
| `Epistemic Representation` → Fraction → `Representational System` → `Representation Element` → Denominator | The lower term, required non-zero — the base the numerator is taken against. |
| `Epistemic Representation` → Fraction → `Representational System` → `Representation Element` → Fraction Bar | The vinculum or slash binding numerator to denominator, and marking the division the form abbreviates. |
| `Epistemic Representation` → Fraction → `Representational System` → `Representation Element` → Fraction Expression | The written token $\frac{3}{4}$ or `3/4` as a checkable artifact. |
| `Epistemic Representation` → Fraction → `Representational System` → `Representation Element` → Whole-Number Part | The integer prefix of a mixed number, $2$ in $2\frac{3}{4}$. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` | Grouping: rules, structures, and conventions constituting the construct. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Formation` | Grouping: rules of well-formed combination. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Formation` → Fraction Formation Rule | $a/b$ is well formed exactly when the denominator is a defined, non-zero term. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Transformation Rule` | Grouping: rules licensing the rewrite of well-formed fractions. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Transformation Rule` → Equivalence Rule | $a/b \mapsto ka/kb$ for $k \neq 0$: scaling both terms preserves the value. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Transformation Rule` → Reduction Rule | Divide numerator and denominator by their greatest common divisor to reach the lowest-terms representative. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Transformation Rule` → Fraction-to-Decimal Rule | Rewrite $a/b$ as the decimal expansion of $a \div b$ — finite, or repeating and marked as such. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Transformation Rule` → Fraction Arithmetic Rule | $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$ and $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$ — the licences that let fractions compute. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Convention` | Grouping: stabilized notational and interpretive choices. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Convention` → Zero-Denominator Prohibition | Division by zero stays undefined; the prohibition follows from the meaning of the form, not from an arbitrary rule. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Convention` → Sign Placement Convention | The sign sits on the numerator or on the fraction, never on the denominator alone. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Convention` → Lowest-Terms Convention | The reduced representative is the canonical name of the class; unreduced forms are the same value in another inscription. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Convention` → Improper-Form Licence | Writing a value above one as an improper fraction instead of a mixed number is permitted, and often required for computation. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Interpretation` | Grouping: meaning assignments carried by the construct. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Interpretation` → Part–Whole Reading | $a/b$ as $a$ parts out of $b$ equal parts of one whole. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Interpretation` → Quotient Reading | $a/b$ as the result of dividing $a$ by $b$ — the reading that makes fractions a number system. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Interpretation` → Ratio Reading | $a/b$ as the comparison $a : b$ — the bridge to ratio and rate. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Interpretation` → Operator Reading | $a/b$ as the rescaling $x \mapsto \frac{a}{b}x$ applied to a quantity. |
| `Epistemic Representation` → Fraction → `Representational System` → `Constitutive Substrate` → `Interpretation` → Measure Reading | $a/b$ as a magnitude on a subdivided unit — three-quarters of a metre. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The instance is well identified once notation, value, and act are separated, and once the arithmetic fraction is distinguished from the ratio, the decimal, the rational number, and the algebraic fraction: **pass**. Its definition is precise for integer terms and a non-zero denominator, and equivocal in ordinary use, where "fraction" names both the written form and the number written: **partial**. Its determinacy is carried by the declared terms and reading — integers or expressions, part–whole or quotient — and without them the construct is under-determined at its edges: **partial**. It is internally consistent: the formation rule, the equivalence and reduction rules, and the lowest-terms convention agree, and the algebraic and continued forms declare their departure rather than contradicting it: **pass**. Its representational adequacy covers the forms, elements, rules, and readings in use: **pass**. Its purpose adequacy — carrying an exact rational magnitude in a form that stays exact under addition and multiplication while remaining comparable to decimals and ratios — is high: **pass**.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note separates the fraction from the ratio, the quotient, the decimal, the percentage, the rate, and the rational number, and names the division beneath them. |
| **Definitional Clarity** | Partial | Precise for integer terms and a non-zero denominator; ordinary usage applies "fraction" both to the inscription and to the number it denotes, and to quantities and algebraic quotients, so the note must disambiguate explicitly. |
| **Conceptual Determinacy** | Partial | Which instances qualify depends on what the terms range over and which reading is declared; the equivalence rule decides borderline cases (same value, different inscription), not the notation. |
| **Internal Consistency** | Pass | The formation rule, the equivalence and reduction rules, and the lowest-terms and sign conventions are mutually compatible; the algebraic and continued branches declare their departure rather than contradicting it. |
| **Representational Adequacy** | Pass | Proper, improper, mixed, unit, decimal, complex, continued, and algebraic forms are covered, together with the elements, the rewrite licences, the conventions, and the five readings. |
| **Purpose Adequacy** | Pass | Supports exact rational arithmetic, comparison with decimals and ratios, part–whole and operator reasoning, and the transport of a magnitude across units — the uses that motivate the construct. |

## QA

### Which are the types of fractions?

| Type | Description | Case |
| --- | --- | --- |
| **Proper Fraction** | Numerator smaller in magnitude than the denominator. | $3/4$ |
| **Improper Fraction** | Numerator at least as large in magnitude as the denominator. | $7/4$ |
| **Mixed Number** | A whole number beside a proper fraction. | $1\frac{3}{4}$ |
| **Unit Fraction** | Numerator equal to one. | $1/7$ |
| **Decimal Fraction** | Denominator a power of ten. | $75/100$ |
| **Complex Fraction** | A fraction whose numerator or denominator is itself a fraction. | $\frac{3/4}{2/5}$ |
| **Continued Fraction** | A nested chain of unit fractions. | $1 + \frac{1}{2 + \frac{1}{3}}$ |
| **Equivalent Fractions** | Different inscriptions of one value. | $3/4 = 6/8 = 9/12$ |
| **Reduced Fraction** | Lowest-terms representative of the class. | $6/8 \to 3/4$ |
| **Algebraic Fraction** | Quotient of two algebraic expressions. | $\frac{x+1}{x-1}$ |

### Is a fraction a number or an expression?

> Both, in different roles, and the roles must be kept apart. As an **expression** the fraction is an inscription — a numerator, a denominator, and a bar — that the equivalence and reduction rules rewrite. As a **number** it is the value the inscription denotes: the rational number that is the equivalence class of all its inscriptions. The expression is what the `Computation` acts on; the number is what the `Concept` names. Confusing them produces the classic errors: reading $6/8$ as a different number from $3/4$ (an expression-level difference mistaken for a value-level difference), or reading $0.75$ as a different number from $3/4$ (a notation-level difference mistaken for a value-level difference).

### Why can the denominator never be zero?

> Because the fraction is defined as the quotient $a \cdot b^{-1}$, and zero has no multiplicative inverse in any field: no number $x$ satisfies $0 \cdot x = 1$. The prohibition is not an arbitrary addition to the notation but a consequence of what the fraction denotes, and the formation rule records that consequence. A limit such as $\lim_{b \to 0} a/b$ diverges or is undefined, which is why the notation is not extended by a convention assigning $a/0$ a value.

### Which are the possible interpretations of the following situation?

![Two circles cut in thirds: one third shaded, and all three thirds shaded](../assets/notes/epistemica/mathematical/fraction/fraction-part-whole.png)

1. **Part-to-Part Comparison:** Relate the number of colored parts to the number of non-colored parts (1 : 2).
2. **Fractional Representation:** Represent the number of colored parts as \(1 \times \frac{1}{3}\).
3. **Whole as Unity:** The fully shaded circle is \(\frac{3}{3} = 1\) — three thirds make one whole.


## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Number](note.html?n=epistemica/mathematical/number/number.md)
- [Arithmetic](note.html?n=epistemica/mathematical/number/arithmetic.md)
- [Division](note.html?n=epistemica/mathematical/number/division.md)
- [Multiplication](note.html?n=epistemica/mathematical/number/multiplication.md)
- [Ratio](note.html?n=epistemica/mathematical/number/ratio.md)
- [Percentage](note.html?n=epistemica/mathematical/number/percentage.md)
- [Numeric System](note.html?n=epistemica/mathematical/number/numeric-system.md)
- [Fraction (mathematics)](https://en.wikipedia.org/wiki/Fraction)
- [Rational number](https://en.wikipedia.org/wiki/Rational_number)
- [Continued fraction](https://en.wikipedia.org/wiki/Continued_fraction)
- Euclid. *Elements*, Book VII — the theory of integer ratios and parts.
- Freudenthal, H. (1983). *Didactical Phenomenology of Mathematical Structures*. Reidel — the fraction as a phenomenologically grounded construct.
- Kieren, T. E. (1976). On the mathematical, cognitive and instructional foundations of rational numbers. In *Number and Measurement* (pp. 101–144). ERIC/SMEAC.
- Lamon, S. J. (2007). Rational numbers and proportional reasoning. In *Second Handbook of Research on Mathematics Teaching and Learning* (pp. 629–667). Information Age.
- Wu, H.-H. (2011). *Understanding Numbers in Elementary School Mathematics*. American Mathematical Society.
