---
tags: [principle, ontology, epistemology, method, normative]
---

# Principle

> **Principle** — a general proposition, rule, or commitment that establishes a constraint, regularity, standard, or foundational condition governing a domain of reality, inquiry, reasoning, or practice.

> A more principled approach to principles separates **what a principle is** from **the domain in which it holds or operates**. Ontic, epistemic, technical, and normative principles differ primarily in what they concern and what makes them valid. A principle's **domain of validity** must not be confused with its **domain of application**: a principle grounded in reality can be applied in inquiry or practice without thereby becoming epistemic or technical.

## Formulation

> What is a principle?
> What is the most fundamental categorization of principles?
> Are ontic, epistemic, technical, and normative principles exhaustive?
> How is a principle classified when it spans several domains?

## What is a principle?

A **principle** is a general proposition, rule, or commitment that serves as a fundamental basis for understanding, explaining, evaluating, or organizing something.

This definition encompasses different kinds of things. For example:

- **Ontic:** Conservation of energy.
- **Epistemic:** Evidence should be proportionate to the strength of a claim.
- **Technical:** A control system should remain stable under specified operating conditions.
- **Normative:** Equal cases should be treated equally.
- **Logical:** A proposition and its negation cannot both be true in the same respect and at the same time, under classical logic.

These principles do not have the same status. Some describe reality, others regulate inquiry or action, and others establish standards of reasoning or evaluation. Consequently, we should not define a principle exclusively as a *fundamental truth*; that definition would exclude principles that prescribe how we should reason or act.

> **Principle:** A general proposition, rule, or commitment that establishes a constraint, regularity, standard, or foundational condition governing a domain of reality, inquiry, reasoning, or practice.

The phrase *foundational condition* matters because not every principle is a law of nature, and not every principle is necessarily true.

## The primary classification

Three fundamental domains can be distinguished:

1. **Reality** — what exists and how it behaves.
2. **Epistemic practice** — how we know, investigate, represent, and justify claims about reality.
3. **Technical practice** — how we produce, control, maintain, and transform reality.

| Principle type | Domain | Fundamental concern | Examples |
| --- | --- | --- | --- |
| **Ontic Principle** | Reality | What exists, how it behaves, and what relations or constraints characterize it | Conservation laws; causal regularities; thermodynamic principles |
| **Epistemic Principle** | Knowledge and inquiry | How claims are established, knowledge is produced, and representations are evaluated | Falsifiability; evidential adequacy; reproducibility |
| **Technical Principle** | Technical activity | How agents produce, maintain, control, and transform things | Feedback control; modularity; redundancy in safety-critical systems |

These categories distinguish principles according to their **primary domain of reference**.

### Ontic principles

Ontic principles concern the organization, properties, relations, and dynamics of reality. Examples:

- Conservation of energy.
- The principle of least action.
- The principle that physical processes are constrained by the properties of their material substrates.

Their central question is: **what is the case in reality, or what constraints govern what can happen?**

Ontic principles should be distinguished from ontic laws, regularities, and facts. A principle might be a foundational theoretical proposition rather than an independently established law of nature.

### Epistemic principles

Epistemic principles concern the conditions and standards of knowledge production and justification. Examples:

- Claims should be supported by appropriate evidence.
- Experimental results should be reproducible under sufficiently similar conditions.
- Explanations should be evaluated against competing explanations.
- The strength of a conclusion should not exceed what its evidence supports.

Their central question is: **under what conditions can we establish, justify, or improve knowledge?**

Epistemic principles can be descriptive or normative. A principle might describe how scientists actually investigate phenomena, or prescribe how they ought to conduct investigations.

### Technical principles

Technical principles concern the organization and execution of activities directed toward producing or transforming outcomes. Examples:

- Feedback can be used to regulate a system toward a target state.
- Redundancy can improve reliability when components fail independently and the architecture supports effective failover.
- Modular decomposition can facilitate the independent development and maintenance of system components.
- Material selection must account for the operating conditions imposed on a component.

Their central question is: **how can we reliably achieve or maintain a desired state under specified conditions?**

Technical principles are not necessarily universal truths. Their validity may depend on the intended outcome, the operating environment, the available resources, and the constraints of the system. For example, redundancy is not always beneficial: it can introduce additional failure modes or complexity.

## Is this categorization genuinely fundamental?

It is fundamental in an important sense, but it is not necessarily exhaustive. The three categories classify principles by their relationship to reality, knowledge, and practical intervention, but these domains overlap.

Consider the principle of feedback:

- **Ontic interpretation:** Feedback relations occur in physical, biological, and social systems.
- **Epistemic interpretation:** Feedback can be used to improve an inquiry process.
- **Technical interpretation:** Feedback can regulate the behavior of a machine.

The same general idea appears in three domains, but the principles are not identical in their formulation or validity conditions. Similarly, the principle of reproducibility is epistemic when understood as a standard for evaluating scientific findings, but reproducible production is also a technical concern.

Therefore, a principle's **domain of validity** should be distinguished from its **domain of application**. A principle grounded in physical reality can be applied in epistemic or technical practice without thereby becoming exclusively epistemic or technical.

> Classify a principle primarily by the domain in which its validity conditions are established, rather than by every domain in which it can be applied.

This rule will not resolve every borderline case, but it gives the taxonomy a consistent starting point.

## Should normative principles be a fourth fundamental category?

There is a strong argument for distinguishing them, but we need to be precise. Consider four propositions:

1. **Ontic:** A system loses energy through friction under specified conditions.
2. **Epistemic:** A claim should be supported by sufficient evidence.
3. **Technical:** A machine should remain within its specified operating limits.
4. **Normative:** Public institutions should treat citizens equally under the law.

The fourth proposition does not merely describe reality, regulate inquiry, or specify how to achieve a technical objective. It establishes a standard for evaluating conduct or institutions:

| Principle type | Primary concern |
| --- | --- |
| Ontic | Reality and its organization |
| Epistemic | Knowledge and inquiry |
| Technical | Production and intervention |
| **Normative** | What ought to be done, permitted, required, or valued |

Normative principles can operate within epistemic and technical practices: a researcher may have an ethical obligation to avoid fabricating data, while an engineer may have an obligation to prioritize public safety. The distinction is therefore between the **normative status of a principle** and the **domain in which it operates**. We should not automatically assume that every principle that uses the word *should* is normative in the same sense: a technical requirement may be conditional on an objective, whereas a moral obligation may be asserted independently of that objective.

## A more rigorous classification architecture

Rather than forcing every distinction into one mutually exclusive taxonomy, principles can be classified along several axes.

**Axis 1 — Primary domain.** What does the principle primarily concern? Ontic, Epistemic, Technical, Normative.

**Axis 2 — Logical or functional character.** What kind of proposition or rule is it? Descriptive, Explanatory, Constitutive, Regulative, Prescriptive, Evaluative. These categories are not necessarily mutually exclusive; a technical safety principle may be both regulative and prescriptive.

**Axis 3 — Scope.** How widely does the principle apply? Universal, Domain-general, Domain-specific, Context-dependent. The scope of a principle should not be confused with its truth: a universal claim may be false, and a context-dependent principle may be well established.

**Axis 4 — Epistemic status.** How is the principle established or justified? Empirically established, Theoretically derived, Logically necessary (relative to a specified logical framework), Methodologically adopted, Normatively justified, Heuristically useful. Some principles may have multiple grounds.

## The resulting model

```text
Principle
│
├── Primary Domain
│   ├── Ontic Principle
│   ├── Epistemic Principle
│   ├── Technical Principle
│   └── Normative Principle
│
├── Functional Character
│   ├── Descriptive
│   ├── Explanatory
│   ├── Constitutive
│   ├── Regulative
│   ├── Prescriptive
│   └── Evaluative
│
├── Scope
│   ├── Universal
│   ├── Domain-General
│   ├── Domain-Specific
│   └── Context-Dependent
│
└── Justificatory Status
    ├── Empirically Established
    ├── Theoretically Derived
    ├── Logically Necessary
    ├── Methodologically Adopted
    ├── Normatively Justified
    └── Heuristically Useful
```

This is a **multidimensional classification**, not a strict decomposition tree. A principle can have one primary domain, several functional characteristics, a particular scope, and multiple grounds of justification.

For instance, a feedback-control principle could be classified as: primary domain **technical**; functional character **explanatory and regulative**; scope **domain-general**, within specified classes of systems; justificatory status **theoretically derived and empirically tested**. Its physical implementation may depend on ontic principles, but that does not make the technical principle identical to those physical principles.

## Principles versus laws, rules, and methods

| Concept | Defining characteristic |
| --- | --- |
| **Principle** | A general proposition or commitment that establishes a foundation, constraint, or standard. |
| **Law** | A proposition expressing a purportedly general relation or regularity, often within a scientific domain. |
| **Rule** | A specification governing permissible actions, transitions, or operations. |
| **Method** | An organized procedure for accomplishing an epistemic or practical objective. |
| **Criterion** | A condition or standard used to evaluate or classify something. |
| **Axiom** | A proposition adopted as a starting point within a formal or theoretical system. |
| **Heuristic** | A strategy that guides problem-solving without guaranteeing correctness or success. |

These concepts overlap in ordinary language, but their distinctions matter analytically. A principle can motivate a method, a rule can implement a principle, and a criterion can operationalize a principle for evaluation.

## Recommendation

> **Principle:** A general proposition or commitment that establishes a foundational condition, constraint, regularity, or standard governing a domain of reality, inquiry, or practice.

Primary classification:

1. **Ontic Principles** — principles concerning reality.
2. **Epistemic Principles** — principles concerning knowledge and inquiry.
3. **Technical Principles** — principles concerning the production and transformation of reality.
4. **Normative Principles** — principles concerning what ought to be done, permitted, required, or valued.

The key qualification is that this classification concerns the **principal domain** of each principle, not necessarily the complete range of its applications. This gives a relatively compact foundation while allowing principles to be classified more precisely by their logical character, scope, and justification.

## References

- https://en.wikipedia.org/wiki/Principle
- [Principle](/glossarium/?t=principle)
- [Social Action Principle](note.html?n=social/action/guidance/social-action-principle.md)
