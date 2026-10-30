---
tags: [arithmetic, relation, quantity]
qa:
  - "Which are the types of ratios: unit ratio, numerator-unit ratio, denominator-unit ratio, etc.?"
---

# Ratio

> A **ratio** is an ordered comparison of two quantities of the same kind, expressing the relative magnitude of one against the other as a quotient — $a : b$ reads as *a per b*, and its value is $a/b$.

> A ratio does not measure either quantity; it measures the **relation between them**. That is why it is dimensionless by convention, and why one ratio is realized by infinitely many pairs: the ratio fixes a class $\{(ka, kb) : k \neq 0\}$, never a single ordered pair.

## Formulation

### What is this epistemic instance?

> The **ratio instance** is the representational construct that carries a comparison of relative magnitude. Given two quantities $a$ and $b$ of the same kind, the ratio is the quotient read as a relation,
>
> $$a : b \;=\; \frac{a}{b},$$
>
> and the equality of ratios is the equality of their classes: $a : b = c : d$ exactly when $a d = b c$. Two readings are routinely intended and must be kept apart: the **part-to-part** reading ($a : b$ — how the parts compare with each other) and the **part-to-whole** reading ($a : (a+b)$ — the share each part is of the total). The written form does not decide between them; the context does.

> Ratio is not its neighbours, and the distinctions are load-bearing:

| Construct | What it compares | Result |
| --- | --- | --- |
| **Ratio** | two quantities of the same kind | a dimensionless number (the quotient read as a relation) |
| **Rate** | two quantities of different kinds | a number carrying a unit (km/h, $/kg, bits/s) |
| **Proportion** | two ratios, asserted equal | a truth-valued equation ($a : b = c : d$) |
| **Percentage** | a part against the whole, consequent fixed at 100 | a dimensionless number per hundred |
| **Scale** | a magnitude against its depiction or standard | a mapping factor (1 : 50, decibels) |
| **Quotient** | the arithmetic result of dividing | a number, not a comparison |

> The same arithmetic operation underlies all six: division. What differs is what the quotient is *taken to represent* — a relation between like quantities (ratio), a derived quantity with a unit (rate), an equality claim (proportion), a normalized share (percentage), a mapping (scale), or a bare number (quotient).

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the **Ratio Representation**: the structure through which relative magnitude is encoded, interpreted, and manipulated. A ratio is not a segment of reality, an agent, nor an operation; it is a representational construct of the arithmetic–algebraic system, with a written form, constitutive rules, and readings.

> `readable as` an **`Epistemic Construction`** when attention falls on **Ratio** as a concept in the mathematical edifice — an artifact constituted, taught, and extended alongside number, fraction, and proportion. `readable as` an **`Epistemic Operation`** when attention falls on the act of *taking* a ratio — the comparison performed on two measured quantities.

> The quantities compared are read in the **Ontic Order**; the ratio that relates them is epistemic.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in three ways the decomposition keeps apart. First, **aspect**: "ratio" names the construct ($a : b$), the reading (part-to-part or part-to-whole), and the value ($a/b$); only the first is a representation, and the third is a number. Second, **kind of relata**: a ratio of like quantities is dimensionless, while a ratio of unlike quantities is a rate with a unit — the boundary is set by commensurability, not by notation. Third, **use**: the same written ratio can serve as a proportion's term, a percentage's source, or a scale's factor.

> The ambiguity is resolved by declaring `Epistemic Representation` primary and typing the forms under `Representational System`: quotient form, percent form, scale form, rate form, and the normalized forms (per-one and reduced). The operation and concept readings stay prose rather than becoming a second tree. Collapsing ratio into quotient would erase the comparison; collapsing it into rate would erase the like-kind condition. The typology of ratios — unit, part-to-part, strict, compound, and the rest — is a set of classification axes over one construct, not a partition into sub-constructs; see [QA](#sec-which-are-the-types-of-ratios-unit-ratio-numerator-unit-ratio-denominator-unit-ratio-etc).

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the ratio as a representational construct — into its written forms, its constitutive rules and properties, and its readings.
>
> **Stopping rule.** A row is terminal when it names a concrete form, rule, property, convention, or reading; the arithmetic of division itself is not decomposed here (see [Division](note.html?n=epistemica/mathematical/division.md)).
>
> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique.
>
> **Typing.** The root type is `Epistemic Representation`, declared once; the forms hang under `Representational System`, the rules and readings under its `Constitutive Substrate`.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Representation` → Ratio | The representational construct expressing how many times one quantity contains another of the same kind. |
| `Epistemic Representation` → Ratio → `Representational System` | Grouping: the sign system in which a ratio is written. |
| `Epistemic Representation` → Ratio → `Representational System` → Quotient Form | The fraction or division form $a/b$ that carries the ratio as a quotient. |
| `Epistemic Representation` → Ratio → `Representational System` → Quotient Form → `Representation Element` | Grouping: constituents of the quotient form. |
| `Epistemic Representation` → Ratio → `Representational System` → Quotient Form → `Representation Element` → Antecedent | The compared quantity $a$, written as numerator. |
| `Epistemic Representation` → Ratio → `Representational System` → Quotient Form → `Representation Element` → Consequent | The comparison quantity $b$, written as denominator; zero consequent leaves the ratio undefined. |
| `Epistemic Representation` → Ratio → `Representational System` → Quotient Form → `Representation Element` → Ratio Glyph | The colon, fraction bar, or *to* that expresses the comparison rather than a division. |
| `Epistemic Representation` → Ratio → `Representational System` → Quotient Form → `Representation Element` → Ratio Expression | The written token `3 : 2` or `3/2` as a checkable artifact. |
| `Epistemic Representation` → Ratio → `Representational System` → Percent Form | The ratio rescaled so the consequent is 100 — the percentage reading of the same relation. |
| `Epistemic Representation` → Ratio → `Representational System` → Scale Form | The ratio used as a mapping factor between a magnitude and its depiction or standard (1 : 50). |
| `Epistemic Representation` → Ratio → `Representational System` → Rate Form | The ratio of two quantities of different kinds, carrying the unit that the like-kind ratio lacks. |
| `Epistemic Representation` → Ratio → `Representational System` → Unit-Consequent Form | The normalized form $a : 1$ — $a$ units of the antecedent per one unit of the consequent; the ratio underlying a unit rate. |
| `Epistemic Representation` → Ratio → `Representational System` → Unit-Antecedent Form | The reciprocal normalized form $1 : b$ — one unit of the antecedent per $b$ units of the consequent. |
| `Epistemic Representation` → Ratio → `Representational System` → Reduced Form | The representative $a : b$ with $\gcd(a, b) = 1$ — the smallest integer pair of the class, obtained by dividing both terms by their common measure. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` | Grouping: rules, properties, and conventions constituting the construct. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → Equivalence Rule | $(a, b) \sim (ka, kb)$ for $k \neq 0$: scaling both terms preserves the ratio, and equality of ratios is equality of these classes. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Property` | Grouping: properties carried by the construct. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Property` → Dimensionlessness | A ratio of same-kind quantities carries no unit; the units cancel in the quotient. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Property` → Scaling Invariance | The value depends on the pair only through the quotient, never on the absolute magnitudes compared. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Convention` | Grouping: stabilized notational and interpretive choices. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Convention` → Common Unit Convention | Both terms are expressed in one unit before the ratio is taken; mixing units silently changes it. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Convention` → Dimensionless Reading | Reading the quotient without a unit is a convention that rate and scale forms depart from. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Interpretation` | Grouping: meaning assignments carried by the construct. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Interpretation` → Part-to-Part Reading | $a : b$ as a comparison of parts with each other — three parts to two parts. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Interpretation` → Part-to-Whole Reading | $a : (a + b)$ as the share of the total — three parts out of five. |
| `Epistemic Representation` → Ratio → `Representational System` → `Constitutive Substrate` → `Interpretation` → Ordered-Pair Reading | The ratio as the class $[a : b]$ of proportional pairs — a point in a projective space of ordered pairs. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The instance is well identified once ratio, rate, proportion, percentage, scale, and quotient are separated: **pass**. Its definition is clear in the arithmetic setting and equivocal in ordinary use, where "ratio" slides into rate and proportion: **partial**. Its determinacy is carried by the declared relata and reading — same-kind, ordered, part-to-part or part-to-whole — and without them the construct is under-determined: **partial**. It is internally consistent: the like-kind condition, the equivalence rule, and the dimensionless convention agree, and the rate and scale forms are explicitly typed as departures: **pass**. Its representational adequacy covers the forms, properties, and readings in use: **pass**. Its purpose adequacy — compressing a comparison into one number while preserving the scale-invariant structure that makes such comparisons portable — is high: **pass**.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note distinguishes the ratio from the rate, the proportion, the percentage, the scale, and the quotient, and names the shared division beneath them. |
| **Definitional Clarity** | Partial | The definition is precise for like-kind quantities; ordinary usage applies "ratio" to unlike quantities (rate) and to ratio equations (proportion), and the note must disambiguate explicitly. |
| **Conceptual Determinacy** | Partial | Which instances qualify depends on the declared relata, order, and reading; the equivalence rule decides borderline cases (same value, different pair), not the notation. |
| **Internal Consistency** | Pass | The like-kind condition, the equivalence rule, and the dimensionless convention are mutually compatible; the rate and scale branches declare their departure rather than contradicting it. |
| **Representational Adequacy** | Pass | Quotient, percent, scale, rate, and the normalized (unit-consequent, unit-antecedent, reduced) forms are covered, together with the properties (dimensionlessness, scaling invariance) and the two ordinary readings. |
| **Purpose Adequacy** | Pass | Supports comparison, normalization, proportion and percentage construction, and the transport of a relation across magnitudes — the uses that motivate the construct. |

## QA

### Which are the types of ratios?

| Type | Description | Case |
|---|---|---|
| **Unit Ratio** | A ratio expressed with one term equal to 1. | 3:1 |
| **Antecedent-Normalized Ratio** | A ratio whose first term is normalized to 1. | 1:2 |
| **Consequent-Normalized Ratio** | A ratio whose second term is normalized to 1. | 3:1 |
| **Reduced Ratio** | A ratio whose terms have been divided by their greatest common divisor (GCD). | 6:2 → 3:1 |
| **Unreduced Ratio** | A ratio whose terms have not been reduced to their simplest integer form. | 6:2 |
| **Part-to-Part Ratio** | Compares one part of a quantity with another part. | 3:2 |
| **Part-to-Whole Ratio** | Compares one part with the total quantity. | 3:5 |
| **Whole-to-Part Ratio** | Compares the total quantity with one of its parts. | 5:3 |
| **Equivalent Ratios** | Different numerical representations expressing the same proportional relationship. | 3:1 = 6:2 |
| **Inverse Ratio** | A ratio obtained by exchanging the positions of its terms. | 3:2 → 2:3 |
| **Compound Ratio** | A ratio obtained by combining two or more ratios. | (2:3) × (3:4) = 1:2 |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Division](note.html?n=epistemica/mathematical/division.md)
- [Multiplication](note.html?n=epistemica/mathematical/multiplication.md)
- [Normalization](note.html?n=epistemica/mathematical/normalization.md)
- [Proportionality](note.html?n=epistemica/mathematical/proportionality.md)
- [Percentage](note.html?n=epistemica/mathematical/percentage.md)
- [Scale](note.html?n=epistemica/mathematical/scale.md)
- [Ratio (mathematics)](https://en.wikipedia.org/wiki/Ratio)
- [Proportionality (mathematics)](https://en.wikipedia.org/wiki/Proportionality_(mathematics))
- [Rate (mathematics)](https://en.wikipedia.org/wiki/Rate_(mathematics))
- Euclid. *Elements*, Book V — the theory of proportions.
- Frege, G. (1884). *Die Grundlagen der Arithmetik* — on the treatment of relations and quantities as numbers.
- Kieren, T. E. (1976). On the mathematical, cognitive and instructional foundations of rational numbers. In *Number and Measurement* (pp. 101–144). ERIC/SMEAC.
- Lamon, S. J. (2007). Rational numbers and proportional reasoning. In *Second Handbook of Research on Mathematics Teaching and Learning* (pp. 629–667). Information Age.
