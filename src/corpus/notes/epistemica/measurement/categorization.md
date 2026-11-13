---
tags: [note, measurement, categorization, classification, nominal]
qa:
  - "is a nominal classification a measurement at all?"
  - "what makes a classification exhaustive rather than merely descriptive?"
  - "why is inter-coder agreement not a measurement uncertainty?"
  - "when is a code a measurement and when is it a mere tag?"
  - "can a classification be wrong without being unreliable?"
  - "why does the nominal class forbid a mean?"
---

# categorization

> **categorization** assigns a label to an observable: each item of the observed segment receives a value drawn from a declared label set, and the value records which class of items the item belongs to. it is the weakest class of [measurement](/view.html?p=notes/epistemica/measurement/measurement.md) and the one most of inquiry uses, because most observables are registered by deciding *which kind* they are before anything else is asked of them.

> the scale licenses equality and nothing else. two items are the same under the assignment exactly when they carry the same label; an item is different exactly when it carries another. the labels' order is not information, their distances are not information, and a mean of labels has no referent at all. the admissible transformation is any one-to-one relabelling of the label set: reassigning `A, B, C` as `1, 2, 3` or as `red, green, blue` changes the notation and no claim.

> the class is exact when the label set is a partition. the classes must be declared before assignment, disjoint, and collectively cover the segment the procedure addresses — otherwise two items can carry two labels or none, and the assignment is not a function at all. exhaustiveness is what separates a classification from a descriptive vocabulary, and it is the condition most often omitted when a code list is adopted from elsewhere.

> the class's error is not an uncertainty around a true value; it is disagreement. a label has no distribution, so two assigners who disagree have made two assignments, and the question is which one the declaration endorses — which is settled by the definition of the classes, not by averaging them.

## formulation

### what is this epistemic instance?

> the **categorization instance** is the representational scheme that assigns a label from a declared label set to each item of an observed segment, under a partition that the classes jointly exhaust and are mutually disjoint.

> three components carry it:

> 1. **a label set** — the finite or enumerable set of values `{A, B, C, …}` the assignment may take, in no order and with no metric.
> 2. **a partition rule** — the declared conditions under which an item belongs to each class. the rule is what makes the assignment reproducible; without it, the labels are a vocabulary and the assignment is a habit.
> 3. **an assignment procedure** — the method by which an item is placed: an inspection, a test, a decision tree, an instrument's threshold. the procedure produces the label, never the class.

> formally, let $S$ be the observed segment and $\ell$ a label set partitioned by declared conditions $C_A, C_B, \ldots$ with $\bigcup_i C_i = S$ and $C_i \cap C_j = \varnothing$ for $i \neq j$. the categorization is the map
>
> $$c : S \to \ell, \qquad c(x) = A \iff x \in C_A,$$
>
> and its admissible transformations are the bijections $\varphi : \ell \to \ell'$. a statement about a labelled item is meaningful exactly when it survives every such relabelling; "the label is `A`" survives, "the label is higher than `B`" does not, and "the average label is 2.4" does not.

> the map is a homomorphism for identity: two items map to the same value exactly when the partition puts them in the same class, and to different ones exactly when it does not. that is the whole of the structure the class preserves, and it is why nothing beyond membership follows from a label.

### what epistemic element type does this epistemic instance belong to?

> primary type: **`epistemic representation`** — the **categorization scheme**: the representational construct through which an observable is carried as a label under a declared partition, together with the label set and the rules that constitute the assignment.

> `readable as` an **`epistemic act`** when attention falls on placing one item: classifying this specimen. `readable as` an **`epistemic practice`** when attention falls on the organized doing — taxonomy, nosology, coding standards, the institutional work that maintains a classification. `readable as` an **`epistemic construction`** when attention falls on a classification statement or a reported code as a description of a segment.

> the exclusion is argued, not asserted. an act has no constitutive parts to grow, so the partition, the label set, and the admissibility rule would have no home under it. the practice is a [measurement system](/view.html?p=notes/epistemica/measurement/system.md)'s register, and a reported code is one product of the scheme, not the scheme.

> the items categorized are read in the **ontic order**; the scheme that sorts them is epistemic. the ontic decomposition of the kinds sorted belongs to the naturalis grammar, and the sorted population's ontic character to the sciences that study it: neither is grown here.

### is the type of this `epistemic element instance` ambiguous?

> yes, in four ways the decomposition keeps apart.

> **aspect.** *categorization* names the act of placing, the scheme that makes the placing well formed, and the result — a classification. this note types the scheme; the act and the result stay `readable as` prose.

> **class.** the class is the weakest of the three in [measurement](/view.html?p=notes/epistemica/measurement/measurement.md), and the boundary that matters runs upward: a classification that also fixes an order is [ordering](/view.html?p=notes/epistemica/measurement/ordering.md) as well, and one that also fixes a magnitude is [quantification](/view.html?p=notes/epistemica/measurement/quantification.md). the common case is a classification read as the weaker of the two declarations, which is the safe error only if the order or magnitude is genuinely not claimed.

> **sense.** the false friends are load-bearing, and every one of them is a different construct:

| construct | what it does | why it is not this |
| --- | --- | --- |
| **categorization** | assigns a label from a declared partition | — |
| **classification** | the result of a categorization | the product, not the scheme: a report of the labels, not the partition that produced them |
| **taxonomy** | an ordered hierarchy of kinds | a special case with a second structure — parenthood and rank — which is what makes a hierarchy more than a flat partition |
| **coding** | assigns a token by an external convention | the convention can be arbitrary, and a categorization is answerable to the item's relations; coding is categorization only when the code tracks the partition |
| **clustering** | forms classes from the data | it induces the partition where categorization declares one; the classes arrive after, not before (see [formal concept analysis](/view.html?p=notes/epistemica/singular/formal-concept-analysis-fca.md)) |
| **quantification** | binds a magnitude to a numeral in a unit | a label has no unit and no magnitude (see [quantification](/view.html?p=notes/epistemica/measurement/quantification.md)) |
| **ordering** | assigns a rank | order is a further structure a label may or may not carry (see [ordering](/view.html?p=notes/epistemica/measurement/ordering.md)) |

> **relatum.** only a countable item of a segment can be categorized. the partition sorts items, not their properties, and a property itself can be categorized only when properties are the items of the observed segment.

> the ambiguity is resolved by declaring `epistemic representation` primary and by hanging the partition and the label set as `constitutive substrate` and `representation system` constituents of one substrate, exactly as the quantitative class does.

### what is the recursive instance decomposition of this epistemic instance?

> **boundary.** this table decomposes one epistemic instance — the categorization scheme — into the label system that carries the assigned label, the rules and structures constituting the partition, and the predicates it carries. the acts that place items are named in prose and linked; the sorted kinds belong to the naturalis grammar.

> **stopping rule.** a row is terminal when it names a label element, a foundation, a convention, a formation rule, a transformation rule, an interpretation, or a predicate. the statistics of a contingency table are not decomposed here (see [statistics](/view.html?p=notes/epistemica/epistemic/discipline/statistics.md)), and neither is the taxonomy that a hierarchy adds.

> **identity.** instance tree path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch.

| instance tree path | description |
| --- | --- |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization | the scheme assigning a label from a declared partition to each item of an observed segment — the nominal class of measurement. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` | grouping: the sign system carrying the assigned label. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ instance) label notation | the notation in which a label is written and read — a token, a code, a term — together with the class mark that declares it nominal. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `representation element` | grouping: combinable constituents of the notation. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `representation element` (→ instance) categorized item | the item of the observed segment that receives the label. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `representation element` (→ instance) label | the value assigned from the declared label set — a name for the class, no order and no magnitude intended. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `representation element` (→ instance) label set | the enumerated values the assignment may take, closed and declared before any item is placed. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `representation element` (→ instance) classification statement | the written assignment `item 17 is type A` as a checkable artifact. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` | grouping: the rules and structures constituting the partition. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` | grouping: the principles the scheme is founded on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) identity relation | the only relation the class preserves: an item is the same kind as another exactly when the partition puts them together. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) partition principle | the label set divides the observed segment into mutually disjoint classes whose union is the segment; without it the assignment is not a function. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) uniqueness condition | the admissible transformations are the bijections of the label set — which is why the order of the labels and the gaps between them carry no information. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` | grouping: stabilized choices the scheme rests on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) class-definition convention | the declared conditions under which an item belongs to each class — the definition that replaces judgement. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) exclusivity convention | each item carries exactly one label; overlapping classes are refused or resolved by a declared precedence. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) exhaustiveness convention | every item of the addressed segment has some label — a residual or "other" class is declared rather than improvised. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) labelling convention | how labels are written and ordered in the notation, and that their order is not order among items. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` | grouping: rules of well-formed classification statements. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) label-assignment rule | an item receives the label whose class conditions it satisfies, and no other. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) class-admissibility rule | which operations the label admits: equality and difference of label alone; no order, no difference of magnitude, no mean. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` | grouping: licences rewriting one classification statement into another within the class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) relabelling rule | replace each label by a distinct counterpart — `A,B,C ↦ red,green,blue` — preserving the partition and nothing else. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) class-merging rule | collapse two labels into one, weakening the partition; the operation is licensed and the information about the distinction is lost, not merely renamed. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` | grouping: assignments of meaning to the assigned label. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) membership reading | the label says which class the item belongs to, and nothing about how much of anything it has. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has property) `property` | grouping: predicates the scheme carries. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has property) `property` (→ instance) class count | the number of declared labels, which fixes the resolution the classification can report. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has property) `property` (→ instance) inter-assigner agreement | how often two independent assigners reach the same label — the reliability the class admits, in place of an uncertainty. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has property) `property` (→ instance) partition adequacy | whether the declared classes actually dissect the segment — exhaustively and without overlap — rather than carving it at convenient places. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has property) `property` (→ instance) construct validity | whether the classes track the property the classification claims to register, rather than an available and correlated one. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) categorization (→ has property) `property` (→ instance) reproducibility | whether the procedure yields the same label for the same item under a repeat of the conditions. |

### what is a critical conceptual evaluation of this `epistemic element instance`?

> **evaluated concept.** *categorization*, precisified as "the representational scheme that assigns a label from a declared label set to each item of an observed segment, under a partition whose classes are mutually disjoint and jointly exhaustive, and whose admissible transformations are the bijections of the label set." the evaluation applies the criteria of the [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

> **verdict.** strong on determinacy and on misuse resistance, weak on the question the word cannot settle by itself — whether classification counts as measurement. the partition condition is what earns the concept its strength: it makes the assignment a function, the reliability a checkable rate, and the class's liabilities explicit. what it does not do is make a label a magnitude, and the scheme does not pretend otherwise.

| criterion | verdict | diagnostic focus |
| --- | --- | --- |
| conceptual identification | strong | distinguished from classification (the product), taxonomy (a hierarchy added to the partition), coding (a convention-driven token), clustering (an induced partition), ordering and quantification. |
| definitional clarity | strong | label set, partition rule, and procedure are stated conditions; equality-only and bijection-only are stated, not implied. |
| conceptual determinacy | strong | boundary rule: an assignment is a categorization when its admissible transformations are the relabellings. borderline cases — an unordered code that tracks a hidden order — are decided by what the declaration claims, and the hidden order is then a separate claim. |
| definitional completeness | strong | partition, exclusivity, exhaustiveness, admissibility, and the transformation class are all stated; the residual class is required rather than left to appear. |
| internal consistency | strong | exhaustive disjoint classes make the assignment a function, and a function cannot both place an item twice and be a homomorphism for identity. |
| structural coherence | strong | partition, exclusivity and exhaustiveness are three conventions on one foundation; no convention undercuts another. |
| conceptual tractability | strong | declare the classes, check disjointness and coverage, assign, and report agreement — a finite and auditable procedure. |
| extensional fidelity | moderate | coding schemes adopted by convention can place items differently under the same declaration, and the scheme cannot detect the drift without a re-definition. |
| intensional adequacy | strong | the defining property is the partition and the identity preservation, which is exactly what a nominal assignment is for. |
| ontological adequacy | strong | the items are ontic, the labels epistemic, and the class is not confused with a magnitude or a rank. |
| discriminative power | strong | separates a label from a rank and from a quantity by a single transformation test, which is the distinction that matters for every downstream statistic. |
| granularity adequacy | moderate | a flat partition is coarse for hierarchical kinds, and the taxonomy false friend records that the hierarchy is a further structure rather than a defect of the class. |
| representational coverage | strong | covers binary, multi-class, exhaustive and residual classifications, and indifferently applies to specimens, cases, texts, and diagnoses. |
| ontological parsimony | strong | one label set, one partition, one procedure; the taxonomy is not smuggled in as a constituent. |
| conceptual distinctiveness | strong | the partition requirement plus the transformation class is the whole of the nominal position, without the Stevens vocabulary's surplus. |
| boundary differentiation | moderate | against ordering and quantification the boundary is sharp; against ordinary descriptive vocabulary it turns on exhaustiveness, which must be checked rather than assumed. |
| epistemic leverage | strong | the label's licence becomes explicit, which is what stops a classification from being reported as a measurement order. |
| inferential productivity | strong | from the partition follows what may be counted, cross-tabulated, or tested, and what may not be averaged. |
| explanatory power | moderate | explains why disagreement rather than uncertainty is the class's doubt, and does not explain why a classifier chose one partition over another. |
| problem-solving utility | strong | disjointness and coverage are checkable conditions, so a defective code list is found by inspection rather than by controversy. |
| contextual robustness | strong | holds across biology, medicine, administration, and the social sciences, since it asserts nothing about the kinds beyond the partition. |
| combinatorial fluidity | strong | a partition composes with a count, a contingency table, and a hierarchy as separate structures rather than as one overloaded scheme. |
| cross-domain portability | strong | transfers without reformulation, which is precisely the strength of claiming nothing beyond membership. |
| temporal stability | moderate | the class is stable, the partitions are not: diagnostic and administrative classes are revised, and an old label does not always denote a current class. |
| operationalizability | strong | the declaration and the procedures are records; agreement is computed, not judged. |
| measurement validity | moderate | a nominal scheme cannot validate itself; construct validity is a property carried by the scheme and settled outside it. |
| reliability | moderate | agreement is computable and interpretable, and a high rate of agreement can still accompany a bad partition. |
| inter-subjective reproducibility | moderate | the declaration makes reproduction possible, while the agreement statistic measures how far practice achieves it. |
| falsifiability | strong | a proposed order or distance among labels, or a demonstrated violation of exhaustiveness, refutes the class claim. |
| sensitivity to evidence | strong | an item that fits no class, or two assigners who split on the same item, can expose a defective partition and force a revision. |
| purpose adequacy | strong | fit for sorting, counting, and communicating kinds; unfit for anything requiring amount, which it refuses in the admissibility rule. |
| normative justification | moderate | the partition is answerable to the purpose: a classification that serves one inquiry badly can serve another well, and the scheme does not choose between them. |
| misuse resistance | moderate | the admissibility rule blocks the mean of labels, and the scheme still permits a class list to encode a hidden hierarchy, which is the most common abuse. |

## qa

### why is inter-coder agreement not a measurement uncertainty?

> because a label has no distributable value to be uncertain about. an uncertainty is a doubt around a magnitude — the true length lies in an interval — and a category has no magnitude to lie around. two assigners who disagree have produced two assignments, and the disagreement is evidence about the partition and the procedure: an ambiguous class condition, an item that straddles two classes, an observer effect.

> the practical payoff is that agreement failure names a repair. a high disagreement rate sends one back to the class definitions or the assignment procedure, not to an error bar, and the reported number is a rate rather than an interval.

### can a classification be wrong without being unreliable?

> yes. reliability asks whether the procedure gives the same label twice; validity asks whether the labels track the property the classification claims. a code list can be applied consistently — every coder reaching the same label every time — and still sort by an incidental feature such as spelling or provenance rather than by the kinds claimed. the scheme carries both as properties, and it cannot settle construct validity from inside the partition.

## references

- [Measurement](/view.html?p=notes/epistemica/measurement/measurement.md)
- [Ordering](/view.html?p=notes/epistemica/measurement/ordering.md)
- [Quantification](/view.html?p=notes/epistemica/measurement/quantification.md)
- [Measurement Theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)
- [Formal Concept Analysis](/view.html?p=notes/epistemica/singular/formal-concept-analysis-fca.md)
- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- stevens, s. s. (1946). on the theory of scales of measurement. *science*, 103(2684), 677–680.
- cohen, j. (1960). a coefficient of agreement for nominal scales. *educational and psychological measurement*, 20(1), 37–46.
- krippendorff, k. (2004). *content analysis: an introduction to its methodology* (2nd ed.). sage.
- roberts, f. s. (1979). *measurement theory: with applications to decisionmaking, utility, and the social sciences*. addison-wesley. see [the entry](/view.html?p=documents/books/roberts-1979-measurement-theory-addison-wesley.md).
