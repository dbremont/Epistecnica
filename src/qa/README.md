# Q/A Log

> The open questions behind the corpus — a searchable log of the questions
> worked through, with answers where there are any. Served at `/qa/`.

## Layout

```
src/qa/
├── README.md        # this document
└── app/             # served statically at /qa/
    ├── index.html   # catalog: full-text search, agent/run/tag facets
    ├── entry.html   # single entry viewer (?id=qa-00001), prev/next
    └── data/
        ├── qa.json        # source of truth (hand-normalized, committed)
        └── qa-index.json  # generated search index (do not edit)
```

- Entries are `{id, question, answer, agent, run, date, source, tags, status}`;
  ids are stable (`qa-%05d`) and never reused — new entries append.
- Regenerate the index after any `qa.json` change: `make qa-index`
  (`bin/build_qa_index.py`, chunked and progress-aware).
- The catalog and the viewer feed the universal search (`make search-index`).
- This log is distinct from a note's own `qa:` front matter (the `QA · N` chip
  in the note viewer), which holds the questions attached to that note.
