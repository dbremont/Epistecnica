---
tags: [document, separation, rare-earth, actinide, ml]
---

# Augustine, L. J., Wang, Y., Adelman, S. L., Batista, E. R., Kozimor, S. A., Perez, D., Schrier, J., & Yang, P. (2024). Advancing Rare-Earth (4f) and Actinide (5f) Separation through Machine Learning and Automated High-Throughput Experiments. https://doi.org/10.1021/acssuschemeng.4c06166

```python
@article{augustine2024advancing,
  title = {Advancing Rare-Earth (4f) and Actinide (5f) Separation through Machine Learning and Automated High-Throughput Experiments},
  author = {Augustine, L. J. and Wang, Y. and Adelman, S. L. and Batista, E. R. and Kozimor, S. A. and Perez, D. and Schrier, J. and Yang, P.},
  journal = {ACS Sustainable Chemistry \& Engineering},
  volume = {12},
  number = {45},
  pages = {16692--16699},
  year = {2024},
  doi = {10.1021/acssuschemeng.4c06166},
}
```

## Notes

The paper takes the oldest complaint about liquid–liquid extraction and answers it with a machine. Basic purification methods have been refined for a century, so finding conditions that beat the existing ones is not a matter of a better idea but of searching a large experimental space — and the space is expensive when the aqueous phase is radioactive. The authors replace the search with Bayesian Optimization driving a robot, and measure what the substitution saves.

The instrument is the **LANL Super Separator**, a custom robotics platform built for actinide reprocessing campaigns. It automates almost every step of liquid–liquid extraction, chromatography, crystallization and (co)precipitation, holding the variables that matter — analyte, extractant and holdback concentration, pH, temperature — under programmatic control. For this paper the chemistry is thorium: Th⁴⁺ extracted from aqueous HNO₃ into an organic phase of 20 v% tributyl phosphate in n-dodecane, with N,N-di-2-ethylhexylbutyramide (DEHBA) as the extractant. Four variables are varied at once — aqueous Th concentration, HNO₃ concentration, DEHBA concentration, and temperature — and the response is the distribution ratio.

Bayesian Optimization proposes the next condition from the measurements already made, and the instrument executes it. The campaign used **339 distribution-ratio measurements covering 113 unique conditions**. A complete characterization of the same space by conventional high-throughput screening would have required an estimated **1296 measurements**, so the optimization reached its optimum while saving an estimated **74%** of the experimental effort.

Two things about that number are worth keeping straight. It is measured against an *estimated* full grid, not against a measured baseline — the estimate is the authors' own, and the comparison is with a screening strategy rather than with a chemist's experience. And the distribution ratio is an equilibrium quantity for one metal in one solvent system; it is the input to a separation process, not the process. What the paper establishes is that the search over conditions can be automated and shortened, which is exactly the part of separation development that does not scale by insight.

The saving is also a safety result, not only an economic one. Fewer experiments with actinides means less dose, less analytical load, and less radioactive waste per condition tested, which is why the authors frame the method as a sustainability argument as much as a throughput one.

The data from the thorium campaign are deposited in the **Separation Archive for f-elements (SAFE)** at `https://safe.lanl.gov`, alongside the datasets of the later papers in this line.

## References

- https://doi.org/10.1021/acssuschemeng.4c06166
- [PubMed 39545104](https://pubmed.ncbi.nlm.nih.gov/39545104/) · [PMC11558677](https://pmc.ncbi.nlm.nih.gov/articles/PMC11558677/)
- [SAFE — Separation Archive for f-elements](https://safe.lanl.gov)
- [Separation Science and Technology](/view.html?p=notes/technica/cto/es/multinode/separation-science-and-technology.md) — the technical domain this paper works inside
- [Rare Earth](/view.html?p=notes/production/foundation/rare-earth.md) · [Rare Earth Elements](/view.html?p=notes/technica/cto/industry/rare-earth-elements.md) — the material the separation serves
