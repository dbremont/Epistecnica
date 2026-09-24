---
tags: [physical]
---

# Liu, A., Feng, B., Xue, B., Wang, B., Wu, B., Lu, C., Zhao, C., Deng, C., Zhang, C., Ruan, C., & others. (2024). Deepseek-v3 Technical Report. ArXiv Preprint ArXiv:2412.19437.


```python
@article{liu2024deepseek,
  title={Deepseek-v3 Technical Report},
  author={Liu, Aixin and Feng, Bei and Xue, Bing and Wang, Bingxuan and Wu, Bochao and Lu, Chengda and Zhao, Chenggang and Deng, Chengqi and Zhang, Chenyu and Ruan, Chong and others},
  journal={arXiv preprint arXiv:2412.19437},
  year={2024}
}
```

## Notes

---

## Index

Learn:

- Transformer
- Attention
- RL
- …

![image.png](documents/articles/liu-2024-deepseek-technical-report-arxiv-preprint/image.png)

**Model:**

- **Name**: DeepSeek-V3
- **Type**: Mixture-of-Experts (MoE) language model
- **Total Parameters**: 671 billion (671B)
- **Activated Parameters per Token**: 37 billion (37B)

**Architecture:**

- **Multi-head Latent Attention (MLA)**:
    - Enhances inference efficiency.
    - Reduces training costs.
    - Previously validated in **DeepSeek-V2**.
- **DeepSeekMoE Architecture**:
    - Optimized for efficient computation and scalability.
    - Also validated in **DeepSeek-V2**.

**Training:**

- **Auxiliary-Loss-Free Load Balancing**:
    - Pioneered by DeepSeek-V3.
    - Ensures balanced utilization of experts without additional loss terms.
- **Multi-Token Prediction Training Objective**:
    - Improves model performance by predicting multiple tokens simultaneously.
    - Leads to stronger overall capabilities.
- **Pre-Training**:
    - **Dataset Size**: 14.8 trillion tokens.
    - **Dataset Quality**: Diverse and high-quality.
- **Fine-Tuning**:
    - **Supervised Fine-Tuning (SFT)**: Tailors the model for specific tasks.
    - **Reinforcement Learning (RL)**: Further enhances performance through reward-based training.
- **Efficiency**:
    - **Training Cost**: 2.788 million H800 GPU hours.
    - **Training Stability**: No irrecoverable loss spikes or rollbacks during the entire training process.

> No Detail From the Paper: **FP8 Training System**, “Co-design of algorithms, frameworks, and hardware”, “Achieving near-full computation-communication overlap”, …, …
> 

> We introduce an innovative methodology to distill reasoning capabilities from the long-Chain-of-Thought (CoT) model, specifically from one of the DeepSeek R1 series models, into standard LLMs, particularly DeepSeek-V3. Our pipeline elegantly incorporates the verification and reflection patterns of R1 into DeepSeek-V3 and notably improves its reasoning performance. Meanwhile, we also maintain control over the output style and length of DeepSeek-V3.
> 

> Due to the effective load balancing strategy, DeepSeek-V3 keeps a good load balance during its full training. Therefore, DeepSeek-V3 does not drop any tokens during training.
> 

> …
> 

## Introduction

> List of current models: Closed models (OpenAI, Anthropic's Claude, Google Gemini); Open models (DeepSeek, LLaMA, Qwen, and Mistral).
> 

> **Auxiliary-loss-free strategy** (Wang et al., 2024a) for load balancing (Wang et al., [2024a](https://arxiv.org/html/2412.19437v1#bib.bib93)) for load balancing, with the aim of minimizing the adverse impact on model performance that arises from the effort to encourage load balancing.
> 

> DeepSeek-V3 employs a **multi-token prediction training objective**, which we have observed to enhance the overall performance on evaluation benchmarks.
> 

> In order to achieve efficient training, we support the **FP8** mixed precision training and implement comprehensive optimizations for the training framework.
> 

> **Low-precision training** has emerged as a promising solution for efficient training (Kalamkar et al., 2019; Narang et al., 2017; Peng et al., 2023b; Dettmers et al., 2022), its evolution being closely tied to advancements in hardware capabilities (Micikevicius et al., 2022; Luo et al., 2024; Rouhani et al., 2023a).
> 

> As for the training framework, we design the **DualPipe algorithm for efficient pipeline** parallelism, which has fewer pipeline bubbles and hides most of the communication during training through computation-communication overlap. https://arxiv.org/abs/2202.00717
> 

> We also develop efficient cross-node all-to-all communication kernels to fully utilize InfiniBand (IB) and NVLink bandwidths.
> 

> We meticulously optimize the memory footprint, making it possible to train DeepSeek-V3 without using costly tensor parallelism.
> 

> In the first stage, the maximum context length is extended to 32K, and in the second stage, it is further extended to 128K. Following this, we conduct post-training, including **Supervised Fine-Tuning (SFT)** and **Reinforcement Learning (RL)** on the base model of DeepSeek-V3, to align it with human preferences and further unlock its potential. During the post-training stage, we **distill the reasoning capability from the DeepSeek-R1** series of models, and meanwhile carefully maintain the balance between model accuracy and generation length.
> 

## Architecture

> …
> 

![image.png](documents/articles/liu-2024-deepseek-technical-report-arxiv-preprint/image-1.png)

> We first introduce the basic architecture of DeepSeek-V3, featured by Multi-head Latent Attention (MLA) (DeepSeek-AI, [2024c](https://arxiv.org/html/2412.19437v1#bib.bib16)) for efficient inference and DeepSeekMoE (Dai et al., [2024](https://arxiv.org/html/2412.19437v1#bib.bib13)) for economical training.
> 

> The basic architecture of DeepSeek-V3 is still within the Transformer (Vaswani et al., [2017](https://arxiv.org/html/2412.19437v1#bib.bib92)) framework.
> 

> DeepSeek-V3 also adopts MLA and DeepSeekMoE, which have been thoroughly validated by DeepSeek-V2. Compared with DeepSeek-V2, an exception is that we additionally introduce an auxiliary-loss-free load balancing strategy (Wang et al., [2024a](https://arxiv.org/html/2412.19437v1#bib.bib93)) for DeepSeekMoE to mitigate the performance degradation induced by the effort to ensure load balance.
> 

### Multi-Head Latent Attention

![image.png](documents/articles/liu-2024-deepseek-technical-report-arxiv-preprint/image-2.png)

> For attention, DeepSeek-V3 adopts the MLA architecture.
> 

> **Reader:** What is attention? What attention does?  How many “attention” instances/implementation are there?
> 

> References: RoPE + Attention.
> 

> The core of MLA is the **low-rank joint compression** for attention keys and values to reduce **Key-Value (KV)** cache during inference.
> 

> …
> 

### **Basic Architecture of DeepSeekMoE**

> For Feed-Forward Networks (FFNs), DeepSeek-V3 employs the DeepSeekMoE architecture (Dai et al., [2024](https://arxiv.org/html/2412.19437v1#bib.bib13)). Compared with traditional MoE architectures like GShard (Lepikhin et al., [2021](https://arxiv.org/html/2412.19437v1#bib.bib45)), DeepSeekMoE uses finer-grained experts and isolates some experts as shared ones.
> 

### **Auxiliary-Loss-Free Load Balancing**

> For MoE models, an unbalanced expert load will lead to routing collapse (Shazeer et al., [2017](https://arxiv.org/html/2412.19437v1#bib.bib81)) and diminish computational efficiency in scenarios with expert parallelism. Conventional solutions usually rely on the auxiliary loss (Fedus et al., [2021](https://arxiv.org/html/2412.19437v1#bib.bib21); Lepikhin et al., [2021](https://arxiv.org/html/2412.19437v1#bib.bib45)) to avoid unbalanced load. However, too large an auxiliary loss will impair the model performance (Wang et al., [2024a](https://arxiv.org/html/2412.19437v1#bib.bib93)). To achieve a better trade-off between load balance and model  performance, we pioneer an auxiliary-loss-free load balancing strategy (Wang et al., [2024a](https://arxiv.org/html/2412.19437v1#bib.bib93)) to ensure load balance.
> 

> …
> 

## Multi-Token Prediction

> Inspired by Gloeckle et al. ([2024](https://arxiv.org/html/2412.19437v1#bib.bib26)),  we investigate and set a Multi-Token Prediction (MTP) objective for  DeepSeek-V3, which extends the prediction scope to multiple future 
tokens at each position. On the one hand, an MTP objective densifies the training signals and may  improve data efficiency.
> 

> …
> 

## Infrastructure

> DeepSeek-V3 is trained on a cluster equipped with 2048 NVIDIA H800 GPUs. Each node in the H800 cluster contains 8 GPUs connected by NVLink and NVSwitch within nodes. Across different nodes, InfiniBand (IB) interconnects are utilized to facilitate communications.
> 

> Training Framework: The training of DeepSeek-V3 is supported by the HAI-LLM framework, an efficient and lightweight training framework crafted by our engineers from the ground up.
> 

> …
> 

## FP8 Training

> …
> 

![image.png](documents/articles/liu-2024-deepseek-technical-report-arxiv-preprint/image-3.png)

- Fine-Grained Quantization
- Online Quantization
- …

## Pre-Training

> Compare with DeepSeek-V2, we optimize the pre-training corpus by enhancing the ratio of mathematical and programming examples; while explaining coverage beyond English and Chinese.
> 

## Hyper-Parameters

> …
> 

### Model Hyper-Parameters

> …
> 

> We set the number of Transformer layers to 61 and the hidden dimension to 7168.
> 

> All learnable parameters are randomly initialized with a standard deviation of 0.006.
> 

> In MLA, we set the number of attention heads $n_h$ to 128 and the per-head dimension $d_h$ to 128.
> 

**Multi-Head Attention (MLA)**:

- Number of attention heads (**nh**): **128**.
- Per-head dimension (**dh**): **128**.
- Key-Value (KV) compression dimension (**dc**): **512**.
- Query compression dimension (**dc′**): **1536**.
- Decoupled queries and keys:
    - Per-head dimension (**dhR**): **64**.

**Feed-Forward Networks (FFNs)**:

- All FFNs, except for the first three layers, are replaced with **Mixture of Experts (MoE)** layers.
- **MoE Layer Configuration**:
    - Number of shared experts: **1**.
    - Number of routed experts: **256**.
    - Intermediate hidden dimension of each expert: **2048**.
    - Activated experts per token: **8**.
    - Maximum nodes a token can be sent to: **4**.

**Multi-Token Prediction**:

- Multi-token prediction depth (**D**): **1**.
    - Each token predicts:
        - The exact next token.
        - One additional token.

**Additional Components**:

- **RMSNorm layers** are added after the compressed latent vectors.
- **Scaling factors** are applied at the width bottlenecks.

**Model Size:**

- **Total Parameters**: **671 billion (671B)**.
- **Activated Parameters per Token**: **37 billion (37B)**.

### Training Hyper-Parameters

> …
> 

Optimizer & Hyperparameters

- **Optimizer**: AdamW (Loshchilov & Hutter, 2017)
- **Hyperparameters**:
    - **β₁** = **0.9**
    - **β₂** = **0.95**
    - **Weight Decay** = **0.1**

Training & Data Details

- **Maximum Sequence Length**: **4K tokens**
- **Total Pre-training Tokens**: **14.8 trillion (T) tokens**

Learning Rate Scheduling

1. **Warm-up Phase**:
    - Learning rate linearly increased **from 0 to 2.2 × 10⁻⁴** during the **first 2K steps**.
2. **Stable Learning Rate Phase**:
    - Learning rate kept **constant at 2.2 × 10⁻⁴** until the model consumes **10T training tokens**.
3. **Decay Phase**:
    - Learning rate decays **to 2.2 × 10⁻⁵** over **4.3T tokens** using a **cosine decay curve**.
4. **Final Phase (Last 500B tokens)**:
    - **First 333B tokens**: Learning rate remains **2.2 × 10⁻⁵**.
    - **Last 167B tokens**: Learning rate switched to **7.3 × 10⁻⁶**.

Gradient & Batch Size Configuration:

- **Gradient Clipping Norm**: **1.0**
- **Batch Size Scheduling**:
    - Gradually increased **from 3,072 to 15,360** during the first **469B tokens**.
    - **Kept at 15,360** for the remainder of training.

Parallelism & Routing:

- **Pipeline Parallelism**:
    - Different layers deployed **across different GPUs**.
    - Each MoE layer’s routed experts **uniformly deployed on 64 GPUs across 8 nodes**.
- **Node-limited Routing**:
    - Each token can be sent to **at most 4 nodes** (**M = 4**).

Load Balancing & Loss Configuration

- **Auxiliary-Loss-Free Load Balancing**:
    - Bias update speed (**γ**):
        - **0.001** for the **first 14.3T tokens**.
        - **0.0** for the **remaining 500B tokens**.
    - Balance loss weight (**α**): **0.0001** (to prevent extreme imbalance in a sequence).
- **Multi-Token Prediction (MTP) Loss Weight (λ)**:
    - **0.3** for the **first 10T tokens**.
    - **0.1** for the **remaining 4.8T tokens**.

## Post-Training

> We curate our instruction-tuning datasets to include **`1.5M`** instances spanning multiple domains, with each domain employing distinct data creation methods tailored to its specific requirements.
> 

- Reasoning Data,
- Non-Reasoning Data,
- Reinforcement Learning**:**  We employ a rule-based Reward Model (RM) and a model-based RM in our RL process.
- ..

## **Conclusion, Limitations, and Future Directions**

> …
> 

## References

- https://arxiv.org/html/2412.19437
- [DeepSeek-AI, :, Bi, X., Chen, D., Chen, G., Chen, S., Dai, D., Deng, C., Ding, H., Dong, K., Du, Q., Fu, Z., Gao, H., Gao, K., Gao, W., Ge, R., Guan, K., Guo, D., Guo, J., … Zou, Y. (2024). DeepSeek LLM: Scaling Open-Source Language Models with Longtermism. [https://arxiv.org/abs/2401.02954](https://arxiv.org/abs/2401.02954).](DeepSeek-AI,%20,%20Bi,%20X%20,%20Chen,%20D%20,%20Chen,%20G%20,%20Chen,%20S%2018b598edb7908024b929c5dc28625a06.md)
- [ ]  D. Guo, Q. Zhu, D. Yang, Z. Xie, K. Dong, W. Zhang, G. Chen, X. Bi, Y. Wu, Y. K. Li, F. Luo, Y. Xiong, and W. Liang. Deepseek-coder: When the large language model meets programming - the rise of code intelligence.  CoRR, abs/2401.14196, 2024.  URL [https://doi.org/10.48550/arXiv.2401.14196](https://doi.org/10.48550/arXiv.2401.14196).
- [ ]  M. Sun, X. Chen, J. Z. Kolter, and Z. Liu.  Massive activations in large language models.  arXiv preprint arXiv:2402.17762, 2024.
- Llama 3 model card, 2024a.  URL [https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md).
- Qwen.  Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
- Qwen.  Introducing Qwen1.5, 2024a.  URL [https://qwenlm.github.io/blog/qwen1.5](https://qwenlm.github.io/blog/qwen1.5).
- Qwen. Qwen2.5: A party of foundation models, 2024b.  URL [https://qwenlm.github.io/blog/qwen2.5](https://qwenlm.github.io/blog/qwen2.5).
- A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. d. l. Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, et al.  Mistral 7b.  arXiv preprint arXiv:2310.06825, 2023.
- Mistral.  Cheaper, better, faster, stronger: Continuing to push the frontier of ai and making it accessible to all, 2024.  URL [https://mistral.ai/news/mixtral-8x22b](https://mistral.ai/news/mixtral-8x22b).
- [ ]  vPIPE : A Virtualized Acceleration System for Achieving Efficient and Scalable Pipeline 
Parallel DNN Training [https://i.cs.hku.hk/~heming/papers/tpds21-vpipe.pdf](https://i.cs.hku.hk/~heming/papers/tpds21-vpipe.pdf)
- https://news.ycombinator.com/item?id=42824337
- Llama 3 model card, 2024a.  [https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md).
- Llama 3.1 model card, 2024b.  [https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md).
- Claude 3.5 sonnet, 2024.  [https://www.anthropic.com/news/claude-3-5-sonnet](https://www.anthropic.com/news/claude-3-5-sonnet).
- [ ]  J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al.  Program synthesis with large language models. *arXiv preprint arXiv:2108.07732*, 2021.
- Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, et al.  Constitutional AI: Harmlessness from AI feedback. arXiv preprint arXiv:2212.08073, 2022.
- [ ]  Y. Bai, S. Tu, J. Zhang, H. Peng, X. Wang, X. Lv, S. Cao, J. Xu, L. Hou, Y. Dong, J. Tang, and J. Li. LongBench v2: Towards deeper understanding and reasoning on realistic long-context multitasks.  arXiv preprint arXiv:2412.15204, 2024.
- M. Bauer, S. Treichler, and A. Aiken.  Singe: leveraging warp specialization for high performance on GPUs. In Proceedings of the 19th ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming, PPoPP ’14, page 119–130, New York, NY, USA, 2014. Association for Computing Machinery.
- [ ]  Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi.   PIQA: reasoning about physical commonsense in natural language. In The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020, New York, NY, USA, February 7-12, 2020, pages 7432–7439. AAAI Press, 2020.
- M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba.  Evaluating large language models trained on code. *CoRR*, abs/2107.03374, 2021.
- P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord. Think you have solved question answering? try arc, the AI2 reasoning challenge. CoRR, abs/1803.05457, 2018.   [http://arxiv.org/abs/1803.05457](http://arxiv.org/abs/1803.05457).
- K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al.  Training verifiers to solve math word problems.  arXiv preprint arXiv:2110.14168, 2021.
- Y. Cui, T. Liu, W. Che, L. Xiao, Z. Chen, W. Ma, S. Wang, and G. Hu. A span-extraction dataset for Chinese machine reading comprehension. In K. Inui, J. Jiang, V. Ng, and X. Wan, editors, Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 5883–5889, Hong Kong, China, Nov. 2019. Association for Computational Linguistics.
- [ ]  D. Dai, C. Deng, C. Zhao, R. X. Xu, H. Gao, D. Chen, J. Li, W. Zeng, X. Yu, Y. Wu, Z. Xie, Y. K. Li, P. Huang, F. Luo, C. Ruan, Z. Sui, and W. Liang. Deepseekmoe: Towards ultimate expert specialization in mixture-of-experts language models.
- DeepSeek-AI. Deepseek-coder-v2: Breaking the barrier of closed-source models in code intelligence. CoRR, abs/2406.11931, 2024a.
- [ ]  DeepSeek-AI. Deepseek LLM: scaling open-source language models with longtermism. CoRR, abs/2401.02954, 2024b.
- DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model. CoRR, abs/2405.04434, 2024c.
- [ ]  T. Dettmers, M. Lewis, Y. Belkada, and L. Zettlemoyer. Gpt3. int8 (): 8-bit matrix multiplication for transformers at scale. Advances in Neural Information Processing Systems, 35:30318–30332, 2022.
- H. Ding, Z. Wang, G. Paolini, V. Kumar, A. Deoras, D. Roth, and S. Soatto. Fewer truncations improve language modeling. arXiv preprint arXiv:2404.10830, 2024.
- D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In J. Burstein, C. Doran, and T. Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers), pages 2368–2378. Association for Computational Linguistics, 2019.
- Y. Dubois, B. Galambosi, P. Liang, and T. B. Hashimoto. Length-controlled alpacaeval: A simple way to debias automatic evaluators. arXiv preprint arXiv:2404.04475, 2024.
- W. Fedus, B. Zoph, and N. Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. CoRR, abs/2101.03961, 2021.
- [ ]  M. Fishman, B. Chmiel, R. Banner, and D. Soudry. Scaling FP8 training to trillion-token llms. arXiv preprint arXiv:2409.12517, 2024.
- E. Frantar, S. Ashkboos, T. Hoefler, and D. Alistarh. Gptq: Accurate post-training quantization for generative pre-trained transformers. arXiv preprint arXiv:2210.17323, 2022.
- L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, et al. The Pile: An 800GB dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027, 2020.
- [ ]  A. P. Gema, J. O. J. Leang, G. Hong, A. Devoto, A. C. M. Mancino, R. Saxena, X. He, Y. Zhao, X. Du, M. R. G. Madani, C. Barale, R. McHardy, J. Harris, J. Kaddour, E. van Krieken, and P. Minervini. Are we done with mmlu? CoRR, abs/2406.04127, 2024.
- [ ]  F. Gloeckle, B. Y. Idrissi, B. Rozière, D. Lopez-Paz, and G. Synnaeve. Better & faster large language models via multi-token prediction. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. [OpenReview.net](http://openreview.net/), 2024.
- Google. Our next-generation model: Gemini 1.5, 2024.
- R. L. Graham, D. Bureddy, P. Lui, H. Rosenstock, G. Shainer, G. Bloch, D. Goldenerg, M. Dubman, S. Kotchubievsky, V. Koushnir, et al. Scalable hierarchical aggregation protocol (SHArP): A hardware architecture for efficient data reduction. In 2016 First International Workshop on Communication Optimizations in HPC (COMHPC), pages 1–10. IEEE, 2016.
- A. Gu, B. Rozière, H. Leather, A. Solar-Lezama, G. Synnaeve, and S. I. Wang. Cruxeval: A benchmark for code reasoning, understanding and execution, 2024.
- D. Guo, Q. Zhu, D. Yang, Z. Xie, K. Dong, W. Zhang, G. Chen, X. Bi, Y. Wu, Y. K. Li, F. Luo, Y. Xiong, and W. Liang. Deepseek-coder: When the large language model meets programming - the rise of code intelligence. CoRR, abs/2401.14196, 2024.
- [ ]  A. Harlap, D. Narayanan, A. Phanishayee, V. Seshadri, N. Devanur, G. Ganger, and P. Gibbons. Pipedream: Fast and efficient pipeline parallel dnn training, 2018.
- [ ]  B. He, L. Noci, D. Paliotta, I. Schlag, and T. Hofmann. Understanding and minimising outlier features in transformer training. In The Thirty-eighth Annual Conference on Neural Information Processing Systems.
- Y. He, S. Li, J. Liu, Y. Tan, W. Wang, H. Huang, X. Bu, H. Guo, C. Hu, B. Zheng, et al. Chinese simpleqa: A chinese factuality evaluation for large language models. arXiv preprint arXiv:2411.07140, 2024.
- D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
- D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874, 2021.
- Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, J. Lei, et al. C-Eval: A multi-level multi-discipline chinese evaluation suite for foundation models. arXiv preprint arXiv:2305.08322, 2023.
- N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. CoRR, abs/2403.07974, 2024.
- A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. d. l. Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.
- M. Joshi, E. Choi, D. Weld, and L. Zettlemoyer. TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension. In R. Barzilay and M.-Y. Kan, editors, Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1601–1611, Vancouver, Canada, July 2017. Association for Computational Linguistics.
- D. Kalamkar, D. Mudigere, N. Mellempudi, D. Das, K. Banerjee, S. Avancha, D. T. Vooturi, N. Jammalamadaka, J. Huang, H. Yuen, et al. A study of bfloat16 for deep learning training. arXiv preprint arXiv:1905.12322, 2019.
- S. Krishna, K. Krishna, A. Mohananey, S. Schwarcz, A. Stambler, S. Upadhyay, and M. Faruqui. Fact, fetch, and reason: A unified evaluation of retrieval-augmented generation. CoRR, abs/2409.12941, 2024.
- T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. P. Parikh, C. Alberti, D. Epstein, I. Polosukhin, J. Devlin, K. Lee, K. Toutanova, L. Jones, M. Kelcey, M. Chang, A. M. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: a benchmark for question answering research. Trans. Assoc. Comput. Linguistics, 7:452–466, 2019.
- G. Lai, Q. Xie, H. Liu, Y. Yang, and E. H. Hovy. RACE: large-scale reading comprehension dataset from examinations. In M. Palmer, R. Hwa, and S. Riedel, editors, Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing, EMNLP 2017, Copenhagen, Denmark, September 9-11, 2017, pages 785–794. Association for Computational Linguistics, 2017.
- N. Lambert, V. Pyatkin, J. Morrison, L. Miranda, B. Y. Lin, K. Chandu, N. Dziri, S. Kumar, T. Zick, Y. Choi, et al. Rewardbench: Evaluating reward models for language modeling. arXiv preprint arXiv:2403.13787, 2024.
- D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer, and Z. Chen. Gshard: Scaling giant models with conditional computation and automatic sharding. In 9th International Conference on Learning Representations, ICLR 2021. [OpenReview.net](http://openreview.net/), 2021.
- Y. Leviathan, M. Kalman, and Y. Matias. Fast inference from transformers via speculative decoding. In International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu, Hawaii, USA, volume 202 of Proceedings of Machine Learning Research, pages 19274–19286. PMLR, 2023.
- H. Li, Y. Zhang, F. Koto, Y. Yang, H. Zhao, Y. Gong, N. Duan, and T. Baldwin. CMMLU: Measuring massive multitask language understanding in Chinese. arXiv preprint arXiv:2306.09212, 2023.
- S. Li and T. Hoefler. Chimera: efficiently training large-scale neural networks with bidirectional pipelines. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, SC ’21, page 1–14. ACM, Nov. 2021. 10.1145/3458817.3476145.
- T. Li, W.-L. Chiang, E. Frick, L. Dunlap, T. Wu, B. Zhu, J. E. Gonzalez, and I. Stoica. From crowdsourced data to high-quality benchmarks: Arena-hard and benchbuilder pipeline. arXiv preprint arXiv:2406.11939, 2024a.
- W. Li, F. Qi, M. Sun, X. Yi, and J. Zhang. Ccpm: A chinese classical poetry matching dataset, 2021.
- Y. Li, F. Wei, C. Zhang, and H. Zhang. EAGLE: speculative sampling requires rethinking feature uncertainty. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. [OpenReview.net](http://openreview.net/), 2024b.
- B. Y. Lin. ZeroEval: A Unified Framework for Evaluating Language Models, July 2024.
- I. Loshchilov and F. Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101, 2017.
- S. Lundberg. The art of prompt design: Prompt boundaries and token healing, 2023.
- Y. Luo, Z. Zhang, R. Wu, H. Liu, Y. Jin, K. Zheng, M. Wang, Z. He, G. Hu, L. Chen, et al. Ascend HiFloat8 format for deep learning. arXiv preprint arXiv:2409.16626, 2024.
- MAA. American invitational mathematics examination - aime. In American Invitational Mathematics Examination - AIME 2024, February 2024.
- P. Micikevicius, D. Stosic, N. Burgess, M. Cornea, P. Dubey, R. Grisenthwaite, S. Ha, A. Heinecke, P. Judd, J. Kamalu, et al. FP8 formats for deep learning. arXiv preprint arXiv:2209.05433, 2022.
- Mistral. Cheaper, better, faster, stronger: Continuing to push the frontier of ai and making it accessible to all, 2024.
- S. Narang, G. Diamos, E. Elsen, P. Micikevicius, J. Alben, D. Garcia, B. Ginsburg, M. Houston, O. Kuchaiev, G. Venkatesh, et al. Mixed precision training. In Int. Conf. on Learning Representation, 2017.
- B. Noune, P. Jones, D. Justus, D. Masters, and C. Luschi. 8-bit numerical formats for deep neural networks. arXiv preprint arXiv:2206.02915, 2022.
- NVIDIA. Improving network performance of HPC systems using NVIDIA Magnum IO NVSHMEM and GPUDirect Async. [https://developer.nvidia.com/blog/improving-network-performance-of-hpc-systems-using-nvidia-magnum-io-nvshmem-and-gpudirect-async](https://developer.nvidia.com/blog/improving-network-performance-of-hpc-systems-using-nvidia-magnum-io-nvshmem-and-gpudirect-async), 2022.
- NVIDIA. Blackwell architecture. [https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/), 2024a.
- NVIDIA. TransformerEngine, 2024b. URL [https://github.com/NVIDIA/TransformerEngine](https://github.com/NVIDIA/TransformerEngine). Accessed: 2024-11-19.
- OpenAI. Hello GPT-4o, 2024a. URL [https://openai.com/index/hello-gpt-4o/](https://openai.com/index/hello-gpt-4o/).
- OpenAI. Multilingual massive multitask language understanding (mmmlu), 2024b. URL [https://huggingface.co/datasets/openai/MMMLU](https://huggingface.co/datasets/openai/MMMLU).
- OpenAI. Introducing SimpleQA, 2024c. URL [https://openai.com/index/introducing-simpleqa/](https://openai.com/index/introducing-simpleqa/).
- OpenAI. Introducing SWE-bench verified we’re releasing a human-validated subset of swe-bench that more, 2024d. URL [https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/).
- B. Peng, J. Quesnelle, H. Fan, and E. Shippole. Yarn: Efficient context window extension of large language models. arXiv preprint arXiv:2309.00071, 2023a.
- H. Peng, K. Wu, Y. Wei, G. Zhao, Y. Yang, Z. Liu, Y. Xiong, Z. Yang, B. Ni, J. Hu, et al. FP8-LM: Training FP8 large language models. arXiv preprint arXiv:2310.18313, 2023b.
- P. Qi, X. Wan, G. Huang, and M. Lin. Zero bubble pipeline parallelism. arXiv preprint arXiv:2401.10241, 2023a.
- P. Qi, X. Wan, G. Huang, and M. Lin. Zero bubble pipeline parallelism, 2023b. URL [https://arxiv.org/abs/2401.10241](https://arxiv.org/abs/2401.10241).
- Qwen. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
- Qwen. Introducing Qwen1.5, 2024a. URL [https://qwenlm.github.io/blog/qwen1.5](https://qwenlm.github.io/blog/qwen1.5).
- Qwen. Qwen2.5: A party of foundation models, 2024b. URL [https://qwenlm.github.io/blog/qwen2.5](https://qwenlm.github.io/blog/qwen2.5).
- S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He. Zero: Memory optimizations toward training trillion parameter models. In SC20: International Conference for High Performance Computing, Networking, Storage and Analysis, pages 1–16. IEEE, 2020.
- D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. arXiv preprint arXiv:2311.12022, 2023.
- B. D. Rouhani, R. Zhao, A. More, M. Hall, A. Khodamoradi, S. Deng, D. Choudhary, M. Cornea, E. Dellinger, K. Denolf, et al. Microscaling data formats for deep learning. arXiv preprint arXiv:2310.10537, 2023a.
- B. D. Rouhani, R. Zhao, A. More, M. Hall, A. Khodamoradi, S. Deng, D. Choudhary, M. Cornea, E. Dellinger, K. Denolf, et al. Microscaling data formats for deep learning. arXiv preprint arXiv:2310.10537, 2023b.
- K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd schema challenge at scale, 2019.
- Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. Li, Y. Wu, and D. Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.
- N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. V. Le, G. E. Hinton, and J. Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. In 5th International Conference on Learning Representations, ICLR 2017. [OpenReview.net](http://openreview.net/), 2017. URL [https://openreview.net/forum?id=B1ckMDqlg](https://openreview.net/forum?id=B1ckMDqlg).
- F. Shi, M. Suzgun, M. Freitag, X. Wang, S. Srivats, S. Vosoughi, H. W. Chung, Y. Tay, S. Ruder, D. Zhou, D. Das, and J. Wei. Language models are multilingual chain-of-thought reasoners. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023. [OpenReview.net](http://openreview.net/), 2023. URL [https://openreview.net/forum?id=fR3wGCk-IXp](https://openreview.net/forum?id=fR3wGCk-IXp).
- Y. Shibata, T. Kida, S. Fukamachi, M. Takeda, A. Shinohara, T. Shinohara, and S. Arikawa. Byte pair encoding: A text compression scheme that accelerates pattern matching. 1999.
- J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu. Roformer: Enhanced transformer with rotary position embedding. Neurocomputing, 568:127063, 2024.
- K. Sun, D. Yu, D. Yu, and C. Cardie. Investigating prior knowledge for challenging chinese machine reading comprehension, 2019a.
- M. Sun, X. Chen, J. Z. Kolter, and Z. Liu. Massive activations in large language models. arXiv preprint arXiv:2402.17762, 2024.
- X. Sun, J. Choi, C.-Y. Chen, N. Wang, S. Venkataramani, V. V. Srinivasan, X. Cui, W. Zhang, and K. Gopalakrishnan. Hybrid 8-bit floating point (HFP8) training and inference for deep neural networks. Advances in neural information processing systems, 32, 2019b.
- M. Suzgun, N. Scales, N. Schärli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. V. Le, E. H. Chi, D. Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve them. arXiv preprint arXiv:2210.09261, 2022.
- V. Thakkar, P. Ramani, C. Cecka, A. Shivam, H. Lu, E. Yan, J. Kosaian, M. Hoemmen, H. Wu, A. Kerr, M. Nicely, D. Merrill, D. Blasig, F. Qiao, P. Majcher, P. Springer, M. Hohnerbach, J. Wang, and M. Gupta. CUTLASS, Jan. 2023. URL [https://github.com/NVIDIA/cutlass](https://github.com/NVIDIA/cutlass).
- H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. LLaMA: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023a.
- H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, D. Bikel, L. Blecher, C. Canton-Ferrer, M. Chen, G. Cucurull, D. Esiobu, J. Fernandes, J. Fu, W. Fu, B. Fuller, C. Gao, V. Goswami, N. Goyal, A. Hartshorn, S. Hosseini, R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, I. Kloumann, A. Korenev, P. S. Koura, M. Lachaux, T. Lavril, J. Lee, D. Liskovich, Y. Lu, Y. Mao, X. Martinet, T. Mihaylov, P. Mishra, I. Molybog, Y. Nie, A. Poulton, J. Reizenstein, R. Rungta, K. Saladi, A. Schelten, R. Silva, E. M. Smith, R. Subramanian, X. E. Tan, B. Tang, R. Taylor, A. Williams, J. X. Kuan, P. Xu, Z. Yan, I. Zarov, Y. Zhang, A. Fan, M. Kambadur, S. Narang, A. Rodriguez, R. Stojnic, S. Edunov, and T. Scialom. Llama 2: Open foundation and fine-tuned chat models. CoRR, abs/2307.09288, 2023b.
- A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.
- L. Wang, H. Gao, C. Zhao, X. Sun, and D. Dai. Auxiliary-loss-free load balancing strategy for mixture-of-experts. CoRR, abs/2408.15664, 2024a.
- Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, T. Li, M. Ku, K. Wang, A. Zhuang, R. Fan, X. Yue, and W. Chen. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. CoRR, abs/2406.01574, 2024b.
- T. Wei, J. Luan, W. Liu, S. Dong, and B. Wang. Cmath: Can your language model pass chinese elementary school math test?, 2023.
- M. Wortsman, T. Dettmers, L. Zettlemoyer, A. Morcos, A. Farhadi, and L. Schmidt. Stable and low-precision training for large-scale vision-language models. Advances in Neural Information Processing Systems, 36:10271–10298, 2023.
- H. Xi, C. Li, J. Chen, and J. Zhu. Training transformers with 4-bit integers. Advances in Neural Information Processing Systems, 36:49146–49168, 2023.
- C. S. Xia, Y. Deng, S. Dunn, and L. Zhang. Agentless: Demystifying llm-based software engineering agents. arXiv preprint, 2024.
- H. Xia, T. Ge, P. Wang, S. Chen, F. Wei, and Z. Sui. Speculative decoding: Exploiting speculative execution for accelerating seq2seq generation. In Findings of the Association for Computational Linguistics: EMNLP 2023, Singapore, December 6-10, 2023, pages 3909–3925. Association for Computational Linguistics, 2023.
- G. Xiao, J. Lin, M. Seznec, H. Wu, J. Demouth, and S. Han. Smoothquant: Accurate and efficient post-training quantization for large language models. In International Conference on Machine Learning, pages 38087–38099. PMLR, 2023.
- L. Xu, H. Hu, X. Zhang, L. Li, C. Cao, Y. Li, Y. Xu, K. Sun, D. Yu, C. Yu, Y. Tian, Q. Dong, W. Liu, B. Shi, Y. Cui, J. Li, J. Zeng, R. Wang, W. Xie, Y. Li, Y. Patterson, Z. Tian, Y. Zhang, H. Zhou, S. Liu, Z. Zhao, Q. Zhao, C. Yue, X. Zhang, Z. Yang, K. Richardson, and Z. Lan. CLUE: A chinese language understanding evaluation benchmark. In D. Scott, N. Bel, and C. Zong, editors, Proceedings of the 28th International Conference on Computational Linguistics, COLING 2020, Barcelona, Spain (Online), December 8-13, 2020, pages 4762–4772. International Committee on Computational Linguistics, 2020.
- R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish your sentence? In A. Korhonen, D. R. Traum, and L. Màrquez, editors, Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers, pages 4791–4800. Association for Computational Linguistics, 2019.
- W. Zhong, R. Cui, Y. Guo, Y. Liang, S. Lu, Y. Wang, A. Saied, W. Chen, and N. Duan. AGIEval: A human-centric benchmark for evaluating foundation models. CoRR, abs/2304.06364, 2023.
- J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou. Instruction-following evaluation for large language models. arXiv preprint arXiv:2311.07911, 2023.
