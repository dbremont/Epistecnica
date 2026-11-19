---
tags: [document, paper, machine-learning, llm, systems]
---

# Fu, T., Min, Z., Zhang, H., Yan, J., Dai, G., Ouyang, W., & Wang, Y. (2025). Cache-to-Cache: Direct Semantic Communication Between Large Language Models. *arXiv*:2510.03215. https://arxiv.org/abs/2510.03215

```python
@inproceedings{fu2025cache,
  title = {Cache-to-Cache: Direct Semantic Communication Between Large Language Models},
  author = {Fu, Tianyu and Min, Zihan and Zhang, Hanling and Yan, Jichao and Dai, Guohao and Ouyang, Wanli and Wang, Yu},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2026},
  note = {arXiv:2510.03215},
}
```

## Notes

> The paper attacks an assumption nobody states: that when two language models cooperate, they must **talk**. In every multi-model system — router plus specialist, planner plus coder, critic plus generator — the hand-off is text: the first model serialises its internal state into tokens, and the second re-encodes them. That is a **lossy interface**: the representation that carried the meaning is discarded, and the cost is paid twice, once in information and once in the token-by-token generation latency.

> The evidence that the interface is the problem comes first. **Oracle experiments** show that enriching a model's KV-cache semantics improves its answers *without enlarging the cache* — so the cache is not merely a computational artefact, it is a usable representation of what the model knows at that point. **C2C** then does the obvious thing: a learned network projects the source model's KV-cache into the target model's cache space and fuses the two, with a **gate** selecting which target layers accept the transfer. No intermediate text is generated.

| Claim | Result |
| --- | --- |
| Against the individual models | +6.4 to +14.2% average accuracy |
| Against text communication | +3.1 to +5.4% |
| Latency | ~2.5x faster on average |

> The conceptual content is that **text is a low-bandwidth, high-latency serialisation of a richer state**, and that the serialisation is where the multi-agent system loses what it was supposed to combine. The corpus's [LLM system modelling](/view.html?p=notes/technica/cybernetics/theory/llm-system-modelling.md) note treats the model as a component in a pipeline; this paper says the *link* between components, not the components, is where the capability is being thrown away. Read against the [Model Context Protocol](/view.html?p=notes/technica/cybernetics/application/model-context-protocol-mcp.md), it is the strongest counter-position to the protocol view: MCP standardises a text-shaped interface, C2C argues the interface should be latent.

> The caveat matters and is structural: the projection is **learned per model pair**, so this is a point-to-point channel, not a protocol. Every new pair of models needs its own projection trained, and the transfer presumes access to the source model's cache — which rules it out for closed-weight APIs. It is a demonstration that the latent channel carries more, not yet a standard that anyone can implement between arbitrary models.

## References

- [Cache-to-Cache — arXiv](https://arxiv.org/abs/2510.03215)
- [LLM System Modelling](/view.html?p=notes/technica/cybernetics/theory/llm-system-modelling.md) — the pipeline the interface belongs to
- [Model Context Protocol](/view.html?p=notes/technica/cybernetics/application/model-context-protocol-mcp.md) — the text-shaped interface this argues against
- [Knowledge Distillation](/view.html?p=notes/technica/cybernetics/synthesis/knowledge-distillation.md) — the other way to move capability between models
