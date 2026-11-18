---
tags: [document, crop-modelling, agronomy, plant-physiology, simulation]
---

# Boote, K. J., Jones, J. W., White, J. W., Asseng, S., & Lizaso, J. I. (2013). Putting Mechanisms into Crop Production Models. Plant, Cell & Environment, 36(9), 1658–1672. https://doi.org/10.1111/pce.12119

```python
@article{boote2013putting,
  title = {Putting mechanisms into crop production models},
  author = {Boote, K. J. and Jones, J. W. and White, J. W. and Asseng, S. and Lizaso, J. I.},
  journal = {Plant, Cell \& Environment},
  volume = {36},
  number = {9},
  pages = {1658--1672},
  year = {2013},
  doi = {10.1111/pce.12119},
}
```

## Notes

Crop models simulate the carbon, nitrogen and water balances on daily or hourly time steps and produce growth, development and — at season end — yield. Boote and colleagues open with what that buys: because the model integrates genetics, environment and management, it can be used to reason from gene function to field performance and from field performance to a changed climate. The paper is a position statement on **how much mechanism such a model must contain**, written by five of the people who build the widely used crop simulation models.

**The history is short and the trajectory is clear.** The models began as empirical yield regressions and acquired process by process — phenology first, then assimilation, partitioning, water and nitrogen. The paper reviews that arc and then locates the current models on a scale of mechanistic detail: from hourly leaf-to-canopy assimilation, through daily canopy photosynthesis, to the simplest daily radiation-use-efficiency formulation. The choice is not a matter of taste; each level buys extrapolative power with parameters, and parameters with data.

**The gaps are named specifically**, and they are the useful part of the paper. Models need better prediction of the transpiration response to elevated CO₂; of high-temperature effects on phenology and reproductive fertility; and of root growth and nutrient uptake under stressful edaphic conditions — waterlogging, salinity, low fertility. Each gap is a place where the model is empirical where the physiology is known, and where a climate or management extrapolation therefore carries unearned confidence.

**The argument for mechanism is an argument about extrapolation.** A model calibrated on today's weather and today's cultivars interpolates well and extrapolates badly; the mechanistic modules are what let it answer a question the calibration data never covered — a new CO₂ level, a new temperature regime, a new cultivar with a changed trait. The paper's closing claim is that this is also the bridge between genomics and the field: a model that represents the trait, not just the yield, can test what a gene would do in a real environment, and so can separate the genotype × environment × management interaction that a field trial alone cannot resolve.

What the paper does not do is settle the parameter problem. More mechanism means more parameters, and more parameters mean more calibration data that the experiment station rarely has. The honest reading is a trade stated rather than resolved: mechanism for extrapolation, at a cost paid in measurement.

## References

- https://doi.org/10.1111/pce.12119
- [Crop Productivity](/view.html?p=notes/technica/general/agro/crop-productivity.md) — the yield reading this model formalises
- [Plant Cultivation Technical Domain Set](/view.html?p=notes/technica/general/plant-cultivation-technical-domain-set.md) — the management variables the model integrates
- [Crop yield response functions in nutrient application: A review](/view.html?p=documents/papers/dhakal-2021-crop-yield-response-functions-nutrient-application-agronomy-journal.md) — the empirical counterpart: the response function rather than the process model
- [Plant Genetic Improvement](/view.html?p=notes/technica/general/plant-genetic-improvement.md) — the cultivar traits a mechanistic model would carry
- [Agro](/view.html?p=notes/technica/general/agro/agro.md) — the domain entry note
