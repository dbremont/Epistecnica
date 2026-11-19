---
tags: [document, paper, machine-learning, quantization, inference, llm]
---

# Breaking the 1.58-bit Barrier for Ternary LLMs (2026). *arXiv*:2609.16338. https://arxiv.org/abs/2609.16338

## Notes

> **Ternary LLMs** store every weight as one of three symbols, $\{-1, 0, +1\}$, and the cost of doing so is conventionally referenced to the information-theoretic floor: $\log_2 3 \approx 1.585$ **bits per weight**. That number is the entropy of a uniformly random trit, and it is treated as the limit a ternary representation cannot beat.

> The paper's starting observation is that the *deployed* formats do not reach the floor and the *floor itself* is not the real limit. The prevailing deployment packs **five ternary weights into one byte** (five-trit packing), and because the group sizes used in practice are powers of two, the effective storage rounds up to **1.625 bits per weight**. So there are two gaps to close: the packing overhead, and the assumption that the entropy of a *uniform* trit is the bound.

| Layer | Where the bits go |
| --- | --- |
| **Entropy floor** | $\log_2 3 \approx 1.585$ bits/weight — the information content of an independent uniform trit |
| **Five-trit packing** | 3⁵ = 243 ≤ 256, so 8 bits per 5 weights = 1.6 bits/weight |
| **Power-of-two group sizes** | Padding the groups to a power of two rounds the effective rate to **1.625 bits/weight** |
| **The paper** | A representation that goes *below* 1.585 — which requires exploiting structure or non-uniformity, since independent uniform trits cannot be compressed below their entropy |

> The result is a compression claim, and the interesting part is the *kind* of claim: beating an entropy bound is only possible by giving up the assumption that the weights are independent and uniform — the same move as in any compression scheme, where the model of the source is the source of the gain. It matters practically because ternary weights are a deployment strategy: the difference between 1.625 and, say, 1.4 bits per weight is the difference between a model that fits one memory budget and one that does not.

> The caveat to carry: the abstract states the barrier and the direction, not the full method; the entry records what is claimed and flags that the evidence should be read in the paper rather than inferred from the title.

## References

- [Breaking the 1.58-bit Barrier for Ternary LLMs — arXiv](https://arxiv.org/abs/2609.16338)
- [Quantization](/view.html?p=notes/technica/cybernetics/inference/quantization.md) — the inference technique this is a special case of
- [Inference](/view.html?p=notes/technica/cybernetics/inference/inference.md) — the serving frame
