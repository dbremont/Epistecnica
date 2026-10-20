---
tags: [domain]
---

# Representation Problem:  Text (String)


> How to represent a **sequence of symbols**?
> 

> A **text file** is a computer file that contains plain text data without any specific formatting or data structure.
> 

## Representation Systems (Encodings)

> **Character Encodings**: Using numerical codes to represent characters (letters, digits, symbols). Examples include ASCII, Unicode, and UTF-8.
> 

> **String Representations**: Representing sequences of characters to represent textual data.
> 

Text encoding is the process of representing text characters using a numeric code. There are many text encoding systems, each of which assigns a unique number or sequence of numbers to each character or symbol. Here are some standard text encodings:

- **ASCII**: ASCII (American Standard Code for Information Interchange) is a text encoding system that uses a 7-bit code to represent 128 characters, including letters, digits, and punctuation marks. ASCII is the most widely used text encoding system by most computer systems.
- **Unicode**: Unicode is a universal character encoding standard that represents nearly every character or symbol used in any writing system. It uses a 32-bit code to represent each character, including more than 143,000 characters.
- **UTF-8**: UTF-8 is a variable-length encoding system representing any character in the Unicode character set. Depending on its code point value, UTF-8 uses one to four bytes to represent each character. UTF-8 is the most widely used encoding system on the web.
- **UTF-16**: UTF-16 is a fixed-length encoding system that uses 16 bits to represent each character in the Unicode character set. UTF-16 is less widely used than UTF-8 but is still used in some applications.
- **ISO-8859**: ISO-8859 is a family of text encoding systems that use a fixed number of bits to represent each character. The most commonly used variants are ISO-8859-1 (Latin-1), which includes characters in Western European languages, and ISO-8859-5, which includes characters in Cyrillic languages.
- **Windows-1252**: Windows-1252 is a text encoding system similar to ISO-8859-1 but includes additional characters used in the Windows operating system.
- **Shift JIS**: Shift JIS is a text encoding system used in Japan that includes both ASCII and Japanese characters. It uses a variable-length encoding system similar to UTF-8.
- **EUC-JP**: EUC-JP is another text encoding system used in Japan. It includes both ASCII and Japanese characters and uses a fixed-length encoding system.
- **Big5**: Big5 is a text encoding system used in Taiwan that includes both ASCII and Chinese characters. Big5 uses a variable-length encoding system.
- **GB2312**: GB2312 is a text encoding system used in China that includes both ASCII and Chinese characters. GB2312 uses a fixed-length encoding system.

## ML Representations

> **Word Embeddings (e.g., Word2Vec, GloVe) are** dense vector representations of words that capture semantic relationships, allowing ML models to understand word meanings.
> 

> **Bag of Words (BoW):** A representation of text data where the frequency of words in a document is used as features for classification or clustering.
> 

> **Term Frequency-Inverse Document Frequency (TF-IDF)** is a numerical statistic that reflects the importance of a word within a document relative to a collection of documents.
> 

> A Word Embedding is a representation of a word.
> 

### **Set-theoretic Models**

> **Set-theoretic models** represent documents as sets of words or phrases. Similarities are usually derived from set-theoretic operations on those sets.
> 

Common models are: 

- Standard Boolean model
- Extended Boolean model
- Fuzzy retrieval

### **Algebraic Models**

> **Algebraic models** represent documents and queries as vectors, matrices, or tuples.
> 

The similarity of the query vector and document vector is represented as a scalar value: 

- Vector space model
- Generalized vector space model
- (Enhanced) Topic-based Vector Space Model
- Extended Boolean model
- Latent semantic indexing, a.k.a. latent semantic analysis.

### **Probabilistic Models**

> **Probabilistic models** treat the process of document retrieval as a probabilistic inference. Similarities are computed as probabilities that a document is relevant for a given query.
> 

Probabilistic theorems like the Bayes’ theorem are often used in these models.

- Binary Independence Model
- Probabilistic relevance model on which is based the okapi (BM25) relevance function
- Uncertain inference
- Language models
- Divergence-from-randomness model
- Latent Dirichlet allocation

## Metrics

| **Metric** | **Type** | **Description** | **Definition / Calculation** | **Use Cases** | **Properties / Notes** |
| --- | --- | --- | --- | --- | --- |
| **Levenshtein Distance** | Edit Distance | Minimum number of insertions, deletions, substitutions to convert one string to another | Dynamic programming counting edits | Spell checking, DNA sequence comparison | Allows substitutions; classic edit distance |
| **Damerau-Levenshtein Distance** | Edit Distance | Like Levenshtein, but also counts transpositions of adjacent chars as one edit | Extended DP with transpositions | OCR correction, typographical errors | More realistic for human typing errors |
| **Hamming Distance** | Edit Distance | Number of differing characters between two equal-length strings | Count positions with differing characters | Error detection/correction codes, fixed-length strings | Only for strings of equal length |
| **Jaro Distance** | Similarity Score | Accounts for character matches and transpositions, normalized to [0,1] | Based on matching characters and transpositions | Record linkage, duplicate detection | Designed for short strings like names |
| **Jaro-Winkler Distance** | Similarity Score | Jaro distance giving more weight to common prefix | Extension of Jaro with prefix scaling | Name matching, data deduplication | Boosts strings that match from start |
| **Cosine Similarity (with n-grams)** | Similarity | Cosine similarity computed on vectorized n-grams | Vectorize strings into n-gram frequency vectors | Document similarity, plagiarism detection | Sensitive to string length and n-gram size |
| **Longest Common Subsequence (LCS)** | Distance | Length of longest subsequence common to both strings | DP computing max matching subsequence | Bioinformatics, diff tools | Ignores non-contiguous matches |
| **Longest Common Substring** | Similarity | Length of longest contiguous substring shared | DP or suffix tree based algorithm | Plagiarism detection, substring matching | Requires contiguous match |
| **Overlap Coefficient (n-grams)** | Similarity | Ratio of shared n-grams over smaller total n-gram count | ( \frac{ | Ngrams(s_1) \cap Ngrams(s_2) | }{\min( |
| **Ratcliff-Obershelp Similarity** | Similarity | Measures similarity based on the number of matching characters in longest common subsequences | Recursive matching of common substrings | Duplicate detection, fuzzy matching | Gives intuitive similarity score |
| **Smith-Waterman** | Local Alignment | Finds best matching local subsequence with possible gaps | DP for local sequence alignment | Bioinformatics (protein/DNA matching) | Allows gaps, scores alignment quality |
| **Needleman-Wunsch** | Global Alignment | Finds best global alignment including gaps | DP for global sequence alignment | Sequence comparison in bioinformatics | Penalizes gaps, aligns entire strings |
| **Q-Gram Distance** | Distance | Counts number of non-overlapping q-length substrings differing | Count differing q-grams | Approximate string matching | Sensitive to choice of q |
| **Monge-Elkan Distance** | Similarity | Aggregates similarities of best matching substrings | Combines base metrics over substrings | Record linkage, name matching | Works well with composite strings |
| **Weighted Edit Distance** | Edit Distance | Edit distance with varying costs per operation | DP with weighted costs | OCR, speech recognition | Models domain-specific error costs |

## References

- Matthew E. Peters, et al.: [Deep contextualized word representations](https://arxiv.org/abs/1802.05365), 2018.
- Tomas Mikolov, et al.: Efficient Estimation of Word Representations in Vector Space, 2013.
- Tomas Mikolov, et al.: Distributed Representations of Words and Phrases and their Compositionality, NIPS 2013.
- Quoc V. Le and Tomas Mikolov: Distributed Representations of Sentences and Documents, 2014.
- Jeffrey Pennington, et al.: GloVe: Global Vectors for Word Representation, 2014.
- Ryan Kiros, et al.: Skip-Thought Vectors, 2015.
- Piotr Bojanowski, et al.: Enriching Word Vectors with Subword Information, 2017.
- Daniel Cer et al.: Universal Sentence Encoder, 2018.
- Thomas Hofmann: Probabilistic Latent Semantic Indexing, SIGIR 1999.
- David Blei, Andrew Y. Ng, and Michael I. Jordan: Latent Dirichlet Allocation, J. Machine Learning Research, 2003.
- Luke Vilnis, Andrew McCallum. Word Representations via Gaussian Embeddings. ICLR2015.
- Miller, G. A. (1995). WordNet: a lexical database for English. 38(11), 39–41.
- Fei Xu, Joshua Tenenbaum Word Learning as Bayesian Inference 2007. Psychological Review 114(2).
- G. Salton , A. Wong , C. S. Yang, A vector space model for automatic indexing, Communications of the ACM, v.18 n.11, p.613–620, Nov. 1975
- Turney, Peter D., and Patrick Pantel. “From frequency to meaning: Vector space models of semantics.” Journal of artificial intelligence research 37 (2010): 141-188.
- “Question Answering from Unstructured Text by Retrieval and Comprehension” by Hovy, Gerber, and Hermjakob (2002) - This paper presented an early approach to question answering that used both information retrieval and natural language processing techniques.
- “T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer” by Raffel et al. (2020) - This paper introduced the T5 (Text-to-Text Transfer Transformer) model, which has achieved state-of-the-art performance on a wide range of natural language processing tasks, including question answering.
- Blei, D. M., Ng, A. Y., Jordan, M. I. (2003). Latent dirichlet allocation. Journal of Machine Learning Research, 3(Jan), 993–1022.
- Clark, Stephen, Bob Coecke, and Mehrnoosh Sadrzadeh. “A compositional distributional model of meaning.” Proceedings of the Second Quantum Interaction Symposium (QI-2008). 2008.
- Words:
    - [Word embedding](https://www.wikiwand.com/en/Word_embedding)
    - [Embedding](https://www.wikiwand.com/en/Embedding)
- [Text File](https://en.wikipedia.org/wiki/Text_file)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [What is the difference between UTF-8 and Unicode?](https://stackoverflow.com/questions/643694/what-is-the-difference-between-utf-8-and-)
- [Unicode](https://en.wikipedia.org/wiki/Unicode)
- [Code Page](https://en.wikipedia.org/wiki/Code_page)
- [Data Structures for Text Sequences](https://www.cs.unm.edu/~crowley/papers/sds.pdf)
- [It’s not wrong that “🤦🏼‍♂️”.length == 7 (2019) (hsivonen.fi)](https://news.ycombinator.com/item?id=36159443)
- [**Computational Typography**](note.html?n=technica/computation/miscelanea/computational-typography.md)