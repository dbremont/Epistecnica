# Natural Language Processing (NLP)

 : spaCy (spaCy%207f9a4a5ee64542adb2d99afac81520c3.md), Natural Language Toolkit (nltk) (Natural%20Language%20Toolkit%20(nltk)%200f764f179edd42b6a16a377fcb24b199.md)

> **Natural Language Processing (NLP)** is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language, enabling machines to understand, interpret, and generate human language.
> 

> **Linguistics** is the **scientific** study of language and its structure, including the analysis of language form, language meaning, and language in context.
> 

> **Word Embeddings (e.g., Word2Vec, GloVe) are** dense vector representations of words that capture semantic relationships, allowing ML models to understand word meanings.
> 

> **Bag of Words (BoW):** A representation of text data where the frequency of words in a document is used as features for classification or clustering.
> 

> **Term Frequency-Inverse Document Frequency (TF-IDF)** is a numerical statistic that reflects the importance of a word within a document relative to a collection of documents.
> 

> In IR documents are typically transformed into a suitable representation. Each retrieval strategy incorporates a specific model for its document representation purposes.
> 

> A Word Embedding is a representation of a word.
> 

## Índice

### **Core Tasks in NLP**

| **NLP Task** | **Description** |
| --- | --- |
| **Tokenization** | Breaking down text into smaller units like words or subwords. |
| **Part-of-speech tagging** | Identifying the grammatical categories (noun, verb, adjective, etc.) of each token. |
| **Named Entity Recognition** | Identifying and classifying named entities (people, organizations, locations, etc.) in text. |
| **Parsing** | Analyzing the syntactic structure of a sentence. |
| **Semantic Role Labeling** | Identify the roles words play in a sentence (e.g., who did what to whom). |
| **Sentiment Analysis** | Determining the sentiment expressed in a piece of text. |
| **Machine Translation** | Automatically translating text from one language to another. |
| **Text Summarization** | Creating a concise summary of a longer text. |
| **Question Answering** | Building systems that can answer questions posed in natural language. |
| **Topic Modelling** | … |
| **Dependency Parsing** | A representation that shows the grammatical structure of a sentence and the relationships between words. |
| **Constituency Parsing** | A hierarchical tree representation of the syntactic structure of a sentence. |
| **Subword Tokenization** | Splits words into smaller units, handling out-of-vocabulary words effectively. |
| **Stopwords Removal** |  |
| **Stemming/Lemmatization** |  |

## Methods

| **Category** | **Method** | **Technical Description** |
| --- | --- | --- |
| Text Preprocessing | Tokenization | Splitting text into minimal units such as words, subwords, or sentences using rule-based or learned models. |
|  | Sentence Segmentation | Identifying sentence boundaries using punctuation, abbreviations, and statistical models. |
|  | Lowercasing | Converting all characters in the text to lowercase for normalization. |
|  | Stopword Removal | Removing frequent but semantically weak words from a text using language-specific stopword lists. |
|  | Lemmatization | Mapping word forms to their morphologically and syntactically valid base forms. |
|  | Stemming | Reducing words to their root forms using rule-based heuristics without context sensitivity. |
|  | Normalization | Standardizing text format by handling punctuation, special characters, and diacritics. |
|  | Spelling Correction | Identifying and correcting misspelled words using edit distance or probabilistic models. |
|  | Noise Removal | Filtering irrelevant characters, HTML tags, emojis, and special symbols. |
| Morphological Analysis | POS Tagging | Assigning part-of-speech categories to tokens using morphological and contextual features. |
|  | Lemmatization | As above, in the context of morphosyntactic disambiguation. |
|  | Morphological Segmentation | Decomposing words into morphemes (stems, prefixes, suffixes). |
| Syntactic Analysis | Dependency Parsing | Analyzing grammatical structure and establishing syntactic relations between words using trees or graphs. |
|  | Constituency Parsing | Constructing parse trees that segment and label phrases based on grammar rules. |
|  | Chunking (Shallow Parsing) | Identifying and labeling multi-token units such as noun or verb phrases. |
| Semantic Analysis | Named Entity Recognition (NER) | Detecting and classifying entities in text (e.g., person, organization, date) using sequence labeling models. |
|  | Coreference Resolution | Determining expressions that refer to the same entity across sentences. |
|  | Word Sense Disambiguation (WSD) | Resolving lexical ambiguity by determining the correct sense of a word in context. |
|  | Semantic Role Labeling (SRL) | Identifying arguments and their semantic roles (e.g., agent, patient) for predicates. |
|  | Relation Extraction | Identifying semantic relationships between pairs of entities in a sentence. |
|  | Textual Entailment | Determining if one sentence logically follows from another. |
|  | Frame Semantics | Mapping text to conceptual structures called frames that represent situations and participants. |
|  | Semantic Parsing | Translating natural language into formal logical representations. |
| Discourse & Pragmatics | Discourse Parsing | Analyzing coherence relations between clauses and sentences (e.g., contrast, cause). |
|  | Dialogue Act Tagging | Classifying utterances into pragmatic functions (e.g., question, command, statement). |
|  | Anaphora Resolution | Resolving pronouns and noun phrases to their referents in prior context. |
|  | Topic Segmentation | Dividing a text or discourse into thematically coherent segments. |
| Vectorization | Bag-of-Words (BoW) | Representing documents as frequency vectors over a vocabulary without preserving order. |
|  | TF-IDF | Term weighting based on term frequency and inverse document frequency to reduce common word bias. |
|  | Word Embeddings (Word2Vec, GloVe) | Dense vector representations capturing semantic similarity through co-occurrence statistics. |
|  | FastText | Word embeddings enhanced with subword information for morphology-sensitive modeling. |
|  | Contextual Embeddings (BERT, ELMo) | Token representations dynamically computed from the entire input using deep contextual encoders. |
|  | Sentence Embeddings | Vector representations for entire sentences (e.g., Sentence-BERT, Universal Sentence Encoder). |
|  | Document Embeddings | Fixed-length vectors representing documents using aggregation or neural encoders. |
|  Text Classification | Sentiment Analysis | Classifying text by emotional tone using lexicons or supervised learning. |
|  | Spam Detection | Filtering unwanted or malicious text based on training examples or rule-based patterns. |
|  | Topic Classification | Assigning one or more topics from a predefined taxonomy using classification models. |
|  | Intent Detection | Identifying user intent from short queries, common in dialogue systems. |
| Sequence Modeling | Named Entity Recognition (NER) | As above, when applied as sequence labeling. |
|  | Chunking | As above, within sequential tagging frameworks. |
|  | POS Tagging | As above, applied to sequences of tokens. |
|  | Language Modeling | Predicting next token(s) given previous context using probabilistic or neural models. |
|  | Text Generation | Generating fluent, contextually appropriate text (e.g., GPT, T5). |
| Text Generation | Machine Translation | Translating text between languages using encoder-decoder or Transformer models. |
|  | Summarization | Condensing documents while preserving key information (extractive or abstractive). |
|  | Question Generation | Generating natural questions from a given text. |
|  | Dialogue Generation | Producing conversational responses, either rule-based or generative. |
| Information Retrieval | Document Retrieval | Ranking and retrieving documents relevant to a query using inverted indices or embeddings. |
|  | Passage Ranking | Ranking smaller text units (paragraphs or sentences) relevant to a search query. |
|  | Query Expansion | Reformulating queries to improve recall using synonyms, embeddings, or relevance feedback. |
|  | Semantic Search | Leveraging embeddings to retrieve semantically similar documents or passages. |
| Evaluation & Metrics | Accuracy, Precision, Recall, F1 | Standard classification metrics used to evaluate NLP models. |
|  | BLEU, ROUGE | Metrics for evaluating machine translation and summarization based on n-gram overlap. |
|  | Perplexity | Evaluation metric for language models based on inverse probability of test sequences. |
|  | Exact Match, EM | Binary score for correctness in tasks like QA and parsing. |
| Advanced Applications | Question Answering (QA) | Extracting or generating answers from documents in response to questions. |
|  | Textual Similarity | Measuring semantic closeness between text pairs using vector or symbolic methods. |
|  | Knowledge Base Construction | Populating structured databases with facts extracted from unstructured text. |
|  | Cross-lingual NLP | Applying models across different languages using multilingual embeddings or translation. |
|  | Zero-shot / Few-shot Learning | Performing tasks without (or with few) labeled examples using pretrained models. |
|  | Multimodal NLP | Combining text with other modalities (image, audio) in tasks like VQA or image captioning. |

## Semantics

> 

## Stopwords

> Stopwords are common words (like *the*, *is*, *in*) that are often removed in NLP preprocessing because they carry little semantic meaning.
> 

## Lemmatization

> **Lemmatization** is the process of mapping a surface word form to its canonical representation (*lemma*) by using morphological analysis and part-of-speech disambiguation, such that the lemma reflects the dictionary headword under contextually appropriate syntactic and inflectional constraints.
> 

### **Applications**

| Application | Description |
| --- | --- |
| **Information Retrieval** | Finding relevant information from large text corpora (e.g., search engines). |
| **Speech Recognition** | Converting spoken language into text. |
| **Text-to-Speech** | Converting text into spoken language. |
| **Chatbots and Conversational Agents** | Building systems that can interact with users in natural language. |
| **Document Classification** | Categorizing text documents into predefined categories. |
| **Spam Detection** | Identifying and filtering out unwanted or harmful messages. |
| **Language Generation** | Automatically creating coherent and contextually appropriate text (e.g., GPT-3, BERT). |

### **Challenges in NLP**

Here's a table based on the provided list:

| **Challenge** | **Description** |
| --- | --- |
| **Ambiguity** | Words and sentences can have multiple interpretations. |
| **Context and Pragmatics** | Understanding the context and implied meanings in conversations. |
| **Idioms and Colloquialisms** | Handling non-literal expressions and culturally specific phrases. |
| **Multilinguality** | Developing models that work across different languages. |
| **Resource Limitations** | The scarcity of annotated data for many languages and tasks. |
| **Ethics and Bias** | Ensuring fairness and avoiding harmful biases in NLP systems. |

### **Evaluation and Metrics**

Here's a table based on the provided list:

| **Metric** | **Description** |
| --- | --- |
| **Accuracy** | The fraction of correct predictions made by a model. |
| **Precision, Recall, and F1 Score** | Metrics for evaluating classification tasks. |
| **BLEU Score** | A metric for evaluating machine translation quality. |
| **ROUGE Score** | A metric for evaluating text summarization quality. |
| **Perplexity** | A measure of how well a language model predicts a sample. |

## Language Modelling

> **Problem**: Generate text based on a prompt or assign a probability score of pertinence to a language of a sentence.
> 

> "LLM models" typically refer to Large Language Models, advanced artificial intelligence systems trained on vast amounts of text data, capable of understanding and generating human-like text.
> 

## **Origins of the Idea**

> **Claude Shannon’s** work on language models and information theory was influenced by the earlier work of Norbert Wiener, a mathematician and cyberneticist who developed the concept of cybernetics in the 1940s. Wiener was interested in studying communication and control systems and believed that natural language could be modeled using statistical and probabilistic methods.
> 

> In particular, **Wiener** developed the idea of a **Markov process**, a mathematical model that describes a system in which the future state of the system depends only on its current state and not on its past history. Shannon used this idea to develop the Markov model of language, which describes the probability of a given word occurring in a sentence based on the preceding words.
> 

> **Shannon** also drew inspiration from the work of other researchers, such as **George Kingsley Zipf**, who had studied the **statistical distribution** of **word frequencies** in language and had observed that a small number of words are used very frequently, while a large number of words are used only rarely.
> 

> Overall, **Shannon’s** work on language models and information theory built upon the ideas and insights of several earlier researchers, and his contributions helped to establish the foundations of modern natural language processing and computational linguistics.
> 

## References

- Shannon, C. E. (1948). A Mathematical Theory of Communication. 5(1), 3–55.
- Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, Yonghui Wu. Exploring the Limits of Language Modeling. arXiv:1602.02410. [pdf]
- https://news.ycombinator.com/item?id=36027522
- Chinchilla's wild implications
[https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications](https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications)
- “Emergent” abilities in LLMs develop gradually and predictably study ([quantamagazine.org](http://quantamagazine.org/))
[https://news.ycombinator.com/item?id=39811155](https://news.ycombinator.com/item?id=39811155)
- https://www.jasonwei.net/blog/emergence
- Large Models of What? Mistaking Engineering Achievements for Human Linguistic Agency
[https://arxiv.org/abs/2407.08790](https://arxiv.org/abs/2407.08790)
- https://artificialanalysis.ai/
- https://github.com/karpathy/LLM101n
- [Natural Language Processing (NLP): What Is It & How Does it Work?](https://monkeylearn.com/natural-language-processing/)
- [The Waluigi Effect (mega-post)](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post)
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Computational linguistics](https://en.wikipedia.org/wiki/Computational_linguistics)
- [What is Temperature in NLP? (lukesalamone.github.io)](https://news.ycombinator.com/item?id=35131112)
- [A Brief Timeline of NLP from Bag of Words to the Transformer Family](https://medium.com/nlplanet/a-brief-timeline-of-nlp-from-bag-of-words-to-the-transformer-family-7caad8bbba56) The Ultimate Guide to Word Embeddings https://neptune.ai/blog/word-embeddings-guide
- 
- [‣](https://app.notion.com/p/18b598edb79080c6a6d7cc6ef32f4709?pvs=21)
