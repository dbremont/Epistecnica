# Retrieval Model


Retrieval Model

> A **retrieval model** is a method used by a search system to decide **how relevant** each document is to a user’s query. It provides a **rule or formula** for comparing documents with the query and assigning a **score** that reflects how well each document matches what the user is looking for.
> 

> Different models use different strategies. Some use logic (like Boolean rules), others use statistics (like probabilities or term frequencies), and modern models often use machine learning or deep learning to learn what "relevance" means from past examples.
> 

The model defines:

- **How documents and queries are represented**, for example as collections of words, vectors, or features.
- **How similarity or relevance is calculated**, such as using the number of shared words, statistical likelihoods, or learned patterns from data.
- **How documents are ranked**, meaning how they are ordered from most relevant to least relevant.

| **Category** | **Model** | **Description** |
| --- | --- | --- |
| **Set-Theoretic Models** | **Boolean Model** | Documents and queries as sets of terms; uses Boolean logic (AND, OR, NOT). |
|  | **Extended Boolean Model** | Introduces soft Boolean logic with weighted terms and partial matching. |
|  | **Fuzzy Set Model** | Allows degrees of membership; manages vagueness in term matching. |
| **Algebraic Models** | **Vector Space Model (VSM)** | Represents documents/queries as vectors; uses cosine similarity. |
|  | **Latent Semantic Indexing (LSI)** | Applies SVD to reduce dimensionality and uncover latent semantics. |
|  | **Latent Dirichlet Allocation (LDA)** | A topic model; documents are mixtures of topics, which are distributions over words. |
| **Probabilistic Models** | **Binary Independence Model (BIM)** | Assumes term independence; computes probability of relevance. |
|  | **BM25 (Okapi)** | Ranking function using term frequency, document length normalization, and IDF. |
|  | **Language Modeling Approach** | Ranks documents by the probability they generate the query (e.g., Query Likelihood Model). |
| **Feature-Based Models** | **Learning to Rank (LTR)** | Supervised ML models trained to optimize ranking (e.g., RankNet, LambdaMART, XGBoost Rank). |
|  | **Feature Vector Models** | Combines various IR features (TF-IDF, click data, etc.) into a single score using regression/ML. |
| **Neural Models** | **Embedding-Based Models** | Represent queries and documents in dense vector spaces (e.g., DSSM, Word2Vec-based models). |
|  | **Transformer-Based Models** | Use contextual embeddings (e.g., BERT, RoBERTa, T5) for ranking and retrieval. |
|  | **Two-Stage Retrieval Models** | First retrieve candidates (e.g., BM25), then rerank with deep models (e.g., BERT). |
| **Graph-Based Models** | **PageRank / HITS** | Use hyperlink structure to rank documents (mainly web IR). |
|  | **Graph Neural Networks (GNNs)** | Capture document relationships via graph structure and embeddings. |
| **Hybrid Models** | **Neural + Probabilistic** | Combine classical IR signals with deep neural networks (e.g., ColBERT, DeepCT, SPLADE). |
|  | **Ensemble Models** | Combine multiple IR models (e.g., BM25 + BERT + LTR). |