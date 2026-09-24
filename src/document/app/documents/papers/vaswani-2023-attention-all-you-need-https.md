# Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2023). Attention Is All You Need. https://arxiv.org/abs/1706.03762.


```python
@misc{vaswani2023attentionneed,
      title={Attention Is All You Need}, 
      author={Ashish Vaswani and Noam Shazeer and Niki Parmar and Jakob Uszkoreit and Llion Jones and Aidan N. Gomez and Lukasz Kaiser and Illia Polosukhin},
      year={2023},
      eprint={1706.03762},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/1706.03762}, 
}
```

## Notes

---

> The dominant **sequence transduction models** are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism.
> 

> We propose a new **simple network architecture**, the **Transformer**, based solely on **attention mechanisms**, dispensing with recurrence and convolutions entirely.
> 

> Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.
> 

Evaluations:

- WMT 2014 English-to-German Translation Task: BLEU Score: 28.4.
- WMT 2014 English-to-French Translation Task: **BLEU Score**: **41.8**.

QA:

- How **computation states** are encoded?
- What does **dependency** means in **”modelling dependencies”** in transduction models?
- What is the nature of task control in Transformer models, and how can prompt-encoded instructions such as “summarize x” induce coherent, task-specific computation through distributed, polysemantic circuits in the absence of explicit internal routing or symbolic control structures? → What *exists* is a **distributed, emergent routing mechanism encoded in the weights and attention patterns**, learned during training.
- What does intermediare ‘thinking’ steps means in Transformers? It refers to a **sequence of internal state transformations** that progressively refine representations as information flows through the network.
- Does attention has a loop to support autoregression? No—**attention itself has no loop**; autoregression is enforced by **causal masking**, while any looping occurs only in the external decoding process, not within the attention mechanism.

## Index

## Terminology

| **Term** | **Definition** |
| --- | --- |
| Induction | The process of learning a **general function or rule** from a training dataset that can then be applied to **any new, unseen instance**. The emphasis is on **generalization**. |
| Transduction | The process of predicting the **labels of a specific set of test instances** directly, using the training data as guidance, without necessarily learning a global function. The emphasis is on **specific predictions rather than general rules**. |
| Autoregressive | A modeling paradigm in which each output element is generated conditionally on previously generated outputs, forming a sequential dependency structure. The model learns a conditional distribution of the form $p(x_t∣x < t)$
, emphasizing step-by-step dependency propagation rather than simultaneous prediction. |
| Amortized Inference | An inference strategy in which the cost of solving an inference problem is **shifted to training time** by learning a parameterized inference function that maps observations directly to approximate posterior quantities, enabling **fast, reusable inference at test time** across many instances.  |
| The Geometry of Meaning | A representational framework in which semantic content is encoded as **positions, directions, and subspaces in a high-dimensional vector space**, and meaning is computed through **geometric relations** (e.g., distance, angle, projection, and transformation) rather than symbolic rules. Interpretation and inference emerge from **continuous transformations of these representations** across layers of the model. |
| Attention Mechanism | A differentiable routing and weighting mechanism that computes **context-dependent combinations of representations** by assigning dynamic importance weights to input elements based on their relevance to a query. Attention enables **selective information integration**, supports **long-range dependency modeling**, and functions as a **soft, data-dependent control structure** rather than a fixed computational pathway. |
| Model Stability | The degree to which a model’s **functional behavior and output distributions remain consistent under small perturbations** to parameters, inputs, or internal states. In large language models, stability reflects a balance between **robust, distributed representations** (insensitive to random noise) and **sensitivity along specific, task-aligned directions**, with autoregressive decoding potentially amplifying minor internal differences into divergent outputs. |
| Cross-Entropy Loss | A probabilistic loss function that measures the **discrepancy between a true target distribution and a model’s predicted distribution**, typically by penalizing the negative log-likelihood assigned to the correct outcome. It operationalizes **maximum likelihood estimation**, encouraging the model to assign high probability mass to observed data while providing well-behaved gradients for optimization in classification and language modeling tasks. |

## Introduction

> Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have are the state of the art approaches in sequence modelling and transduction problems such as language modelling and machine translation.
> 

> The encoder-decoder architecture has try to push the boundaries in language modelling.
> 

> Recurrent models typically factor computation along the symbol positions  of the input and output sequences. Aligning the positions to steps in  computation time, they generate a sequence of hidden states $h_t$, as a function of the previous hidden state $h_{t−1}$ and the input for position t.  This inherently sequential nature precludes parallelization within  training examples, which becomes critical at longer sequence lengths, as  memory constraints limit batching across examples.
> 

> **Attention mechanisms** have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences.
> 

## **Background**

> The goal of reducing sequential computation also forms the foundation of the **Extended Neural GPU**, **ByteNet** and **ConvS2S**, all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions.
> 

> **Self-attention**, sometimes called **intra-attention** is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence.
> 

> …
> 

## Model Architecture

> …
> 

![](https://arxiv.org/html/1706.03762v7/extracted/1706.03762v7/Figures/ModalNet-21.png)

> The transformer uses a encoder-decoder structure. Here the encoder maps an input sequence of symbol representations $(x_1, x_2, …, x_n)$ to a sequence of continuous representations $z  = (z_1, …, z_n)$. Given **$z$,** the decoder than generates an output sequence $(y_1, …, y_m)$ of symbols one element at a time.
> 

### **Encoder and Decoder Stacks**

> **Encoder:**  The encoder is composed of a stack of $N = 6$ identical layers.  Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected **feed-forward network**.
> 

> **Decoder:**  The decoder is composed of a stack of $N = 6$ identical layers.  It has three sub layers.
> 

### Attention

> An attention function can be described as mapping a query of a set of key-value pairs to an output, where the query, key, values, and output are all vectors. The output as a weighted sum of the values, where the weight as-signed to each value is computed by a compatibility function of the query with the corresponding key.
> 

**Applications of Attention in our Model**: 

- In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder.
- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder.
- …

### Embeddings and Softmax

> Similarly to other sequence transduction models, we use learned  embeddings to convert the input tokens and output tokens to vectors of  dimension $d_{model}$.
> 

> ….
> 

### **Positional Encoding**

> Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks.
> 

## Why Self-Attention

> …
> 

## Training

> We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs.
> 

> Hardware and Schedule:  We trained our models on one machine with 8 **NVIDIA P100 GPUs**.
> 

> **Optimizer:**  We use the Adam optimizer.
> 

> **Regularization**:  We employ three types of regularization during training “Residual Dropout’,  “Label Smoothing“, .. (where is the other)?
> 

## Results

> …
> 

![image.png](documents/papers/vaswani-2023-attention-all-you-need-https/image.png)

## Follow-Up Work

- Oren, Matanel, et al. "Transformers are multi-state rnns." *arXiv preprint arXiv:2401.06104* (2024).
- …

## References

- [‣](https://app.notion.com/p/3f35bea9676546abbc588911bfd83c41?pvs=21)
- https://arxiv.org/html/1706.03762v7
1. Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016). *Layer normalization*. arXiv preprint arXiv:1607.06450.
2. Bahdanau, D., Cho, K., & Bengio, Y. (2014). *Neural machine translation by jointly learning to align and translate*. CoRR, abs/1409.0473.
3. Britz, D., Goldie, A., Luong, M.-T., & Le, Q. V. (2017). *Massive exploration of neural machine translation architectures*. CoRR, abs/1703.03906.
4. Cheng, J., Dong, L., & Lapata, M. (2016). *Long short-term memory-networks for machine reading*. arXiv preprint arXiv:1601.06733.
5. Cho, K., van Merrienboer, B., Gulcehre, C., Bougares, F., Schwenk, H., & Bengio, Y. (2014). *Learning phrase representations using RNN encoder-decoder for statistical machine translation*. CoRR, abs/1406.1078.
6. Chollet, F. (2016). *Xception: Deep learning with depthwise separable convolutions*. arXiv preprint arXiv:1610.02357.
7. Chung, J., Gülçehre, Ç., Cho, K., & Bengio, Y. (2014). *Empirical evaluation of gated recurrent neural networks on sequence modeling*. CoRR, abs/1412.3555.
8. Dyer, C., Kuncoro, A., Ballesteros, M., & Smith, N. A. (2016). *Recurrent neural network grammars*. In *Proc. of NAACL*.
9. Gehring, J., Auli, M., Grangier, D., Yarats, D., & Dauphin, Y. N. (2017). *Convolutional sequence to sequence learning*. arXiv preprint arXiv:1705.03122v2.
10. Graves, A. (2013). *Generating sequences with recurrent neural networks*. arXiv preprint arXiv:1308.0850.
11. He, K., Zhang, X., Ren, S., & Sun, J. (2016). *Deep residual learning for image recognition*. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 770–778.
12. Hochreiter, S., Bengio, Y., Frasconi, P., & Schmidhuber, J. (2001). *Gradient flow in recurrent nets: The difficulty of learning long-term dependencies*.
13. Hochreiter, S., & Schmidhuber, J. (1997). *Long short-term memory*. *Neural computation*, 9(8), 1735–1780.
14. Huang, Z., & Harper, M. (2009). *Self-training PCFG grammars with latent annotations across languages*. In *Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing*, 832–841.
15. Jozefowicz, R., Vinyals, O., Schuster, M., Shazeer, N., & Wu, Y. (2016). *Exploring the limits of language modeling*. arXiv preprint arXiv:1602.02410.
16. Kaiser, Ł., & Bengio, S. (2016). *Can active memory replace attention?* In *Advances in Neural Information Processing Systems (NIPS)*.
17. Kaiser, Ł., & Sutskever, I. (2016). *Neural GPUs learn algorithms*. In *International Conference on Learning Representations (ICLR)*.
18. Kalchbrenner, N., Espeholt, L., Simonyan, K., van den Oord, A., Graves, A., & Kavukcuoglu, K. (2017). *Neural machine translation in linear time*. arXiv preprint arXiv:1610.10099v2.
19. Kim, Y., Denton, C., Hoang, L., & Rush, A. M. (2017). *Structured attention networks*. In *International Conference on Learning Representations (ICLR)*.
20. Kingma, D., & Ba, J. (2015). *Adam: A method for stochastic optimization*. In *ICLR*.
21. Kuchaiev, O., & Ginsburg, B. (2017). *Factorization tricks for LSTM networks*. arXiv preprint arXiv:1703.10722.
22. Lin, Z., Feng, M., dos Santos, C. N., Yu, M., Xiang, B., Zhou, B., & Bengio, Y. (2017). *A structured self-attentive sentence embedding*. arXiv preprint arXiv:1703.03130.
23. Luong, M.-T., Le, Q. V., Sutskever, I., Vinyals, O., & Kaiser, L. (2015). *Multi-task sequence to sequence learning*. arXiv preprint arXiv:1511.06114.
24. Luong, M.-T., Pham, H., & Manning, C. D. (2015). *Effective approaches to attention-based neural machine translation*. arXiv preprint arXiv:1508.04025.
25. Marcus, M. P., Marcinkiewicz, M. A., & Santorini, B. (1993). *Building a large annotated corpus of English: The Penn Treebank*. *Computational linguistics*, 19(2), 313–330.
26. McClosky, D., Charniak, E., & Johnson, M. (2006). *Effective self-training for parsing*. In *Proceedings of the Human Language Technology Conference of the NAACL, Main Conference*, 152–159.
27. Parikh, A., Täckström, O., Das, D., & Uszkoreit, J. (2016). *A decomposable attention model*. In *Empirical Methods in Natural Language Processing (EMNLP)*.
28. Paulus, R., Xiong, C., & Socher, R. (2017). *A deep reinforced model for abstractive summarization*. arXiv preprint arXiv:1705.04304.
29. Petrov, S., Barrett, L., Thibaux, R., & Klein, D. (2006). *Learning accurate, compact, and interpretable tree annotation*. In *Proceedings of the 21st International Conference on Computational Linguistics and 44th Annual Meeting of the ACL*, 433–440.
30. Press, O., & Wolf, L. (2016). *Using the output embedding to improve language models*. arXiv preprint arXiv:1608.05859.
31. Sennrich, R., Haddow, B., & Birch, A. (2015). *Neural machine translation of rare words with subword units*. arXiv preprint arXiv:1508.07909.
32. Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). *Outrageously large neural networks: The sparsely-gated mixture-of-experts layer*. arXiv preprint arXiv:1701.06538.
33. Srivastava, N., Hinton, G. E., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). *Dropout: A simple way to prevent neural networks from overfitting*. *Journal of Machine Learning Research*, 15(1), 1929–1958.
34. Sukhbaatar, S., Szlam, A., Weston, J., & Fergus, R. (2015). *End-to-end memory networks*. In *Advances in Neural Information Processing Systems (NIPS)*.
35. Sutskever, I., Vinyals, O., & Le, Q. V. (2014). *Sequence to sequence learning with neural networks*. In *Advances in Neural Information Processing Systems (NIPS)*, 3104–3112.
36. Wu, Y., Schuster, M., Chen, Z., Le, Q. V., et al. (2016). *Google’s neural machine translation system: Bridging the gap between human and machine translation*. arXiv preprint arXiv:1609.08144.
37. https://github.com/tensorflow/tensor2tensor
