---
tags: [note, mathematics, quantity, representation]
qa:
  - "Why does a ratio scale license 'twice as much' while an interval scale does not?"
  - "Is counting a measurement?"
  - "Why is logical quantification (∀, ∃) not this construct?"
---

# Quantification

> **Quantification** binds a magnitude to a number: it fixes a scale, names a unit, and writes a value — so that *more than* becomes *how much*, and the result can be compared, combined, and converted. It is the representational scheme through which the quantitative properties of reality enter arithmetic.

> The scheme is not one act. Counting binds a cardinality to a numeral with the unit left implicit; measuring binds a magnitude to a numeral in a unit; estimating binds an interval around it; ranking binds an order. What they share is the structure this note decomposes: a scale that licenses certain readings, a unit that fixes what the numeral counts in multiples of, and a notation that carries both.

> A quantity is never a bare number. `42` quantifies nothing until a unit and a scale say what kind of magnitude it stands for and which operations it admits: `42 kg` is a mass, `42 °C` an interval-scaled temperature, `42nd` a rank, and `42` alone is as likely a count as a line number. Remove the unit and the quantity is gone, though the number remains.

> Numbers and the schemes that bind them to magnitudes co-evolve: what counts as quantifiable is partly fixed by the notation available for it, and the notation is extended by what inquiry needs to quantify (see [Number](/note.html?p=notes/epistemica/mathematical/number/number.md)).

## Formulation

### What is this epistemic instance?

> The **quantification instance** is the representational scheme that assigns a numeric value to a magnitude under a declared unit and scale. Three components carry it, and none stands alone:
>
> 1. **A scale** — the structure of admissible comparisons. The classical four levels fix what the assignment licenses: *nominal* (equality alone), *ordinal* (order), *interval* (order and differences, no ratios), *ratio* (order, differences, and ratios, with a meaningful zero). An *absolute* scale is the ratio case whose unit is the natural count.
> 2. **A unit** — the reference magnitude in which the value is expressed, together with the system that fixes which units are admitted and how derived ones compose (SI, CGS, imperial, natural).
> 3. **A numeral** — the value written against that unit: how many times the reference magnitude the magnitude is.

> Formally, a quantification of a quantitative attribute $A$ of a segment is a map
>
> $$q : A \to \mathbb{R} \times U, \qquad q(a) = (v, u),$$
>
> together with a scale structure $S$ under which $v$ is read. The map is not arbitrary: it must preserve the empirical relations the attribute carries — if $a_1$ is longer than $a_2$ then $q(a_1) > q(a_2)$; if $a_3$ is the concatenation of $a_1$ and $a_2$ then $v_3 = v_1 + v_2$ in the same unit. Which relations must be preserved is exactly what the declared scale level says.

> The scheme is portable across attributes: the same structure quantifies a length, a mass, a duration, a probability, a price, a count. What changes between them is the unit, the dimension, and the level — never the form of the binding.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the **quantification scheme**: the representational construct through which a magnitude is carried as a number in a unit on a scale, together with the sign system and the rules that constitute it.

> `readable as` an **`Epistemic Act`** when attention falls on a single act of assigning a value — the guide types `Measurement` as an action element, and counting, estimating, and ranking sit at the same grain. `readable as` an **`Epistemic Practice`** when attention falls on the organized doing — metrology, the laboratories and standards bodies that sustain it. `readable as` an **`Epistemic Construction`** when attention falls on a quantity statement as a description of a segment.

> The exclusion is argued, not asserted. An act has no constitutive parts to grow, so the scale levels, the unit systems, and the conversion rules decomposed below would have no home under it — the act is what fires the scheme, not what the scheme is made of. The practice is [Measurement Theory](/note.html?p=notes/epistemica/measurement/measurement-theory.md)'s subject, and a quantity statement is one product of the scheme, not the scheme.

> The magnitudes quantified are read in the **Ontic Order**; the scheme that binds them is epistemic. The ontic decomposition of a magnitude belongs to the naturalis grammar: it is named here and never grown.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in four ways the decomposition keeps apart.

> **Aspect.** *Quantification* names the act of assigning a value, the scheme that makes the assignment well formed, and the result — a quantity. This note types the scheme; the act and the result stay `readable as` prose, so no row below carries two types.

> **Sense.** The false friends are load-bearing, and every one of them is a different construct:

| Construct | What it does | Why it is not this |
| --- | --- | --- |
| **Quantification** | binds a magnitude to a number on a declared scale | — |
| **Quantization** | replaces a value drawn from a continuum by one of finitely many levels | it discretizes a range of values; it binds nothing to a unit or a scale (see [Quantization](/note.html?p=notes/epistemica/mathematical/quantization.md)) |
| **Measurement** | assigns a value to an observable under a scale | one act the scheme makes possible, on a registered observable (see [Measurement Theory](/note.html?p=notes/epistemica/measurement/measurement-theory.md)) |
| **Counting** | assigns a cardinality to a collection | the scheme's discrete case, with the unit implicit (see [Enumeration](/note.html?p=notes/epistemica/mathematical/discrete/enumeration-counting.md)) |
| **Measure** in mathematics | assigns a size to a set | a set function in measure theory, not a binding of a magnitude to a unit (see [Measure](/note.html?p=notes/epistemica/mathematical/measure/measure.md)) |
| **Logical quantification** | binds a variable under ∀ or ∃ | it ranges over a domain of things, not over how much of an attribute an item carries |

> **Level.** A nominal or ordinal assignment quantifies an attribute without yielding a magnitude reading. "Twice as hot" is meaningless on an interval scale, and "twice the number" is meaningless on a nominal one. The scheme admits every level; the magnitude reading is licensed only from the interval level up.

> **Relatum.** Only a quantitative property can be quantified. Turning a quality into a measurable attribute is itself a construction — operationalization — and its warrant belongs to measurement theory rather than here; see [Quantitative Property](/note.html?p=notes/epistemica/mathematical/number/quantitative-property.md).

> The ambiguity is resolved by declaring `Epistemic Representation` primary, typing the five scale levels as `Convention`s of one substrate, and keeping the modes — counting, measuring, estimating, ranking — as prose. Filing the modes as sub-schemes would split one representation into four; filing the levels as sub-schemes would make an interval reading a different construct from a ratio reading of the same magnitude.

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the quantification scheme — into the sign system that carries it, the rules and structures constituting it, and the predicates it carries. The acts that exercise the scheme are named in prose and linked, never grown here; the same holds for the magnitudes bound, whose decomposition belongs to the naturalis grammar.

> **Stopping rule.** A row is terminal when it names a notation element, a foundation, a convention, a formation rule, a transformation rule, an interpretation, or a predicate. The arithmetic that consumes the value is not decomposed here (see [Arithmetic](/note.html?p=notes/epistemica/mathematical/number/arithmetic.md)), and neither is the metrology that produces it (see [Measurement Theory](/note.html?p=notes/epistemica/measurement/measurement-theory.md)).

> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch.

> **Typing.** The root type is `Epistemic Representation`, declared once. The notation hangs under `Representational System`; its constituents under `Representation Element`; its rules under `Constitutive Substrate`, by constitutive kind. The predicates hang by `Has Property`, which asserts a feature of the element rather than registering one from a segment.

> **Reading.** The tree is read as **representation**: it records how a magnitude is carried, not how the segment that bears the magnitude is parsed. The scale levels are conventions of this one substrate, never separate schemes.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification | The scheme binding a magnitude to a numeric value under a declared unit and scale — the representational construct through which a quantitative property enters arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` | Grouping: the sign system carrying the bound quantity. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Instance) Quantity Notation | Numeral, unit symbol, and scale mark taken together: the notation in which a quantified magnitude is written, read, and checked. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` | Grouping: combinable constituents of the notation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Magnitude | The size the value stands for — what the numeral measures in multiples of the unit; read in the Ontic Order, never grown here. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Numeric Value | The numeral bound to the magnitude: the number of units the notation records. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Unit | The reference magnitude in which the value is expressed — the standard of the same kind that the magnitude is a multiple of. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Unit Symbol | The written token naming the unit — `m`, `kg`, `s`, `%`, `°C` — the part of the expression a reader decodes. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Quantity Expression | The written quantity `9.81 m·s⁻²` as a checkable artifact: numeral, unit symbol, and exponent composed under the formation rules. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Scale Mark | The token or structure declaring the admissible readings — a rank position, a category label, an interval marker — and therefore the level the value is read at. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` | Grouping: the rules and structures constituting the scheme. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the principles the scheme is founded on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Dimensional Basis | The assignment of base quantities — length, mass, time, electric current, temperature, amount of substance, luminous intensity — from which every derived dimension is a product of powers. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Commensurability Principle | A magnitude can be compared with, and expressed as a multiple of, a unit of the same kind; without it the binding is undefined. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Additivity Assumption | Concatenating two magnitudes of the same kind adds their measures — the assumption that makes extensive quantities add and leaves intensive ones without a sum. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: stabilized choices the scheme rests on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Nominal Scale Convention | Values are names: equality and difference alone; the numerals are labels, and no order or arithmetic is licensed. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Ordinal Scale Convention | Values are ranks: order is licensed, differences are not — first, second, third fixes a sequence, not a distance. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Interval Scale Convention | Values are positions with an arbitrary zero: order and differences are licensed, ratios are not — 20 °C is not twice 10 °C. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Ratio Scale Convention | Values are multiples of a unit with a meaningful zero: order, differences, and ratios are licensed — 20 kg is twice 10 kg. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Absolute Scale Convention | Values are counts of a natural unit: the ratio case whose unit is fixed by the attribute itself — 5 items, 3 events, 2 children. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Unit System Convention | The declared family of units — SI, CGS, imperial, natural — fixing which units are admitted and how derived units compose. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Prefix Convention | The decimal multiples and submultiples of a unit — kilo, milli, micro — written as prefixes rather than as separate units. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Zero-Point Convention | What the zero of the scale denotes: absence of the magnitude, an arbitrary origin, or a distinguished reference point such as 0 °C. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Significant-Figures Convention | How many digits the written value carries, and therefore how much precision it claims to have. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Uncertainty-Reporting Convention | How the doubt is attached to the value — a standard uncertainty, an interval, or a coverage factor — and at which digit it is stated. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Traceability Convention | A value stands only if an unbroken chain of comparisons links it to a declared reference standard. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` | Grouping: rules of well-formed quantity expressions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Dimensional Homogeneity Rule | Only quantities of the same dimension may be equated, added, or compared — `3 m + 2 s` is not a well-formed expression. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Quantity Expression Formation Rule | How numeral, unit symbol, and exponent compose into a well-formed quantity — `9.81 m·s⁻²`, never `m 9.81 s⁻²`. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Scale-Admissibility Rule | Which operations a value admits at its declared level: equality at nominal, order at ordinal, differences at interval, ratios at ratio. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` | Grouping: licences rewriting one quantity expression into another. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Unit Conversion Rule | Rewrite into another unit of the same dimension by multiplying by the conversion factor — `1 km ↦ 1000 m`; the magnitude is preserved, the numeral is not. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Rescaling Rule | Rewrite under an affine change of scale — factor and offset, as `°C ↦ K` or a logarithmic unit — the case where the zero moves. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Nondimensionalization Rule | Rewrite a dimensional quantity as a dimensionless number by dividing it by a reference of the same dimension. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Dimensional Analysis Rule | Rewrite a relation into its dimension products alone, licensing a check on any equation before it is trusted. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Normalization Rule | Rewrite values into a common range or distribution — min–max, z-score — so that quantities in different units become comparable. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` | Grouping: assignments of meaning to the written quantity. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Magnitude Denotation | The numeral denotes a multiple of the unit: `3.2 m` means 3.2 times the reference metre. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Scale-Level Reading | What a reader may conclude from the value: equality, order, difference, or ratio, according to the declared level. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Zero Reading | What the zero of the scale says about the attribute: absence of the magnitude, an arbitrary origin, or a conventional reference point. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` | Grouping: predicates the scheme carries, asserted of a quantification rather than registered from a segment. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Precision | How close repeated quantifications of the same magnitude fall to one another — a predicate of the scheme's execution, not of the magnitude. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Accuracy | How close a quantified value falls to the magnitude it stands for. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Resolution | The smallest difference in magnitude the notation can express at the declared precision — the granularity of the scale. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Measurement Uncertainty | The doubt attached to a value, carried as an interval or a distribution rather than as a single number. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Dimension | The kind of magnitude a quantity belongs to, expressed as a product of powers of the base dimensions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Commensurability | Whether two quantities can be expressed in a common unit, and therefore compared or combined at all. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Additivity | Whether concatenating two magnitudes adds their values — the extensive case, denied to intensive quantities. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Unit Invariance | The magnitude is invariant under conversion; only the written value changes, and the scheme is worthless if it does not. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Sensitivity | How much the written value changes per unit change of the magnitude — the derivative the notation can resolve. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Quantification (→ Has Property) `Property` (→ Instance) Construct Validity | Whether the scale quantifies the attribute it claims to quantify, rather than a proxy correlated with it. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdict.** The scheme is determinate where its declaration is explicit and indeterminate where it is left implicit: once the scale level, the unit, and the dimension are fixed, every question this note asks has a checkable answer — which operations are licensed, which rewrites preserve the magnitude, which expressions are well formed. Its weakness is the same explicitness: the classic errors in quantitative work — a mean of ordinal ranks, a ratio of Celsius temperatures, a conversion that silently changes dimension — are failures of the declaration, not of the arithmetic, and the definition cannot by itself prevent them.

| Criterion | Verdict | Diagnostic Focus |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from quantization (a value-range discretization), measure (a set function), counting (the discrete case with an implicit unit), and logical quantification (variable binding); the scheme's three components are stated outright. |
| Definitional Clarity | Strong | "Scale, unit, numeral" plus "the map preserves the empirical relations the attribute carries" are stated conditions, not metaphors; each scale level is named with the operations it licenses. |
| Conceptual Determinacy | Moderate | Boundary rule: a claim is a quantification iff a magnitude is bound to a value under a declared scale. Borderline cases — ordinal indices, composite scores, proxy metrics — are decided by the declared level rather than by the numeral, which is why the level must be recorded, not assumed. |
| Internal Consistency | Strong | The scale levels are conventions of one substrate, never rival definitions of the scheme; the conversion rules preserve the magnitude exactly as the interpretation says they must, so notation and meaning cannot drift apart. |
| Representational Adequacy | Strong | Elements, foundations, conventions, formation rules, transformations, and interpretations are carried in separate branches, so a scale-level claim is never confused with a notational one and a predicate is never mistaken for a constituent. |
| Purpose Adequacy | Strong | The scheme serves the three uses quantification exists for — comparison, combination, and conversion — and it never claims a magnitude reading where only an ordinal one is licensed. |

## QA

### Why does a ratio scale license "twice as much" while an interval scale does not?

> Because a ratio needs a zero that means absence. On a ratio scale the value is a multiple of the unit: 0 kg is no mass, and 20 kg is exactly twice 10 kg, because both are multiples of the same unit from the same origin. On an interval scale the zero is a convention rather than an absence: 0 °C is the freezing point of water, not the absence of temperature, and the origin can be moved by an affine rescaling without changing any magnitude.

> Ratios are not preserved by affine transformations. $(20\ \text{°C})/(10\ \text{°C}) = 2$, but the same two temperatures in kelvin give $(293.15\ \text{K})/(283.15\ \text{K}) \approx 1.035$. The "2" is an artefact of the chosen origin, and a scale that does not fix its origin cannot license it. Differences *are* preserved by affine maps, which is exactly why an interval scale licenses "10 degrees warmer" and refuses "twice as warm".

### Is counting a measurement?

> In the scheme's terms, counting is its discrete case: it binds a cardinality to a numeral, with the unit left implicit (one item) and the scale absolute. Whether that counts as *measurement* depends on which reading of measurement is meant, and the two readings agree here.

> Under this guide, measurement is the act of assigning a value to an observable under a scale, and counting satisfies it — the observable is the cardinality of a collection, the scale is absolute, the value is exact. Under the representational theory of measurement, measurement is a homomorphism from an empirical relational system into a numerical one, and counting is the special case whose empirical system is a set of distinguishable items ordered only by inclusion and identity.

> The consequence worth keeping is that counting has no uncertainty of the measurement kind. Its error is the failure to count correctly — a mistake, not a distribution around a true value. Cases in between, such as a census or a wildlife count, are aggregations with estimated cardinality: the scheme treats them as quantifications with a count unit whose uncertainty is real, and the difference from an exact tally is precisely whether the cardinality was observed or inferred.

### Why is logical quantification (∀, ∃) not this construct?

> Because the relata differ. Logical quantification binds a *variable* to a domain — $\forall x\, P(x)$, $\exists x\, P(x)$ — and its product is a truth condition for a formula, not a value for a magnitude. Nothing in it names a unit or a scale, and no comparison, combination, or conversion of magnitudes is licensed by it: "for all $x$" ranges over a domain, not over how much of an attribute an item carries.

> The confusion is etymological — both senses descend from *quantum*, "how much" — but the questions are different. The logical sense asks how many *things* in a domain satisfy a predicate; the quantitative sense asks how much of an attribute an item bears. The two meet in one place: the cardinality of a finite domain, which is why the boundary is worth stating rather than erasing. The logical construct is decomposed in logic, and the quantifier glyph is as inert in this scheme as the operator glyphs are in arithmetic.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Number](/note.html?p=notes/epistemica/mathematical/number/number.md) · [Quantitative Property](/note.html?p=notes/epistemica/mathematical/number/quantitative-property.md) · [Ratio](/note.html?p=notes/epistemica/mathematical/number/ratio.md) · [Fraction](/note.html?p=notes/epistemica/mathematical/number/fraction.md) · [Numeric System](/note.html?p=notes/epistemica/mathematical/number/numeric-system.md) · [Rounding](/note.html?p=notes/epistemica/mathematical/number/rounding.md)
- [Measurement Theory](/note.html?p=notes/epistemica/measurement/measurement-theory.md) · [System of Units of Measurement](/note.html?p=notes/epistemica/measurement/system-of-units-of-measurement.md) · [Enumeration (Counting)](/note.html?p=notes/epistemica/mathematical/discrete/enumeration-counting.md) · [Measure](/note.html?p=notes/epistemica/mathematical/measure/measure.md) · [Quantization](/note.html?p=notes/epistemica/mathematical/quantization.md)
- [Quantification (science)](https://en.wikipedia.org/wiki/Quantification_(science))
- Stevens, S. S. (1946). On the theory of scales of measurement. *Science*, 103(2684), 677–680.
- Suppes, P., Krantz, D. H., Luce, R. D., & Tversky, A. (1971). *Foundations of Measurement, Vol. I: Additive and Polynomial Representations*. Academic Press.
- BIPM. (2019). *The International System of Units (SI Brochure)*, 9th edition.
- JCGM. (2012). *International Vocabulary of Metrology — Basic and General Concepts and Associated Terms (VIM)*, 3rd edition.
- Hand, D. J. (2004). *Measurement Theory and Practice: The World Through Quantification*. Arnold.
