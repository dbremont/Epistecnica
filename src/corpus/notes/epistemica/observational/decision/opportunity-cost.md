---
tags: [note, decision-making, economics, value]
---

# Opportunity Cost

> **Opportunity cost** is the value of the best alternative forgone when a choice is made among mutually exclusive alternatives. It is the cost that no invoice records: what the resources would have produced had they been committed elsewhere.

> The concept's whole discipline lies in one word — **best**. Opportunity cost is not the sum of everything rejected; it is the value of the single alternative that would have been chosen instead. A choice that forgoes three options at 120, 90, and 40 costs 120, not 250.

## Formulation

### What is this epistemic instance?

> The **opportunity-cost instance** is the decision-theoretic concept that prices a selection by what it displaces. Given a set of mutually exclusive alternatives $A=\{a_1,\dots,a_n\}$ and a valuation $V$ defined on them, selecting $a_i$ entails forgoing the rest; the cost of that selection is the value of the best of them:
>
> $$OC(a_i)=\max_{a_j\in A,\;j\neq i}V(a_j)$$
>
> Four conditions make the expression well defined: the alternatives must be **available** (a feasible set, not a wish list), **mutually exclusive** with respect to the same resources, **valuable** on one comparable measure, and one of them must be **selected**. Scarcity is what makes the set exclusive in the first place: with resources sufficient for every alternative there is nothing to forgo.

> The five essential elements, stated in the concept's own vocabulary:
>
> 1. **Scarcity** — resources are insufficient to pursue every alternative.
> 2. **Alternatives** — several uses compete for the same resources.
> 3. **Exclusivity** — choosing one prevents pursuing another, at least with the same resources.
> 4. **Selection** — one alternative is chosen.
> 5. **Foregone value** — the value of the best unselected alternative.

> The compact statement is:
>
> **Opportunity Cost: Alternative Set × Valuation → Next-Best Forgone Value → Cost of Selection.**
>
> - **Alternative set** — the mutually exclusive feasible options.
> - **Valuation** — the comparable measure $V$ over them.
> - **Next-best forgone value** — the maximum over the unselected.
> - **Cost of selection** — the magnitude $OC(a_i)$ attached to the choice.

> Two limiting cases fix the concept's edges. With a single alternative, $OC(a_1)=0$: nothing is forgone, and the expression returns the absence of a choice rather than a free lunch. With ties at the top, the maximum is still well defined, but the cost is then the value the agent would have got from *any* of the equally good alternatives — the cost of the choice is determinate even when the identity of the forgone alternative is not.

> A government with RD\$100 million may build a hospital (expected social value 150), fund technical education (120), or build roads (90). Choosing the hospital costs 120 — the value of technical education, the best alternative sacrificed — and the choice's net advantage is 30, not 150. The roads' 90 is not part of the cost, because the roads could not have been built with the same money once education was forgone. Summing the rejected alternatives double-counts a world in which the budget could buy all three, which is precisely the world in which they are not alternatives.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Construction` → `Concept`** — a constructed discriminator of aspects of the segment. Opportunity cost does not exist in the world alongside the money spent and the hospital built; it is a distinction drawn over a decision situation, which singles out the value displaced by a selection and makes it comparable with the value gained.

> `readable as` an **`Epistemic Criterion`** — the rule functions as a test of an allocation: is the value obtained at least the value of what was given up? `readable as` an **`Epistemic Standard`** when it is imposed as the budgeting rule of an organisation ("every proposal must state what it displaces"). `readable as` a **`Description`** — the formal statement $OC(a_i)=\max_{j\neq i}V(a_j)$ asserts a relation between a choice and its alternative set.

> It is not a social element and not a natural one. The outlay is real — money spent, land committed, an hour consumed — but the outlay is the *explicit* cost; the opportunity cost is a valuation of a counterfactual, and a counterfactual is constituted by the evaluation model, not found in the world.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in six ways the decomposition keeps apart.

> **One — concept or magnitude.** "Opportunity cost" names both the rule and the number it returns. The rule is the concept; the number is an instance of its application. The note decomposes the concept and treats any particular figure as a value of the magnitude row.

> **Two — concept, criterion, or standard.** The discriminator, the test of an allocation, and the budgeting rule are the same content read at different epistemic roles. `Concept` is declared primary; the other readings stay as prose.

> **Three — opportunity cost or explicit cost.** The explicit (accounting) cost is the outlay actually paid; the opportunity cost is the best alternative forgone, which may be larger, smaller, or equal to the payment. The two coincide only when the forgone alternative is the cash itself. The note takes the forgone-value reading and keeps the accounting reading as a boundary case.

> **Four — ex ante or ex post.** Before the choice, the alternative set is live and the cost is *experienced* as the pull of the options not taken. After the choice, the alternatives are gone and the cost cannot be measured — only reconstructed against a counterfactual. This is the subjectivist reading: cost is displaced by choice, so an *ex post* opportunity cost is always someone's estimate of what might have been.

> **Five — whose valuation.** $V$ may be the agent's utility, the firm's profit, or a planner's social value. The last is the hardest: "expected social value" requires interpersonal comparison, and different weights on the beneficiaries yield different costs for the same choice. The note does not legislate a $V$; it requires that $V$ be declared, and treats the choice of $V$ as an evaluation-model decision.

> **Six — a false extension.** The phrase is often used without an alternative set: "the opportunity cost of not doing X" for an X that was never feasible, or a cost computed against an alternative no one could have chosen. Without a declared feasible set the expression is unfalsifiable, because any figure can be defended by widening $A$ to include something arbitrarily valuable.

> The ambiguity is resolved by declaration: `Concept` primary; explicit cost a boundary case; *ex ante* the operative reading, *ex post* a reconstruction; $V$ declared rather than assumed; and the feasible alternative set a precondition of the expression's meaning.

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the opportunity-cost concept — into its alternative set, its valuation, its selection and foregone set, the next-best rule that picks out the cost, the resulting magnitude, the scarcity condition that makes the alternatives compete, the neighbouring cost concepts it must be distinguished from, the representational system it is stated in, the trade-off it represents, the comparison that evaluates it, and the standard that governs it. Adjacent concepts — sunk cost, explicit cost, regret, marginal cost, comparative advantage — are named and bounded but not decomposed here; they carry their own notes or their own QA.
>
> **Stopping rule.** A row is terminal when it names a concrete condition, concept, representation element, observable, check, or standard. The next-best rule is expanded one level further — into the operator and the exclusion — and no further.
>
> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path is unique, and no type segment terminates a branch.
>
> **Typing.** The root type is `Concept`, reached through `Epistemic Construction`; the grouping segments name types licensed by the guide's permitted link forms. The alternative set, valuation, selection, foregone set, next-best rule, magnitude, scarcity condition, and boundary concepts are constituent concepts; the decision problem, budget constraint, and value function are representation elements; the displaced value is the represented observable; the counterfactual comparison is the evaluation; the comparative rationality standard is the governing standard.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost | The concept: the value of the best alternative forgone by a selection among mutually exclusive alternatives. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` | Grouping: the constituent concepts of the concept. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Alternative Set | The set $A$ of options among which the choice is made — the concept's first argument. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Alternative Set (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Mutual Exclusivity | No two alternatives can be pursued with the same resources: selection of one removes the others from the feasible set. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Alternative Set (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Feasibility | Only options actually available to the decision-maker count; an unavailable option is a wish, not a cost. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Valuation | The measure $V$ that assigns a comparable value to each alternative — the concept's second argument. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Valuation (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Value Measure | The declared cardinal measure — money, utility, expected social welfare — on which the alternatives are compared. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Valuation (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Comparability | The requirement that the values of different alternatives be commensurable enough for a maximum to be taken. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Selection | The alternative $a_i$ actually chosen — the option whose cost is being computed. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Foregone Set | The complement $A\setminus\{a_i\}$: the alternatives the selection removes. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Next-Best Rule | The rule that reduces the foregone set to the single alternative that defines the cost. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Next-Best Rule (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Maximum Operator | $\max_{a_j\in A,\,j\neq i}V(a_j)$: the cost is the largest forgone value, not their sum. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Next-Best Rule (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Exclusion Of The Selection | The condition $j\neq i$: the chosen alternative is not part of its own cost. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost Magnitude | $OC(a_i)$: the value the concept returns for a given selection and alternative set. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Scarcity Condition | The condition under which alternatives compete at all: resources are insufficient to pursue every option. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Scarcity Condition (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Resource Constraint | The budget, time, land, or attention limit that bounds the feasible set. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Scarcity Condition (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Competing Use | Several uses claiming the same constrained resources, which is what makes them alternatives. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Conceptual Boundary | Grouping: the neighbouring cost notions the concept must be separated from. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Conceptual Boundary (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Explicit Cost | The outlay actually paid — a special case in which the forgone alternative is the cash itself. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Conceptual Boundary (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Accounting Cost | The recorded payment: a bookkeeping quantity that can diverge from the value of what was given up. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Conceptual Boundary (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Sunk Cost | The temporal mirror: an outlay already made and unrecoverable, which no longer belongs to any live alternative set. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Conceptual Boundary (→ Part) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Regret | The comparison after the fact of the realised outcome with the counterfactual — the *ex post* shadow of the *ex ante* cost. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Has) `Representational System` | Grouping: the sign system in which the concept is stated. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Decision Problem | The $(S,E)$ structure — solution space and evaluation model — in which the alternative set and the valuation are declared. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Budget Constraint | The formal statement of the resource limit that makes $A$ exclusive. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Value Function | The functional form of $V$ over the alternatives, from which the maximum is taken. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Represents) `Observable` (→ Instance) Displaced Value | The represented feature: the value that the chosen allocation removes from the reachable alternatives. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Evaluated By) `Validation` (→ Instance) Counterfactual Comparison | The check that compares the chosen outcome with the best forgone alternative — the only way the cost can be assessed. |
| `Epistemic Element` (→ Kind) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Opportunity Cost (→ Governed By) `Epistemic Standard` (→ Instance) Comparative Rationality Standard | The standard that a selection is justified when $V(a_i)\ge OC(a_i)$ — the value obtained is at least the value displaced. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The concept is formally sharp and inferentially productive: it passes Conceptual Identification, Definitional Clarity, Internal Consistency, Boundary Differentiation, and Purpose Adequacy once the alternative set and the valuation are declared. It is partial in two respects — the cost is a counterfactual and therefore observable only by reconstruction, and the requirement that $V$ be a single comparable measure is strong, failing exactly where the alternatives are valued in incommensurable currencies. Its determinacy is conditional rather than absolute: widen or narrow the alternative set and the cost changes, so the concept's precision is the precision of the modelling choices behind it.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note separates opportunity cost from explicit cost (the payment), accounting cost (the record), sunk cost (the past outlay), and regret (the *ex post* comparison) — the four notions it is most often confused with. |
| **Definitional Clarity** | Pass | The definition is an explicit formula, $OC(a_i)=\max_{j\neq i}V(a_j)$, with both arguments — the alternative set and the valuation — named and bounded. |
| **Conceptual Determinacy** | Partial | The formula is determinate; the concept is not, because the alternative set and the feasible set are modelling choices. Widening $A$ raises the cost, narrowing it lowers it, and nothing in the formula fixes $A$. |
| **Internal Consistency** | Pass | "Best forgone" and "not the sum" agree once mutual exclusivity is stated: alternatives that could all be pursued simultaneously are not alternatives to one another. The selection rule $a^\*=\arg\max_i\big(V(a_i)-OC(a_i)\big)$ follows directly and reproduces $\arg\max_i V(a_i)$. |
| **Representational Adequacy** | Partial | The concept represents value displaced, not value at risk: expectations hide dispersion, and a mean-preserving spread across alternatives leaves $OC$ unchanged while the option value of keeping alternatives open changes. Incommensurable criteria require a multi-criteria representation, not a single $V$. |
| **Purpose Adequacy** | Pass | For the *ex ante* evaluation of a choice among mutually exclusive uses of scarce resources — the purpose it exists for — the concept is the right discriminator, and its *ex post* weakness is the price of an *ex ante* concept. |
| **Boundary Differentiation** | Pass | The boundary with explicit, accounting, and sunk cost, and with regret, is stated in the ambiguity section and carried in the table as constituent boundary concepts. |
| **Inferential Productivity** | Pass | It yields the selection rule, the reasoning behind comparative advantage (the cost of a good is what its production displaces), the sunk-cost fallacy (past outlays are in no live alternative set), and the pricing of non-market goods. |
| **Operationalizability** | Partial | The counterfactual value is unobservable: measurements are reconstructions from market prices or elicited valuations, and the wider the alternative set the more speculative the reconstruction. |

> The disciplined cut is to keep the concept's two arguments explicit. An opportunity cost asserted without a stated alternative set and a stated valuation is not a measurement but a rhetorical move — the concept's formal precision does not transfer to an assertion that omits its premises.

## QA

### Why is the cost the best alternative and not the sum of all rejected alternatives?

> Because the alternatives are mutually exclusive: choosing one prevents pursuing the others *with the same resources*. If the hospital, the schools, and the roads could all be built, they would not be alternatives to each other and the selection would forgo nothing. Once only one can be had, the alternatives are substitutes, and the value of a set of substitutes is the value of the best of them — the same reason a person who can take one of three jobs does not lose three salaries but the best salary forgone. Summing the rejected options answers a different question: what would all of them have been worth together, in a world without the constraint that defines the problem.

### Is opportunity cost the same as accounting or explicit cost?

> No. The explicit cost is the outlay actually paid; the accounting cost is how that outlay is recorded. Opportunity cost is the value of the best alternative forgone, which may exceed the payment (a firm using its own building forgoes the rent it could have charged — an implicit cost with no invoice) or fall below it (a payment that buys an option better than any alternative was worth). The two coincide only in the special case where the forgone alternative is the cash itself, which is why the explicit cost is a boundary case in the decomposition rather than the concept's core.

### Is opportunity cost *ex ante* or *ex post*?

> *Ex ante*, and this is the subjectivist point that Buchanan pressed against the textbook treatment. Before the choice the alternatives are live and the cost is experienced as the value of what is being given up; after the choice the alternative set is destroyed, and nothing remains to be measured. An *ex post* "opportunity cost" is therefore a reconstruction: it compares the realised outcome with an alternative that no longer exists, and its value depends on which alternatives the reconstructor is willing to imagine. This is also why the concept is not regret: regret is an emotion attached to the reconstruction, while the cost is a premise of the choice.

### Does the value of the chosen alternative enter the cost?

> No. $OC(a_i)$ is defined over $j\neq i$: the cost of a choice is what it displaces, not what it returns. The gain is separate. The two are combined only in the decision rule — choose $a_i$ when $V(a_i)\ge OC(a_i)$ — and the difference $V(a_i)-OC(a_i)$ is the net advantage of the choice. Confusing the two produces the common error of reporting the value obtained (150) as though it were the cost avoided, when the cost is 120 and the advantage only 30.

### What happens when the values are uncertain?

> The formula is stated for known values; under uncertainty $V$ is replaced by an expectation, $V(a_j)=\mathbb{E}[v(a_j)]$, and the maximum is taken over expected values. That is the minimal extension, and it is not innocent: maximising an expectation over alternatives ignores the dispersion of the outcomes and the value of keeping options open. An alternative that can be deferred has an option value that no static $OC$ captures, and a mean-preserving spread across alternatives changes the prudence of committing without changing the computed cost. Where the alternatives are genuinely uncertain, the concept belongs inside a decision model with states and probabilities — the decision problem's $(\mathcal{S},\mathcal{A},T,\mathcal{M},\phi)$ — rather than applied to point estimates.

### Is there an opportunity cost of everything?

> Only relative to a declared alternative set and a feasible set. The phrase "the opportunity cost of not doing X" is meaningful when X was available and something else was chosen instead; it is empty when X was never feasible, because no value was displaced. Widening the alternative set without limit makes the cost as large as the imagination allows — any allocation can be said to have forgone something priceless — and the concept then loses the discriminating power that makes it useful. Feasibility is not a technicality of the formula; it is what converts a comparison into a cost.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Decision Problem](/view.html?p=notes/epistemica/observational/decision/decision-problem.md) — the $(S,E)$ structure whose evaluation model supplies $V$.
- [Decision Theory](/view.html?p=notes/epistemica/observational/decision/theory.md) — the field entry: alternatives, states, preferences, and decision rules.
- [Trade-Off](/view.html?p=notes/epistemica/optimization/trade-off.md) — the multi-criteria case where no single $V$ is available.
- [Expected Value](/view.html?p=notes/epistemica/observational/probability/expected-value.md) — the expectation that replaces $V$ under uncertainty.
- [Choice](/view.html?p=notes/social/action/activity/choice.md) — the social action whose cost this concept prices.
- [Scarcity](/view.html?p=notes/social/dynamic/state/economic/scarcity.md) — the condition that makes alternatives compete.
- [Utility](/view.html?p=notes/social/dynamic/state/economic/production/utility.md) — one candidate valuation $V$.
- [Value](/view.html?p=notes/social/synontic/value.md) — the synontic element the valuation measures.
- Wieser, F. von (1927). *Social Economics* (A. F. Hinrichs, Trans.). Adelphi. (Original work *Theorie der gesellschaftlichen Wirtschaft*, 1914 — the source of *Opportunitätskosten*.)
- Bastiat, F. (1850). *Ce qu'on voit et ce qu'on ne voit pas*. (The unseen cost as the economist's subject.)
- Buchanan, J. M. (1969). *Cost and Choice: An Inquiry in Economic Theory*. Markham. (Cost as *ex ante* and displaced by choice.)
- Mankiw, N. G. (2020). *Principles of Economics* (9th ed.). Cengage. (The textbook statement of opportunity cost as the value of the next-best alternative.)
- [Opportunity cost](https://en.wikipedia.org/wiki/Opportunity_cost)
