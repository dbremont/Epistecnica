---
tags: [document]
---

# Buzsáki, G., & Mizuseki, K. (2014). The log-dynamic brain: How skewed distributions affect network operations. *Nature Reviews Neuroscience*, 15(4), 264–278. https://doi.org/10.1038/nrn3687

```latex
@article{buzsaki2014logdynamic,
  title={The log-dynamic brain: how skewed distributions affect network operations},
  author={Buzs{\'a}ki, Gy{\"o}rgy and Mizuseki, Kenji},
  journal={Nature Reviews Neuroscience},
  volume={15},
  number={4},
  pages={264--278},
  year={2014},
  publisher={Nature Publishing Group},
  doi={10.1038/nrn3687},
  pmid={24569488},
  pmcid={PMC4051294}
}
```

## Notes

The review's claim is that the brain's functional and structural parameters are **not** Gaussian. Synaptic weights, firing rates, population synchrony, spine sizes, the number of synapses between a pair of neurons, the strength of corticocortical projections and axon calibres all have strongly skewed, heavy-tailed — typically **lognormal** — distributions, and the deviation is not a measurement nuisance but the signature of how the tissue is organised.

The mechanism offered is multiplicative: where a quantity is the product of many positive factors rather than their sum, its logarithm is a sum, and the central limit theorem delivers a normal distribution for the log — a lognormal for the quantity. Biological parameters accumulate through many interactive, multiplicative steps, which is why the lognormal appears at every level the paper surveys.

The levels, from macroscopic to microscopic:

- **LFP and EEG power** — power falls near-linearly with frequency on a log–log plot, and rhythms are nested across scales (phase–amplitude coupling).
- **Population synchrony** — the fraction of neurons firing in a sharp-wave ripple or a theta cycle is lognormal: no characteristic event size.
- **Firing rates** — spontaneous and evoked rates of cortical principal cells span four orders of magnitude, with a fast-firing minority and a vast slow-firing majority.
- **Synaptic weights and spike transmission** — most pairs are weakly coupled; a small minority are strong and reliably so.
- **Spine sizes, release sites and synapse counts** — lognormal, and their changes are multiplicative in the current size.
- **Corticocortical connectivity** — connection strengths span five orders of magnitude per area.
- **Axon calibres** — the great majority below 0.8 µm, the thickest 0.1 % up to 10 µm.

The consequence the authors draw is the one worth keeping: a **selected minority of neurons and synapses does most of the work** in most situations — the "we use 10 % of our brain" folklore read correctly, as a statement about skew rather than about idleness — while the slow-firing, weakly connected majority supplies the flexibility and the global context. The network keeps a relatively fixed log-rate backbone across sleep, waking, novel environments and anaesthesia, and the plastic majority is what moves.

The caveats are stated in the paper and matter for anyone using its numbers: every recording method samples against the slow-firing tail (short sessions miss slow cells, spike sorting drops them, arbitrary cut-offs truncate the left tail), and separating principal cells from interneurons changes the right tail. The review's methodological moral is that an arithmetic mean of a lognormal quantity describes no actual neuron, and that comparisons across groups should be made on the log scale or with medians.

## References

- Publisher: https://doi.org/10.1038/nrn3687
- PubMed: https://pubmed.ncbi.nlm.nih.gov/24569488/
- PMC (author manuscript): https://pmc.ncbi.nlm.nih.gov/articles/PMC4051294/
- [Power Law](/view.html?p=notes/nature/power-law.md) — the other heavy-tailed form, and the one the paper distinguishes from the lognormal
- [Firing Rates](/view.html?p=notes/nature/firing-rates.md) — the quantity the review's middle section is about
- [Brain](/view.html?p=notes/nature/life/organism/human/brain.md) — the natural system whose parameters the distributions describe
