# DeepSeek-AI, :, Bi, X., Chen, D., Chen, G., Chen, S., Dai, D., Deng, C., Ding, H., Dong, K., Du, Q., Fu, Z., Gao, H., Gao, K., Gao, W., Ge, R., Guan, K., Guo, D., Guo, J., … Zou, Y. (2024). DeepSeek LLM: Scaling Open-Source Language Models with Longtermism. https://arxiv.org/abs/2401.02954.


```python
@misc{deepseekai2024deepseekllmscalingopensource,
      title={DeepSeek LLM: Scaling Open-Source Language Models with Longtermism}, 
      author={DeepSeek-AI and : and Xiao Bi and Deli Chen and Guanting Chen and Shanhuang Chen and Damai Dai and Chengqi Deng and Honghui Ding and Kai Dong and Qiushi Du and Zhe Fu and Huazuo Gao and Kaige Gao and Wenjun Gao and Ruiqi Ge and Kang Guan and Daya Guo and Jianzhong Guo and Guangbo Hao and Zhewen Hao and Ying He and Wenjie Hu and Panpan Huang and Erhang Li and Guowei Li and Jiashi Li and Yao Li and Y. K. Li and Wenfeng Liang and Fangyun Lin and A. X. Liu and Bo Liu and Wen Liu and Xiaodong Liu and Xin Liu and Yiyuan Liu and Haoyu Lu and Shanghao Lu and Fuli Luo and Shirong Ma and Xiaotao Nie and Tian Pei and Yishi Piao and Junjie Qiu and Hui Qu and Tongzheng Ren and Zehui Ren and Chong Ruan and Zhangli Sha and Zhihong Shao and Junxiao Song and Xuecheng Su and Jingxiang Sun and Yaofeng Sun and Minghui Tang and Bingxuan Wang and Peiyi Wang and Shiyu Wang and Yaohui Wang and Yongji Wang and Tong Wu and Y. Wu and Xin Xie and Zhenda Xie and Ziwei Xie and Yiliang Xiong and Hanwei Xu and R. X. Xu and Yanhong Xu and Dejian Yang and Yuxiang You and Shuiping Yu and Xingkai Yu and B. Zhang and Haowei Zhang and Lecong Zhang and Liyue Zhang and Mingchuan Zhang and Minghua Zhang and Wentao Zhang and Yichao Zhang and Chenggang Zhao and Yao Zhao and Shangyan Zhou and Shunfeng Zhou and Qihao Zhu and Yuheng Zou},
      year={2024},
      eprint={2401.02954},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2401.02954}, 
}
```

## Notes

---

> …
> 

## Index

## Introduction

> This paper studies the scaling laws; introduce a project **DeepSeek LLM**  to develop an open-source language model.
> 

> Over the past years, **LLMs** based on the decoder-only transformer architecture have become the cornerstone and pathway to achieving AGI.
> 

> **LLMs** undergo self-supervised pre-training by predicting the next word in text, gaining skills like summarization and code completion, while fine-tuning and reward modeling enhance their ability to follow user instructions.
> 

> Reader: The paper describe the previous of LLMs works.
> 

> **LLaMA**,  have focus on producing fixed-size high-quality models, often neglecting the research exploration into **LLM** scaling laws.
> 

> This work will try to explore how scaling laws of batch size and learning rate. Scaling laws of data & model; basically how to predict model performace using (model size,  data, …).
> 

> In our study we show that there is a remarkable performace different explain by the selection of training dataset; making it; very relevant.
> 

> Architecture:
> 

> Trainign: Pretraining, Supervised Fine Tuning (SFT),  and Direct Preference Optimization (DPO).
> 

## Pre-Training

> Data Processing: Deduplication, Increase Information Density in the trainig set,  filtering, mixing.
> 

> Tokenizer -  Byte-level Byte-Pair Encoding (BBPE) algorithm.
> 

> Vocabulary Size (Unique Tokens): 100,000.
> 

> How the tokenizer was train? Multilingual Corpus of 24 DB.
> 

> What was the training + architecture set up?
> 

> What was the micro-design of Deep Seek LLM?
> 

> How it handles positional encoding?
> 

> What kinds of attention mechanism uses?
> 

> Hyperparameters:  Initilization, Optimizer Parameters.
> 

> What scheduler was used?
> 

> Infrastructure: What trainig framework was used?
> 

> How flash attention works?
> 

## Scaling Laws

> History of Research on the Scaling Laws, scaling laws tries to state the relation with some input (data, compute), and the result (inference system capabilty & performance).
> 

> This paper makes explicit the hyperparameters.
> 

> What is it meant by **scalign laws of hyperparameters**?
> 

> Batch Size, Learning Rate.
> 

> What is the IsoFLOP profile approach?
> 

> What is the impact of data quality on model-data allocation strategies?
> 

> What is a model-data allocation strategy?
> 

> Estimating Optimal Model and Data Scaling → …
> 

## Alignment

> Data Distribution:  Math, Coding, Langauge, Safetey Data on Sensitive Topics.
> 

> What is the aligment pipeline? Supervised Fine-Tuning,  DPO.
> 

> What evaluation metric was used to guided the optimization? Perplexity.
> 

## Evaluation

> How much tokens were used in training?
> 

> What is the COT format stablish by WEI (2002)?
> 

> Does Instruction Following Models needs special kind of training? What data does it  need to synthetinize this models?
> 

## Conclusion, Limitation, and Future Work

## References

- https://arxiv.org/html/2401.02954
- J. Ainslie, J. Lee-Thorp, M. de Jong, Y. Zemlyanskiy, F. Lebrón, and S. Sanghai. Gqa: Training
generalized multi-query transformer models from multi-head checkpoints. arXiv preprint
arXiv:2305.13245, 2023.
- J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry,
Q. Le, et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732,
2021.
- J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge, Y. Han, F. Huang, et al. Qwen
technical report. arXiv preprint arXiv:2309.16609, 2023.
- Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi. PIQA: reasoning about physical commonsense in natural language. In The Thirty-Fourth AAAI Conference on Artificial Intelligence, AAAI  2020, The Thirty-Second Innovative Applications of Artificial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2020, New York, NY, USA, February 7-12, 2020, pages 7432–7439. AAAI Press, 2020. doi: 10.1609/aaai.v34i05.6239. URL [https://doi.org/10.1609/aaai.v34i05.6239](https://doi.org/10.1609/aaai.v34i05.6239)
- T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam,
G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child,
A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray,
B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Lan-
guage models are few-shot learners, 2020.
- M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda,
N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin,
B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet,
F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss,
A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse,
A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage,
M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and
W. Zaremba. Evaluating large language models trained on code. CoRR, abs/2107.03374, 2021.
URL [https://arxiv.org/abs/2107.03374](https://arxiv.org/abs/2107.03374)
- P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord. Think you
have solved question answering? try arc, the AI2 reasoning challenge. CoRR, abs/1803.05457,
2018. URL [http://arxiv.org/abs/1803.05457](http://arxiv.org/abs/1803.05457).
- K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek,
J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. arXiv preprint
arXiv:2110.14168, 2021.
- T. Computer. Redpajama: an open dataset for training large language models, 2023. URL
[https://github.com/togethercomputer/RedPajama-Data](https://github.com/togethercomputer/RedPajama-Data).
- Z. Dai, Z. Yang, Y. Yang, J. Carbonell, Q. V. Le, and R. Salakhutdinov. Transformer-xl: Attentive
language models beyond a fixed-length context. arXiv preprint arXiv:1901.02860, 2019.
- T. Dao. FlashAttention-2: Faster attention with better parallelism and work partitioning. 2023.
- T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Ré. FlashAttention: Fast and memory-efficient exact
attention with IO-awareness. In Advances in Neural Information Processing Systems, 2022.
- Z. Du, Y. Qian, X. Liu, M. Ding, J. Qiu, Z. Yang, and J. Tang. Glm: General language model
pretraining with autoregressive blank infilling. In Proceedings of the 60th Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), pages 320–335,
2022.
- D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner. DROP: A reading compre-
hension benchmark requiring discrete reasoning over paragraphs. In J. Burstein, C. Doran, and
T. Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, NAACL-HLT
2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers), pages 2368–
2378. Association for Computational Linguistics, 2019. doi: 10.18653/V1/N19-1246. URL
[https://doi.org/10.18653/v1/n19-1246](https://doi.org/10.18653/v1/n19-1246).
- L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite,
N. Nabeshima, et al. The Pile: An 800GB dataset of diverse text for language modeling. arXiv
preprint arXiv:2101.00027, 2020.
- Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang, M. Huang, N. Duan, and W. Chen. Tora: A tool-
integrated reasoning agent for mathematical problem solving. CoRR, abs/2309.17452, 2023.
doi: 10.48550/ARXIV.2309.17452. URL [https://doi.org/10.48550/arXiv.2309.1745](https://doi.org/10.48550/arXiv.2309.1745)
2.
- P. Goyal, P. Dollár, R. Girshick, P. Noordhuis, L. Wesolowski, A. Kyrola, A. Tulloch, Y. Jia,
and K. He. Accurate, large minibatch sgd: Training imagenet in 1 hour. arXiv preprint
arXiv:1706.02677, 2017.
- D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring
massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
- D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Mea-
suring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874,
2021.
- T. Henighan, J. Kaplan, M. Katz, M. Chen, C. Hesse, J. Jackson, H. Jun, T. B. Brown, P. Dhari-
wal, S. Gray, et al. Scaling laws for autoregressive generative modeling. arXiv preprint
arXiv:2010.14701, 2020.
- J. Hestness, S. Narang, N. Ardalani, G. Diamos, H. Jun, H. Kianinejad, M. M. A. Patwary,
Y. Yang, and Y. Zhou. Deep learning scaling is predictable, empirically. arXiv preprint
arXiv:1712.00409, 2017.
- J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. de Las Casas,
L. A. Hendricks, J. Welbl, A. Clark, T. Hennigan, E. Noland, K. Millican, G. van den Driessche,
B. Damoc, A. Guy, S. Osindero, K. Simonyan, E. Elsen, J. W. Rae, O. Vinyals, and L. Sifre.
Training compute-optimal large language models. CoRR, abs/2203.15556, 2022. doi: 10.48550
/ARXIV.2203.15556. URL [https://doi.org/10.48550/arXiv.2203.15556](https://doi.org/10.48550/arXiv.2203.15556).
- Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, J. Lei, et al. C-Eval: A
multi-level multi-discipline chinese evaluation suite for foundation models. arXiv preprint
arXiv:2305.08322, 2023
- Huggingface Team. Tokenizers: Fast state-of-the-art tokenizers optimized for research and
production, 2019. URL [https://github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers).
- F. i, M. Suzgun, M. Freitag, X. Wang, S. Srivats, S. Vosoughi, H. W. Chung, Y. Tay, S. Ruder,
D. Zhou, D. Das, and J. Wei. Language models are multilingual chain-of-thought reasoners.
In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali,
Rwanda, May 1-5, 2023. [OpenReview.net](http://openreview.net/), 2023. URL [https://openreview.net/pdf?id=](https://openreview.net/pdf?id=)
fR3wGCk-IXp.
- H. Ivison, Y. Wang, V. Pyatkin, N. Lambert, M. Peters, P. Dasigi, J. Jang, D. Wadden, N. A. Smith,
I. Beltagy, and H. Hajishirzi. Camels in a changing climate: Enhancing lm adaptation with
tulu 2. 2023.
- A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. d. l. Casas, F. Bressand,
G. Lengyel, G. Lample, L. Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.
- M. Joshi, E. Choi, D. Weld, and L. Zettlemoyer. TriviaQA: A large scale distantly supervised chal-
lenge dataset for reading comprehension. In R. Barzilay and M.-Y. Kan, editors, Proceedings of
the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers) , pages 1601–1611, Vancouver, Canada, July 2017. Association for Computational
Linguistics. doi: 10.18653/v1/P17-1147. URL [https://aclanthology.org/P17-1147](https://aclanthology.org/P17-1147).
- J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford,
J. Wu, and D. Amodei. Scaling laws for neural language models. CoRR, abs/2001.08361, 2020.
URL [https://arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361)
- V. A. Korthikanti, J. Casper, S. Lym, L. McAfee, M. Andersch, M. Shoeybi, and B. Catanzaro.
Reducing activation recomputation in large transformer models. Proceedings of Machine
Learning and Systems, 5, 2023
- T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. P. Parikh, C. Alberti, D. Epstein,
I. Polosukhin, J. Devlin, K. Lee, K. Toutanova, L. Jones, M. Kelcey, M. Chang, A. M. Dai,
J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: a benchmark for question answering
research. Trans. Assoc. Comput. Linguistics, 7:452–466, 2019. doi: 10.1162/tacl\_a\_00276.
URL [https://doi.org/10.1162/tacl_a_00276](https://doi.org/10.1162/tacl_a_00276).
- W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica.
Efficient memory management for large language model serving with pagedattention. In
Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles, 2023.
- G. Lai, Q. Xie, H. Liu, Y. Yang, and E. H. Hovy. RACE: large-scale reading comprehension
dataset from examinations. In M. Palmer, R. Hwa, and S. Riedel, editors, Proceedings of
the 2017 Conference on Empirical Methods in Natural Language Processing, EMNLP 2017,
Copenhagen, Denmark, September 9-11, 2017, pages 785–794. Association for Computational
Linguistics, 2017. doi: 10.18653/V1/D17-1082. URL [https://doi.org/10.18653/v1/d1](https://doi.org/10.18653/v1/d1)
7-1082.
- H. Li, Y. Zhang, F. Koto, Y. Yang, H. Zhao, Y. Gong, N. Duan, and T. Baldwin. CMMLU: Measur-
ing massive multitask language understanding in Chinese. arXiv preprint arXiv:2306.09212,
2023.
- X. Liu, X. Lei, S. Wang, Y. Huang, Z. Feng, B. Wen, J. Cheng, P. Ke, Y. Xu, W. L. Tam, X. Zhang,
L. Sun, H. Wang, J. Zhang, M. Huang, Y. Dong, and J. Tang. Alignbench: Benchmarking
chinese alignment of large language models. CoRR, abs/2311.18743, 2023. doi: 10.48550/A
RXIV.2311.18743. URL [https://doi.org/10.48550/arXiv.2311.18743](https://doi.org/10.48550/arXiv.2311.18743).
- I. Loshchilov and F. Hutter. Decoupled weight decay regularization. arXiv preprint
arXiv:1711.05101, 2017.
- H. Luo, Q. Sun, C. Xu, P. Zhao, J. Lou, C. Tao, X. Geng, Q. Lin, S. Chen, and D. Zhang.
Wizardmath: Empowering mathematical reasoning for large language models via reinforced
evol-instruct. arXiv preprint arXiv:2308.09583, 2023.
- S. McCandlish, J. Kaplan, D. Amodei, and O. D. Team. An empirical model of large-batch
training. arXiv preprint arXiv:1812.06162, 2018.
- T. Mihaylov, P. Clark, T. Khot, and A. Sabharwal. Can a suit of armor conduct electricity? a new
dataset for open book question answering, 2018.
- D. Narayanan, M. Shoeybi, J. Casper, P. LeGresley, M. Patwary, V. Korthikanti, D. Vainbrand,
P. Kashinkunti, J. Bernauer, B. Catanzaro, et al. Efficient large-scale language model training
on gpu clusters using megatron-lm. In Proceedings of the International Conference for High
Performance Computing, Networking, Storage and Analysis, pages 1–15, 2021.
- L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal,
K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback.
Advances in Neural Information Processing Systems, 35:27730–27744, 2022.
- G. Penedo, Q. Malartic, D. Hesslow, R. Cojocaru, A. Cappelli, H. Alobeidli, B. Pannier, E. Al-
mazrouei, and J. Launay. The refinedweb dataset for falcon llm: outperforming curated
corpora with web data, and web data only. arXiv preprint arXiv:2306.01116, 2023.
- A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, et al. Language models are
unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
- R. Rafailov, A. Sharma, E. Mitchell, S. Ermon, C. D. Manning, and C. Finn. Direct preference
optimization: Your language model is secretly a reward model. 2023.
- S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He. Zero: Memory optimizations toward training tril-
lion parameter models. In SC20: International Conference for High Performance Computing,
Networking, Storage and Analysis, pages 1–16. IEEE, 2020.
- K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd
schema challenge at scale, 2019.
- C. J. Shallue, J. Lee, J. Antognini, J. Sohl-Dickstein, R. Frostig, and G. E. Dahl. Measuring the
effects of data parallelism on neural network training. Journal of Machine Learning Research,
20(112):1–49, 2019.
- N. Shazeer. Glu variants improve transformer. arXiv preprint arXiv:2002.05202, 2020.
- M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and B. Catanzaro. Megatron-lm:
Training multi-billion parameter language models using model parallelism. arXiv preprint
arXiv:1909.08053, 2019.
- S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari, J. Casper, Z. Liu, S. Prabhumoye,
G. Zerveas, V. Korthikanti, et al. Using deepspeed and megatron to train megatron-turing nlg
530b, a large-scale generative language model. arXiv preprint arXiv:2201.11990, 2022.
- S. L. Smith, P.-J. Kindermans, C. Ying, and Q. V. Le. Don’t decay the learning rate, increase the
batch size. arXiv preprint arXiv:1711.00489, 2017.
- J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu. Roformer: Enhanced transformer with rotary
position embedding. Neurocomputing, 568:127063, 2024.
- K. Sun, D. Yu, D. Yu, and C. Cardie. Investigating prior knowledge for challenging chinese
machine reading comprehension, 2019.
- M. Suzgun, N. Scales, N. Schärli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. V. Le,
E. H. Chi, D. Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve
them. arXiv preprint arXiv:2210.09261, 2022.
- H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal,
E. Hambro, F. Azhar, et al. LLaMA: Open and efficient foundation language models. arXiv
preprint arXiv:2302.13971, 2023a.
- H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra,
P. Bhargava, S. Bhosale, D. Bikel, L. Blecher, C. Canton-Ferrer, M. Chen, G. Cucurull, D. Esiobu,
J. Fernandes, J. Fu, W. Fu, B. Fuller, C. Gao, V. Goswami, N. Goyal, A. Hartshorn, S. Hosseini,
R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, I. Kloumann, A. Korenev, P. S. Koura,
M. Lachaux, T. Lavril, J. Lee, D. Liskovich, Y. Lu, Y. Mao, X. Martinet, T. Mihaylov, P. Mishra,
I. Molybog, Y. Nie, A. Poulton, J. Reizenstein, R. Rungta, K. Saladi, A. Schelten, R. Silva, E. M.
Smith, R. Subramanian, X. E. Tan, B. Tang, R. Taylor, A. Williams, J. X. Kuan, P. Xu, Z. Yan,
I. Zarov, Y. Zhang, A. Fan, M. Kambadur, S. Narang, A. Rodriguez, R. Stojnic, S. Edunov, and
T. Scialom. Llama 2: Open foundation and fine-tuned chat models. CoRR, abs/2307.09288,
2023b. doi: 10.48550/arXiv.2307.09288. URL [https://doi.org/10.48550/arXiv.2307](https://doi.org/10.48550/arXiv.2307).
09288.
- A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polo-
sukhin. Attention is all you need. Advances in neural information processing systems, 30,
2017.
- J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. Chi, Q. V. Le, and D. Zhou.
Chain-of-thought prompting elicits reasoning in large language models. In NeurIPS, 2022.
URL [http://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf](http://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf)
4f15af0f7b31abca4-Abstract-Conference.html.
- A. Yang, B. Xiao, B. Wang, B. Zhang, C. Yin, C. Lv, D. Pan, D. Wang, D. Yan, F. Yang, F. Deng,
F. Wang, F. Liu, G. Ai, G. Dong, H. Zhao, H. Xu, H. Sun, H. Zhang, H. Liu, J. Ji, J. Xie, J. Dai,   K. Fang, L. Su, L. Song, L. Liu, L. Ru, L. Ma, M. Wang, M. Liu, M. Lin, N. Nie, P. Guo,
R. Sun, T. Zhang, T. Li, T. Li, W. Cheng, W. Chen, X. Zeng, X. Wang, X. Chen, X. Men,
X. Yu, X. Pan, Y. Shen, Y. Wang, Y. Li, Y. Jiang, Y. Gao, Y. Zhang, Z. Zhou, and Z. Wu.
Baichuan 2: Open large-scale language models. Technical report, Baichuan Inc., 2023. URL
[https://cdn.baichuan-ai.com/paper/Baichuan2-technical-report.pdf](https://cdn.baichuan-ai.com/paper/Baichuan2-technical-report.pdf)
- L. Yu, W. Jiang, H. Shi, J. Yu, Z. Liu, Y. Zhang, J. T. Kwok, Z. Li, A. Weller, and W. Liu.
Metamath: Bootstrap your own mathematical questions for large language models. CoRR,
abs/2309.12284, 2023. doi: 10.48550/ARXIV.2309.12284. URL [https://doi.org/10.485](https://doi.org/10.485)
50/arXiv.2309.12284.
- R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish
your sentence? In A. Korhonen, D. R. Traum, and L. Màrquez, editors, Proceedings of the 57th
Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July
28- August 2, 2019, Volume 1: Long Papers, pages 4791–4800. Association for Computational
Linguistics, 2019. doi: 10.18653/v1/p19-1472. URL [https://doi.org/10.18653/v1/p1](https://doi.org/10.18653/v1/p1)
9-1472.
- B. Zhang and R. Sennrich. Root mean square layer normalization. Advances in Neural
Information Processing Systems, 32, 2019.
- G. Zhang, L. Li, Z. Nado, J. Martens, S. Sachdeva, G. Dahl, C. Shallue, and R. B. Grosse. Which
algorithmic choices matter at which batch sizes? insights from a noisy quadratic model.
Advances in neural information processing systems, 32, 2019.
- L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing,
H. Zhang, J. E. Gonzalez, and I. Stoica. Judging llm-as-a-judge with mt-bench and chatbot
arena. 2023.
- W. Zhong, R. Cui, Y. Guo, Y. Liang, S. Lu, Y. Wang, A. Saied, W. Chen, and N. Duan. AGIEval: A
human-centric benchmark for evaluating foundation models. CoRR, abs/2304.06364, 2023.
doi: 10.48550/arXiv.2304.06364. URL [https://doi.org/10.48550/arXiv.2304.06364](https://doi.org/10.48550/arXiv.2304.06364).
- J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou. Instruction-following
evaluation for large language models. arXiv preprint arXiv:2311.07911, 2023.
- https://en.wikipedia.org/wiki/Hyperparameter_optimization
- https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets
