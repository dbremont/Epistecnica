---
tags: [document, agronomy, fertilizer, nutrient-management, economics]
---

# Dhakal, C. K., & Lange, K. (2021). Crop Yield Response Functions in Nutrient Application: A Review. Agronomy Journal, 113(6), 5222–5234. https://doi.org/10.1002/agj2.20863

```python
@article{dhakal2021crop,
  title = {Crop yield response functions in nutrient application: A review},
  author = {Dhakal, C. K. and Lange, K.},
  journal = {Agronomy Journal},
  volume = {113},
  number = {6},
  pages = {5222--5234},
  year = {2021},
  doi = {10.1002/agj2.20863},
}
```

## Notes

The question the paper addresses is deceptively practical: how much nutrient should be applied? The economically optimal rate is found by fitting a curve of yield against applied nutrient and reading the point where the marginal product equals the marginal cost — which makes the **choice of the curve** the technical decision, not a statistical afterthought. A function that bends the wrong way gives a confidently wrong recommendation.

The review sets out the production economics first, then the functional forms:

| Form | Shape | What it assumes |
| --- | --- | --- |
| **Quadratic** | Yield rises then falls | A maximum, and a decline at high rates — convenient, and often wrong at the top end |
| **Mitscherlich–Baule** | Yield rises toward an asymptote | Diminishing returns with no decline — the classic agronomic response |
| **Deterministic plateau** | Linear rise to a plateau, then flat | A yield ceiling reached at a threshold rate |
| **Stochastic plateau** | Plateau with a random plateau level or a random threshold | The plateau itself varies with weather and site — linear or quadratic variants |

> The review's conclusion is that the **stochastic plateau** forms explain observed nutrient response better than the deterministic ones, because the plateau is not a fixed property of the soil: it moves with the season, the site and the preceding crop. A model that treats it as fixed underestimates the variance and overstates the precision of the recommendation.

The recommendation follows: fit the stochastic plateau together with **carryover** information — the nutrient left from the previous application — in a dynamic optimisation, rather than optimising each season as if it began from zero. That is the same argument the crop-productivity note makes about the long-run nutrient balance: nitrogen is lost and must be timed, phosphorus accumulates and must be accounted for across seasons.

The paper is a review, not a trial: it compares forms and their economic implications, and it closes by asking for more evidence on which forms perform best in which crop and soil environments. Its value to a technical corpus is the framing — the yield response function is where agronomy and economics meet, and the choice among the forms is a modelling decision with a direct cost in fertiliser and in lost yield.

## References

- https://doi.org/10.1002/agj2.20863
- [Crop Productivity](/view.html?p=notes/technica/general/agro/crop-productivity.md) — the yield reading the response function quantifies
- [Fertilizer Industry](/view.html?p=notes/technica/production/industry/chemical/fertilizer.md) — the nutrient supply the function is fitted to
- [Putting mechanisms into crop production models](/view.html?p=documents/papers/boote-2013-putting-mechanisms-crop-production-models-plant-cell-environment.md) — the process-model counterpart: mechanism rather than response curve
- [Plant Cultivation Technical Domain Set](/view.html?p=notes/technica/general/plant-cultivation-technical-domain-set.md) — the nutrient regime the recommendation enters
- [Agro](/view.html?p=notes/technica/general/agro/agro.md) — the domain entry note
