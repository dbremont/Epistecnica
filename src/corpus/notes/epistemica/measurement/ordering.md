---
tags: [note, measurement, ordering, order, ordinal]
qa:
  - "is ordering a class of measurement and not a preliminary to it?"
  - "when may an ordinal scale carry a mean?"
  - "what does a tie mean on an ordinal scale?"
  - "why does a monotone transformation preserve an ordinal measurement and destroy an interval one?"
  - "how does an ordinal scale become an interval scale?"
  - "is a preference order a measurement?"
---

# ordering

> **ordering** assigns a rank to an observable: each item receives a value from a declared ordered range, and the value records where the item stands relative to the others. it is the middle class of [measurement](/view.html?p=notes/epistemica/measurement/measurement.md) — stronger than a label, weaker than a magnitude — and it is what inquiry uses whenever it can compare without being able to say by how much.

> the scale licenses order and nothing further. if one item ranks above another, the observable stands above it too; what the gap between two ranks amounts to is not information. the admissible transformation is any strictly increasing map: reassigning `1, 2, 3` as `10, 20, 25` or as `0, 5, 6` rearranges the numerals and preserves every ordering claim. a mean of ranks and a difference of ranks are therefore not licensed — they shrink or stretch as the relabelling shifts, and what they report is an artefact of the numerals.

> the class is exact when the assignment is a total preorder: complete (any two items are comparable) and transitive (if one outranks a second and the second a third, the first outranks the third). incomparability and intransitivity are not small defects — they mean the observable carries no order for the assignment to preserve, and what remains is a preference report about a procedure, not a measurement of the observable.

> ties are part of the structure, not a gap in it. two items with the same rank are recorded as indifferent, and the preorder says exactly that: neither outranks the other. collapsing a tie into a forced choice invents a distinction the observable did not exhibit, which is the ordinal mirror of reading a label as a rank.

## formulation

### what is this epistemic instance?

> the **ordering instance** is the representational scheme that assigns a value from an ordered range to each item of an observed segment, so that the order among the values preserves the order the observable carries.

> three components carry it:

> 1. **a ranked value range** — the ordered values `1 < 2 < 3 < …` the assignment may take, whose only usable structure is their succession.
> 2. **a comparison criterion** — the declared relation on items that the assignment is meant to track: longer than, preferred to, warmer than, more advanced than. the criterion, not the numerals, is what the procedure reads.
> 3. **an assignment procedure** — the method by which ranks are produced: a comparison against a reference series, a threshold ladder, a rating, a judge's ordering. it produces ranks and can produce ties.

> formally, let $S$ be the observed segment carrying a declared comparison relation $\succsim$ that is total and transitive. the ordering is the map
>
> $$o : S \to R, \qquad o(x) \ge o(y) \iff x \succsim y,$$
>
> where $R$ is an ordered value set, and the admissible transformations are the strictly increasing maps $\varphi : R \to R'$. a statement about a rank is meaningful exactly when it survives every such $\varphi$: "$x$ ranks above $y$" survives; "$x$ is two ranks above $y$", "$x$ outranks $y$ by as much as $z$ outranks $w$", and "the mean rank is 2.4" do not.

> the map is a homomorphism for order. it cannot be more: the observable exhibits no comparative relation beyond $\succsim$, so nothing richer can be preserved, and a procedure that produces a spacing produces it from somewhere other than the observable — a convention, a fitted model, or a scale borrowed from a different attribute.

### what epistemic element type does this epistemic instance belong to?

> primary type: **`epistemic representation`** — the **ordering scheme**: the representational construct through which an observable is carried as a rank under a declared comparison criterion, together with the ordered range and the rules that constitute the assignment.

> `readable as` an **`epistemic act`** when attention falls on ordering one item against others. `readable as` an **`epistemic practice`** when attention falls on the organized doing — psychometric scaling, judging panels, competitive ranking, the institutional work that maintains a ranking. `readable as` an **`epistemic construction`** when attention falls on a ranking as a description of a segment.

> the exclusion is argued, not asserted. an act has no constitutive parts to grow, so the comparison criterion and the preorder conditions would have no home under it. the practice is [measurement theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)'s subject when its yardstick is formalized, and a ranking is one product of the scheme.

> the items ranked are read in the **ontic order**; the comparative relation they bear is ontic as well, and its decomposition belongs to the naturalis grammar.

### is the type of this `epistemic element instance` ambiguous?

> yes, in four ways the decomposition keeps apart.

> **aspect.** *ordering* names the act of ranking, the scheme that makes the ranking well formed, and the result — a ranking. this note types the scheme; the act and the result stay `readable as` prose.

> **class.** the class sits between a label and a magnitude, and both boundaries are live. below it, a ranking whose values are used as classes collapses into [categorization](/view.html?p=notes/epistemica/measurement/categorization.md), and what is lost is the order. above it, a ranking whose gaps have been given an empirical basis is a [quantification](/view.html?p=notes/epistemica/measurement/quantification.md), and what was added is a difference the observable exhibits — see the QA below on how that crossing is licensed.

> **sense.** the false friends are load-bearing, and every one of them is a different construct:

| construct | what it does | why it is not this |
| --- | --- | --- |
| **ordering** | assigns a rank under a declared preorder | — |
| **ranking** | the result of an ordering | the product, not the scheme |
| **sorting** | places items into ordered bins | a coarser case whose bins are classes first and ranks second; sorting alone preserves no fine order (see [categorization](/view.html?p=notes/epistemica/measurement/categorization.md)) |
| **preference** | records a stated choice | a preference can be intransitive or incomplete, in which case it is not a warrant for an ordering of the observable (see [decision making](/view.html?p=notes/epistemica/observational/decision/decision-making.md)) |
| **voting rule** | aggregates preferences into an order | the aggregate order is constructed by a rule, not registered from the observable; what it measures is the rule's output |
| **rating scale** | a labelled ladder a judge uses | the ladder supplies ranks; whether it supplies more is the empirical question the class settles (see [ordering versus quantification](#how-does-an-ordinal-scale-become-an-interval-scale-1)) |
| **quantification** | binds a magnitude to a numeral in a unit | order plus differences plus a unit, which the ordinal class lacks (see [quantification](/view.html?p=notes/epistemica/measurement/quantification.md)) |

> **relatum.** only a segment whose items bear a comparative relation can be ordered. the relation is declared by the criterion and checkable by it; an order imposed by the procedure rather than read from the observable is a ranking of the procedure's output.

> the ambiguity is resolved by declaring `epistemic representation` primary and by hanging the preorder conditions as `foundation` members of one substrate, with the admissibility rule confined to what order alone licenses.

### what is the recursive instance decomposition of this epistemic instance?

> **boundary.** this table decomposes one epistemic instance — the ordering scheme — into the ranked value system that carries the assigned rank, the rules and structures constituting the preorder, and the predicates it carries. the acts of comparing and ranking are named in prose and linked; the preference structure that a decision procedure aggregates is not grown here.

> **stopping rule.** a row is terminal when it names a comparison element, a foundation, a convention, a formation rule, a transformation rule, an interpretation, or a predicate. the statistics of ranks — rank correlation, the median as an ordinal summary — are not decomposed here, and neither is the conjoint-measurement machinery that lifts an order into a quantity.

> **identity.** instance tree path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch.

| instance tree path | description |
| --- | --- |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering | the scheme assigning a rank from an ordered range to each item of an observed segment, preserving the order the observable carries — the ordinal class of measurement. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` | grouping: the sign system carrying the assigned rank. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ instance) rank notation | the notation in which a rank is written and read — an ordinal numeral, a ladder position, a letter grade — together with the class mark that declares it ordinal. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `representation element` | grouping: combinable constituents of the notation. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `representation element` (→ instance) ranked item | the item of the observed segment that receives the rank. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `representation element` (→ instance) rank | the position assigned — a value whose succession alone carries information. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `representation element` (→ instance) ordered value range | the succession of values the assignment may take, declared in advance and fixed in number. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `representation element` (→ instance) tie | the shared rank of two items the criterion finds indifferent — recorded as indifference, never resolved by the notation. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `representation element` (→ instance) ordering statement | the written assertion `item 17 ranks above item 4` as a checkable artifact. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` | grouping: the rules and structures constituting the ordering. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` | grouping: the principles the scheme is founded on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) order relation | the comparative relation the observable carries — outranks, is warmer than, is preferred to — declared by the criterion and antecedent to the numerals. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) weak-order completeness | any two items of the segment are comparable: for every pair, one outranks the other or they tie, with no undecided pair left in the record. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) transitivity | if one item outranks a second and the second a third, the first outranks the third — the condition that makes a ranking a preorder rather than a tally. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `foundation` (→ instance) uniqueness condition | the admissible transformations are the strictly increasing maps — which is why the gaps between ranks carry no information. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` | grouping: stabilized choices the scheme rests on. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) comparison-criterion convention | the declared relation on items the ranking tracks, stated before ranking so that the ranking is read as a report of it. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) direction convention | which end of the range is higher — ascending or descending ranks — declared so that a reader cannot reverse the order. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) tie convention | how indifference is recorded and what a tie licenses in the downstream report. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `convention` (→ instance) rank-assignment convention | how ranks are allocated when ties occur — a dense succession, a competition ranking, an average of the shared positions — a notational choice that does not change the order. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` | grouping: rules of well-formed ordering statements. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) order-preservation rule | a rank is assigned so that the numerals' succession matches the criterion's order; an inversion between them is an error of the assignment. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `formation` (→ instance) class-admissibility rule | which operations the rank admits: order and indifferent comparison; no difference, no ratio, no mean. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` | grouping: licences rewriting one ordering statement into another within the class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) monotone re-ranking | replace every rank by any strictly increasing image — `1,2,3 ↦ 10,20,25` — preserving every order and indifference and nothing else. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) order-preserving regrouping rule | collapse the range into coarser ordered bins; every coarse claim survives, every fine distinction is lost. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `transformation rule` (→ instance) order-inverting rule | reverse the direction of the range and restate direction with it; licensed only as a renotation, never as a change of order. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` | grouping: assignments of meaning to the assigned rank. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) comparative reading | a higher rank asserts that the item outranks the others under the criterion, and nothing about by how much. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has) `representational system` (→ part) `constitutive substrate` (→ part) `interpretation` (→ instance) tie reading | an equal rank asserts indifference under the criterion — the two items stand the same way to the others, and the observable is not asked to break the tie. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` | grouping: predicates the scheme carries. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` (→ instance) order resolution | how many distinct ranks the range fixes — what the ranking can distinguish and what it merges. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` (→ instance) order fidelity | whether the ranking reproduces every comparison the criterion makes, with no inversion and no spurious tie. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` (→ instance) tie rate | the share of item pairs recorded as indifferent — a fact about the criterion's discriminating power and the range's fineness. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` (→ instance) inter-judge agreement | how often two independent comparisons reach the same order — the reliability the class admits in place of an uncertainty. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` (→ instance) additivity of differences | whether equal rank steps represent equal jumps in the observable; if they do, the assignment is not merely ordinal and has crossed into the quantitative class. |
| `epistemic element` (→ kind) `epistemic representation` (→ instance) ordering (→ has property) `property` (→ instance) construct validity | whether the criterion tracks the property the ordering claims to rank, rather than an available and correlated one. |

### what is a critical conceptual evaluation of this `epistemic element instance`?

> **evaluated concept.** *ordering*, precisified as "the representational scheme that assigns a rank from an ordered value range to each item of an observed segment, so that the rank's order preserves the order carried by a declared comparison relation that is total and transitive, with strictly increasing maps as its admissible transformations." the evaluation applies the criteria of the [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

> **verdict.** strong on what a rank may assert and unusually strong on the boundary it shares with quantification, weak where a range is declared without the preorder conditions having been checked. the class earns its place by refusing the difference: a ranking that cannot report a distance is exact at the relation it does report. what it does not do is decide by itself whether a particular ladder measures a distance, and the crossing rule — conjoint measurability — settles that outside this class.

| criterion | verdict | diagnostic focus |
| --- | --- | --- |
| conceptual identification | strong | distinguished from ranking (the product), sorting (coarser classes first), preference (which may be intransitive), voting rules (constructed aggregates), and quantification. |
| definitional clarity | strong | range, criterion, procedure, and the preorder conditions are stated; monotone admissibility is stated, not left to be inferred from the numerals. |
| conceptual determinacy | strong | boundary rule: an assignment is an ordering when its admissible transformations are the strictly increasing maps. borderline cases, such as a Likert ladder used as an ordering, are classified by the transformations the declared reading admits. |
| definitional completeness | strong | completeness, transitivity, ties, and the tie conventions are all stated; the case where the preorder fails is named rather than absorbed. |
| internal consistency | strong | transitivity is what makes a ranking a preorder rather than a tally, and the admissibility rule refuses differences exactly where the ranking cannot transport them. |
| structural coherence | strong | the criterion, the direction, and the tie conventions are conventions on one foundation; the rank-assignment convention is marked as notational and cannot change the order. |
| conceptual tractability | strong | check completeness and transitivity, assign ranks, and report inversions and tie rate — the audit is finite. |
| extensional fidelity | moderate | a ranking applies wherever a criterion is declared, and the criteria can be vague, so the same observable admits several legitimate orders under different criteria. |
| intensional adequacy | strong | the defining property is order preservation under comparison, which is precisely the ordinal class's function. |
| ontological adequacy | strong | ranks are epistemic, the comparative relation is ontic, and the class does not smuggle a spacing into either. |
| discriminative power | strong | the same range can be read as a label, a rank, or a magnitude, and the transformation test separates the three readings rather than the notation. |
| granularity adequacy | moderate | a fixed range is coarse for attributes with a fine order, and the class offers no finer instrument without becoming quantitative — which is a limit, not a defect. |
| representational coverage | strong | covers ties, incomplete criteria, coarse bins, and indifferently applies to specimens, preferences, and ranks of institutions. |
| ontological parsimony | strong | one range, one criterion, one procedure; the preorder conditions are stated once as foundations rather than repeated as conventions. |
| conceptual distinctiveness | strong | the mildness is the point — order without the arithmetic that order alone cannot license. |
| boundary differentiation | strong | against categorization it adds exactly one relation; against quantification it withholds exactly one, and the crossing test is named. |
| epistemic leverage | strong | the class answers, for every rank-based statistic, whether the statistic is licensed, and most disputes over rating scales turn on precisely that. |
| inferential productivity | strong | from the preorder follows what is comparable, what is indifferent, and what lifts — via conjoint measurement — into an interval if the structure supports it. |
| explanatory power | moderate | explains why order is measurable without being a magnitude, and leaves open why a particular criterion was chosen. |
| problem-solving utility | strong | intransitivity and incompleteness become checkable failures of the criterion rather than embarrassments hidden by a tally. |
| contextual robustness | strong | applies across psychometrics, preference, ranking of institutions, and ordinal classification, since it asserts nothing beyond comparison. |
| combinatorial fluidity | strong | joins conjoint measurement as the route out of the ordinal class, and count statistics as the route within it. |
| cross-domain portability | strong | transfers without reformulation, which is why ranking is the most widely used measurement class beyond the physical sciences. |
| temporal stability | moderate | the class is stable, the criteria are not: a ranking of institutions or abilities can encode a criterion that later evidence retires. |
| operationalizability | strong | the criterion, range, and direction are records; inversions and ties are computed. |
| measurement validity | moderate | the class can report fidelity to its own criterion and cannot certify that the criterion tracks the intended property. |
| reliability | moderate | a ranking is reproducible where the criterion is precise, and two judges can legitimately disagree where it is not. |
| inter-subjective reproducibility | moderate | the comparison criterion is what makes reproduction possible, and a vague criterion reproduces the judgment rather than the order. |
| falsifiability | strong | a demonstrated pair where the ranking inverts the criterion, or a demonstrated equal spacing under unequal ranks, refutes the class claim. |
| sensitivity to evidence | strong | a tie that proves a distinction, or a spacing that survives conjoint testing, can promote the assignment and force the class claim to be revised upward. |
| purpose adequacy | strong | fit for comparing, selecting, and reporting relative standing; unfit for any arithmetic the class refuses, which it states plainly. |
| normative justification | moderate | the criterion may encode a value judgement, and the scheme records the criterion rather than hiding it — a procedural, not a substantive, guarantee. |
| misuse resistance | moderate | the admissibility rule refuses differences and means, and the scheme still permits a range to present itself as a ladder of equal steps, which the crossing rule exposes but does not prevent. |

## qa

### when may an ordinal scale carry a mean?

> only when the ranking has ceased to be merely ordinal. a mean of ranks is licensed when the equal steps the arithmetic assumes are empirically grounded — that is, when the observable supports comparisons of *differences*: this pair is further apart than that pair, as reliably as either ranks above the other. conjoint measurement is the standard route: when the attribute can be embedded in a structure whose order satisfies the solvability and separability conditions, a numerical representation unique up to an affine transformation exists, and the mean then draws on real distances.

> absent that demonstration, the mean of `1, 2, 3` letters is a statistic about the assignment procedure. it changes when the letters are relabelled, which is precisely what a statement about the observable must not do.

### how does an ordinal scale become an interval scale?

> when the difference relation is registered as well as the order. the ordinal class observes only which of two items stands higher; the interval class observes how far apart pairs are, relative to other pairs. the crossing is licensed by a representation theorem — not by a wider ladder — because the theorem is what makes the resulting numbers unique up to an affine map, and therefore makes their differences mean something.

> the practical consequence is that a finer rating scale does not make an instrument quantitative. what makes it quantitative is an empirical structure with a difference relation under it; the number of rungs is notation.

### is a preference order a measurement?

> a preference order is a measurement of the preference, and a measurement of the observable only when the preference tracks it. if a judge's ranking is transitive and complete and reproduces how the items stand under the criterion, it is an ordering of that criterion. if it is intransitive, or turns on context and framing, the ranking reports the judge's procedure and the observable's order is not what is being measured.

## references

- [Measurement](/view.html?p=notes/epistemica/measurement/measurement.md)
- [Categorization](/view.html?p=notes/epistemica/measurement/categorization.md)
- [Quantification](/view.html?p=notes/epistemica/measurement/quantification.md)
- [Measurement Theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md)
- [Decision Making](/view.html?p=notes/epistemica/observational/decision/decision-making.md)
- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- stevens, s. s. (1946). on the theory of scales of measurement. *science*, 103(2684), 677–680.
- luce, r. d., & tukey, j. w. (1964). simultaneous conjoint measurement. *journal of mathematical psychology*, 1(1), 1–27.
- krantz, d. h., luce, r. d., suppes, p., & tversky, a. (1971). *foundations of measurement, vol. i: additive and polynomial representations*. academic press.
- roberts, f. s. (1979). *measurement theory: with applications to decisionmaking, utility, and the social sciences*. addison-wesley. see [the entry](/view.html?p=documents/books/roberts-1979-measurement-theory-addison-wesley.md).
- michell, j. (1990). *an introduction to the logic of psychological measurement*. erlbaum.
