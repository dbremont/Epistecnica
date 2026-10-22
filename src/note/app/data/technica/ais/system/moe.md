---
qa:
  - Which are the type of models GPT? MoE?
  - How does a sparse MoE layer decouple parameter count from per-token computation, and what do the router and its top-k gating actually compute?
  - What is expert load imbalance, and how do auxiliary load-balancing losses, Expert Choice routing, and auxiliary-loss-free balancing each mitigate it — at what cost?
  - How do the capacity factor and top-1 routing in the Switch Transformer trade off token dropping against communication and memory, and why does dropping happen at all?
  - Why do sparsely-gated MoEs require noisy gating and router z-loss, and how do ST-MoE and the router z-loss stabilize training and fine-tuning?
  - How does expert parallelism differ from data and model parallelism, what all-to-all communication does it inject into every layer, and how do MegaBlocks-style dropless designs remove the padding waste?
  - Distinguish total, effective, and activated parameters in MoE scaling: how should a compute-optimal budget allocate experts versus width/depth relative to a dense model?
  - Why do MoE models fine-tune and do few-shot inference worse than dense models of comparable activated compute, and what do OpenMoE/OLMoE routing analyses (context-independent specialization, early routing learning, drop-towards-the-end) reveal about the cause?
  - How does DeepSeekMoE's fine-grained expert segmentation plus shared experts differ from the classic coarse MoE recipe, and what does it buy in expert specialization?
  - Under what batch-size and memory-bandwidth conditions does an MoE actually beat a dense model at inference, and when is it slower?
---

# Mixture of Experts (MoE)


> 

- A technique where only a subset of model parameters (experts) are activated for a given input, significantly reducing computational overhead.
- **Impact**: Allows scaling models without proportional increases in computational cost, improving efficiency.
- A conditional-computation architecture that selectively activates subsets of a model's parameters at particular computational stages, allowing the model to increase its total parameter capacity without proportionally increasing the computation required for each input.
- https://huggingface.co/blog/moe

## References

- Jacobs, R. A., Jordan, M. I., Nowlan, S. J., & Hinton, G. E. (1991). Adaptive mixtures of local experts. *Neural Computation, 3*(1), 79–87. https://doi.org/10.1162/neco.1991.3.1.79
- Jordan, M. I., & Jacobs, R. A. (1994). Hierarchical mixtures of experts and the EM algorithm. *Neural Computation, 6*(2), 181–214. https://doi.org/10.1162/neco.1994.6.2.181
- Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. *International Conference on Learning Representations*. https://arxiv.org/abs/1701.06538
- Lepikhin, D., Lee, H., Xu, Y., Chen, D., Firat, O., Huang, Y., Krikun, M., Shazeer, N., & Chen, Z. (2021). GShard: Scaling giant models with conditional computation and automatic sharding. *International Conference on Learning Representations*. https://arxiv.org/abs/2006.16668
- Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. *Journal of Machine Learning Research, 23*(120), 1–39. https://www.jmlr.org/papers/v23/21-0998.html
- Riquelme, C., Puigcerver, J., Mustafa, B., Neumann, M., Jenatton, R., Pinto, A. S., Keysers, D., & Houlsby, N. (2021). Scaling vision with sparse mixture of experts. *Advances in Neural Information Processing Systems, 34*, 8583–8595. https://arxiv.org/abs/2106.05974
- Du, N., Huang, Y., Dai, A. M., Tong, S., Lepikhin, D., Xu, Y., Krikun, M., Zhou, Y., Yu, A. W., Firat, O., Zoph, B., Goodrich, B., Wang, A., Yang, Y., Zhang, J., & others. (2022). GLaM: Efficient scaling of language models with mixture-of-experts. *Proceedings of the 39th International Conference on Machine Learning*. https://arxiv.org/abs/2112.06905
- Zoph, B., Bello, I., Kumar, S., Du, N., Huang, Y., Dean, J., Shazeer, N., & Fedus, W. (2022). ST-MoE: Designing stable and transferable sparse expert models. *arXiv*. https://arxiv.org/abs/2202.08906
- Zhou, Y., Lei, T., Liu, H., Du, N., Huang, Y., Zhao, V., Dai, A. M., Le, Q. V., Laudon, J., et al. (2022). Mixture-of-experts with expert choice routing. *Advances in Neural Information Processing Systems, 35*. https://arxiv.org/abs/2202.09368
- Lewis, M., Bhosale, S., Dettmers, T., Goyal, N., & Zettlemoyer, L. (2021). BASE layers: Simplifying training of large, sparse models. *Proceedings of the 38th International Conference on Machine Learning* (Vol. 139, pp. 6265–6274). PMLR. https://proceedings.mlr.press/v139/lewis21a.html
- Gale, T., Narayanan, D., Young, C., & Zaharia, M. (2023). MegaBlocks: Efficient sparse training with mixture-of-experts. *Proceedings of Machine Learning and Systems, 5*. https://arxiv.org/abs/2211.15841
- Mistral AI. (2024). *Mixtral of experts*. arXiv. https://arxiv.org/abs/2401.04088
- Dai, D., Deng, C., Zhao, C., Xu, R. X., Gao, H., Chen, D., Li, J., Zeng, W., Yu, X., Wu, Y., Xie, Z., Li, Y. K., Huang, P., Luo, F., Ruan, C., Sui, Z., & Liang, W. (2024). DeepSeekMoE: Towards ultimate expert specialization in mixture-of-experts language models. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 1280–1297. https://doi.org/10.18653/v1/2024.acl-long.70
- DeepSeek-AI. (2024). *DeepSeek-V3 technical report*. arXiv. https://arxiv.org/abs/2412.19437
- Wang, L., Gao, H., Zhao, C., Sun, X., & Dai, D. (2024). *Auxiliary-loss-free load balancing strategy for mixture-of-experts*. arXiv. https://arxiv.org/abs/2408.15664
- Xue, F., Zheng, Z., Fu, Y., Ni, J., Zheng, Z., Zhou, W., & You, Y. (2024). OpenMoE: An early effort on open mixture-of-experts language models. *Proceedings of the 41st International Conference on Machine Learning* (Vol. 235, pp. 55625–55655). PMLR. https://arxiv.org/abs/2402.01739
- Muennighoff, N., Soldaini, L., Groeneveld, D., Lo, K., Morrison, J., Min, S., Shi, W., Walsh, P., Tafjord, O., Lambert, N., Gu, Y., Arora, S., Bhagia, A., Schwenk, D., Wadden, D., Wettig, A., Hui, B., Dettmers, T., Kiela, D., ... Koh, P. W. (2025). OLMoE: Open mixture-of-experts language models. *International Conference on Learning Representations*. https://arxiv.org/abs/2409.02060
- Yuksel, S. E., Wilson, J. N., & Gader, P. D. (2012). Twenty years of mixture of experts. *IEEE Transactions on Neural Networks and Learning Systems, 23*(8), 1177–1193. https://doi.org/10.1109/TNNLS.2012.2200299
- Fedus, W., Dean, J., & Zoph, B. (2022). *A review of sparse expert models in deep learning*. arXiv. https://arxiv.org/abs/2209.01667
- Mu, S., & Lin, S. (2025). *A comprehensive survey of mixture-of-experts: Algorithms, theory, and applications*. arXiv. https://arxiv.org/abs/2503.07137
- Bishop, C. M. (2006). *Pattern recognition and machine learning*. Springer. https://doi.org/10.1007/978-0-387-45528-0
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. https://www.deeplearningbook.org/
- Murphy, K. P. (2022). *Probabilistic machine learning: An introduction*. MIT Press. https://probml.github.io/pml-book/book1.html
- Prince, S. J. D. (2023). *Understanding deep learning*. MIT Press. https://udlbook.github.io/udlbook/
- ChatVariety Team. (2026). *Mixture of experts architecture engineering: Designing, training, and serving sparse MoE language models*. Independently Published.
