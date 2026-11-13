---
tags: [note, measurement, representation, quantity, order]
qa:
  - "is a nominal classification a measurement at all?"
  - "why is ordering a class of measurement and not a preliminary to it?"
  - "what exactly does a ratio scale license that an interval scale does not?"
  - "is the four-level scale hierarchy one construct or four?"
  - "can an ordinal scale ever carry a mean?"
  - "what decides which class an attribute belongs to — the procedure, the numerals, or the relations it carries?"
  - "is counting measurement?"
---

# measurement

> **measurement** assigns a value to an observable under a declared scale — a label, a rank, or a magnitude in a unit, depending on what the scale licenses. it is the genus under which every such assignment is read, and the scale is what divides it into classes: assign a *name* and it is categorization, a *rank* and it is ordering, a *magnitude in a unit* and it is quantification.

> the division is not a grading of better and worse measurement. it records what an assigned value may support: equality alone lets you sort items into classes; order lets you say one is more; a magnitude lets you say *how much more*, add two of them, and convert between units. each class is exact at what it does, and the error is not rising late in the hierarchy but claiming a class the scale does not license — a mean of ranks, a ratio of celsius temperatures, a distance between two labels.

> the classes share one act. to measure is to declare an empirical relational structure, choose a value system, and map the one into the other preserving the relations the class exploits. what changes between the classes is which relations are preserved: identity alone at categorization, identity and order at ordering, identity, order, difference, and — with a natural zero — ratio at quantification. that single requirement is what makes these one construct rather than three practices that happen to share a word.

> the scheme is empirical in a way a number is not. `3` measures nothing; `3 rd`, `class 3` and `3 kg` are three measurements of three classes, and only the last has a unit. see [quantification](/view.html?p=notes/epistemica/measurement/quantification.md) for the class that binds a magnitude, and [number](/view.html?p=notes/epistemica/mathematical/number/number.md) for the notation all three classes write in.

## formulation

### what is this epistemic instance?

> the **measurement instance** is the representational scheme that assigns a value to an observable under a declared scale. three components carry it, and the first is what sets the class:

> 1. **a scale class** — which relations of the observable the value must preserve. the classes are *categorization*, whose admissible transformation is any bijection of the labels; *ordering*, whose admissible transformation is any strictly increasing map — so order survives and distance does not; and *quantification*, whose admissible transformation is an affine rescaling at the interval level or a change of unit at the ratio level, so order, difference, and ratio survive in turn.
> 2. **a value** — what is assigned: a label, a rank, or a numeral. only in the quantitative class is it a numeral in a unit.
> 3. **a declaration** — the recorded statement of which class applies, since the same numeral can carry any of the three: `3` is a class label, a third place, or three of something. an undeclared measurement is read at whichever class the reader assumes, and that reading is where most measurement error enters.

> formally, let $\mathcal{A}$ be the empirical relational structure the observable carries — a set with the relations among its items that the method can register — and let $\mathcal{V}$ be a value system (a set of labels, of ranks, or of real numbers under arithmetic). a measurement is a map
>
> $$m : \mathcal{A} \to \mathcal{V}$$
>
> that is a homomorphism for the relations the declared class preserves, and the class is exactly the choice of which relations those are. the set of transformations $\varphi$ for which $\varphi \circ m$ is again admissible is the *uniqueness class* of the measurement, and a numerical statement about the value is meaningful precisely when it is invariant under that class.

> the classes nest because the relations nest. every quantitative measurement preserves order, and every order-preserving measurement preserves identity, so the classes form one chain of increasing structure. this is the sense in which ordering is a class of measurement and not a stage to be outgrown: an ordinal assignment that is exact at its class is a completed measurement, and it is only its misuse — reading it as interval — that makes it a poor one.

### what epistemic element type does this epistemic instance belong to?

> primary type: **`epistemic representation`** — the **measurement scheme**: the representational construct through which an observable is carried as a value under a declared scale, together with the sign system that carries the value and the rules that constitute the assignment.

> `readable as` an **`epistemic act`** when attention falls on a single act of assigning a value to one item. `readable as` an **`epistemic practice`** when attention falls on the organized doing — metrology, psychometrics, taxonomy, the institutional work that sustains a scale. `readable as` an **`epistemic construction`** when attention falls on a measurement statement as a description of a segment.

> the exclusion is argued, not asserted. an act has no constitutive parts to grow, so the scale, the declaration, and the class rules would have no home under it; the act fires the scheme, it is not what the scheme is made of. the practice is [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)'s subject, and a measurement statement is one product of the scheme, not the scheme.

> the observables measured are read in the **ontic order**; the scheme that binds them is epistemic. the ontic decomposition of a property or a magnitude belongs to the naturalis grammar: it is named here and never grown.

### is the type of this `epistemic element instance` ambiguous?

> yes, in four ways the decomposition keeps apart.

> **aspect.** *measurement* names the act of assigning a value, the scheme that makes the assignment well formed, and the result — a measurement statement. this note types the scheme; the act and the result stay `readable as` prose, so no row below carries two types.

> **class.** this is the ambiguity the note exists to resolve. a nominal, an ordinal and an interval reading share a notation and a vocabulary but not a licenced set of operations, and they are filed here as three classes of one scheme rather than as three schemes. the classes are decomposed in the notes that own them — [categorization](/view.html?p=notes/epistemica/measurement/categorization.md), [ordering](/view.html?p=notes/epistemica/measurement/ordering.md), [quantification](/view.html?p=notes/epistemica/measurement/quantification.md) — and this note decomposes the shared structure.

> **sense.** the false friends are load-bearing, and every one of them is a different construct:

| construct | what it does | why it is not this |
| --- | --- | --- |
| **measurement** | assigns a value to an observable under a declared scale | — |
| **quantification** | binds a magnitude to a numeral in a unit | one class of this scheme, the one that carries a unit (see [quantification](/view.html?p=notes/epistemica/measurement/quantification.md)) |
| **categorization** | assigns a label to an observable | one class, equality alone, no unit (see [categorization](/view.html?p=notes/epistemica/measurement/categorization.md)) |
| **ordering** | assigns a rank to an observable | one class, order without distance (see [ordering](/view.html?p=notes/epistemica/measurement/ordering.md)) |
| **measurement theory** | explains where a numerical assignment comes from | the representational account of the map, not the scheme it analyses (see [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)) |
| **measure** in mathematics | assigns a size to a set | a set function in measure theory, whose relatum is a set and whose value is not read on a declared scale of an attribute (see [measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md)) |
| **quantization** | replaces a continuum value by one of finitely many levels | it discretizes a range of values; it assigns nothing to an observable under a scale (see [quantization](/view.html?p=notes/epistemica/mathematical/quantization.md)) |
| **operationalization** | decides which observable stands for an attribute | the construction that precedes measurement — it fixes *what* is observed, not *how* the value is read (see [quantitative property](/view.html?p=notes/epistemica/mathematical/number/quantitative-property.md)) |

> **relatum.** only a property of a segment can be measured. the properties read here are ontic; the value assigned is epistemic. the naturalis grammar owns the decomposition of the property, and this note binds it without growing it.

> the ambiguity is resolved by declaring `epistemic representation` primary and by hanging the three classes as `scale` instances under one `representational system`, each of which a `convention` member of the shared substrate names. the classes are therefore read from the instance path itself — a class segment declares what a value may assert — and no class is a second scheme.

### what is the recursive instance decomposition of this epistemic instance?

> **boundary.** this table decomposes one epistemic instance — the measurement scheme — into the value system that carries an assigned value, the rules and structures constituting class membership, and the predicates it carries. the classes themselves are named here and decomposed in their own notes; the acts that exercise the scheme are named in prose and linked, never grown here; the observables measured belong to the naturalis grammar.

> **stopping rule.** a row is terminal when it names a scale level, a foundation, a convention, a formation rule, a transformation rule, an interpretation, or a predicate. the arithmetic that consumes a quantitative value is not decomposed here (see [arithmetic](/view.html?p=notes/epistemica/mathematical/number/arithmetic.md)), nor is the metrology that sustains a scale (see [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)).

> **identity.** instance tree path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch.

> **typing.** the root type is `epistemic representation`, declared once. the value system hangs under `representational system`; its constituents under `representation element` and `constitutive substrate`, by constitutive kind; its predicates under `has property`.

> **reading.** the tree is read as **representation**: it records how an observable is carried as a value, not how the segment bearing the property is parsed. the classes are the declared content of one scale structure, never separate schemes.

| instance tree path | description |
| --- | --- |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement | the scheme assigning a value to an observable under a declared scale — the genus whose classes are categorization, ordering and quantification. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` | grouping: the sign system carrying the assigned value. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ instance) measurement notation | the notation in which an assigned value is written and read: a label, a rank position, or a numeral with its unit, together with the class mark that fixes how it is read. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `representation element` | grouping: combinable constituents of the notation. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `representation element` (→ instance) observed property | the feature of the segment being assigned a value; read in the ontic order, never grown here. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `representation element` (→ instance) assigned value | what the notation records: a label, a rank, or a numeral — the product the declaration makes interpretable. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `representation element` (→ instance) value token | the written token itself — `two-way`, `3rd`, `9.81 m·s⁻²` — the part of the expression a reader decodes. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `representation element` (→ instance) class mark | the token or structure declaring which class the value is read at, and therefore which operations it licenses. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `representation element` (→ instance) measurement statement | the written assignment `that specimen is 12 mm` as a checkable artifact: the observable, the value, and the class taken together. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` | grouping: the rules and structures constituting the scheme and its classes. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` | grouping: the principles the scheme is founded on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) empirical relational structure | the observable's items together with the relations the method can register — identity, order, concatenation — antecedent to any assignment. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) representation homomorphism | the requirement that the assignment preserve the relations the class exploits; without it a value system is a parallel notation, not a representation. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) uniqueness condition | the class of transformations under which the assignment stays admissible — bijection, monotone map, affine map, unit change — which is what fixes the class and the meaning of the value. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) class nesting principle | the relations preserved by a class are preserved by every richer class — identity by all, order by ordering and quantification, difference by interval and ratio — which is why the classes form one chain rather than three schemes. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` | grouping: stabilized choices the scheme rests on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) nominal scale convention | values are labels: equality and difference of label alone; no order, distance, or arithmetic is licensed. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) ordinal scale convention | values are ranks: order is licensed, differences are not — first, second, third fixes a sequence, not a distance. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) interval scale convention | values are positions with an arbitrary zero: order and differences are licensed, ratios are not. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) ratio scale convention | values are multiples of a unit with a meaningful zero: order, differences, and ratios are licensed. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) class-declaration convention | the class a value is read at is recorded with it; an undeclared class leaves the meaning of the value to whichever class the reader assumes. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` | grouping: rules of well-formed assignments. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) class-admissibility rule | which operations a value admits at its declared class: equality at nominal, order at ordinal, differences at interval, ratios at ratio. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) class-assignment condition | when an observable may be assigned a value at a given class at all — the relations the observable must exhibit before that class is admissible. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) class-exhaustiveness rule | an assignment places each item in exactly one value at its class: a partition at nominal, a total preorder at ordinal. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` | grouping: licences rewriting one assignment into another within the class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) class-preserving transformation | the rewrite the class admits — relabelling, monotone re-ranking, affine rescaling, unit conversion — and therefore the boundary of what the value may assert. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` | grouping: assignments of meaning to the assigned value. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) class-level reading | what a value licenses a reader to conclude — sameness, order, difference, or ratio — according to its declared class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` | grouping: predicates the scheme carries, asserted of a measurement rather than registered from a segment. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) class | which of the three classes the measurement belongs to, and hence which operations it admits. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) level | the position within a class: nominal within categorization, ordinal within ordering, interval or ratio within quantification. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) meaningfulness | whether a numerical statement about the value survives every admissible transformation of its class — the test that separates a usable operation from an artefact of the numerals. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) representational precision | how much of the observable's relational structure the declared class captures: a partition loses the order an ordinal class keeps, an ordinal class loses the differences a quantitative one keeps. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) inter-measurement agreement | whether two independent assignments under the same declaration produce the same value — the replacement, at the nominal class, for the uncertainty a magnitude carries. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) measurement uncertainty | the doubt attached to an assigned value; carried as an interval or distribution in the quantitative class, and as disagreement among assigners where no magnitude exists. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) traceability | an unbroken chain of comparisons links the assignment to a declared reference — a standard unit, a defined label set, or an ordered criterion set. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) measurement (→ has property) `property` (→ instance) construct validity | whether the observable assigned a value actually stands for the property the measurement claims to measure, rather than a proxy correlated with it. |

### what is a critical conceptual evaluation of this `epistemic element instance`?

> **evaluated concept.** *measurement*, precisified as "the representational scheme that assigns a value to an observable under a declared scale, where the declared scale fixes which relations of the observable the value must preserve and therefore which class — categorization, ordering, or quantification — the assignment belongs to." the evaluation applies the criteria of the [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

> **verdict.** strong as a genus and determinately classed, weak on exactly the boundary the literature disputes. the precised definition decides, for any assignment, which class it is — the admissible transformation is the test, and it is checkable — and it refuses the vice the word usually permits, calling a label or a rank a quantity. what it does not settle is whether the two weaker classes are measurement at all, and the correction below answers that by construction rather than by argument.

| criterion | verdict | diagnostic focus |
| --- | --- | --- |
| conceptual identification | strong | distinguished from quantification (the class that carries a unit), categorization and ordering (the classes that carry none), measurement theory (the account of the map), measure (a set function), quantization (a discretization), and operationalization (the choice of observable). |
| definitional clarity | strong | "assigns a value to an observable under a declared scale" plus "the scale fixes the relations preserved" states the conditions outright; the class is defined by the uniqueness condition rather than by the numerals, which removes the usual vagueness. |
| conceptual determinacy | strong | boundary rule: the admissible transformations decide the class — bijection, strictly increasing map, affine map, unit change. borderline cases, such as an index that orders but does not space its categories, are classified by what the assignment preserves, not by how it is written. |
| definitional completeness | strong | classes, values, declarations, the homomorphism requirement, the uniqueness condition, and the class-nesting rule are all stated; exclusions are carried by the false-friend table rather than assumed. |
| internal consistency | strong | the classes are one scheme because their relations nest, and the nesting principle is a stated foundation, not an observation; the decomposition's class rows and the class notes cannot disagree without failing the admissibility rule. |
| structural coherence | strong | the shared substrate (foundations, conventions, formation, transformations, interpretation) is carried once and the classes carry only what differs; no class is a rival definition of the genus. |
| conceptual tractability | strong | name the observable, list its registrable relations, read off the admissible transformations, and the class follows — the procedure is finite and auditable. |
| extensional fidelity | moderate | the genus admits whole fields in which the weakest class is settled by convention (typologies, coding schemes), so the extension is only as reliable as the declaration behind each assignment. |
| intensional adequacy | strong | the defining property is what inquiry needs from measurement — that a value support the operations its class licenses — rather than the numerals' appearance. |
| ontological adequacy | strong | the genus is typed as a representation of an ontic property; labels ranking and magnitudes sit inside it as classes, never as separate kinds of entity. |
| discriminative power | strong | separates the three classes by the operations they license, which is the distinction that matters for every downstream use of a measured value. |
| granularity adequacy | moderate | one genus over three classes is coarse for psychometrics, where the ordinal-to-interval transition is the standing problem, and fine enough for the physical case — a granularity that follows the purpose, as the stopping rule allows. |
| representational coverage | strong | covers deterministic and probabilistic assignments, single and multi-attribute ones, and the discrete and continuous codomains; what it does not cover is named as excluded rather than absorbed. |
| ontological parsimony | strong | one genus, three classes, one scale structure, one substrate; the class notes add no root of their own. |
| conceptual distinctiveness | strong | the uniqueness-condition reading of the classes is the representational theory's own criterion, and it is what the common four-level vocabulary lacks when used as a list of names. |
| boundary differentiation | moderate | the boundary against *measurement theory* is stated, but the boundary against ordinary econometric and administrative usage — where "measured" means merely "recorded" — is only implied by the declaration requirement. |
| epistemic leverage | strong | one rule — read the admissible transformations — settles what a value supports, which is the most common error in applied measurement. |
| inferential productivity | strong | from the class follows what may be averaged, differenced, ratioed, or only compared, and every downstream statistical move inherits its licence. |
| explanatory power | moderate | it explains why a class-based error is a representational one rather than an arithmetic one, and it does not explain how an inquiry comes to adopt a scale, which is measurement theory's and metrology's work. |
| problem-solving utility | strong | the four-level vocabulary becomes checkable: an argument over "is this really interval-scaled?" is decided by the admissible transformations. |
| contextual robustness | strong | holds across the physical, biological, social, and administrative domains, because the criterion is relational and not substance-specific. |
| combinatorial fluidity | strong | joins the other philosophia grammars — the observable to naturalis, the value to arithmetic, the practice to the epistemic practice lane. |
| cross-domain portability | strong | travels from length to preference to classification without reformulation; only the value system changes. |
| temporal stability | moderate | the genus is stable, but which classes a domain accepts has moved historically — psychological measurement was forced into the quantitative class long before it satisfied the conditions. |
| operationalizability | strong | the declaration and the admissibility rule are the procedure; both are records, not judgements. |
| measurement validity | strong | the scheme does not measure its own subject; construct validity is carried as a property, which is the right place for it. |
| reliability | moderate | repeatability is strong where a procedure is standardized and weakest at the nominal class, where two coders can disagree without either being wrong. |
| inter-subjective reproducibility | moderate | declaration and admissibility make reproduction possible, and coding schemes still rely on conventions that must be adopted before they can be reproduced. |
| falsifiability | strong | the class claim is refutable: exhibit an operation the assignment licenses that the declared class forbids, or a transformation the class admits that changes a statement treated as meaningful. |
| sensitivity to evidence | strong | a demonstrated operation can promote a domain from ordinal to quantitative, and a demonstrated artefact can demote it back. |
| purpose adequacy | strong | exactly what is asked of a genus — classify, licence operations, expose misuse — at the price of not carrying any single class's machinery. |
| normative justification | strong | the only norm imposed is the declaration requirement, and it is a condition of intelligibility rather than a value judgement. |
| misuse resistance | moderate | the declaration and the admissibility rule block the central abuses, and the genus still permits a class to be declared on convention alone, which is where institutional pressure enters. |

> **standing objection, answered.** the representational theory's critics hold that nominal and ordinal assignments are not measurement, because measurement is the discovery of ratios among magnitudes and a label discovers none. the precised genus neither refutes nor concedes that: it holds that the three classes differ in the relations assigned, and that only the quantitative class establishes the ratio a quantitative science is built on. the common word denotes the family; the class decides how much of the claim is made. the position is not this note's invention — mari, maul, torres irribarra and wilson (2017) argue the metrological case that quantification is neither necessary nor sufficient for measurement, and separate the three concepts so that a definition of measurement can apply beyond physics without being trivialized.

## qa

### is a nominal classification a measurement at all?

> under this scheme, yes — and the answer costs nothing to the quantitative reading. a classification is an assignment of a value to an observable under a declared scale, the scale licenses equality and nothing more, and that is a complete class rather than a failed quantity. what makes it a measurement in this sense is that it is a homomorphism for identity: two items get the same label exactly when identity is the only relation the method registered.

> the standing objection is that this only relabels classification as measurement. the honest reply is that the scheme does not claim more for it — a nominal value licenses no order, no mean, and no distance, and the admissibility rule forbids exactly those operations. the cost of calling it measurement is only that the word no longer implies a ratio; the benefit is that one rule explains why a mean of eye-colour codes is an error rather than a statistical choice.

### why is ordering a class of measurement and not a preliminary to it?

> because the order it establishes is the empirical relation measurement exists to preserve. an ordinal assignment reports a real fact — that one item is more than another — and the fact is what the procedure was built to register; the distance it cannot report was never observed, so the class is exact at what it does rather than approximate at what it does not.

> the class becomes a preliminary only through a category mistake: treating the assigned rank as a spacing, computing means and differences with it, and calling the result quantitative. the correction is not to stop ordering but to stop reading the order at the wrong class — see [ordering](/view.html?p=notes/epistemica/measurement/ordering.md).

### what exactly does a ratio scale license that an interval scale does not?

> ratios, because it alone fixes a zero that means absence. the interval scale's zero is a convention, movable by an affine rescaling that leaves the empirical content intact — which is why `20 °c` is not twice `10 °c` while `20 kg` is twice `10 kg`. the general test is the one the scheme states as a foundation: a numerical statement is licensed when it survives every admissible transformation of its class.

## references

- [Quantification](/view.html?p=notes/epistemica/measurement/quantification.md)
- [Categorization](/view.html?p=notes/epistemica/measurement/categorization.md)
- [Ordering](/view.html?p=notes/epistemica/measurement/ordering.md)
- [Measurement Theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)
- [Measurement System](/view.html?p=notes/epistemica/measurement/system.md)
- [International System of Units](/view.html?p=notes/epistemica/measurement/isu.md)
- [Measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md)
- [Quantitative Property](/view.html?p=notes/epistemica/mathematical/number/quantitative-property.md)
- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- helmholtz, h. von. (1887). *zählen und messen, erkenntnistheoretisch betrachtet*. in *philosophische aufsätze* (pp. 17–52). fues's verlag.
- hölder, o. (1901). die axiome der quantität und die lehre vom mass. *berichte über die verhandlungen der königlich sächsischen gesellschaft der wissenschaften zu leipzig*, 53, 1–64.
- campbell, n. r. (1920). *physics: the elements*. cambridge university press.
- stevens, s. s. (1946). on the theory of scales of measurement. *science*, 103(2684), 677–680.
- suppes, p., & zinnes, j. l. (1963). basic measurement theory. in r. d. luce, r. r. bush, & e. galanter (eds.), *handbook of mathematical psychology* (vol. 1, pp. 1–76). wiley.
- krantz, d. h., luce, r. d., suppes, p., & tversky, a. (1971). *foundations of measurement, vol. i: additive and polynomial representations*. academic press.
- roberts, f. s. (1979). *measurement theory: with applications to decisionmaking, utility, and the social sciences*. addison-wesley. see [the entry](/view.html?p=documents/books/roberts-1979-measurement-theory-addison-wesley.md).
- narens, l. (1985). *abstract measurement theory*. mit press.
- michell, j. (1997). quantitative science and the definition of measurement in psychology. *british journal of psychology*, 88(3), 355–383.
- mari, l., maul, a., torres irribarra, d., & wilson, m. (2017). quantities, quantification, and the necessary and sufficient conditions for measurement. *measurement*, 100, 115–121. <https://doi.org/10.1016/j.measurement.2016.12.050>
- tal, e. (2017). measurement in science. in e. n. zalta (ed.), *the stanford encyclopedia of philosophy*. stanford university.

### lectures and talks

> titles, makers and channels as published; the gloss says what each is, not what it covers.

- *foundations of measurement* — lecture series, kristina kozaj. a series on the foundations of measurement. <https://www.youtube.com/playlist?list=PLrKlhVqlZwK6UcJ7K-XpaLmWoGehnXLAX>
- *how we measure the world* — michael de podesta, the royal institution. a lecture on measurement as metrology practises it. <https://www.youtube.com/watch?v=dguZLChkRV8>
- *reginald victor jones' 1981 christmas lectures* — the royal institution. the royal institution's 1981 christmas lectures. <https://www.youtube.com/playlist?list=PLbnrZHfNEDZw-UIpDJcH_g8d6Ii84pEDs>
- *measurement science* — tu delft opencourseware, coord. m. pertijs. a bachelor course on measurement systems: sensors, readout and signal conditioning, instrumentation amplifiers, adcs, and instruments; error sources and uncertainty in results. <https://ocw.tudelft.nl/courses/measurement-science/>
