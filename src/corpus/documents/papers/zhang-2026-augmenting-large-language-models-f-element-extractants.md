---
tags: [document, separation, rare-earth, actinide, ml]
---

# Zhang, B., Summers, T. J., Augustine, L. J., Taylor, M. G., Geist, A., Li, R., Batista, E. R., Perez, D., Yang, P., & Schrier, J. (2026). Augmenting Large Language Models for Automated Discovery of F-Element Extractants. https://doi.org/10.1021/jacs.5c19738

```python
@article{zhang2026augmenting,
  title = {Augmenting Large Language Models for Automated Discovery of F-Element Extractants},
  author = {Zhang, B. and Summers, T. J. and Augustine, L. J. and Taylor, M. G. and Geist, A. and Li, R. and Batista, E. R. and Perez, D. and Yang, P. and Schrier, J.},
  journal = {Journal of the American Chemical Society},
  volume = {148},
  number = {5},
  pages = {5520--5532},
  year = {2026},
  doi = {10.1021/jacs.5c19738},
}
```

## Notes

Every paper in this line runs into the same wall: the f-elements are chemically so alike that a selective extractant is a small difference in a large molecule, and designing one is slow. This paper puts a language model on the generative side of that problem and a quantum-mechanical calculation on the judging side.

The workflow is explicitly **quasi-autonomous**, with a human gate in the middle. Molecular design is guided by **SAFE-MolGen**, a large-language-model-based agentic system working over curated extraction data; it proposes new ligands and gives them a preliminary ranking using a supervised machine-learning model trained on experimental datasets, so that the ranking reflects realistic experimental conditions rather than an idealized binding affinity. Human-approved candidates then pass to a second, automated pipeline that builds three-dimensional metal–ligand complexes and runs quantum-mechanical free-energy calculations to assess the metal selectivity directly.

That architecture is the argument. The LLM is a generator, not an authority: it proposes structures in a data-sparse field where enumerating the space by hand is the bottleneck, the supervised model filters on what the experimental record says about conditions, and the free-energy calculation is what actually adjudicates selectivity. A molecule that survives all three has a physical reason to be selective, not just a plausible-looking structure.

The demonstration is **Am(III)/Eu(III)** — the canonical hard pair, a trivalent actinide against a trivalent lanthanide, separated industrially because the two are nearly identical in charge and radius and because the actinide is the one that must be kept out of the product. The authors report several newly designed ligands predicted to exhibit **higher Am(III)/Eu(III) selectivity than the benchmark extractant CyMe₄BTBP**.

What the abstract claims, and what it does not: these are predictions from screening and free-energy calculation. Synthesis and measurement are not reported here, so the paper establishes a pipeline that produces candidates with a computational case, not a demonstrated separation. The distinction matters in this field, where the history of extractant design is full of molecules that looked selective and were not.

The work is also a statement about where the discovery bottleneck has moved. The 2022 paper predicted a distribution coefficient for a ligand someone had chosen; the 2024 paper optimized the conditions for a system someone had chosen; this paper generates the ligand itself, with a physics check behind it. That is the direction the domain's technical evolution spine records as the current era.

## References

- https://doi.org/10.1021/jacs.5c19738
- [PubMed 41605809](https://pubmed.ncbi.nlm.nih.gov/41605809/)
- [Separation Science and Technology](/view.html?p=notes/technica/general/separation-science-and-technology.md) — the technical domain this paper works inside
- [Liu et al. (2022) — distribution-coefficient prediction](/view.html?p=documents/papers/liu-2022-advancing-rare-earth-separation-machine-learning.md)
- [Augustine et al. (2026) — adaptive experimental design for the same metals](/view.html?p=documents/papers/augustine-2026-coupling-dft-automated-experimentation-rare-earth.md)
- [Rare Earth Elements](/view.html?p=notes/technica/production/industry/rare-earth-elements.md)
