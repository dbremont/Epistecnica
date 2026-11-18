---
tags: [note, documentation, design]
---

# Design Document

> A **design document** is the artefact that argues a technical decision **before** it is implemented: the problem and its constraints, the alternatives, the proposed design, the risks, and the plan for adopting it. It is a document about *reasoning*, not about status — the code will eventually describe what was built, but it will never explain why this shape was chosen and what was rejected.

## Structure

| Section | Question it answers | What its absence costs |
| --- | --- | --- |
| **Context / problem** | What situation forces a decision, and what constrains it? | The reader cannot tell whether the design answers the right question |
| **Goals and non-goals** | What is this design for, and what is it explicitly not for? | Scope creep: the document is read as a promise for everything adjacent |
| **Alternatives considered** | What else was possible, and why was it rejected? | The decision looks arbitrary, and the same ground is re-argued in six months |
| **Proposed design** | What are the components, interfaces, data and flows? | The reader cannot evaluate the claim |
| **Risks and mitigations** | What can go wrong, and what happens if it does? | Risk is discovered during implementation instead of before it |
| **Rollout / migration** | How does the system get from here to there? | A correct design that cannot be adopted |
| **Open questions** | What is not settled, and who decides it? | False completeness: the unresolved parts get decided by accident |

> Two rows carry most of the value. **Non-goals** and **alternatives** are what distinguish a design document from a status report: a status report says what will be done, a design document says what will *not* be done, and why the discarded option was discarded.

## Process

> A design document is written **early enough to be argued with**, circulated before the implementation commits to anything, and revised with comments attributed rather than silently absorbed. Its schedule is part of its function: a document that arrives after the code is a description, which the code already is.

> Reviewers should be able to disagree with the **reasoning**, not merely with the style. That is the test of whether the document is doing its job — and the reason the alternatives section is mandatory: a reviewer can only disagree with a choice that was presented as a choice.

## Relations

| Artefact | What it carries | Relation to the design document |
| --- | --- | --- |
| **Architecture Decision Record (ADR)** | One decision, its context and its consequence | The durable, minimal subset — one design document may produce several ADRs |
| **Specification** | What the system must do | Input: the requirements the design answers |
| **Design document** | How and why the system will be shaped this way | The argument that connects specification to implementation |
| **Implementation plan / ticket** | The sequence of work | Output: the design decomposed into steps |

## References

- [Write an Effective Design Doc — Refactoring English](https://refactoringenglish.com/excerpts/write-an-effective-design-doc/)
- [Documentation](/view.html?p=notes/technica/computation/system/documentation.md) — the discipline this document type belongs to
- [Design](/view.html?p=notes/technica/computation/system/design.md) — the system-design master
- [Software Specification](/view.html?p=notes/technica/computation/system/design/software-specification.md) — the requirements the design answers
- [Program](/view.html?p=notes/technica/production/industry/software/production/program.md) — knowledge capture in the production process
