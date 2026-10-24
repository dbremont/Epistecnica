---
tags: [technica, atlas, method]
---

# Technical Element Forest (TEF)

> The technical element forest is the complete, ever-expanding recursive decomposition of the technica corpus: every note a technical element instance, every directory a grouping, typed by the canonical technica guide wherever the grouping's index note declares its type.

This note is the local companion of the canonical guide
[Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md),
which owns the schema, the Tabular taxonomy, and the Recursive-view grammar.
The forest applies that grammar to this corpus: the directory tree of
`src/note/app/data/technica/` read as an instance tree, where the corpus
layout *is* the decomposition.

The **complete decomposition** lives in the **[Technica
atlas](data/technica/atlas/atlas.html)** — the viewer over the tree store
[`atlas.json`](data/technica/atlas/atlas.json). This note states the
contract; the atlas carries the full, ever-expanding forest with outline,
card, and node-inspector views.

## Formulation

### What is this technical element instance?

> The technical element forest is the corpus-level inventory of the
> technical elements the technica notes decompose: a typed tree over every
> note, grown from the directory structure and generated into a single
> store.

It is a `Technical Element Set` in the sense of the canonical guide: a
structured collection of technical elements organized as a coherent
technical whole. Unlike a hand-authored decomposition note, the forest is
generated — the corpus directory tree supplies the structure, the index
notes supply the grouping types, and the notes index supplies titles,
descriptions, and tags.

### What technical element type does this technical instance belong to?

> `Technical Element Set`.

The forest is a set of technical elements, so it belongs to the
`Technical Element Set` type. Its section roots are typed by their own
nature — the Active Inference System and Computation branches are
`Technical Domain`s, the object directories are constitutive or production
technical objects, and the robotic-system branch is a production technical
system. Read as an atlas (an instrument for orientation), it is *readable
as* `Technical Element Infrastructure`; that reading stays prose and is not
decomposed here.

### Is the type of this `technical element instance` unambiguous?

No at the root: `Technical Element Set` is the only type that covers a
whole corpus inventory. Two recurring branch ambiguities are worth stating:

- **Domain vs. technique.** A directory like `synthesis/` groups both
  problems (practice notes) and techniques (general/constitutive technique
  notes). The index note's declared type wins for the grouping; the mixed
  children are the guide's own practice→technique chain, not an ambiguity
  of the forest.
- **Object vs. system.** `application/` groups system types while `pto/`
  groups tools; both are production-facing. The curated root types
  distinguish them (`Production Technical System` vs. `Production Technical
  Object`), and the guide's verb rules (implements vs. realizes) apply in
  the notes themselves.

### What is the recursive instance decomposition of this technical element?

> The table below is the **backbone**: the forest root and its six section
> branches. The **complete, ever-expanding decomposition** — every branch
> grown to its leaf notes — is not held in this note: it is the tree store
> [`atlas.json`](data/technica/atlas/atlas.json), rendered by the
> **[Technica atlas](data/technica/atlas/atlas.html)**. Read the note for
> the contract; open the atlas for the full tree and its views.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Technica | The forest root: the whole technica corpus as one technical element set. |
| `Technical Element Set` → Technica → Active Inference System | Grouping (`Technical Domain`): the AIS branch — domains, synthesis, architecture, inference, tooling, application, and the synthesized systems. |
| `Technical Element Set` → Technica → Computacion | Grouping (`Technical Domain`): the Computation branch — algorithms, computational complexity, and their theory. |
| `Technical Element Set` → Technica → Constitutive Technical Objects (CTO) | Grouping (`Constitutive Technical Object`): the constitutive structure of technical objects (es, lib, platform). |
| `Technical Element Set` → Technica → Operation | Grouping (`Technical Operation`): how technical work is carried out. |
| `Technical Element Set` → Technica → Production Technical Object (PTO) | Grouping (`Production Technical Object`): production tools and their parts. |
| `Technical Element Set` → Technica → Robotic System | Grouping (`Production Technical System`): actuators, goals, internal computation. |

### What is a critical conceptual evaluation of this `technical element instance`?

> The forest is an index, not a theory. It states where each note sits in
> the decomposition; it does not decide the decomposition's content.

- **Strength.** One typed index over the whole corpus makes the
  decomposition auditable: a note that does not fit any branch is visible
  immediately, and a new branch has to declare its type.
- **Risk of conflation.** Because the tree *is* the directory layout, a
  convenient filesystem move silently becomes an ontological claim. The
  guard is the sync rule below: every new instance must be added to the
  store, and the store is validated on every `make check`.
- **Type drift.** Grouping types come from index-note declarations with a
  curated fallback; a stale fallback outlives its reason. Prefer declaring
  the type in the index note (`> \`Type\` — …`) over extending the table.

## The Sync Rule

> Any change that adds an instance to a decomposition tree of a technical
> element must also add it to the forest.

- Every new instance in a decomposition tree of a technical element must
  also be present in [`atlas.json`](data/technica/atlas/atlas.json) —
  regenerate the store after any corpus edit under
  `src/note/app/data/technica/` with `make atlas-index`.
- `make atlas-check` (part of `make check`) validates the store: unique
  sibling labels, grouping types non-empty, instances leaf-only with an
  existing corpus path, stats consistent.
- The store is generated data: it is never edited by hand, and it carries
  no changelog entry. The notes it indexes do.

## Entry Map

> The forest is the index; the atlas is its viewer; the notes are its
> instances.

- **The full tree** — the [Technica atlas](data/technica/atlas/atlas.html) renders the complete, ever-expanding decomposition from the tree store [atlas.json](data/technica/atlas/atlas.json): outline, branch cards, an element search, and a node inspector.
- **Guide** — [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) (schema owner).
- **Epistemic complement** — [REES](note.html?n=epistemica/rees.md) and its [atlas](data/epistemica/rees.html): the same grammar applied to the epistemic corpus.
- **Catalog** — [technica](index.html?dir=technica) in the notes catalog browses the corpus the forest indexes.

## References

- [Technica atlas](data/technica/atlas/atlas.html) — the complete, ever-expanding decomposition (views over [atlas.json](data/technica/atlas/atlas.json))
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
- [REES](note.html?n=epistemica/rees.md) — the epistemic-element atlas this one mirrors
