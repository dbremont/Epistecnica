---
tags: [note, clustering, firms, 10-k, method]
---

# Firm Clustering

> **Firm Clustering** is the firm-classification pipeline that contrasts official taxonomies (NAICS, GICS, SIC) with data-driven clustering of firm filings. It is both an epistemic process and an industry-analysis method: it delimits the population of firms, tests where official categories hold, and exposes where they break.

## Formulation

### What epistemic element type does this epistemic instance belong to?

**Firm Clustering belongs to the `Epistemic Activity (Process)` epistemic element type — ordered tool applications forming a classification process.**

### What is this epistemic instance?

> SEC filings feed a text pipeline (spaCy config plus notebooks) that clusters firms empirically, testing where official taxonomies hold and where they break. Classification assigns firms to one or more categories — industry, sector, subsector or strategic group — by primary revenue source, input-output relations, production technologies, customer base or strategic behaviour.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: one pipeline, decomposed at shallow depth — the process plus its source, tool, and output constituents. Instance Tree Path holds instances only.

| Instance Tree Path | Description | Epistemic Category | Epistemic Element Type Tree Path |
| --- | --- | --- | --- |
| Firm Clustering | Empirical firm-classification process. | Agency | `(root) := <<Epistemic Element>> -> Epistemic Activity (Process)` |
| Firm Clustering → SEC Filings Corpus | 10-K evidence artifact feeding the pipeline. | Representation | `(root) := <<Epistemic Element>> -> Concrete Epistemic Artifact` |
| Firm Clustering → Clustering Configuration | spaCy pipeline configuration tool. | Methodology | `(root) := <<Epistemic Element>> -> Epistemic Tool` |
| Firm Clustering → Cluster Map | Empirical grouping output artifact. | Representation | `(root) := <<Epistemic Element>> -> Concrete Epistemic Artifact` |

## Classification questions

- To which market or industry does this firm belong?
- What other firms belong to the same market or industry?
- Where do official taxonomies (NAICS, GICS, SIC) agree with empirical clustering, and where do they diverge?
- Which grouping is stable across data sources and methods?

## References

- Produceologia `docs/Toolkit/Method/Clustering.md`
- Produceologia `docs/Toolkit/Data/SEC/README.md` (filing categories)
- [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md)
- [Industry Analysis](/view.html?p=notes/epistemica/singular/industry/type/industry-analysis.md)
