---
tags: [ml, technical-report]
---

# Yang, C., et al. (2025). Nanbeige4-3B Technical Report: Exploring the Frontier of Small Language Models. arXiv:2512.06266. https://doi.org/10.48550/arXiv.2512.06266


```bibtex
@misc{yang2025nanbeige43b,
  title={Nanbeige4-3B Technical Report: Exploring the Frontier of Small Language Models},
  author={Yang, Chen and Peng, Guangyue and Zhu, Jiaying and Le, Ran and Feng, Ruixiang and Zhang, Tao and Ruan, Wei and Liu, Xiaoqi and Cheng, Xiaoxue and Xu, Xiyun and Song, Yang and Gao, Yanzipeng and Jia, Yiming and Xing, Yun and Wen, Yuntao and Wang, Zekai and An, Zhenwei and Sun, Zhicong and Chen, Zongchao},
  year={2025},
  eprint={2512.06266},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  doi={10.48550/arXiv.2512.06266},
  url={https://arxiv.org/abs/2512.06266}
}
```

## Notes

---

> Technical report for Nanbeige4-3B, a family of small-scale language models
> pretrained on 23T high-quality tokens and finetuned on over 30 million
> diverse instructions, aimed at extending the scaling-law boundary for
> small models. Pre-training uses a Fine-Grained Warmup-Stable-Decay
> (FG-WSD) scheduler that progressively refines the data mixture across
> stages. Post-training improves SFT data quality through a joint
> deliberative-generation refinement and chain-of-thought reconstruction
> mechanism; the flagship reasoning model then distills into Nanbeige4-3B
> through Dual Preference Distillation (DPD), followed by multi-stage
> reinforcement learning with verifiable rewards and preference modeling
> to strengthen reasoning and human alignment. Reported to outperform
> models of comparable parameter scale and to rival much larger models
> across a wide range of benchmarks.
> 

## References

- [arXiv abstract](https://arxiv.org/abs/2512.06266)
- [arXiv PDF](https://arxiv.org/pdf/2512.06266)
- [Model checkpoints](https://huggingface.co/Nanbeige)
