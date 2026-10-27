---
tags: [epistemology, logic, discipline]
---

# Logic

> In this set of notes, Logic is treated as a **discipline** — an **Epistemic Aggregate**: the organized inquiry into valid inference — which conclusions follow necessarily from which premises, and why.

> **Logic** is the discipline dedicated to the **study of consequence**: the characterization of which arguments are valid, which inferences are licensed by their form rather than their content, and which formal systems capture that licensing exactly. It encodes the regularity of **inferential necessity** — the fact that some conclusions cannot fail to hold if their premises do — into formal languages, proof systems, and semantics, thereby providing the universal scaffolding on which every other discipline's reasoning rests. Arguments inspire our systems, and through those systems we distinguish proof from persuasion.

Logic is the discipline of **form over content**: where mathematics reasons
*within* a formal system, logic studies *the systems themselves* — their
languages, their rules of derivation, their semantics, and their metalogical
properties (soundness, completeness, decidability). Its product is a
*warranted inference*; its warrant is a proof that the inference rule preserves
truth, not an observation that it works in practice.

This note is the discipline-level Aggregate; it is the formal parent of
[Mathematics](note.html?n=epistemica/discipline/mathematics.md) and
[Computer Science](note.html?n=epistemica/discipline/computer-science.md), and
its concepts appear across the mathematical catalogue (e.g.
[Boolean Algebra](note.html?n=epistemica/mathematical/boolean-algebra.md)). The
schema it instantiates is owned by the canonical
[Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

## Formulation

### What is this epistemic instance?

> Logic is the organized inquiry system into valid inference: it fixes formal languages in which arguments can be written, proof systems that license derivation, semantics that assign truth, and metalogical results that relate the two. Its product is a warranted claim of the form *this conclusion follows necessarily from these premises*; its warrant is a soundness proof, not an appeal to intuition.

### What epistemic element type does this epistemic instance belong to?

> An **`Aggregate`** — the organized inquiry system of logic: one coherent body scoping orientation, target, representations, operations, evaluations, communication, and infrastructure around the study of consequence.

### Is the type of this `epistemic element instance` ambiguous?

> No at the root: logic is a structured collection of epistemic elements organized as one coherent epistemic whole, so `Aggregate` is its primary type. Two boundaries are worth stating. Against **mathematics**: logic supplies the inference rules mathematics uses, but mathematics asks *what follows within a theory* while logic asks *what licensing itself is* — the study of the rules, not their application. Against **epistemology** (the reflexive branch of EES): logic studies the *form* of warranted inference; epistemology studies the *nature, conditions, and limits of knowing* — adjacent, but the reflexive inquiry takes knowing as its target while logic takes consequence as its target. The boundary with **rhetoric and argumentation** is drawn by formality: logic's warrant is formal derivability, not persuasive effect.

### What is the recursive instance decomposition of this epistemic instance?

> The table below decomposes logic as an organized inquiry system, grown along the branches of inquiry. A deep core (orientation, target, representation, operation, evaluation) is developed to levels 4–5; the rest is carried to level 3–4. Each leaf resolves to a concrete instance.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Logic | The organized inquiry into valid inference: one body of logical knowledge with its orientation, target, representations, operations, evaluations, and infrastructure. |
| `Aggregate` → Logic → `Epistemic Orientation` | Grouping: the directing structure of the inquiry. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of the inquiry. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Purpose` → Consequence Purpose | Telos: determine which conclusions follow necessarily from which premises. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Purpose` → Formalization Purpose | Telos: encode an argument's form so that its validity is checkable mechanically. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Purpose` → Foundation Purpose | Telos: supply the inference rules on which mathematics and computer science rest. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Question` | Grouping: questions directing the inquiry. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Question` → Validity Question | Formulated question: is this argument valid — does the conclusion follow from the premises? |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Question` → Completeness Question | Formulated question: can every truth of the semantics be derived in the proof system? |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Question` → Decidability Question | Formulated question: is there an effective procedure deciding validity for this logic? |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Goal` | Grouping: desired outcomes. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Goal` → Sound System Goal | Desired outcome: a proof system whose every derivable formula is semantically valid. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Gap` | Grouping: gaps motivating the inquiry. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Gap` → Incompleteness Gap | Deficiency: a semantic truth that no derivation in the system reaches. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Role` | Grouping: roles performed within the inquiry. |
| `Aggregate` → Logic → `Epistemic Orientation` → `Epistemic Role` → Logician | Principal inquirer: constructing formal systems and proving their metalogical properties. |
| `Aggregate` → Logic → `Epistemic Agency` | Grouping: entities and organized activities performing the discipline's work. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Agent` | Grouping: agents performing logical operations. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Agent` → Logician | Entity defining languages, deriving proofs, and proving soundness and completeness. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Act` | Grouping: primitive acts of the logician. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Act` → Formalizing Act | Primitive act replacing an informal argument with a formal derivation. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Act` → Deriving Act | Primitive act applying one inference rule to obtain a new formula. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Act` → Modeling Act | Primitive act exhibiting a structure in which the premises hold and the conclusion fails. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Activity` | Grouping: organized sequences of acts. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Activity` → Proving | Organized derivation of a theorem within a formal system. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Activity` → Refuting | Constructing a countermodel that shows an argument invalid. |
| `Aggregate` → Logic → `Epistemic Agency` → `Epistemic Activity` → Metalogical Analysis | Establishing soundness, completeness, and decidability for a system. |
| `Aggregate` → Logic → `Epistemic Target` | Grouping: the addressed domain of inquiry. |
| `Aggregate` → Logic → `Epistemic Target` → `Target Domain` | Grouping: domains addressed. |
| `Aggregate` → Logic → `Epistemic Target` → `Target Domain` → Argument | Bounded domain: a set of premises and a conclusion, the object whose validity is judged. |
| `Aggregate` → Logic → `Epistemic Target` → `Target Segment` | Grouping: segments selected for study. |
| `Aggregate` → Logic → `Epistemic Target` → `Target Segment` → Formal Argument | An argument transcribed into a formal language so its form can be checked. |
| `Aggregate` → Logic → `Epistemic Target` → `Observable` | Grouping: registrable features of the target. |
| `Aggregate` → Logic → `Epistemic Target` → `Observable` → Validity | Registrable feature: whether every model of the premises is a model of the conclusion. |
| `Aggregate` → Logic → `Epistemic Target` → `Observable` → Satisfiability | Registrable feature: whether some model makes all the formulas true at once. |
| `Aggregate` → Logic → `Epistemic Target` → `Observable` → Consistency | Registrable feature: whether a set of formulas has any model at all. |
| `Aggregate` → Logic → `Epistemic Representation` | Grouping: structures through which content is encoded and manipulated. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` | Grouping: sign systems of the discipline. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language | A vocabulary and grammar in which formulas are written. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Representation Element` | Grouping: combinable constituents of the language. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Representation Element` → Connective | A logical constant combining formulas — ¬, ∧, ∨, →. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Representation Element` → Quantifier | A logical constant binding variables — ∀, ∃. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Representation Element` → Formula | A well-formed string expressing a proposition. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Constitutive Substrate` | Grouping: rules constituting the language. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Constitutive Substrate` → Formation Rule | How symbols combine into well-formed formulas. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Formal Language → `Constitutive Substrate` → Binding Rule | How quantifiers bind variables and avoid capture. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Proof System | A set of axioms and inference rules licensing derivations. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Proof System → Natural Deduction | Exemplar proof system realizing the type: introduction and elimination rules per connective. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Proof System → Hilbert System | Exemplar proof system realizing the type: axioms plus modus ponens. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Semantics | An assignment of truth to formulas over structures — the meaning side of the system. |
| `Aggregate` → Logic → `Epistemic Representation` → `Representational System` → Semantics → Model | Exemplar semantics: a structure satisfying a set of formulas. |
| `Aggregate` → Logic → `Epistemic Operation` | Grouping: operations transforming representations into results. |
| `Aggregate` → Logic → `Epistemic Operation` → `Action` | Grouping: direct transformations of the representation. |
| `Aggregate` → Logic → `Epistemic Operation` → `Action` → Rule Application | Deriving one formula from prior formulas by an inference rule. |
| `Aggregate` → Logic → `Epistemic Operation` → `Action` → Truth Evaluation | Computing the truth value of a formula under a model. |
| `Aggregate` → Logic → `Epistemic Operation` → `Action` → Countermodel Search | Searching for a model of the premises that falsifies the conclusion. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` | Grouping: coordinated routines and generalized ways. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized methods of derivation. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Method` → Proof by Contradiction | Deriving absurdity from the negation of the goal, then concluding the goal. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Method` → Resolution | Refuting a clause set by repeatedly resolving complementary literals. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Method` → Truth Table Enumeration | Checking validity by exhausting the assignments to the atomic formulas. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Principle` | Grouping: rules guiding the operations. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Principle` → Structural Rule | A rule about how premises may be used — weakening, contraction, exchange. |
| `Aggregate` → Logic → `Epistemic Operation` → `Organization` → `Principle` → Cut Elimination | The principle that a derived lemma can be removed from a proof without loss. |
| `Aggregate` → Logic → `Epistemic Evaluation` | Grouping: assessments of the discipline's outputs. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards judging systems and arguments. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Epistemic Standard` → Soundness Standard | A proof system stands only if every derivable formula is semantically valid. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Epistemic Standard` → Completeness Standard | A proof system stands only if every semantically valid formula is derivable. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Epistemic Criterion` → Decidability Criterion | A logic is judged by whether validity is effectively decidable. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Epistemic Criterion` → Expressiveness Criterion | A logic is judged by the distinctions its language can draw. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Validation` | Grouping: checks discharging doubt. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Validation` → Proof Check | A derivation is validated by checking each step against the rule it cites. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Validation` → Countermodel Check | A validity claim is refuted by exhibiting a model of the premises that falsifies the conclusion. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Error` | Grouping: deviations from valid form. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Error` → Fallacy | An argument form whose conclusion is presented as following when it does not. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Feedback` | Grouping: evaluations returned to the system. |
| `Aggregate` → Logic → `Epistemic Evaluation` → `Feedback` → Rule Revision | A failed soundness check returned to the proof system as a required change. |
| `Aggregate` → Logic → `Epistemic Communication` | Grouping: transmission of logical content. |
| `Aggregate` → Logic → `Epistemic Communication` → `Epistemic Inscription` | Grouping: persistent renderings. |
| `Aggregate` → Logic → `Epistemic Communication` → `Epistemic Inscription` → Proof Script | A derivation written line by line, each line citing its rule, for checking. |
| `Aggregate` → Logic → `Epistemic Communication` → `Epistemic Publication` | Grouping: published expositions. |
| `Aggregate` → Logic → `Epistemic Communication` → `Epistemic Publication` → Logic Treatise | Sustained exposition of a formal system and its metalogic. |
| `Aggregate` → Logic → `Epistemic Infrastructure` | Grouping: structures enabling the inquiry. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: tools performing the logic. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Epistemic Tool` → Proof Assistant | Software checking each derivation step against the system's rules. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Epistemic Tool` → Proof Assistant → Lean | Exemplar proof assistant realizing the tool: a dependent type theory kernel. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Epistemic Tool` → SAT Solver | Software deciding propositional satisfiability by systematic search. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Information Repository` | Grouping: stored results and reference. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Information Repository` → Theorem Index | Catalogue of established metalogical results consulted instead of reproved. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Epistemic Institution` | Grouping: bodies sustaining the discipline. |
| `Aggregate` → Logic → `Epistemic Infrastructure` → `Epistemic Institution` → Refereed Journal | Institution certifying and publishing metalogical results that pass peer proof check. |
| `Aggregate` → Logic → `Epistemic Context` | Grouping: conditions surrounding the inquiry. |
| `Aggregate` → Logic → `Epistemic Context` → `Epistemic Condition` | Grouping: conditions under which results are interpreted. |
| `Aggregate` → Logic → `Epistemic Context` → `Epistemic Condition` → Classical Condition | Results conditional on accepting the law of excluded middle and bivalence. |
| `Aggregate` → Logic → `Epistemic Context` → `Epistemic Condition` → Consistency Condition | Metalogical results conditional on the system's assumed consistency. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdict.** Logic is the most conceptually determinate discipline in this inventory after mathematics: its identity, its boundary rule, and its warrant (soundness and completeness relative to a stated semantics) are exceptionally sharp, and its representational adequacy is proven by its role as the universal scaffolding of inference. Its principal limit is *expressive reach*: a formal system captures only the consequence relation it was built to capture, and the step from an informal argument to its formalization is always a judgment the system cannot certify.

| Criterion | Verdict | Diagnostic Focus |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from mathematics (studies the rules of inference, not their application), from epistemology (takes consequence as target, not knowing), and from rhetoric (warrant is formal derivability, not persuasion). |
| Definitional Clarity | Strong | Formal language, proof system, semantics, soundness, and completeness are stated as explicit conditions; the informal-to-formal step is named as a judgment, not hidden. |
| Conceptual Determinacy | Strong | Boundary rule: an argument is logically valid iff every model of its premises models its conclusion. Borderline cases (invalid in one logic, valid in another) are handled by declaring the system. |
| Internal Consistency | Strong | Syntax, proof system, and semantics are related by stated soundness and completeness claims; no branch requires a formula to be both derivable and unrefutable. |
| Representational Adequacy | Strong | The `Aggregate` reading captures the discipline; the decomposition separates proof system (syntax) from semantics (meaning), which is exactly where confusions usually arise. |
| Purpose Adequacy | Strong | Consequence, formalization, and foundation are all served; the note never claims a formalization is faithful to the informal argument it replaces. |
| Expressive Reach | Moderate | Every formal system captures only the consequence relation it was built for; classical, intuitionistic, modal, and substructural logics disagree on what is valid, and no single system is universal. |

Its limits follow from the same source as its strength. The formalization step
is load-bearing and unverified: whether a formal argument faithfully captures
its informal original is a judgment outside the system, and a sound derivation
of the wrong formalization is still a wrong conclusion. The discipline's
deepest results are also *negative*: Gödel's incompleteness theorems bound what
any sufficiently expressive system can prove about itself, and undecidability
bounds what any effective procedure can decide. Overall the instance is mature
and heavily validated; what its warrant is conditional on is the fidelity of the
formalization and the consistency of the system.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) (evaluation criteria)
- [Boolean Algebra](note.html?n=epistemica/mathematical/boolean-algebra.md) — the algebraic reading of propositional logic
- [Mathematics](note.html?n=epistemica/discipline/mathematics.md) — the parent formal discipline
- [Computer Science](note.html?n=epistemica/discipline/computer-science.md) — the discipline that executes logic
- [EES](note.html?n=epistemica/ees.md) — the inventory this discipline is indexed in
- [Logic](https://en.wikipedia.org/wiki/Logic)
- [Mathematical logic](https://en.wikipedia.org/wiki/Mathematical_logic)
- [Gödel's incompleteness theorems](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)
