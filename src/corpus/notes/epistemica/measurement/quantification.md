---
tags: [note, measurement, quantification, quantity, representation]
qa:
  - "why does a ratio scale license 'twice as much' while an interval scale does not?"
  - "is counting a measurement?"
  - "why is logical quantification (∀, ∃) not this construct?"
  - "where does quantification end and ordering begin?"
  - "what is the structure of an instance of quantification — property, procedure, unit?"
  - "what makes a property quantitatively determinable, and when do two items map to the same unit?"
  - "what makes a quantity additive, and how is non-additivity handled?"
  - "what determines which mathematical operations are valid on a quantified value?"
  - "what establishes the correspondence between a magnitude and a numerical value?"
  - "how is a unit established, and why is that part of the procedure?"
  - "how do we distinguish precision from accuracy?"
  - "what makes a measurement traceable and reproducible?"
  - "what do we gain with quantification — comparison, operation, relation?"
---

# quantification

> **quantification** binds a magnitude to a number: it fixes a scale, names a unit, and writes a value — so that *more than* becomes *how much*, and the result can be compared, combined, and converted. it is the representational scheme through which the quantitative properties of reality enter arithmetic.

> the scheme is not one act. counting binds a cardinality to a numeral with the unit left implicit; measuring binds a magnitude to a numeral in a unit; estimating binds an interval around it. what they share is the structure this note decomposes: a scale that licenses certain readings, a unit that fixes what the numeral counts in multiples of, and a notation that carries both.

> a quantity is never a bare number. `42` quantifies nothing until a unit and a scale say what kind of magnitude it stands for and which operations it admits: `42 kg` is a mass, `42 °c` an interval-scaled temperature, and `42` alone is as likely a count as a line number. remove the unit and the quantity is gone, though the number remains.

> quantification is one class of [measurement](/view.html?p=notes/epistemica/measurement/measurement.md), not its whole. categorization assigns a label, ordering assigns a rank, and only quantification assigns a magnitude. the three share the act of assigning a value under a declared scale, which is why one genus covers them; they part at the unit, which only this class has.

> numbers and the schemes that bind them to magnitudes co-evolve: what counts as quantifiable is partly fixed by the notation available for it, and the notation is extended by what inquiry needs to quantify (see [number](/view.html?p=notes/epistemica/mathematical/number/number.md)).

## formulation

### what is this epistemic instance?

> the **quantification instance** is the representational scheme that assigns a numeric value to a magnitude under a declared unit and scale. three components carry it, and none stands alone:
>
> 1. **a scale** — the structure of admissible comparisons. within the quantitative class the assignment licenses two levels: *interval* (order and differences, no ratios) and *ratio* (order, differences, and ratios, with a meaningful zero). an *absolute* scale is the ratio case whose unit is the natural count. the other two classes of measurement — *categorization*, whose scale licenses equality alone, and *ordering*, whose scale licenses order without distance — carry no unit and no magnitude, so they are decomposed in their own notes and reached from [measurement](/view.html?p=notes/epistemica/measurement/measurement.md), never from here.
> 2. **a unit** — the reference magnitude in which the value is expressed, together with the system that fixes which units are admitted and how derived ones compose (si, cgs, imperial, natural).
> 3. **a numeral** — the value written against that unit: how many times the reference magnitude the magnitude is.

> formally, a quantification of a quantitative attribute $a$ of a segment is a map
>
> $$q : a \to \mathbb{r} \times u, \qquad q(a) = (v, u),$$
>
> together with a scale structure $s$ under which $v$ is read. the map is not arbitrary: it must preserve the empirical relations the attribute carries — if $a_1$ is longer than $a_2$ then $q(a_1) > q(a_2)$; if $a_3$ is the concatenation of $a_1$ and $a_2$ then $v_3 = v_1 + v_2$ in the same unit. which relations must be preserved is exactly what the declared scale level says.

> the scheme is portable across attributes: the same structure quantifies a length, a mass, a duration, a probability, a price, a count. what changes between them is the unit, the dimension, and the level — never the form of the binding.

### what epistemic element type does this epistemic instance belong to?

> primary type: **`epistemic representation`** — the **quantification scheme**: the representational construct through which a magnitude is carried as a number in a unit on a scale, together with the sign system and the rules that constitute it.

> `readable as` an **`epistemic act`** when attention falls on a single act of assigning a value — the guide types `measurement` as an action element, and counting, estimating, and ranking sit at the same grain. `readable as` an **`epistemic practice`** when attention falls on the organized doing — metrology, the laboratories and standards bodies that sustain it. `readable as` an **`epistemic construction`** when attention falls on a quantity statement as a description of a segment.

> the exclusion is argued, not asserted. an act has no constitutive parts to grow, so the scale levels, the unit systems, and the conversion rules decomposed below would have no home under it — the act is what fires the scheme, not what the scheme is made of. the practice is [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)'s subject, and a quantity statement is one product of the scheme, not the scheme.

> the magnitudes quantified are read in the **ontic order**; the scheme that binds them is epistemic. the ontic decomposition of a magnitude belongs to the naturalis grammar: it is named here and never grown.

### is the type of this `epistemic element instance` ambiguous?

> yes, in four ways the decomposition keeps apart.

> **aspect.** *quantification* names the act of assigning a value, the scheme that makes the assignment well formed, and the result — a quantity. this note types the scheme; the act and the result stay `readable as` prose, so no row below carries two types.

> **sense.** the false friends are load-bearing, and every one of them is a different construct:

| construct | what it does | why it is not this |
| --- | --- | --- |
| **quantification** | binds a magnitude to a number under a declared unit and scale | — |
| **measurement** (the genus) | assigns a value to an observable under a declared scale | wider: it also covers the classes that assign a label or a rank and bind no magnitude (see [measurement](/view.html?p=notes/epistemica/measurement/measurement.md)) |
| **quantization** | replaces a value drawn from a continuum by one of finitely many levels | it discretizes a range of values; it binds nothing to a unit or a scale (see [quantization](/view.html?p=notes/epistemica/mathematical/quantization.md)) |
| **categorization** | assigns a label to an observable | a class of measurement that licenses equality alone — no order, no unit (see [categorization](/view.html?p=notes/epistemica/measurement/categorization.md)) |
| **ordering** | assigns a rank to an observable | a class of measurement that licenses order but no distance (see [ordering](/view.html?p=notes/epistemica/measurement/ordering.md)) |
| **measurement theory** | explains where a numerical assignment comes from | the representational account of the map, not the scheme it analyses (see [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)) |
| **counting** | assigns a cardinality to a collection | the scheme's discrete case, with the unit implicit (see [enumeration](/view.html?p=notes/epistemica/mathematical/discrete/enumeration-counting.md)) |
| **measure** in mathematics | assigns a size to a set | a set function in measure theory, not a binding of a magnitude to a unit (see [measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md)) |
| **logical quantification** | binds a variable under ∀ or ∃ | it ranges over a domain of things, not over how much of an attribute an item carries |

> **level.** the magnitude reading is licensed only from the interval level up. "twice as hot" is meaningless on an interval scale, and "twice the number" is meaningless on a nominal one — but the nominal case is not a *quantification* at all. it is categorization, a class of measurement that assigns a label where this scheme assigns a magnitude. the boundary is drawn in [measurement](/view.html?p=notes/epistemica/measurement/measurement.md) and developed in [categorization](/view.html?p=notes/epistemica/measurement/categorization.md) and [ordering](/view.html?p=notes/epistemica/measurement/ordering.md); this note carries only the two levels that bind a magnitude.

> **relatum.** only a quantitative property can be quantified. turning a quality into a measurable attribute is itself a construction — operationalization — and its warrant belongs to measurement theory rather than here; see [quantitative property](/view.html?p=notes/epistemica/mathematical/number/quantitative-property.md).

> the ambiguity is resolved by declaring `epistemic representation` primary, typing the five scale levels as `convention`s of one substrate, and keeping the modes — counting, measuring, estimating, ranking — as prose. filing the modes as sub-schemes would split one representation into four; filing the levels as sub-schemes would make an interval reading a different construct from a ratio reading of the same magnitude.

### what is the recursive instance decomposition of this epistemic instance?

> **boundary.** this table decomposes one epistemic instance — the quantification scheme — into the sign system that carries it, the rules and structures constituting it, and the predicates it carries. the acts that exercise the scheme are named in prose and linked, never grown here; the same holds for the magnitudes bound, whose decomposition belongs to the naturalis grammar.

> **stopping rule.** a row is terminal when it names a notation element, a foundation, a convention, a formation rule, a transformation rule, an interpretation, or a predicate. the arithmetic that consumes the value is not decomposed here (see [arithmetic](/view.html?p=notes/epistemica/mathematical/number/arithmetic.md)), and neither is the metrology that produces it (see [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)).

> **identity.** instance tree path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch.

> **typing.** the root type is `epistemic representation`, declared once. the notation hangs under `representational system`; its constituents under `representation element`; its rules under `constitutive substrate`, by constitutive kind. the predicates hang by `has property`, which asserts a feature of the element rather than registering one from a segment.

> **reading.** the tree is read as **representation**: it records how a magnitude is carried, not how the segment that bears the magnitude is parsed. the scale levels are conventions of this one substrate, never separate schemes.

| instance tree path | description |
| --- | --- |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement | the scheme assigning a value to an observable under a declared scale — the genus through which categorization, ordering and quantification are read as one construct. see [measurement](/view.html?p=notes/epistemica/measurement/measurement.md). |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` | grouping: the sign system carrying the bound value — one system elaborated by three classes. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale | the structure of admissible comparisons over the observable: which relations among items the assigned values must preserve. the class is the declared content of the scale, never an extra component. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) categorization class | grouping: values are labels; equality and difference of label alone are licensed. see [categorization](/view.html?p=notes/epistemica/measurement/categorization.md). |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) categorization class (→ instance) nominal scale | the scale whose admissible transformation is any bijection of the label set — labels name classes and fix nothing about order, distance or amount. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) ordering class | grouping: values are ranks; order is licensed, distance is not. see [ordering](/view.html?p=notes/epistemica/measurement/ordering.md). |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) ordering class (→ instance) ordinal scale | the scale whose admissible transformation is any strictly increasing map — the order among items survives, the gaps between them do not. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class | grouping: values are magnitudes in a unit; order, difference, and — with a natural zero — ratio. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ instance) interval scale | the quantitative scale whose admissible transformation is affine — order and differences survive, ratios do not; the zero is a convention. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ instance) ratio scale | the quantitative scale whose admissible transformation is a change of unit — order, differences and ratios survive, and the zero means absence of the magnitude. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ instance) absolute scale | the ratio case whose unit is fixed by the attribute itself — counts of a natural unit, where nothing is rescalable. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` | grouping: the rules and structures constituting class membership. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `foundation` | grouping: the principles class membership is founded on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) empirical relational structure | the relations the observable actually carries — identity, order, concatenation — antecedent to any assignment; a class is admissible only if its values preserve them. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) representation homomorphism | the requirement that the assignment map the relational structure into the value system while preserving the relations the class exploits. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) uniqueness condition | the class of transformations under which the assignment stays admissible; this, and not the numerals, decides what a value statement means. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `convention` | grouping: the stabilized choices class membership rests on — nominal, ordinal, interval, ratio, and each unit system are declared conventions of this one substrate, never separate constructs. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `convention` (→ instance) class-declaration convention | the class a value belongs to is recorded with it; an undeclared class leaves the meaning of the numeral to chance. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `formation` | grouping: rules of well-formed value statements. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `formation` (→ instance) class-admissibility rule | which operations a value admits at its declared class: equality at nominal, order at ordinal, differences at interval, ratios at ratio. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `transformation rule` | grouping: licences rewriting one value statement into another within the class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) class-preserving transformation | the rewrite the class admits — relabelling, monotone re-ranking, affine rescaling, or unit conversion — and therefore the boundary of what the value may assert. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `interpretation` | grouping: assignments of meaning to the assigned value. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) class-level reading | what a value licenses a reader to conclude — sameness, order, difference, or ratio — according to its declared class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` | grouping: the sign system carrying the bound quantity. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ instance) quantity notation | numeral, unit symbol, and scale mark taken together: the notation in which a quantified magnitude is written, read, and checked. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` | grouping: combinable constituents of the notation. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` (→ instance) magnitude | the size the value stands for — what the numeral measures in multiples of the unit; read in the ontic order, never grown here. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` (→ instance) numeric value | the numeral bound to the magnitude: the number of units the notation records. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` (→ instance) unit | the reference magnitude in which the value is expressed — the standard of the same kind that the magnitude is a multiple of. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` (→ instance) unit symbol | the written token naming the unit — `m`, `kg`, `s`, `%`, `°c` — the part of the expression a reader decodes. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` (→ instance) quantity expression | the written quantity `9.81 m·s⁻²` as a checkable artifact: numeral, unit symbol, and exponent composed under the formation rules. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `representation element` (→ instance) scale mark | the token or structure declaring the admissible readings — a rank position, a category label, an interval marker — and therefore the level the value is read at. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` | grouping: the rules and structures constituting the scheme. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` | grouping: the principles the scheme is founded on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) dimensional basis | the assignment of base quantities — length, mass, time, electric current, temperature, amount of substance, luminous intensity — from which every derived dimension is a product of powers. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) commensurability principle | a magnitude can be compared with, and expressed as a multiple of, a unit of the same kind; without it the binding is undefined. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) additivity assumption | concatenating two magnitudes of the same kind adds their measures — the assumption that makes extensive quantities add and leaves intensive ones without a sum. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` | grouping: stabilized choices the scheme rests on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) nominal scale convention | values are names: equality and difference alone; the numerals are labels, and no order or arithmetic is licensed. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) ordinal scale convention | values are ranks: order is licensed, differences are not — first, second, third fixes a sequence, not a distance. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) interval scale convention | values are positions with an arbitrary zero: order and differences are licensed, ratios are not — 20 °c is not twice 10 °c. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) ratio scale convention | values are multiples of a unit with a meaningful zero: order, differences, and ratios are licensed — 20 kg is twice 10 kg. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) absolute scale convention | values are counts of a natural unit: the ratio case whose unit is fixed by the attribute itself — 5 items, 3 events, 2 children. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) unit system convention | the declared family of units — si, cgs, imperial, natural — fixing which units are admitted and how derived units compose. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) prefix convention | the decimal multiples and submultiples of a unit — kilo, milli, micro — written as prefixes rather than as separate units. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) zero-point convention | what the zero of the scale denotes: absence of the magnitude, an arbitrary origin, or a distinguished reference point such as 0 °c. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) significant-figures convention | how many digits the written value carries, and therefore how much precision it claims to have. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) uncertainty-reporting convention | how the doubt is attached to the value — a standard uncertainty, an interval, or a coverage factor — and at which digit it is stated. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) traceability convention | a value stands only if an unbroken chain of comparisons links it to a declared reference standard. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` | grouping: rules of well-formed quantity expressions. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) dimensional homogeneity rule | only quantities of the same dimension may be equated, added, or compared — `3 m + 2 s` is not a well-formed expression. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) quantity expression formation rule | how numeral, unit symbol, and exponent compose into a well-formed quantity — `9.81 m·s⁻²`, never `m 9.81 s⁻²`. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) scale-admissibility rule | which operations a value admits at its declared level: equality at nominal, order at ordinal, differences at interval, ratios at ratio. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` | grouping: licences rewriting one quantity expression into another. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) unit conversion rule | rewrite into another unit of the same dimension by multiplying by the conversion factor — `1 km ↦ 1000 m`; the magnitude is preserved, the numeral is not. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) rescaling rule | rewrite under an affine change of scale — factor and offset, as `°c ↦ k` or a logarithmic unit — the case where the zero moves. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) nondimensionalization rule | rewrite a dimensional quantity as a dimensionless number by dividing it by a reference of the same dimension. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) dimensional analysis rule | rewrite a relation into its dimension products alone, licensing a check on any equation before it is trusted. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) normalization rule | rewrite values into a common range or distribution — min–max, z-score — so that quantities in different units become comparable. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` | grouping: assignments of meaning to the written quantity. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) magnitude denotation | the numeral denotes a multiple of the unit: `3.2 m` means 3.2 times the reference metre. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) scale-level reading | what a reader may conclude from the value: equality, order, difference, or ratio, according to the declared level. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) zero reading | what the zero of the scale says about the attribute: absence of the magnitude, an arbitrary origin, or a conventional reference point. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` | grouping: predicates the scheme carries, asserted of a quantification rather than registered from a segment. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) precision | how close repeated quantifications of the same magnitude fall to one another — a predicate of the scheme's execution, not of the magnitude. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) accuracy | how close a quantified value falls to the magnitude it stands for. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) resolution | the smallest difference in magnitude the notation can express at the declared precision — the granularity of the scale. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) measurement uncertainty | the doubt attached to a value, carried as an interval or a distribution rather than as a single number. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) dimension | the kind of magnitude a quantity belongs to, expressed as a product of powers of the base dimensions. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) commensurability | whether two quantities can be expressed in a common unit, and therefore compared or combined at all. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) additivity | whether concatenating two magnitudes adds their values — the extensive case, denied to intensive quantities. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) unit invariance | the magnitude is invariant under conversion; only the written value changes, and the scheme is worthless if it does not. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) sensitivity | how much the written value changes per unit change of the magnitude — the derivative the notation can resolve. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) scale (→ instance) quantification class (→ has property) `property` (→ instance) construct validity | whether the scale quantifies the attribute it claims to quantify, rather than a proxy correlated with it. |
### what is a critical conceptual evaluation of this `epistemic element instance`?

> **verdict.** the scheme is determinate where its declaration is explicit and indeterminate where it is left implicit: once the scale class and level, the unit, and the dimension are fixed, every question this note asks has a checkable answer — which operations are licensed, which rewrites preserve the magnitude, which expressions are well formed. its weakness is the same explicitness: the classic errors in quantitative work — a mean of ordinal ranks, a ratio of celsius temperatures, a conversion that silently changes dimension — are failures of the declaration, not of the arithmetic, and the definition cannot by itself prevent them.

| criterion | verdict | diagnostic focus |
| --- | --- | --- |
| conceptual identification | strong | distinguished from measurement (the genus, which admits label and rank), categorization and ordering (the classes that bind no magnitude), quantization (a value-range discretization), measure (a set function), counting (the discrete case with an implicit unit), and logical quantification (variable binding); the scheme's three components are stated outright. |
| definitional clarity | strong | "scale, unit, numeral" plus "the map preserves the empirical relations the attribute carries" are stated conditions, not metaphors; each scale level is named with the operations it licenses. |
| conceptual determinacy | moderate | boundary rule: a claim is a quantification iff a magnitude is bound to a value under a declared scale. borderline cases — ordinal indices, composite scores, proxy metrics — are decided by the declared level rather than by the numeral, which is why the level must be recorded, not assumed. |
| internal consistency | strong | the interval and ratio levels are conventions of one substrate, never rival definitions of the scheme, and the other two classes of measurement are excluded from the table rather than demoted to it; the conversion rules preserve the magnitude exactly as the interpretation says they must, so notation and meaning cannot drift apart. |
| representational adequacy | strong | elements, foundations, conventions, formation rules, transformations, and interpretations are carried in separate branches, so a scale-level claim is never confused with a notational one and a predicate is never mistaken for a constituent. |
| purpose adequacy | strong | the scheme serves the three uses quantification exists for — comparison, combination, and conversion — and it never claims a magnitude reading where only an ordering one is licensed, which is what the class boundary in [measurement](/view.html?p=notes/epistemica/measurement/measurement.md) enforces. |

## qa

### why does a ratio scale license "twice as much" while an interval scale does not?

> because a ratio needs a zero that means absence. on a ratio scale the value is a multiple of the unit: 0 kg is no mass, and 20 kg is exactly twice 10 kg, because both are multiples of the same unit from the same origin. on an interval scale the zero is a convention rather than an absence: 0 °c is the freezing point of water, not the absence of temperature, and the origin can be moved by an affine rescaling without changing any magnitude.

> ratios are not preserved by affine transformations. $(20\ \text{°c})/(10\ \text{°c}) = 2$, but the same two temperatures in kelvin give $(293.15\ \text{k})/(283.15\ \text{k}) \approx 1.035$. the "2" is an artefact of the chosen origin, and a scale that does not fix its origin cannot license it. differences *are* preserved by affine maps, which is exactly why an interval scale licenses "10 degrees warmer" and refuses "twice as warm".

### is counting a measurement?

> in the scheme's terms, counting is its discrete case: it binds a cardinality to a numeral, with the unit left implicit (one item) and the scale absolute. whether that counts as *measurement* depends on which reading of measurement is meant, and the two readings agree here.

> under this guide, measurement is the act of assigning a value to an observable under a scale, and counting satisfies it — the observable is the cardinality of a collection, the scale is absolute, the value is exact. under the representational theory of measurement, measurement is a homomorphism from an empirical relational system into a numerical one, and counting is the special case whose empirical system is a set of distinguishable items ordered only by inclusion and identity.

> the consequence worth keeping is that counting has no uncertainty of the measurement kind. its error is the failure to count correctly — a mistake, not a distribution around a true value. cases in between, such as a census or a wildlife count, are aggregations with estimated cardinality: the scheme treats them as quantifications with a count unit whose uncertainty is real, and the difference from an exact tally is precisely whether the cardinality was observed or inferred.

### why is logical quantification (∀, ∃) not this construct?

> because the relata differ. logical quantification binds a *variable* to a domain — $\forall x\, p(x)$, $\exists x\, p(x)$ — and its product is a truth condition for a formula, not a value for a magnitude. nothing in it names a unit or a scale, and no comparison, combination, or conversion of magnitudes is licensed by it: "for all $x$" ranges over a domain, not over how much of an attribute an item carries.

> the confusion is etymological — both senses descend from *quantum*, "how much" — but the questions are different. the logical sense asks how many *things* in a domain satisfy a predicate; the quantitative sense asks how much of an attribute an item bears. the two meet in one place: the cardinality of a finite domain, which is why the boundary is worth stating rather than erasing. the logical construct is decomposed in logic, and the quantifier glyph is as inert in this scheme as the operator glyphs are in arithmetic.

## references

- [philosophia artium epistemicarum et operis](https://raw.githubusercontent.com/csiglab/naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [number](/view.html?p=notes/epistemica/mathematical/number/number.md) · [quantitative property](/view.html?p=notes/epistemica/mathematical/number/quantitative-property.md) · [ratio](/view.html?p=notes/epistemica/mathematical/number/ratio.md) · [fraction](/view.html?p=notes/epistemica/mathematical/number/fraction.md) · [numeric system](/view.html?p=notes/epistemica/mathematical/number/numeric-system.md) · [rounding](/view.html?p=notes/epistemica/mathematical/number/rounding.md)
- [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md) · [system of units of measurement](/view.html?p=notes/epistemica/measurement/isu.md) · [enumeration (counting)](/view.html?p=notes/epistemica/mathematical/discrete/enumeration-counting.md) · [measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) · [quantization](/view.html?p=notes/epistemica/mathematical/quantization.md)
- [quantification (science)](https://en.wikipedia.org/wiki/quantification_(science))
- stevens, s. s. (1946). on the theory of scales of measurement. *science*, 103(2684), 677–680.
- suppes, p., krantz, d. h., luce, r. d., & tversky, a. (1971). *foundations of measurement, vol. i: additive and polynomial representations*. academic press.
- bipm. (2019). *the international system of units (si brochure)*, 9th edition.
- jcgm. (2012). *international vocabulary of metrology — basic and general concepts and associated terms (vim)*, 3rd edition.
- hand, d. j. (2004). *measurement theory and practice: the world through quantification*. arnold.

### foundations, historically ordered

the representational line, oldest first. each entry supplies something the scheme above takes as given: what a quantity is, when an additive unit can exist, and which transformations leave a quantitative statement meaningful.

- helmholtz, h. von. (1887). *zählen und messen, erkenntnistheoretisch betrachtet*. in *philosophische aufsätze* (pp. 17–52). fues's verlag.
- hölder, o. (1901). die axiome der quantität und die lehre vom mass. *berichte über die verhandlungen der königlich sächsischen gesellschaft der wissenschaften zu leipzig*, 53, 1–64.
- campbell, n. r. (1920). *physics: the elements*. cambridge university press.
- bridgman, p. w. (1927). *the logic of modern physics*. macmillan.
- stevens, s. s. (1946). on the theory of scales of measurement. *science*, 103(2684), 677–680.
- scott, d., & suppes, p. (1958). foundational aspects of theories of measurement. *the journal of symbolic logic*, 23(2), 113–128.
- suppes, p., & zinnes, j. l. (1963). basic measurement theory. in r. d. luce, r. r. bush, & e. galanter (eds.), *handbook of mathematical psychology* (vol. 1, pp. 1–76). wiley.
- luce, r. d., & tukey, j. w. (1964). simultaneous conjoint measurement. *journal of mathematical psychology*, 1(1), 1–27.
- pfanzagl, j. (1968). *theory of measurement*. wiley.
- krantz, d. h., luce, r. d., suppes, p., & tversky, a. (1971). *foundations of measurement, vol. i: additive and polynomial representations*. academic press.
- krantz, d. h., luce, r. d., suppes, p., & tversky, a. (1989). *foundations of measurement, vol. ii: geometrical, threshold, and probabilistic representations*. academic press.
- luce, r. d., krantz, d. h., suppes, p., & tversky, a. (1990). *foundations of measurement, vol. iii: representation, axiomatization, and invariance*. academic press.
- roberts, f. s. (1979). *measurement theory: with applications to decisionmaking, utility, and the social sciences* (encyclopedia of mathematics and its applications, vol. 7). addison-wesley. see [the entry](/view.html?p=documents/books/roberts-1979-measurement-theory-addison-wesley.md).
- narens, l. (1985). *abstract measurement theory*. mit press.
- michell, j. (1990). *an introduction to the logic of psychological measurement*. erlbaum.
- michell, j. (1997). quantitative science and the definition of measurement in psychology. *british journal of psychology*, 88(3), 355–383.
- roche, j. (1998). *the mathematics of measurement: a critical analysis*. athlone press.

### the history of quantification as a practice

the scheme's components were not discovered together: a scale arrives before a unit, a unit before a system, a system before a standard others will accept. these track that order.

- kohlrausch, f. (1894). *an introduction to physical measurements* (t. h. waller & h. r. procter, trans.; 3rd ed.). j. & a. churchill. see [the entry](/view.html?p=documents/books/kohlrausch-1894-introduction-physical-measurements-churchill.md).
- kuhn, t. s. (1961). the function of measurement in modern physical science. *isis*, 52(2), 161–193.
- frängsmyr, t., heilbron, j. l., & rider, r. e. (eds.). (1990). *the quantifying spirit in the 18th century*. university of california press. see [the entry](/view.html?p=documents/books/frangsmyr-heilbron-rider-1990-quantifying-spirit-university-california.md).
- wise, m. n. (ed.). (1995). *the values of precision*. princeton university press.
- crosby, a. w. (1997). *the measure of reality: quantification and western society, 1250–1600*. cambridge university press. see [the entry](/view.html?p=documents/books/crosby-1997-measure-reality-quantification-western-europe.md).
- chang, h. (2004). *inventing temperature: measurement and scientific progress*. oxford university press.

### quantification as a social technology

the numeral's authority is not derivational. these are the accounts of where it comes from, and what it costs.

- porter, t. m. (1992). quantification and the accounting ideal in science. *social studies of science*, 22(4), 633–651.
- porter, t. m. (1995). *trust in numbers: the pursuit of objectivity in science and public life*. princeton university press. see [the entry](/view.html?p=documents/books/porter-1995-trust-in-numbers-princeton.md).
- desrosières, a. (1998). *the politics of large numbers: a history of statistical reasoning* (c. naish, trans.). harvard university press.
- poovey, m. (1998). *a history of the modern fact: problems of knowledge in the sciences of wealth and society*. university of chicago press.
- espeland, w. n., & stevens, m. l. (1998). commensuration as a social process. *annual review of sociology*, 24, 313–343.
- merry, s. e. (2016). *the seductions of quantification: measuring human rights, gender violence, and sex trafficking*. university of chicago press.
- tal, e. (2017). measurement in science. in e. n. zalta (ed.), *the stanford encyclopedia of philosophy* (fall 2017 ed.). stanford university.
- muller, j. z. (2018). *the tyranny of metrics*. princeton university press.
