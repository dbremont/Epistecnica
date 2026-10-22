# Sun, X., Chen, Y., Huang, Y., Xie, R., Zhu, J., Zhang, K., Li, S., Yang, Z., Han, J., Shu, X., & others. (2024). Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent. ArXiv.


```python
@article{sun2024hunyuan,
  title={Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent},
  author={Sun, Xingwu and Chen, Yanfeng and Huang, Yiqing and Xie, Ruobing and Zhu, Jiaqi and Zhang, Kai and Li, Shuaipeng and Yang, Zhen and Han, Jonny and Shu, Xiaobo and others},
  journal={arXiv},
  year={2024}
}
```

## Overview

Hunyuan-Large is Tencent's open-source decoder-only Transformer with a mixture-of-experts feed-forward layer: 389B total parameters of which 52B are activated per token, a 256K-token context window, and pre-training on 7T tokens — roughly 1.5T of them synthetic. Each token activates one shared expert plus 1 of 16 specialized experts; the KV cache is compressed by combining Grouped-Query Attention with Cross-Layer Attention (~95% less memory than MHA).

The report's contributions are a large-scale synthetic-data pipeline, the KV-cache compression scheme, recycle routing and expert-specific learning rates, an MoE scaling-law study that selected 52B activated parameters and ~7T tokens, and a post-training recipe of more than 1M SFT instructions followed by single-stage offline+online DPO. Hunyuan-Large outperforms Llama-3.1-70B and is comparable to Llama-3.1-405B on public benchmarks while activating 52B parameters; the weights, the code, and the PenguinScrolls long-context benchmark are released.

## Technical & Epistemic Content Map

> A forest, not a tree: the content splits into independent roots — eight epistemic inquiries (what the work claims, represents, constructs, and evaluates) and seven technical trees (what is built and how it is produced). The report itself is the envelope and is not a node. Backticked segments are type groupings; plain segments are instances. `Source` cites the paper's own section, table, or figure; `—` marks analytic groupings the paper does not itself state.

| Element Type (Technical, Epistemical) | Instance Tree Path | Description | Source |
|---|---|---|---|
| Epistemical | `Aggregate` → Open-Source MoE Inquiry | The inquiry into releasing a large open-source mixture-of-experts model: its purpose, gap, target, and surrounding conditions. | — |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Orientation` | Grouping: the orientation directing the inquiry. | — |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Orientation` → Open-Source MoE Release | Introduce and release the largest open-source Transformer-based MoE model to advance the LLM community. | §1 |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Orientation` → `Epistemic Gap` → Open-Source MoE Scarcity | Most open-source LLMs are dense; MoE models are few and comparatively small. | §1 |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Target` | Grouping: the capability the inquiry addresses. | — |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Target` → Language Model Capability | The model's behaviour across language understanding, reasoning, mathematics, coding, and long-context tasks. | Abstract; §1 |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Target` → `Observable` → Benchmark Score | Task accuracy on public and in-house benchmarks (MMLU, MATH, HumanEval, RULER, PenguinScrolls, and others). | §4 |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Context` | Grouping: the conditions surrounding the inquiry. | — |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Context` → `Epistemic Condition` → Open-Source LLM Landscape | Open-weight dense models dominate; MoE releases are few and small. | §1 |
| Epistemical | `Aggregate` → Open-Source MoE Inquiry → `Epistemic Context` → `Epistemic Condition` → Chinese–English Demand | The corpus, tokenizer, and evaluation reflect practical Chinese and English use. | §2.1.1 |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry | The inquiry into how activated parameters, training tokens, and compute relate, used to size the model. | §2.3.1 |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry → `Epistemic Orientation` | Grouping: the orientation directing the inquiry. | — |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry → `Epistemic Orientation` → `Epistemic Question` → MoE Scaling Laws | What relations hold between activated parameters, training tokens, compute, and performance for MoE models? | §2.3.1 |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry → `Epistemic Construction` | Grouping: the theories, methods, and artifacts the inquiry constructs. | — |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry → `Epistemic Construction` → MoE Scaling Law | The fitted account of how optimal activated parameters and training data scale with compute. | §2.3.1 |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry → `Epistemic Construction` → MoE Scaling Law → IsoFLOPs Analysis | Quadratic fits over 10M–1B activated-parameter MoE models trained on 100B tokens, with 10B–100B token sweeps. | §2.3.1; Figures 3–4 |
| Epistemical | `Aggregate` → MoE Scaling-Law Inquiry → `Epistemic Construction` → MoE Scaling Law → Parameter–Data Trade-off | Optima of ≈58.1B activated parameters and ≈5.6T tokens; 52B and ~7T are selected on the flat part of the curves. | §2.3.1 |
| Epistemical | `Aggregate` → MoE Transformer Formalism | The representational apparatus through which the model is described: tokens, attention, routing, experts, caches, and scaling laws. | §2.2.1 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` | Grouping: the formal apparatus through which the model is described. | — |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism | The decoder-only Transformer with mixture-of-experts notation: tokens, attention, routers, experts, and caches. | §2.2.1; Table 1 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Representation Element` | Grouping: combinable constituents of the formalism. | — |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Representation Element` → Token | Atomic text unit from the 128K vocabulary; the input and output unit of computation. | §2.1.2 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Representation Element` → Attention Head | One head of the attention module: 80 query heads and 8 key/value heads. | Table 1; §2.2.2 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Representation Element` → Router Score | Per-token affinity logit that selects the specialized expert. | §2.2.3 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Representation Element` → Expert Weight Matrix | Feed-forward parameters of one shared or specialized expert. | §2.2.1 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Representation Element` → KV Cache Entry | Stored key/value tensors reused across decoding steps instead of recomputed. | §2.2.2 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` | Grouping: the rules and structures governing the formalism. | — |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` → Compute Budget Formula | C ≈ 9.59·N·D + 2.3×10⁸·D for long-sequence MoE models, with N the activated parameters and D the trained tokens. | §2.3.1 (Eq. 2) |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` → Optimal Parameter Law | N_opt = N_c·C_min^α with N_c = 5.9×10⁻³ and α = 0.5305. | §2.3.1; Figure 3 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` → Optimal Data Law | D_opt = D_c·C_min^β with D_c = 3.2 and β = 0.50. | §2.3.1; Figure 4 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` → Learning Rate Scaling Law | ε_opt(B) = 2·ε_max / (√(B_noise/B) + √(B/B_noise)) for AdamW. | §2.2.4 (Eq. 1) |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` → `Property` → Activation Ratio | 52B activated of 389B total parameters (≈13.4%) for each token. | Table 1 |
| Epistemical | `Aggregate` → MoE Transformer Formalism → `Epistemic Representation` → `Representational System` → MoE Transformer Formalism → `Constitutive Substrate` → `Property` → Model Scale | 389B total parameters, 52B activated, 256K-token context, 7T training tokens. | Table 1; Abstract |
| Epistemical | `Aggregate` → MoE Efficiency Inquiry | The inquiry into training and serving a large MoE efficiently and stably: routing, expert learning rates, and KV-cache memory. | §1; §2.2 |
| Epistemical | `Aggregate` → MoE Efficiency Inquiry → `Epistemic Orientation` | Grouping: the orientation directing the inquiry. | — |
| Epistemical | `Aggregate` → MoE Efficiency Inquiry → `Epistemic Orientation` → `Epistemic Question` → Efficient Large-Scale MoE Training | How can a 389B-parameter MoE with 52B activated parameters be pre-trained and aligned efficiently and stably? | §1; §2.2 |
| Epistemical | `Aggregate` → MoE Efficiency Inquiry → `Epistemic Construction` | Grouping: the theories, methods, and artifacts the inquiry constructs. | — |
| Epistemical | `Aggregate` → MoE Efficiency Inquiry → `Epistemic Construction` → Recycle Routing Strategy | Method that reassigns tokens dropped by capacity-limited top-k routing to specialized experts still below capacity. | §2.2.3; Figure 2 |
| Epistemical | `Aggregate` → MoE Efficiency Inquiry → `Epistemic Construction` → Expert-Specific Learning Rate Strategy | Assigns ε_opt(B) to the shared expert and ε_opt(B/16) ≈ 0.31·ε_opt(B) to specialized experts. | §2.2.4 |
| Epistemical | `Aggregate` → Synthetic Data Inquiry | The inquiry into synthesizing pre-training data: instruction generation, evolution, response generation, and filtering. | §2.1.1; Figure 1 |
| Epistemical | `Aggregate` → Synthetic Data Inquiry → `Epistemic Construction` | Grouping: the theories, methods, and artifacts the inquiry constructs. | — |
| Epistemical | `Aggregate` → Synthetic Data Inquiry → `Epistemic Construction` → Synthetic Data Pipeline | Four-step generation–evolution–response–filtering method producing nearly 1.5T synthetic tokens. | §2.1.1; Figure 1 |
| Epistemical | `Aggregate` → Synthetic Data Inquiry → `Epistemic Construction` → Synthetic Data Pipeline → Instruction Generation | Diverse prompts seeded from web pages, QA data, code repositories, and books. | §2.1.1 Step 1 |
| Epistemical | `Aggregate` → Synthetic Data Inquiry → `Epistemic Construction` → Synthetic Data Pipeline → Instruction Evolution | Clarity and informativeness refinement, self-instruct expansion of low-resource domains, and difficulty escalation. | §2.1.1 Step 2 |
| Epistemical | `Aggregate` → Synthetic Data Inquiry → `Epistemic Construction` → Synthetic Data Pipeline → Response Generation | Specialized models of different sizes produce expert-level answers to the evolved instructions. | §2.1.1 Step 3 |
| Epistemical | `Aggregate` → Synthetic Data Inquiry → `Epistemic Construction` → Synthetic Data Pipeline → Response Filtering | A critique model plus self-consistency checks remove low-quality or inconsistent pairs. | §2.1.1 Step 4 |
| Epistemical | `Aggregate` → Long-Context Inquiry | The inquiry into extending the model's usable context to 256K tokens. | §2.3.3 |
| Epistemical | `Aggregate` → Long-Context Inquiry → `Epistemic Construction` | Grouping: the theories, methods, and artifacts the inquiry constructs. | — |
| Epistemical | `Aggregate` → Long-Context Inquiry → `Epistemic Construction` → Long-Context Training Recipe | Two-stage 32K→256K training with the RoPE base frequency scaled to 10⁹ over a 25% long / 75% normal corpus. | §2.3.3 |
| Epistemical | `Aggregate` → Alignment Inquiry | The inquiry into aligning the model to instructions and human preferences. | §3 |
| Epistemical | `Aggregate` → Alignment Inquiry → `Epistemic Construction` | Grouping: the theories, methods, and artifacts the inquiry constructs. | — |
| Epistemical | `Aggregate` → Alignment Inquiry → `Epistemic Construction` → Instruction Taxonomy | Labelled classification of instruction types used to analyze and balance SFT data. | §3.1.2 |
| Epistemical | `Aggregate` → Alignment Inquiry → `Epistemic Construction` → SFT Data Methodology | Extraction, generalization, balancing, and rule/model/human quality control over more than 1M instructions. | §3.1.2; §3.1.3 |
| Epistemical | `Aggregate` → Alignment Inquiry → `Epistemic Construction` → DPO Alignment Recipe | Single-stage offline+online DPO with an SFT loss term on chosen responses and an exponential moving average. | §3.2 |
| Epistemical | `Aggregate` → Model Evaluation Inquiry | The inquiry into measuring the model's capabilities and long-context behaviour. | §4 |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Evaluation` | Grouping: the assessments supporting the claims. | — |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Evaluation` → Model Capability Evaluation | Benchmark comparison of pre-trained and post-trained models against dense and MoE baselines. | §4.1; §4.2 |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Evaluation` → Model Capability Evaluation → Benchmark Protocol | Fixed few-shot settings and metrics per benchmark; best publicly reported or self-reproduced baseline score. | §4.1.1; §4.2.1 |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Evaluation` → Model Capability Evaluation → LLM-as-Judge Evaluation | LLM-based scoring used on LV-Eval to reduce the false negatives of overly strict metrics. | §4.3.1 |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Evaluation` → Model Capability Evaluation → Long-Context Evaluation | RULER, LV-Eval, and PenguinScrolls measured across 0–128K context intervals. | §4.3; Tables 5–6 |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Construction` | Grouping: the theories, methods, and artifacts the inquiry constructs. | — |
| Epistemical | `Aggregate` → Model Evaluation Inquiry → `Epistemic Construction` → PenguinScrolls | In-house long-context benchmark: four task types, Chinese and English, multi-turn, up to 128K tokens. | §4.3.2; Table 6 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large | The released decoder-only MoE model: 389B total / 52B activated parameters and a 256K-token context. | §2.2.1; Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Purpose` → Open-Weight LLM Provision | Provide a state-of-the-art open-weight LLM for community research and applications. | §1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer | A 64-layer decoder-only stack that replaces the dense feed-forward network with a routed mixture of experts. | §2.2.1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block | One of 64 blocks combining a self-attention sublayer and an MoE feed-forward sublayer. | §2.2.1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Self-Attention Module | Attention over 80 query heads served by 8 key/value heads. | §2.2.1; Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Self-Attention Module → `Constitutive Technique` → Grouped-Query Attention | Groups query heads around a smaller set of shared key/value heads. | §2.2.2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Self-Attention Module → `Constitutive Technique` → Cross-Layer Attention | Shares one KV cache between adjacent layers (every 2 layers). | §2.2.2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Self-Attention Module → `Constitutive Technical Object` → KV Cache | Key/value store reduced to about 5% of MHA memory by GQA+CLA. | §2.2.2; Table 2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Mixture-of-Experts Feed-Forward Layer | Replaces the dense feed-forward network with one shared and 16 specialized experts. | §2.2.1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Mixture-of-Experts Feed-Forward Layer → `Constitutive Technical Object` → Shared Expert | Always-active expert capturing knowledge common to all tokens. | §2.2.3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Mixture-of-Experts Feed-Forward Layer → `Constitutive Technical Object` → Specialized Expert Set | Sixteen domain experts; one is activated per token. | §2.2.3; Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Mixture-of-Experts Feed-Forward Layer → `Constitutive Technique` → Top-1 Expert Routing | Selects the highest-scoring specialized expert for each token. | §2.2.3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Mixture-of-Experts Feed-Forward Layer → `Constitutive Technique` → Recycle Routing | Reassigns capacity-dropped tokens at random to specialized experts below capacity. | §2.2.3; Figure 2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → Rotary Position Embedding | Positional encoding; its base frequency is scaled to 10⁹ for the 256K phase. | §2.2.1; §2.3.3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Architecture` → Decoder-Only MoE Transformer → `Constitutive Technical Object` → Transformer Block → `Constitutive Technical Object` → SwiGLU Activation | Gated activation function inside the expert networks. | §2.2.1; Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Constitutive Technical Object` → Tokenizer | 128K vocabulary: 100K tiktoken tokens plus 28K Chinese tokens; 3.13 characters per token. | §2.1.2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Configuration` → Model Hyperparameters | 64 layers, hidden size 6400, 80 heads / 8 KV heads, 1 shared + 16 specialized experts, 128K vocabulary, 7T tokens, 256K context. | Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Configuration` → Model Hyperparameters → Total Parameters | 389B. | Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Configuration` → Model Hyperparameters → Activated Parameters | 52B, exercised per token by one shared expert plus one specialized expert. | Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Configuration` → Model Hyperparameters → Context Length | 256K tokens after long-context pre-training. | Table 1; Abstract |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Resource` → Pre-Training Corpus | 7T tokens, about 1.5T synthetic, mainly Chinese and English, filtered for quality and toxicity. | §2.1.1; §1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Constraint` → Inference Memory Budget | KV-cache growth with context length dominates serving memory. | §2.2.2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Constraint` → Expert Capacity | Per-expert token capacity bounds load and drops overflow tokens during training. | §2.2.3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Trade-off` → KV Cache Compression versus Quality | GQA+CLA remove about 95% of KV memory with little reported quality loss. | §2.2.2 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Trade-off` → Capacity Factor versus Dropped Tokens | A larger capacity factor reduces drops but lowers training efficiency. | §2.2.3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Property` → Activation Sparsity | Only 52B of the 389B parameters are active per token. | Table 1 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Property` → Bilingual Coverage | Chinese- and English-focused corpus, tokenizer, and evaluation. | §2.1.1; §4 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Capability` → Long-Context Processing | Handles up to 256K tokens after the two-stage long-context pre-training. | §2.3.3; Table 5 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Capability` → Mathematical Reasoning | Strong GSM8K, MATH, and CMATH results among comparable open models. | Table 3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Capability` → Code Generation | HumanEval 71.4 (pre-trained) and 90.0 (instruct). | Table 3; Table 4 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Performance` → Pre-Trained Benchmark Results | MMLU 88.4, C-Eval 91.9, MATH 69.8, HumanEval 71.4 with 52B activated parameters. | Table 3 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Performance` → Instruct Benchmark Results | MMLU 89.9, MATH 77.4, MT-Bench 9.4, Arena-Hard 81.8, AlpacaEval-2.0 51.8. | Table 4 |
| Technical | `Production Virtual Technical Object` → Hunyuan-Large → `Technical Performance` → Long-Context Results | RULER 89.53 (64–128K), LV-Eval 67.87, PenguinScrolls overall 85.23. | Tables 5–6 |
| Technical | `Technical Practice` → Pre-Training | Pre-trains the base model on 7T tokens, then extends the context in two stages up to 256K. | §2 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Data Processing and Synthesis | Filters, anonymizes, labels, and synthesizes the pre-training corpus. | §2.1.1 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Data Processing and Synthesis → `General Technique` → Four-Step Data Synthesis | Instruction generation, instruction evolution, response generation, and response filtering. | §2.1.1; Figure 1 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → MoE Scaling Law Analysis | Fits isoFLOPs curves to choose the activated parameter count and token budget. | §2.3.1 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → MoE Scaling Law Analysis → `General Technique` → IsoFLOPs Curve Fitting | Quadratic fits over small-scale MoE runs across data sizes. | §2.3.1 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Learning Rate Scheduling | Warmup, prolonged gradual decay, and a final annealing phase. | §2.3.2 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Learning Rate Scheduling → `General Technique` → Warmup–Decay–Annealing | Anneals to one-tenth of the peak learning rate over the final 5% of tokens. | §2.3.2 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Expert-Specific Learning Rate Scaling | Separates the learning rates of shared and specialized experts. | §2.2.4 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Expert-Specific Learning Rate Scaling → `General Technique` → Batch-Size Learning-Rate Scaling | Uses ε_opt(B) for the shared expert and ε_opt(B/16) ≈ 0.31·ε_opt(B) for specialized experts. | §2.2.4 (Eq. 1) |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Long-Context Pre-Training | Extends the context from 32K to 256K in two stages of about 10B tokens each. | §2.3.3 |
| Technical | `Technical Practice` → Pre-Training → `Technical Task` → Long-Context Pre-Training → `General Technique` → RoPE Frequency Scaling | Raises the RoPE base frequency to 10⁹ during the 256K stage. | §2.3.3 |
| Technical | `Technical Practice` → Post-Training | Supervised fine-tuning followed by preference alignment on top of the pre-trained base. | §3 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → Supervised Fine-Tuning | Trains on more than 1M instructions for 3 epochs (learning rate 2e-5 to 2e-6, attention dropout 0.1, hidden dropout 0.2). | §3.1; §3.1.3 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → Supervised Fine-Tuning → `General Technique` → Instruction Extraction | Specialized extractors mine instructions and reference answers from public sources. | §3.1.2 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → Supervised Fine-Tuning → `General Technique` → Instruction Generalization | Synthesizes simple-to-complex mappings to expand and harden the instruction set. | §3.1.2 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → Supervised Fine-Tuning → `General Technique` → Instruction Balancing | Uses the labelled taxonomy to rebalance instruction types across capabilities. | §3.1.2 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → Supervised Fine-Tuning → `General Technique` → Quality Filtering | Rule-based, model-based (a 70B critic), and human filtering of instruction data. | §3.1.2 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → DPO Alignment | Single-stage direct preference optimization mixing offline and online data. | §3.2 |
| Technical | `Technical Practice` → Post-Training → `Technical Task` → DPO Alignment → `General Technique` → Online–Offline DPO | Adds an SFT loss term on chosen responses and an exponential moving average to stabilize training. | §3.2 |
| Technical | `Technical Practice` → Model Evaluation | Evaluates the base and instruct models in English and Chinese. | §4 |
| Technical | `Technical Practice` → Model Evaluation → `Technical Evaluation` → Benchmark Suite Evaluation | Runs public benchmarks with fixed few-shot settings against dense and MoE baselines. | §4.1.1; §4.2.1 |
| Technical | `Technical Practice` → Model Evaluation → `Technical Evaluation` → `Validation` → Long-Context Validation | RULER, LV-Eval, and PenguinScrolls measure fitness for extended inputs. | §4.3.1; §4.3.2 |
| Technical | `Technical Standard` → Transformer Architecture | The decoder-only Transformer of Vaswani et al. (2017) as the de facto architectural standard. | §1 |
| Technical | `Technical Blueprint` → Hunyuan-Large Code Repository | Public source code for training, inference, and evaluation. | Abstract |
| Technical | `Technical Lifecycle` → Open-Source Release | Weights, code, and the long-context benchmark are released for reuse and further development. | Abstract; §5 |

## QA

### What technical element type is Hunyuan-Large?

> `Production Virtual Technical Object`: an LLM whose operation is computational. Read together, the model, its configuration, data, practices, and release form a `Technical Element Set`, but the content map keeps them as independent technical trees rather than nesting them under one root. The report itself is the envelope, not a node of the forest.

### How does the MoE scaling law justify 52B activated parameters and 7T tokens?

> Fitting isoFLOPs curves over 10M–1B activated-parameter MoE models gives the optimal parameter law N_opt = N_c·C_min^α (N_c = 5.9×10⁻³, α = 0.5305) and the optimal data law D_opt = D_c·C_min^β (D_c = 3.2, β = 0.50). The optima are about 58.1B activated parameters and 5.6T tokens; because both curves are flat near the optimum, the team selects 52B and roughly 7T tokens.

### What problem does recycle routing solve?

> Standard top-k routing with a capacity factor discards tokens routed to overloaded experts, losing information and destabilizing training. Recycle routing reassigns those tokens at random to specialized experts still below capacity, so efficiency is kept without discarding information.

### Why does each expert get its own learning rate?

> Within a batch the shared expert processes every token while each specialized expert processes only its routed share (about 1/16). Their effective batch sizes differ, so the shared expert uses ε_opt(B) and the specialized experts use ε_opt(B/16); the ratio is about 0.31 in this configuration.

### How is the ~95% KV-cache reduction obtained?

> GQA cuts the key/value heads from 80 to 8, and CLA shares one KV cache between adjacent layers. The combined footprint is 2·n_g·d_h·l instead of the 4·n_h·d_h·l of MHA, a reduction of about 95% with little reported quality loss.

### What are the report's main limitations?

> The gains rest on compute and data at a scale that is not fully described, so independent reproduction is limited. Synthetic data dominates the corpus (1.5T of 7T tokens), carrying quality and bias risks. GQA+CLA and recycle routing trade some capacity and engineering complexity for memory and stability. "Largest open-source MoE" is time-bound and refers to total parameters, not activated ones. Most benchmark scores are self-reported or self-reproduced.

### Which results support the performance claims?

> Pre-trained: MMLU 88.4 (versus 85.2 for Llama-3.1-405B), C-Eval 91.9, MATH 69.8, HumanEval 71.4. Instruct: MMLU 89.9, MATH 77.4, MT-Bench 9.4, Arena-Hard 81.8, AlpacaEval-2.0 51.8. Long context (64–128K): RULER 89.53 versus 86.48 for Llama-3.1-70B-Instruct; PenguinScrolls overall 85.23 versus 69.37.

### Is the parameter count used for comparisons the total or the activated one?

> Activated. Table 1 lists 389B total parameters but 52B activated per token (one shared expert plus one of 16 specialized experts). Comparisons with dense models are on the activated size, which is what makes the 405B-level results at 52B the central efficiency claim.

---

## References

- Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent
[https://arxiv.org/pdf/2411.02265](https://arxiv.org/pdf/2411.02265)
