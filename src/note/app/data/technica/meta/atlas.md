---
tags: [technica, atlas, method]
---

# Technical Element Forest (TEF)

> The technical element forest is the merged decomposition of the technica corpus: every row of every `| Instance Tree Path |` decomposition table, fused into one instance tree and typed by the vocabulary of the canonical technica guide.

This note is the local companion of the canonical guide
[Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md),
which owns the schema, the Tabular taxonomy, and the Recursive-view grammar.

The forest is inferred from the **decomposition tables**, never from the
directory layout of `src/note/app/data/technica/`. A directory is where a
note is filed; a table row is where an element sits in the decomposition.
Only the tables carry the second. The table form is the guide's canonical
one — `| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Technical Element | The synthetic forest root: every decomposition table merged beneath it. |
| `Technical Element Set` → Technical Element → `Constitutive Technical Object` → JobRunr | Branch root: the JobRunr library decomposed by `jobrunr.md`. |
| `Technical Element Set` → Technical Element → `Production Technical System` → Transformer System | Branch root: the Transformer System decomposed by `transformer.md`. |
| `Technical Element Set` → Technical Element → `Production Technical System` → WildFly | Branch root: the running WildFly server decomposed by `wildfly.md`. |
| `Technical Element Set` → Technical Element → `Production Technical System` → Eclipse | Branch root: the Eclipse product instance decomposed by `eclipse.md`. |
| `Technical Element Set` → Technical Element → `Technical Element Set` → System Connector | Branch root: the system connector decomposed by `system-connector.md`. |
| `Technical Element Set` → Technical Element → `Technical Element Set` → Biotechnology | Branch root: the biotechnology ensemble decomposed by `biotechnology.md`. |
| `Technical Element Set` → Technical Element → `Technical Element Set` → Energy Technology | Branch root: the energy-technology ensemble decomposed by `energy-technology.md`. |
| `Technical Element Set` → Technical Element → `Technical Element Set` → Physical Material Technology | Branch root: the physical-material ensemble decomposed by `physical-material-technology.md`. |
| `Technical Element Set` → Technical Element → `Technical Mechanism` → Attention | Branch root: the attention mechanism decomposed by `attention.md`. |
| `Technical Element Set` → Technical Element → `Technical Standard` → Jakarta EE | Branch root: the Jakarta EE standard set decomposed by `java-ee-jakarta-ee.md`. |
| `Technical Element Set` → Technical Element → `Technical Standard` → OpenAPI | Branch root: the OpenAPI standard and tooling decomposed by `openapi.md`. |

The table is the backbone, not the inventory: every branch above is one
table root, and each branch continues to the depth its table reaches. The
atlas stats bar reports the current row, table, node, and depth counts.

### What is a critical conceptual evaluation of this `technical element instance`?

> The forest concept is sound as an **index over the tables** and weak as a
> description of the corpus: it reproduces what the tables say, and says
> nothing about the notes that carry no table.

Evaluated against the canonical
[Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
(minimum set), leading with the verdicts:

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | **Pass** | The forest is explicitly distinguished from the file layout, from the guide's grammar, and from the epistemic REES atlas; its identity is "the merged decomposition tables". |
| Definitional Clarity | **Qualified** | The merge rule (path-keyed trie, sources kept) and the type rules (fourth-column alignment, inline backticked segments) are stated; the resolution of conflicting duplicate types across notes is stated but left as a table defect rather than a forest rule. |
| Conceptual Determinacy | **Qualified** | Membership is determinate — a node exists iff a table row names it — but the boundary is the corpus's table coverage, not the corpus: 11 of 1,962 technica notes carry a decomposition table today, so the forest is a thin spine over a large corpus. |
| Internal Consistency | **Pass** | One synthetic root, unique sibling labels by construction, one type vocabulary, and `meta/` excluded so the atlas never indexes itself. |
| Representational Adequacy | **Qualified** | Faithful and typed where the tables are explicit; intermediate segments without their own row inherit their nearest ancestor's type, and merged nodes keep only the first description — both are losses the inspector cannot show. |
| Purpose Adequacy | **Pass** | As an orientation instrument over the decompositions it is fit: the inspector links every node to the notes that define it, and the views scale from the 11 branch roots down to a named config attribute. |

**Strengths.** The forest makes the decomposition auditable at the corpus
level: a table row that names an element puts it in the forest, and a note
without a table is visibly absent rather than silently mis-filed. The
dendrogram view shows the whole shape of a branch in one screen.

**Risks.** (i) *Coverage illusion* — the tree looks complete while it only
indexes the notes that decompose; the catalog, not the atlas, is the
inventory of the corpus. (ii) *Filing drift* — a note moved between
directories no longer changes its place in the forest, which is the point,
but the reverse also holds: filing a note under a suggestive directory
does not put it in the decomposition. (iii) *Merge smoothing* — two notes
that disagree about an instance's type produce one node with one type and
two sources; the disagreement is invisible in the store.

## The Sync Rule

> The forest is your decomposition tables. Edit a table, regenerate the
> store; do not edit the store.

- Every table row is an instance path; the forest is regenerated from the
  tables after any edit under `src/note/app/data/technica/` with
  `make atlas-index`.
- `make atlas-check` (part of `make check`) validates the merged store:
  one synthetic root, sibling labels unique, every non-root node sourced
  from an existing technica note, note links resolve, stats consistent.
- Table grammar conformance stays with `src/note/bin/conform.py` (every
  fourth-column path resolves to a Recursive-view grammar path); the atlas
  checker validates the store, not the tables.
- `src/note/app/data/technica/meta/` is excluded from parsing: the atlas
  and this note are meta-level tooling, not elements of the forest.
- The store is generated data: it is never edited by hand, and it carries
  no changelog entry. The notes it indexes do.

## Entry Map

> The forest is the merged table; the atlas is its viewer; the notes are
> its sources.

- **The full tree** — the [Technica atlas](data/technica/meta/atlas.html) renders the complete, ever-expanding decomposition from the store [atlas.json](data/technica/meta/atlas.json): outline, branch cards, a dendrogram, an element search, and a node inspector.
- **Guide** — [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) (schema owner).
- **Epistemic complement** — [REES](note.html?n=epistemica/rees.md) and its [atlas](data/epistemica/rees.html): the same grammar applied to the epistemic corpus.
- **Catalog** — [technica](index.html?dir=technica) in the notes catalog browses the corpus that carries the tables.

## References

- [Technica atlas](data/technica/meta/atlas.html) — the complete, ever-expanding decomposition (views over [atlas.json](data/technica/meta/atlas.json))
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) — the evaluation criteria
- [REES](note.html?n=epistemica/rees.md) — the epistemic-element atlas this one mirrors
