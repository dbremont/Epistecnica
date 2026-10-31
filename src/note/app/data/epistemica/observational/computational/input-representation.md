---
tags: [representation]
---

# Input Representation

 : Token (Token%20188c0f5171ec80969e5cd5aba2791b5a.md), Word2Vec (Word2Vec%20bbe322ecec944034bbacd8390b1f6a11.md), One-Hot Encoding (One-Hot%20Encoding%2021f59295bd214d48ae125e1ccb3c47cf.md), Bag of Words (BoW) (Bag%20of%20Words%20(BoW)%20ba1571fd0fd24f28b9bb3654f029991f.md), Data (Data%20264c0f5171ec80bb9fb2fa8e2e3a82a9.md), Representation (Representation%20358c0f5171ec805494e3c15b57740a48.md)

> An **input representation** is the structured form in which raw data is presented to a machine learning model so that it can be processed effectively. It defines how the relevant information from the raw input—such as text, images, audio, or tabular data—is encoded, transformed, or embedded into a mathematical or computational format (e.g., vectors, matrices, or tensors) that the model can interpret and learn from.
> 

> **Encoding** is the process of transforming data from a discrete or symbolic domain (e.g., categorical variables, text tokens) into a numerical vector space representation that preserves relevant structural or statistical properties, enabling its compatibility with the algebraic operations and optimization procedures used in machine learning models.
> 

## Technique Space

> Category Representation Technique:  A **class of techniques** that share common principles or approaches for transforming raw input into representations suitable for machine learning.
> 

> **Representation Technique** – The name of the technique.
> 

> Representation Mechanism: How it transforms or encodes the raw input into a usable form for ML.
> 

| **Category** | **Technique** | **Description** | **Purpose** |
| --- | --- | --- | --- |
| **Categorical** | **One-Hot Encoding** | Binary vector representing categories; only one “hot” value per category. | Preserves category uniqueness; interpretable by ML models. |
|  | **Label Encoding** | Maps categories to integer values. | Provides simple numerical representation; may exploit ordinal relationships. |
|  | **Feature Hashing** | Maps high-cardinality categorical features into fixed-size vectors using a hash function. | Reduces dimensionality and memory usage for large datasets. |
| **Numerical** | **Feature Scaling / Normalization** | Rescales numeric values to common ranges (0–1, z-score). | Prevents features with large scales from dominating; improves optimization. |
|  | **Numerical Binning / Discretization** | Converts continuous values into discrete intervals. | Simplifies patterns; reduces noise; useful for models preferring categorical inputs. |
|  | Log Transformation |  |  |
|  | Power Transformation (Box-Cox, Yeo-Johnson) |  |  |
|  | Binarization (Thresholding) |  |  |
|  | Quantile Transformation (Rank Scaling) |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **Text** | **Bag-of-Words (BoW)** | Counts or indicates presence of words in a document. | Converts text into numeric form for classification or retrieval. |
|  | **TF-IDF** | Weighted version of BoW emphasizing rare but important words. | Highlights distinguishing words; reduces impact of common words. |
|  | **Word Embeddings (Word2Vec, GloVe, BERT)** | Dense vectors capturing semantic and syntactic meaning of words. | Captures deeper relationships for NLP tasks; enables similarity measures. |
|  | **Sequence Encoding / Positional Embeddings** | Represents ordered sequences (text, time series) as vectors. | Preserves temporal or sequential dependencies; used in RNNs, Transformers. |
| **Image (Vision)** | **Convolutional Feature Maps** | Outputs of convolution layers capturing spatial patterns. | Hierarchical visual features for classification, detection, and recognition. |
| **Signal (Time-Series)** | **Wavelet Transform** | Converts signals to frequency or multi-resolution domain. | Reveals periodicities, patterns, and trends not visible in raw data. |
|  | **Smoothing** |  |  |
|  | **Moving Average** |  |  |
| **Graph (Network)** | **Graph Embeddings (Node2Vec, GraphSAGE)** | Maps graph nodes to continuous vectors preserving structure. | Enables ML models to process graph-structured data effectively. |
| **Dimensionality Reduction** | **Principal Component Analysis (PCA)** | Projects data onto orthogonal components preserving variance. | Compresses data; reduces noise and computational cost. |
| **Learned** | **Autoencoder Embeddings** | Compresses input into latent vectors via neural network bottleneck. | Learns compact, meaningful representations for reconstruction or downstream tasks. |
|  | **Learned Embeddings for Categorical Features** | Embedding layers in neural networks for high-cardinality categorical variables. | Captures latent relationships beyond one-hot encoding. |
|  |  |  |  |

### Log Transformation

> 

### Power Transformation (Box-Cox, Yeo-Johnson)

> 

## Latent Space Representation

> 

> A **latent space representation system** in machine learning refers to a compressed, abstract feature space where data points are transformed to facilitate tasks such as dimensionality reduction, feature learning, and generative modeling. In this space, complex relationships in high-dimensional data are captured in a lower-dimensional form, enabling algorithms to more efficiently learn patterns and make predictions.
> 

> Using a latent space enables more efficient high-dimensional data processing and facilitates tasks such as data compression, image generation, and feature extraction.
> 

> In machine learning and artificial intelligence, a latent space is a mathematical representation of data that captures that data's underlying structure or patterns. It is a low-dimensional space where high-dimensional data is mapped into a compressed and more meaningful form.
> 

> Latent spaces are commonly used in deep learning models, particularly in generative models such as Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs). In these models, the latent space represents the distribution of a particular dataset, which can then be used to generate new data similar to the original dataset.
> 

**Algorithms to create a latent space**:

- **Principal Component Analysis (PCA)**: PCA is a technique for dimensionality reduction that identifies the most essential features in a dataset and creates a lower-dimensional representation of that data. It can create a latent space for high-dimensional data such as images.
- **Autoencoders**: Autoencoders are a type of neural network that can be trained to encode high-dimensional data into a lower-dimensional latent space. They are commonly used in generative models such as Variational Autoencoders (VAEs).
- **t-SNE**: t-SNE (t-distributed stochastic neighbor embedding) is a non-linear dimensionality reduction technique that is particularly effective for visualizing high-dimensional data. It can create a latent space for data visualization and clustering.
- **UMAP**: UMAP (Uniform Manifold Approximation and Projection) is a relatively new dimensionality reduction technique similar to t-SNE but more scalable and can handle larger datasets. It can also create a latent space for visualization and clustering.

## Positional Encoding

> 

> Adds information about the position of words in a sequence, often used in transformer models.
> 

> Machine translation, sequence modeling in deep learning
> 

## Text

> Text embedding models map discrete linguistic units (words, phrases, sentences, documents) into continuous, dense, real-valued vectors in $\mathbb{R}^d$, preserving semantic, syntactic, and pragmatic properties of language.
> 

> Formally, an embedding model defines a function: $f: \mathcal{T} \rightarrow \mathbb{R}^d$ where $\mathcal{T}$ is a space of textual units (e.g., tokens, sentences), and $d \ll |\mathcal{V}|$, with $\mathcal{V}$ being the vocabulary.
> 

## **Challenges**

- **Polysemy:** Disambiguation in static models.
- **Alignment Across Languages or Modalities:** Multilingual and multimodal embeddings.
- **Geometry of Embedding Spaces:** Non-Euclidean structures (e.g., hyperbolic embeddings) for hierarchical data.
- **Bias and Fairness:** Encoded biases from training corpora propagate into embeddings.

## References

- [HiFloat8 (FP8)](https://app.notion.com/p/HiFloat8-FP8-137c0f5171ec80b4ac37f67325737f94?pvs=21)
- [What is a latent space?](https://stats.stackexchange.com/questions/442352/what-is-a-latent-space)
- [Latent Space](https://www.wikiwand.com/en/Latent_space)
- [**Embedding**](embedding.md).
- https://www.youtube.com/watch?v=xCzmOyB5J1o
- https://www.youtube.com/watch?v=Oy7Jv8DxzTU
- https://www.youtube.com/watch?v=ulD7IsecPbU
- [https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard)]
- [https://projector.tensorflow.org/](https://projector.tensorflow.org/)
- https://platform.openai.com/tokenizer
- https://gptforwork.com/tools/tokenizer
- [https://huggingface.co/spaces/Xenova/the-tokenizer-playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground)
- https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
