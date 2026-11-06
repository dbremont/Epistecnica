---
tags: [clustering, firms, 10-k]
---

# Firm Clustering

> **Firm Clustering** is the firm-classification pipeline contrasting NAICS and GICS against data-driven 10-K clustering. Source: Produceologia `docs/Toolkit/Method/Clustering.md` (read-only import; the originals are untouched).

## Formulation

### What epistemic element type does this epistemic instance belong to?

**Firm Clustering belongs to the `Epistemic Activity (Process)` epistemic element type — ordered tool applications forming a classification process.**

### What is this epistemic instance?

> SEC filings feed a text pipeline (spaCy config plus notebooks) that clusters firms empirically, testing where official taxonomies hold and where they break.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: one pipeline, decomposed at shallow depth — the process plus its source, tool, and output constituents. Instance Tree Path holds instances only.

| Instance Tree Path | Description | Epistemic Category | Epistemic Element Type Tree Path |
| --- | --- | --- | --- |
| Firm Clustering | Empirical firm-classification process. | Agency | `(root) := <<Epistemic Element>> -> Epistemic Activity (Process)` |
| Firm Clustering → SEC Filings Corpus | 10-K evidence artifact feeding the pipeline. | Representation | `(root) := <<Epistemic Element>> -> Concrete Epistemic Artifact` |
| Firm Clustering → Clustering Configuration | spaCy pipeline configuration tool. | Methodology | `(root) := <<Epistemic Element>> -> Epistemic Tool` |
| Firm Clustering → Cluster Map | Empirical grouping output artifact. | Representation | `(root) := <<Epistemic Element>> -> Concrete Epistemic Artifact` |

## References

- Produceologia `docs/Toolkit/Method/Clustering.md`
- Produceologia `docs/Toolkit/Data/SEC/README.md` (filing categories)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)
