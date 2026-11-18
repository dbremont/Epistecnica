---
tags: [document, separation, rare-earth, ml]
---

# Augustine, L. J., Wang, Y., Taylor, M. G., Tynes, M., Adelman, S. L., Batista, E. R., Kozimor, S. A., Lubbers, N., Perez, D., & Yang, P. (2026). Coupling High-Throughput Density Functional Theory, Automated Experimentation, and Adaptive Experimental Design To Achieve Selective Rare-Earth Element Separations. https://doi.org/10.1021/jacs.6c04301

```python
@article{augustine2026coupling,
  title = {Coupling High-Throughput Density Functional Theory, Automated Experimentation, and Adaptive Experimental Design To Achieve Selective Rare-Earth Element Separations},
  author = {Augustine, L. J. and Wang, Y. and Taylor, M. G. and Tynes, M. and Adelman, S. L. and Batista, E. R. and Kozimor, S. A. and Lubbers, N. and Perez, D. and Yang, P.},
  journal = {Journal of the American Chemical Society},
  volume = {148},
  number = {38},
  pages = {40676--40687},
  year = {2026},
  doi = {10.1021/jacs.6c04301},
}
```

## Notes

The earlier paper in this line optimized a separation that already worked. This one changes the chemistry that makes it work, and the interesting move is where the selectivity is put.

Adjacent lanthanides are about as alike as elements get: same trivalent charge, ionic radii differing by a fraction of an ångström, so an extractant that takes one takes its neighbours nearly as readily. The usual lever is the extractant itself — design a molecule with a slightly better fit for one ion — which is slow and is what the ligand-discovery papers attack. Here the authors hold the extractant fixed and put the selectivity in the **aqueous phase**: a holdback agent complexes part of the metal inventory and keeps it from being extracted, so the relative extraction of two ions becomes a competition between two complexants rather than a property of one.

Database screening, density functional theory calculations, and initial experiments identified **oxaloacetic acid** as a promising holdback agent. Paired with **di(2-ethylhexyl)phosphoric acid (HDEHP, D2EHPA)** as the extractant, it enhanced the selective extraction of four lanthanides — **Nd, Eu, Dy, Ho**.

The experimental space is four-dimensional: pH, extractant concentration, holdback-agent concentration, and salt concentration. Automated high-throughput experiments supplied the measurements and multi-objective Bayesian Optimization chose the next condition, so the matrix was explored adaptively rather than exhaustively.

The results are a demonstration that pH is a selectivity switch, not just a yield knob. At **pH ∼ 2.0** the system extracted **Eu, Dy and Ho selectively over Nd**; dropping the pH modestly to **∼ 0.5** moved the selectivity again, allowing **Eu to be separated from Dy and Ho**. Multi-objective optimization produced a **4-fold increase in separation factors** relative to the HDEHP-only system, without a complete grid-based sampling of the space.

Read as a method, the paper is a hierarchy: DFT and database screening choose the candidate holdback agent, the robot measures, and the optimizer allocates the remaining experiments to the objectives. Read as chemistry, it is a reminder that a separation factor is a ratio of two distribution ratios, and a second complexant in the other phase can move the ratio more than a redesigned extractant moves either term.

What it does not show is a plant. Four elements, one holdback/extractant pair, bench-scale contactors, and separation factors rather than purities; the step from a factor of four to a specified product stream is the process design the domain note separates from the chemistry. The summary above is drawn from the abstract, which is what the publisher makes available for this article.

## References

- https://doi.org/10.1021/jacs.6c04301
- [PubMed 42479975](https://pubmed.ncbi.nlm.nih.gov/42479975/)
- [Separation Science and Technology](/view.html?p=notes/technica/cto/es/multinode/separation-science-and-technology.md) — the technical domain this paper works inside
- [Augustine et al. (2024) — the preceding optimization study](/view.html?p=documents/papers/augustine-2024-advancing-rare-earth-actinide-separation.md)
- [Rare Earth](/view.html?p=notes/production/foundation/rare-earth.md) · [Rare Earth Elements](/view.html?p=notes/technica/cto/industry/rare-earth-elements.md)
