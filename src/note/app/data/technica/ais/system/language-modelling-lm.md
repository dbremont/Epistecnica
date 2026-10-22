# Language Modelling (LM)

 : System Prompt (System%20Prompt%2020dc0f5171ec805d95a4e48257c4436f.md), Retrieval-Augmented Generation (RAG) (Retrieval-Augmented%20Generation%20(RAG)%2013bc0f5171ec80e2bf8bfa0d05235b9a.md)

> 

QA:

- Why are large language models described as autoregressive?  LLMs (Large Language Models) are called **autoregressive** because they generate text **one token at a time**, where each token is **predicted based on the previous ones**.
- What is a retriever in the transformer architecture?
- How to use transformers to inject domain knowledge into a given model?

- How  inference time compute ("thinking")  works?
- How CoT works?

Reasoning

- https://www.science.org/doi/10.1126/science.adw5211

## 🧩 **Model Category**

| Type | Description | Instace(s) |
| --- | --- | --- |
| **n-gram Models** | Statistical models predicting next word from n-1 words | Katz, Kneser-Ney smoothing |
| **Neural Language Models (NNLMs)** | Use neural networks to learn word probabilities | Bengio et al. (2003) |
| **Recurrent Neural Networks (RNNs)** | Sequential models with hidden states | LSTM, GRU |
| **Transformer-based Models** | Use self-attention for long-range dependencies | GPT, BERT, T5 |
| **Hybrid Models** | Combine RNNs with attention or convolution | Transformer-XL, Conformer |

## 🔍 **Training Objectives**

| Objective | Description | Common Use |
| --- | --- | --- |
| **Causal Language Modeling (CLM)** | Predict next token given previous tokens (unidirectional) | GPT, autoregressive text generation |
| **Masked Language Modeling (MLM)** | Predict masked tokens within sequence (bidirectional) | BERT, RoBERTa |
| **Sequence-to-Sequence (Seq2Seq)** | Generate output sequence from input sequence | T5, BART |
| **Permuted Language Modeling** | Predict tokens in random order | XLNet |
| **Denoising Objectives** | Reconstruct original from corrupted input | BART, T5 |
| **Contrastive Learning** | Learn representations by distinguishing similar/dissimilar pairs | SimCSE, CLIP |

## 🎯 **Model Types by Purpose**

| Type | Description | Examples |
| --- | --- | --- |
| **Decoder-only Models** | Autoregressive, generate text token-by-token | GPT series, GPT-Neo |
| **Encoder-only Models** | Produce fixed representations for input | BERT, RoBERTa |
| **Encoder-Decoder Models** | Input-to-output mapping models | T5, BART |
| **Multimodal Models** | Process text + other modalities (images, audio) | CLIP, Flamingo, GPT-4 multimodal |

## ⚙️ **Training Paradigms**

| Paradigm | Description | Examples |
| --- | --- | --- |
| **Supervised Pretraining** | Large corpus, standard LM objectives | Most large LLMs |
| **Self-Supervised Learning** | Train without explicit labels from raw data | MLM, CLM, autoencoding |
| **Instruction Fine-Tuning** | Train on instruction–response pairs | InstructGPT, FLAN-T5 |
| **Reinforcement Learning with Human Feedback (RLHF)** | Align model outputs to human preferences | ChatGPT, GPT-4 |

## 🧠 **Model Size and Scaling**

| Scale | Description | Examples |
| --- | --- | --- |
| **Small (millions of params)** | Lightweight models for efficiency | DistilGPT, TinyBERT |
| **Medium (hundreds M)** | Balance accuracy and resource use | GPT-2 small/medium |
| **Large (billions)** | State-of-the-art performance, resource-heavy | GPT-3, PaLM, LLaMA |
| **Extra Large (tens-hundreds billions)** | Cutting-edge SOTA, requires massive compute | GPT-4, Megatron-Turing NLG |

## Transformer Based Large Language Model (LLM): Key Aspects

| **Aspect** | **Description** |
| --- | --- |
| **Input Processing** | **Tokenization** and **encoding** of raw input text into numerical vectors (tokens). |
| **Embedding Layer** | Maps tokens into continuous vector space (embeddings) to capture semantic meaning. |
| **Positional Encoding** | Adds positional information to embeddings so the model can infer word order and structure. |
| **Transformer Layers** | Core building blocks consisting of multi-head self-attention and feed-forward networks. |
| • Self-Attention | Allows the model to attend to relevant tokens across the entire input sequence. |
| • Feed-Forward Network | Processes token representations to extract higher-level features and patterns. |
| • Layer Normalization & Residual Connections | Stabilizes training and allows deeper stacking of layers. |
| **Output Head** | Converts the processed representations back into token probabilities (via a linear + softmax layer). |
| **Decoding Strategy** | Generates output tokens, either autoregressively (one at a time) or via other sampling methods. |
| **Training Objective** | Usually next-token prediction (causal language modeling), optimized via gradient descent. |
| **Context Handling** | Mechanisms to manage input length and context window, including segmenting or truncation. |
| **Model Parameters** | Weights distributed across all transformer layers and embeddings that encode learned knowledge. |
| **Attention Mechanism** | Key innovation enabling contextual understanding over variable-length input sequences. |
| **Layer Stacking** | Model depth controls capacity to represent complex language features through multiple transformer layers. |
| **Context Window** | Maximum tokens model can consider simultaneously (e.g., 4K, 16K tokens), influencing memory and coherence. |
| **Training Dataset** | Large-scale corpora of text (and optionally code, images, or other modalities) used for training. |

## QA

### Is the entire context window, including the prompt, fed into the LLM's neural network at every inference step? How does it work? Why limits if any? Is the limit built into the architecture itself, or is it caused by something else?

> **Note:** A neural network architecture can be designed to **accept variable-length** or even theoretically unbounded input sequences.
> 

> At inference time, **the entire context window** is fed into the model **at every step** of generation.
> 

This includes:

- The **prompt** (system prompt + user input + previous dialogue, if applicable),
- Plus any **generated tokens so far** (in autoregressive models),
- Up to the **maximum token limit** of the context window.

🧠 Role of Context Window

- The **context window** is the **maximum number of tokens** (prompt + generated) the model can **"see"** at once.
- If you exceed it:
    - **Oldest tokens are dropped** (usually from the start of the prompt).
    - Or, **prompt compression/summarization** techniques may be used in advanced systems (e.g., Anthropic's Claude with 200K+ token context).

Limits on the Context Window in LLMs:

| **Constraint** | **Description** | **Impact** |
| --- | --- | --- |
| **Attention Complexity** | Self-attention has **O(n²)** time and memory complexity with sequence length `n`. | Slows down and increases memory use for long inputs. |
| **Hardware Memory** | GPUs/TPUs have finite memory capacity. Large context windows use more VRAM. | Hard cap on how much input the model can handle. |
| **Training Cost** | Longer contexts require more compute, data, and careful optimization during training. | Makes large-context models expensive to train. |
| **Tokenization Overhead** | Some content (like code, tables) tokenizes into far more tokens than expected. | Context budget is consumed quickly. |
| **Diminishing Returns** | Longer context often brings marginal benefit after a point. | Wasted compute for little performance gain. |

Is the limit built into the architecture itself, or is it caused by something else?

| Source of Limitation | Explanation |
| --- | --- |
| **Model Architecture** | Transformers use self-attention over a fixed-length input. The model is trained with positional embeddings for a maximum number of tokens (e.g., 2k, 4k, 128k). Exceeding this breaks expected positional patterns. |
| **Memory and Compute Constraints** | Attention has **O(n²)** time and memory complexity, where *n* is the number of tokens. Larger windows require significantly more GPU memory and computation. |
| **Training Time Constraints** | During training, the context length is fixed. The model doesn’t learn to handle inputs beyond this. |
| **Tokenizer and Input Format** | Tokenizers break text into fixed-size chunks. The LLM must handle these chunks in their full encoded form, making longer contexts technically infeasible beyond the trained max length. |

To overcome context inefficiencies:

- **Transformers with memory** (e.g., **RMT**, **MoE with caching**)
- **Stateful generation** (e.g., **FlashAttention**, **Key-Value Caching**)

## **Tokenizer**

What is a Token?

- A **token** is a piece of text mapped to a unique integer ID.
- Depending on the tokenizer, a token may represent:
    - A **character** (rare in modern LLMs).
    - A **subword** (most common; e.g., "un", "believ", "able").
    - A **whole word** (in word-level models, but less efficient).
    - Even **punctuation, whitespace, or special symbols**.

| Tokenizer | Used in | Core Idea | Advantages | Drawbacks |
| --- | --- | --- | --- | --- |
| **WordPiece** | BERT, DistilBERT | Start with chars → iteratively merge common word fragments; uses a likelihood-based criterion. | Good handling of rare words (via subwords); relatively compact vocab. | Segmentation can feel unintuitive (“##ing” etc.); less efficient than byte-level. |
| **Byte Pair Encoding (BPE)** | GPT-2, RoBERTa, CLIP | Start with chars → merge the most frequent pairs into new tokens. | Simple, effective; compact vocab; widely adopted. | Vocabulary depends on training data; may split foreign/rare words oddly. |
| **Byte-level BPE** | GPT-3, GPT-4, LLaMA | Same as BPE, but operates on raw bytes (Unicode-safe). | Universal (no “unknown” tokens); handles emojis/code/foreign text. | Longer token sequences compared to pure subword schemes. |
| **Unigram LM** | T5, SentencePiece models | Probabilistic model of subword segmentations; selects the highest likelihood tokenization. | Flexible, often yields more natural segmentations; compact vocab. | More complex training; slower tokenization vs. BPE. |
| **Word-level** | Early RNN/LSTM models | Each unique word = token. | Simple; intuitive mapping. | Huge vocab; no handling of unseen words (OOV problem). |
| **Character-level** | Some small/experimental LMs | Each character = token. | Universal coverage; no OOV. | Very long sequences; inefficient. |
| **SentencePiece (framework)** | T5, ALBERT | Framework that can implement BPE or Unigram LM without pre-tokenization (handles raw text including spaces). | Language-agnostic; robust to whitespace/punctuation. | Adds preprocessing complexity; choices affect performance. |

QA:

- What is the impact of the tokenizer in the learning system?
- …

See:

- https://tiktokenizer.vercel.app/
- https://en.wikipedia.org/wiki/Byte-pair_encoding
- https://huggingface.co/learn/llm-course/en/chapter6/5
- https://github.com/karpathy/minbpe?tab=readme-ov-file
- https://gptforwork.com/tools/tokenizer
- https://platform.openai.com/tokenizer
- https://tiktokenizer.vercel.app/
- [https://huggingface.co/spaces/Xenova/the-tokenizer-playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground)

### Are LLM world modellers?

https://news.ycombinator.com/item?id=44854518

## References]

- https://bbycroft.net/llm
- https://en.wikipedia.org/wiki/Language_model
- [A hacker’s guide to language models [video] (youtube.com)](https://news.ycombinator.com/item?id=37631089)
- https://jalammar.github.io/hidden-states/
- https://jalammar.github.io/explaining-transformers/
- https://www.cs.princeton.edu/courses/archive/spring11/cos126/assignments/markov.html
- Markov Model of Natural Language
[https://www.cs.princeton.edu/courses/archive/spr05/cos126/assignments/markov.html](https://www.cs.princeton.edu/courses/archive/spr05/cos126/assignments/markov.html)
- https://www.reddit.com/r/programming/comments/1aghjgm/markov_chains_are_the_original_language_models/
- Large language models use a surprisingly simple mechanism to retrieve some stored knowledge
[https://news.mit.edu/2024/large-language-models-use-surprisingly-simple-mechanism-retrieve-stored-knowledge-0325](https://news.mit.edu/2024/large-language-models-use-surprisingly-simple-mechanism-retrieve-stored-knowledge-0325)
- LLM Design & Implementation [https://github.com/sangmichaelxie/cs324_p2](https://github.com/sangmichaelxie/cs324_p2)
- https://en.wikipedia.org/wiki/Word_n-gram_language_model
- https://zilliz.com/learn/introduction-to-natural-language-processing-tokens-ngrams-bag-of-words-models
- https://www.youtube.com/watch?v=flXrLGPY3SU&t=710s
- [‣](https://app.notion.com/p/14d598edb7908053a851ed7814c92c3d?pvs=21)
- https://www.youtube.com/watch?v=yBL7J0kgldU&list=WL&index=4&t=1031s
- ‣[https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)‣

Small Language Model:

- https://minigpt-4.github.io/
- https://huggingface.co/docs/transformers/en/model_doc/mobilebert
- https://arxiv.org/abs/2410.20011
- [Phi-3 Technical Report: Highly Capable Language Model Locally on Your Phone](https://arxiv.org/pdf/2404.14219)
- …

World Modelling:

- https://news.ycombinator.com/item?id=34474043
- https://thegradient.pub/othello/

Evaluation

- https://lmarena.ai/

- [ ]  https://news.ycombinator.com/item?id=43931366
- [ ]  [https://drive.google.com/file/d/1cUxKspEXgQ64s4OFEw0kabf_qNauOPiH/view](https://drive.google.com/file/d/1cUxKspEXgQ64s4OFEw0kabf_qNauOPiH/view) → LLM Knowledge Test.
- [ ]  https://news.ycombinator.com/item?id=45110311
