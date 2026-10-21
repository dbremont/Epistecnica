---
tags: [ml]
---

# Dong, J., Zhao, L., Yue, Z., Ma, W., Zhang, L., Li, L., Li, S., Song, Y., Ye, B., & Luo, F. (2026). Groupwise agentic grading and advantage redistribution for code agent RL. arXiv:2609.32577. https://doi.org/10.48550/arXiv.2609.32577


```bibtex
@misc{dong2026gagar,
  title={Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL},
  author={Dong, Jinhao and Zhao, Liang and Yue, Zihao and Ma, Wenhan and Zhang, Linghao and Li, Lei and Li, Shicheng and Song, Yifan and Ye, Bowen and Luo, Fuli},
  year={2026},
  eprint={2609.32577},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  doi={10.48550/arXiv.2609.32577},
  url={https://arxiv.org/abs/2609.32577}
}
```

## Notes

---

> Introduces GAGAR, quality-aware credit redistribution for code-agent RL.
> Binary test rewards give identical GRPO advantages to all passing
> trajectories; GAGAR places each rollout group in a shared workspace where
> an SFT-trained agentic grader jointly inspects and ranks the test-passing
> candidates, then downweights lower-ranked trajectories and rescales the
> advantages of the passing ones sum-preservingly. Evaluated at industrial
> scale on pre-RL SFT checkpoints of MiMo-V2.6-Flash (310B) and MiMo-V2.6-Pro
> (1.02T): better code-agent performance, less trajectory-length growth,
> more stable training. Companion mechanism to the GRS/GAR grading described
> in the MiMo-V2.6 technical report.
> 

## References

- [arXiv abstract](https://arxiv.org/abs/2609.32577)
- [arXiv PDF](https://arxiv.org/pdf/2609.32577)
