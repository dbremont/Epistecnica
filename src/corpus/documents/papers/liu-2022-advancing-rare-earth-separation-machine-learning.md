---
tags: [document, separation, rare-earth, ml]
---

# Liu, T., Johnson, K. R., Jansone-Popova, S., & Jiang, D.-E. (2022). Advancing Rare-Earth Separation by Machine Learning. https://doi.org/10.1021/jacsau.2c00122

```python
@article{liu2022advancing,
  title = {Advancing Rare-Earth Separation by Machine Learning},
  author = {Liu, T. and Johnson, K. R. and Jansone-Popova, S. and Jiang, D.-E.},
  journal = {JACS Au},
  volume = {2},
  number = {6},
  pages = {1428--1434},
  year = {2022},
  doi = {10.1021/jacsau.2c00122},
}
```

## Notes

This is the paper that made the later automated work possible, and it does one thing: it replaces ligand discovery by trial and error with a regression over a representation.

The setting is the one the domain note calls the hard case. Lanthanides constitute the bulk of the rare-earth elements, they need to be separated to be used, and solvent extraction is the most practical way to separate them — while the discovery of better extractant ligands is still largely a matter of synthesizing candidates and measuring them. A model that predicts the distribution coefficient of a ligand before it is made would convert that into a screening problem.

The training data is the literature, assembled deliberately: **1202 reported distribution-coefficient (D) values for 109 different ligands**, with more than 60 entries per Ln(III) and ligand classes spanning phosphine oxides, amides, and N-heterocyclic derivatives. The D values span eight orders of magnitude (log D from −4 to +4), which is a wide dynamic range and one of the reasons a model here is not a formality. Of the 1202 points, **117 were held out at random as a validation set** over 14 lanthanides.

The representation is the methodological contribution. Each ligand is described twice — by molecular physicochemical descriptors and by atomic extended-connectivity fingerprints (ECFP) — and the extraction conditions (temperature, ligand concentration, physical properties of the organic solvent) are added to the input vector, giving **2291 inputs for each predicted log D**. That combination is what "greatly boosts" accuracy over either representation alone, and it is the difference between a model of molecules and a model of experiments.

The models are fully connected neural networks trained in PyTorch. The best configuration — PReLU activation, 15,000 epochs, learning rate 10⁻⁵, weight decay 0.01, three hidden layers of 512, 128 and 16 units — reached a training R² of **0.92** (RMSE 0.40, MAE 0.19) on 1085 points and a validation R² of **0.85** with **RMSE 0.53** and MAE 0.34. The authors read that as predicting log D to within about 0.5, which is roughly a factor of three in D.

The prospective test is the part that matters. Four new DGA ligands with different N-alkyl substituents were synthesized, their D values measured by ICP-OES, and the model's predictions compared with the measurements: **R² from 0.78 to 0.92**, with per-ligand MAE of 0.21, 0.41, 0.38 and 0.22 — errors of the same size as the validation set. Four ligands is a small test, and the authors say so.

Two limits are visible in the paper itself. The largest errors come from ligands carrying rare groups (such as –SR) for which the training set holds little data, so the model's reliability is bounded by the literature's coverage rather than by its architecture. And the training data pools measurements made under heterogeneous conditions across many laboratories, which means the model learns the literature's conditions as much as the chemistry; the conditions are inputs precisely because they cannot be normalized away.

What the output is, finally, is a distribution coefficient — one metal, one ligand, one set of conditions. Turning a table of predicted D values into a separation means taking ratios between metals, which is what the later papers in this line do with the same archive of data.

## References

- https://doi.org/10.1021/jacsau.2c00122
- [PubMed 35783179](https://pubmed.ncbi.nlm.nih.gov/35783179/) · [PMC9241157](https://pmc.ncbi.nlm.nih.gov/articles/PMC9241157/)
- [Separation Science and Technology](/view.html?p=notes/technica/general/cto/es/multinode/separation-science-and-technology.md) — the technical domain this paper works inside
- [Rare Earth](/view.html?p=notes/production/foundation/rare-earth.md) · [Rare Earth Elements](/view.html?p=notes/technica/general/cto/industry/rare-earth-elements.md)
- [Chemical Engineering](/view.html?p=notes/epistemica/epistemic/discipline/chemical-engineering.md) — the discipline that turns a distribution coefficient into a flowsheet
