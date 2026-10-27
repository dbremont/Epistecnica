# Epistecnica — Epistemic Content Extraction Spec

> A reusable method for turning a book into a sourced epistemic-element
> forest and a large `Instance Tree Path | Description` table. The
> Korzybski extraction is the worked example; the algorithm below is
> book-agnostic.

## 1. Purpose

Extract the **epistemic content** of a book: the elements by which its
author orients inquiry, accesses a target, represents and constructs
knowledge, operates on content, evaluates it, communicates it, sustains
it, and parses the reality it addresses.

The method is not a summary and not a literary interpretation. It produces
a typed, recursively decomposable inventory whose rows are traceable to
the book's own text.

Use it when the target is a long, structurally complex source (a book, a
treatise, a long report) and the desired output is a reusable epistemic
inventory rather than a prose summary.

## 2. What the method produces

A complete run produces:

- `epistemic-elements.json` — canonical multi-root forest, the source of truth.
- `epistemic-elements.table.md` — canonical two-column table:
  `Instance Tree Path | Description`, one section per root.
- `epistemic-elements.full.md` — enriched table with root, type, kind,
  order, depth, printed/PDF pages, confidence, aliases.
- `epistemic-elements.csv` — the enriched table as data.
- `epistemic-elements.html` — local searchable/filterable preview.
- `stats.json` — counts by root, type, branch, depth, source coverage.
- `validation.json` — grammar/type/source validation results.
- `coverage-report.md` / `coverage.json` — chunk, key-concept, and
  coverage audit.
- `README.md` — edition, source artifacts, method, caveats.

The JSON forest is primary. Every other artifact is generated from it.

## 3. The algorithm

```text
1. acquire source
   → identify edition, download, verify text layer / OCR quality
2. normalize text
   → split pages, detect printed pages, map PDF ↔ printed, clean headers
3. discover structure
   → parse TOC/chapter headings, index, key concepts
4. define scope
   → include body/prefaces/appendices; exclude notes/bibliography/index
5. chunk
   → chapter/section chunks, split long sections, attach page metadata
6. define grammar
   → type vocabulary, allowed parent→child links, roots, type overrides
7. extract
   → per-chunk JSON candidates with quotes and pages
8. consolidate
   → normalize labels/aliases, dedupe, vote types, merge sources
9. audit coverage
   → key concepts, chunk yield, optional index terms; targeted follow-up
10. assemble
   → multi-root forest, grouping segments, licensed reparenting
11. validate
   → unique paths, licensed links, instance leaves, sources, Title Case
12. render
   → canonical table, enriched table, CSV, HTML, stats, coverage
```

Verification of the source and the type/grammar contract must happen before
extraction. Extraction of a 300-page book without a page map or a fixed type
vocabulary produces untraceable and unmergeable output.

## 4. Stage contracts

### 4.1 Source acquisition

- Identify the exact edition and the text source.
- Prefer a **text-layer PDF** or a trustworthy HTML/plain-text source.
  A scanned PDF is a source artifact, not an extraction source unless OCR
  is part of the run.
- Download and record:
  - source URL;
  - file size and checksum;
  - page count, metadata, edition;
  - whether a text layer exists.
- Keep the requested source artifact even when a different edition supplies
  the text layer. State the edition used for page citations.

**Failure:** image-only PDF, lending restrictions, missing pages, or an
edition mismatch. Resolve before extraction.

### 4.2 Text normalization

- Extract text page by page with a layout-preserving mode.
- Split on form feeds and build a page map:
  - PDF page;
  - printed page (detect from running headers/footers);
  - interpolated printed page for unnumbered title/plate pages;
  - nearest chapter/part.
- Remove running headers/footers, standalone page numbers, and repeated
  furniture without deleting chapter titles.
- Join OCR line-break hyphenation conservatively (`-\n` + lowercase).
- Preserve page markers such as `[[PDF 467 | PRINTED 370]]` for quoting and
  later verification.

Page-number offsets are usually **not constant**: unnumbered part/chapter
title pages shift the PDF↔printed offset. Detect per page; do not apply one
global offset.

### 4.3 Structure and scope

- Parse BOOK / PART / CHAPTER headings from the text; use the TOC as a
  cross-check.
- Identify the index and use its terms only as a coverage checklist, not as
  extracted content.
- Declare scope explicitly:
  - main body;
  - prefaces/introductions;
  - appendices;
  - excluded: notes, bibliography, index, diagram index, publisher matter.
- Record the scope in the output README and stats.

### 4.4 Chunking

- Chunk by book/part/chapter, not by fixed character windows first.
- Split a long section on paragraph boundaries into ~35–60k-character
  windows, with a small overlap.
- A chunk manifest must carry:
  - `chunk_id`;
  - book / part / chapter;
  - start/end PDF page;
  - start/end printed page;
  - char count;
  - `split` flag.
- For very dense appendices, split to ~15–20k characters so the model can
  finish its JSON output within the completion cap.

### 4.5 Type and grammar schema

Use the canonical epistemic vocabulary, not an ad-hoc per-book vocabulary.

- Types come from the canonical guide and the local EES inventory.
- Store:
  - `types`: type name → branch + description;
  - `allowed_parent`: parent type → permitted child types.
- Add `Aggregate → <every top-level branch>` and self-links where recursive
  decomposition is permitted.
- Define a type-priority list for resolving conflicting votes from the
  extractor.
- Define explicit overrides for known misclassifications (e.g. an act
  extracted as an error, a process extracted as a concept).
- Composite instances get a `Set` suffix **only** when genuinely composite
  (a named set/family/levels/trilogy/classification), and only past depth 2.
  Do not apply `Set` to every plural label.

### 4.6 Extraction prompt contract

The prompt must state:

- the book, edition, and chunk metadata;
- the definition of an epistemic element;
- what to include and exclude;
- the exact type vocabulary (with branch hints);
- the root list;
- the output JSON schema;
- the quote/page requirement;
- the rule “instances only; grouping rows are added later”;
- strict JSON formatting rules.

The extraction element shape:

```json
{
  "label": "Title Case label",
  "aliases": ["variant names"],
  "type": "one canonical type",
  "kind": "instance",
  "description": "1–2 sentences in the book's vocabulary",
  "quote": "short verbatim quote",
  "pdf_page": 467,
  "printed_page": 370,
  "root_hints": ["General Semantics Inquiry"],
  "parent_hint": "optional containing instance",
  "composite": false,
  "readable_as": [],
  "confidence": 0.9
}
```

Extraction rules:

- Prefer the book's own most explicit term.
- Do not extract passing illustrative nouns, historical names, book titles,
  publishers, or bibliography entries unless they function as epistemic
  agents/institutions/tools.
- Do not extract generic schema types as instances.
- Every element needs evidence. No quote → no element.
- Merge duplicate mentions inside a chunk into one entry with aliases.

### 4.7 Consolidation

- Normalize labels and aliases:
  - lowercase, strip punctuation, collapse whitespace;
  - handle possessives and simple plurals;
  - keep a stable canonical label.
- Union-find by label/alias forms to dedupe.
- Choose the type by:
  1. majority vote;
  2. type-priority list;
  3. explicit overrides.
- Merge sources, aliases, descriptions, parent hints, and confidence.
- Record `mentions` and `type_votes` for auditability.
- Assign a primary root and optional secondary roots.
- Filter out labels that are exactly a schema type.

### 4.8 Coverage audit

Run at least these checks:

1. **Chunk yield** — every substantive chunk yielded candidates; flag
   chunks with zero or very low yield.
2. **Key concepts** — a curated list of the book's central concepts is
   100% present as a label or alias, or a waiver is recorded.
3. **Optional index coverage** — extract index terms and check the
   epistemic subset against labels/aliases.
4. **Branch coverage** — every top-level branch has instances, or the
   absence is explained.
5. **Source coverage** — every instance has at least one quote/page.

Targeted follow-up is better than a blanket second extraction pass: use
the missing terms' indexed pages or nearby chunks and add sourced entries.

### 4.9 Assembly

- Build one root per declared theme.
- Insert grouping segments from the type hierarchy:
  - branch grouping;
  - subtype groupings (BFS path from branch to instance type).
- Attach instances under the deepest grouping.
- Reparent an instance under `parent_hint` only when the parent exists in
  the same root and the parent→child type link is licensed.
- Prune empty groupings.
- Sort groupings by branch order, then instances alphabetically.
- Apply composite `Set` naming after reparenting.

Multiple roots are allowed to share elements. Prefer a primary assignment
and duplicate only for strong secondary themes; otherwise the table grows
without adding information.

### 4.10 Validation

Fail the run on grammar errors:

- every path unique within a root;
- every non-root row extends an existing path by one link;
- every parent→child type link is licensed;
- grouping nodes never terminate a branch;
- every leaf is an instance;
- every instance has a source;
- instance labels are Title Case;
- composite instances past depth 2 end in `Set` when applicable;
- no duplicate sibling labels.

Warnings are allowed for style or ambiguity, but must be reviewed and
reported.

### 4.11 Rendering

- Canonical table: one section per root; path segments use `→`; type
  grouping segments are backticked; instances are plain Title Case.
- Enriched table adds root, type, kind, order, depth, printed/PDF pages,
  confidence, aliases.
- CSV mirrors the enriched table.
- HTML is a local, dependency-free search/filter preview.
- Write `README.md`, `stats.json`, `validation.json`, and
  `coverage-report.md` next to the artifacts.

## 5. Data contracts

### Chunk manifest

```json
{
  "chunk_id": "chunk-0024",
  "book": "Book II",
  "part": "Part VII",
  "chapter": "Chapter XXIV: On Abstracting",
  "start_pdf": 467,
  "end_pdf": 481,
  "start_printed": 370,
  "end_printed": 385,
  "chars": 42000,
  "split": false
}
```

### Merged candidate

```json
{
  "label": "Abstracting",
  "aliases": ["abstraction", "abstracting process"],
  "type": "Epistemic Act",
  "branch": "Epistemic Agency",
  "primary_root": "General Semantics Inquiry",
  "secondary_roots": ["Reflexive Inquiry"],
  "description": "The nervous process of selecting, omitting, and integrating aspects of experience.",
  "sources": [
    {
      "pdf_page": 475,
      "printed_page": 379,
      "quote": "what the nervous system does is abstracting",
      "chunk": "chunk-0024"
    }
  ],
  "parent_hint": "",
  "composite": false,
  "readable_as": [],
  "confidence": 0.98,
  "mentions": 7,
  "type_votes": {"Epistemic Act": 5, "Action": 2}
}
```

### Forest node

```json
{
  "label": "Abstracting",
  "type": "Epistemic Act",
  "kind": "instance",
  "order": "epistemic",
  "description": "The nervous process of selecting, omitting, and integrating aspects of experience.",
  "aliases": ["abstraction"],
  "sources": [{"pdf_page": 475, "printed_page": 379, "quote": "..."}],
  "confidence": 0.98,
  "composite": false,
  "readable_as": [],
  "children": []
}
```

Forest roots are the same shape with `kind: "root"`.

## 6. Model and API policy

- Prefer non-reasoning models for JSON extraction. Reasoning models may
  spend the entire completion budget on hidden reasoning and return empty
  or truncated content.
- Use a strict JSON response mode where available, plus explicit
  “no prose” instructions.
- Save the raw response before parsing. On invalid JSON:
  - salvage complete objects from the truncated array;
  - split the chunk and retry;
  - only then retry with a repair prompt.
- Use hard budgets:
  - max requests;
  - max total tokens;
  - max concurrency;
  - max tokens per call;
  - max retries.
- Stop immediately on authentication or balance errors.
- On `429`, cool down the model and switch; never busy-loop.
- Make the run resumable: one state file per chunk, skip completed chunks.
- Never print, log, or commit API keys. Read them from the environment or a
  local auth store.
- When a paid cap is reached, stop. Fill only small gaps with a free model
  if that is allowed, and record the exception in the output.

## 7. Quality gates

A run is acceptable only when:

- every substantive chunk is extracted;
- raw → merged counts are reported;
- key concepts are 100% present or explicitly waived;
- validation reports 0 errors;
- every instance has at least one source;
- the canonical table and JSON contain the same nodes;
- stats and coverage reports agree with the forest.

## 8. Multi-root strategy

- A root is a thematic inquiry, not a type.
- Name roots after the book's own organizing concerns.
- Use `Aggregate` roots for inquiry systems; use a specific type root only
  when the root genuinely is that element (e.g. a tool).
- Assign each element a primary root.
- Add a secondary root only when:
  - the extractor explicitly marked it; or
  - a curated keyword list says the element belongs to that theme.
- Duplicate elements across roots when the book genuinely uses them in both
  inquiries; otherwise cross-reference by alias.

## 9. Reuse checklist for a new book

Before extraction:

- [ ] Choose the edition and text source; verify text layer.
- [ ] Record the source artifact, checksum, page count, and edition.
- [ ] Build the page map and inspect a sample of pages.
- [ ] Parse the structure and declare scope.
- [ ] Define the root set.
- [ ] Curate a key-concept checklist.
- [ ] Load the canonical type vocabulary and allowed links.
- [ ] Define type overrides for expected ambiguities.
- [ ] Set token/request/concurrency caps.
- [ ] Freeze the prompt and test it on 1–2 chunks.

After extraction:

- [ ] Merge and dedupe.
- [ ] Audit chunk yield and key concepts.
- [ ] Add targeted/manual entries for gaps.
- [ ] Assemble roots.
- [ ] Validate grammar and sources.
- [ ] Render tables and reports.
- [ ] Record caveats: edition, OCR, model, cap, waivers.

## 10. Pitfalls

- **Image-only PDF.** A scanned source is not a text source. Find a text
  layer or run OCR; do not pretend the scan is extractable.
- **Global page offset.** Unnumbered title pages change the offset. Detect
  per page and interpolate.
- **Running headers in the text.** They pollute quotes and page detection.
  Remove them but keep chapter headings.
- **Reasoning-model truncation.** The completion budget can be consumed by
  reasoning tokens, leaving empty content. Use a non-reasoning model or
  split the chunk.
- **CLI/subagent restrictions.** Free tiers may refuse headless CLI calls,
  and tool-using agents may read/search/write instead of returning JSON.
  Use the platform's task/subagent path or a direct API with a no-tools
  prompt.
- **Truncated JSON.** Never discard a truncated response blindly; salvage
  complete objects, then split the input.
- **Over-aggressive `Set` suffix.** Only true composites get `Set`; plurals
  are not automatically sets.
- **Type drift.** The extractor will call acts “errors” and processes
  “concepts”. Use a priority list and explicit overrides.
- **Root skew.** The dominant root absorbs everything. Curate secondary
  roots and key terms.
- **Silent coverage gaps.** A clean validation report does not prove
  coverage. Audit chunks and key concepts separately.

## 11. Worked example — Korzybski, *Science and Sanity*

- Source artifact: 1933 scan (image-only) plus a 5th-edition text-layer PDF
  (910 pages).
- Scope: body, prefaces, introductions, appendices; notes, bibliography,
  and index excluded.
- 49 substantive chunks; dense appendices split into subchunks.
- 2,010 raw candidates → 688 merged candidates + 8 curated additions.
- 6 roots: General Semantics Inquiry, Non-Aristotelian Revision,
  Time-Binding Inquiry, Sanity Inquiry, Reflexive Inquiry, Structural
  Differential Inquiry.
- Final forest: 1,469 rows, 1,172 instances, 291 groupings, 0 validation
  errors, 0 warnings.
- Coverage: 49/49 chunks; 38/38 key concepts after adding the extensional
  devices and the map–territory relation.
- Run policy: free models first; paid API stopped at the 500k-token cap
  (~511k used); the final small gap was filled with the free model.

The reference implementation lives outside the repo, under the temporary
run workspace. The spec is the reusable artifact; the implementation is
replaceable.

## 12. References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- `src/note/app/data/epistemica/ees.md` — local companion and schema note.
- `src/note/app/data/epistemica/ees.json` — EES tree store and type
  vocabulary.
- `spec/spec.md` — Epistecnica system spec.
- `spec/design.md` — shared design system.
