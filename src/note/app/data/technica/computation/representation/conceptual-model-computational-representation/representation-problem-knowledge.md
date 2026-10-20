---
tags: [domain]
---

# Representation Problem: Knowledge


> Domain: Knowledge representation refers to the process of representing knowledge in a formal and structured way that can be understood and processed by computer systems. It involves capturing information about objects, concepts, relationships, and rules in a domain-specific or generalizable format. The purpose of knowledge representation is to enable reasoning, inference, and manipulation of knowledge within a computational system.
> 

> Symbolic encoing of propositions (believed by some agent).
> 

> **Knowledge Representation Systems**: Representing knowledge and information using formal languages like predicate logic, ontologies, or frames.
> 

> **Knowledge Graphs (KGs)** have emerged as a compelling abstraction for organizing the world’s structured knowledge, and as a way to integrate information extracted from multiple data sources. Knowledge graphs have started to play a central role in representing the information extracted using natural language processing and computer vision. Domain knowledge expressed in KGs is being input into machine learning models to produce better predictions.
> 

> Our goals in this blog post are to (a) explain the basic terminology, concepts, and usage of KGs, (b) highlight recent applications of KGs that have led to a surge in their popularity, and (c) situate KGs in the overall landscape of AI. This blog post is a good starting point before reading a more extensive survey or following research seminars on this topic.
> 

## Representation Systems

- **Logical Representation**: Logic-based representation uses formal logical languages, such as propositional logic, first-order logic, or description logic, to represent knowledge. It involves defining a set of logical statements, rules, and axioms that capture the relationships and constraints within the domain.
- **Semantic Networks**: Semantic networks represent knowledge using nodes representing concepts or objects and edges representing relationships between them. These networks can be hierarchical, allowing for the organization of knowledge into taxonomies or ontologies, or they can be more loosely structured.
- **Frames**: The frame-based representation organizes knowledge using a structured template called a “frame.” Frames consist of slots representing attributes or properties of an object or concept, and values associated with those slots.
- **Ontologies**: Ontologies provide a formal and explicit specification of the concepts and relationships within a domain. They define a set of classes, properties, and instances that represent the knowledge in a structured and standardized way. Ontologies are often represented using ontology languages like RDF (Resource Description Framework) or OWL (Web Ontology Language).
- **Conceptual Graphs**: Conceptual graphs combine elements of semantic networks and logic-based representation. They use nodes to represent concepts and relationships and incorporate logical formalisms to express constraints and rules.
- **Knowledge Graphs**: A knowledge graph is a structured representation of knowledge that captures relationships between entities, concepts, and facts in a specific domain. It consists of interconnected nodes (representing entities) and edges (representing relationships) that provide a rich semantic framework for organizing and understanding information. Knowledge graphs enable efficient data integration, semantic search, and reasoning, making them valuable for various applications, such as question-answering, recommendation systems, and knowledge-based AI.
- **Rule-based Systems**: Rule-based systems represent knowledge as if-then rules, where the “if” part represents conditions or patterns, and the “then” part represents actions or conclusions. These systems use rule engines to match and apply rules based on the available knowledge.
- **Symbolic Representations**: Symbolic representations use symbols and rules to encode knowledge and perform logical reasoning. This approach is used in expert systems and knowledge-based reasoning.
- **Probabilistic Representations**: Knowledge is expressed as probabilities or statistical distributions in probabilistic representations. This is common in Bayesian networks and probabilistic graphical models.
- **Vector Embeddings**: Knowledge can be represented as dense vector embeddings, where semantically similar items are closer together in the vector space. This approach is used in word, sentence, and graph embeddings.
- **Neural Network Representations**: Neural networks and deep learning models learn knowledge representations automatically from data. Hidden layers in neural networks capture abstract features and patterns from the input data.

## Representations System

- **Knowledge Graph Embeddings (KGEs): …**
- **Logical Knowledge Representation: …**
- **Graph Neural Networks (GNNs): …**
- **Temporal Knowledge Graph: …**

## References

- Tools
    - [Vadalog](https://en.wikipedia.org/wiki/Vadalog)
    - [Cayley](https://cayley.io/)
- [Google Knowledge Graph](https://en.wikipedia.org/wiki/Google_Knowledge_Graph)
- [Knowledge graph](https://en.wikipedia.org/wiki/Knowledge_graph)
- [CS 520 Knowledge Graphs](https://web.stanford.edu/~vinayc/kg/2021/index-2021.html)
- [An Introduction to Knowledge Graphs](http://ai.stanford.edu/blog/introduction-to-knowledge-graphs/)
- [Introducing the Knowledge Graph: things, not strings](https://www.blog.google/products/search/introducing-knowledge-graph-things-not/)
- [awesome-knowledge-graph](https://github.com/husthuke/awesome-knowledge-graph)
- ‣Graph Machine Learning in the Era of Large Language Models (LLMs)
[https://arxiv.org/abs/2404.14928](https://arxiv.org/abs/2404.14928)
- Nolting, Soeren, Zhen Han, and Volker Tresp. “Modeling the evolution of temporal knowledge graphs with uncertainty.” arXiv preprint arXiv:2301.04977 (2023).
- Mo, Chong, et al. “Survey on Temporal Knowledge Graph.” 2021 IEEE Sixth International Conference on Data Science in Cyberspace (DSC). IEEE, 2021.
- Bellomarini, Luigi; Fayzrakhmanov, Ruslan R.; Gottlob, Georg; Kravchenko, Andrey; Laurenza, Eleonora; Nenov, Yavor; Reissfelder, Stéphane; Sallinger, Emanuel; Sherkhonov, Evgeny; Vahdati, Sahar; Wu, Lianlong (2022-04-01). “Data science with Vadalog: Knowledge Graphs with machine learning and reasoning in practice”. Future Generation Computer Systems. 129: 407–422. doi:10.1016/j.future.2021.10.021. ISSN 0167-739X. S2CID 243885469.
- Bellomarini, Luigi; Sallinger, Emanuel; Gottlob, Georg (2018-05-01). “The Vadalog system: datalog-based reasoning for knowledge graphs”. Proceedings of the VLDB Endowment. 11 (9): 975–987. doi:10.14778/3213880.3213888. ISSN 2150-8097. S2CID 49300741.
- Bellomarini, Luigi; Fakhoury, Daniele; Gottlob, Georg; Sallinger, Emanuel (2019). “Knowledge Graphs and Enterprise AI: The Promise of an Enabling Technology”. 2019 IEEE 35th International Conference on Data Engineering (ICDE). Macao, Macao: IEEE: 26–37. doi:10.1109/ICDE.2019.00011. ISBN 978-1-5386-7474-1. S2CID 174818761.
- ellomarini, Luigi; Benedetto, Davide; Gottlob, Georg; Sallinger, Emanuel (2022-03-01). “Vadalog: A modern architecture for automated reasoning with large knowledge graphs”. Information Systems. 105: 101528. doi:10.1016/j.is.2020.101528. ISSN 0306-4379. S2CID 218964910.
- Ben Hixon, Peter Clark, Hannaneh Hajishirzi. Learning Knowledge Graphs for Question Answering through Conversational Dialog. NAACL2015. [pdf]
- A review of relational machine learning for knowledge graphs. Proceedings of the IEEE 2015. Nickel, Maximilian and Murphy, Kevin and Tresp, Volker and Gabrilovich, Evgeniy. [Paper]
- Zhu, Cunchao, et al. “Learning from history: Modeling temporal knowledge graphs with sequential copy-generation networks.” Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 35. No. 5. 2021.
- [Ask HN: Any open access alternatives to Google’s knowledge graph?](https://news.ycombinator.com/item?id=13359138)
- A Survey on Knowledge Graphs: Representation, Acquisition and Applications. IEEE TNNLS 2021. Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Marttinen, Philip S. Yu. [Paper]
- Knowledge Graphs. Preprint 2020. Aidan Hogan, Eva Blomqvist, Michael Cochez, Claudia d’Amato, Gerard de Melo, Claudio Gutierrez, José Emilio Labra Gayo, Sabrina Kirrane, Sebastian Neumaier, Axel Polleres, Roberto Navigli, Axel-Cyrille Ngonga Ngomo, Sabbir M. Rashid, Anisa Rula, Lukas Schmelzeisen, Juan Sequeda, Steffen Staab, Antoine Zimmermann. [Paper]
- Davis, Randall, Howard Shrobe, and Peter Szolovits. “What is a knowledge representation?.” AI magazine 14.1 (1993): 17-17.
- Bobrow, Daniel G., and Terry Winograd. “An overview of KRL, a knowledge representation language.” Cognitive science 1.1 (1977): 3-46.
- [CS 227: Knowledge Representation and Reasoning](http://web.stanford.edu/class/cs227/)
- [neo4j](https://neo4j.com/)
- Knowledge Representation Learning: A Quantitative Review. Preprint 2018. Lin, Yankai and Han, Xu and Xie, Ruobing and Liu, Zhiyuan and Sun, Maosong. [Paper]
- Knowledge graph embedding: A survey of approaches and applications. TKDE 2017. Wang, Quan and Mao, Zhendong and Wang, Bin and Guo, Li. [Paper]
- Knowledge graph refinement: A survey of approaches and evaluation methods. Semantic Web 2017. Paulheim, Heiko. [Paper]
- [Constructing Knowledge through Geometry: Ramon Llull’s Figures in Ars Magna, 1305](https://socks-studio.com/2021/11/03/constructing-knowledge-through-geometry-ramon-llulls-figures-in-ars-magna-1305/)
- Davis, Randall, Howard Shrobe, and Peter Szolovits. “What is a knowledge representation?.” AI magazine 14.1 (1993): 17-17.
- Bobrow, Daniel G., and Terry Winograd. “An overview of KRL, a knowledge representation language.” Cognitive science 1.1 (1977): 3-46.
- [CS 227: Knowledge Representation and Reasoning](http://web.stanford.edu/class/cs227/)
- [neo4j](https://neo4j.com/)
- Knowledge Representation Learning: A Quantitative Review. Preprint 2018. Lin, Yankai and Han, Xu and Xie, Ruobing and Liu, Zhiyuan and Sun, Maosong. [Paper]
- Knowledge graph embedding: A survey of approaches and applications. TKDE 2017. Wang, Quan and Mao, Zhendong and Wang, Bin and Guo, Li. [Paper]
- Knowledge graph refinement: A survey of approaches and evaluation methods. Semantic Web 2017. Paulheim, Heiko. [Paper]
- [Constructing Knowledge through Geometry: Ramon Llull’s Figures in Ars Magna, 1305](https://socks-studio.com/2021/11/03/constructing-knowledge-through-geometry-ramon-llulls-figures-in-ars-magna-1305/)

## Representation

> 

| **Category** | **Method** | **Description** | **Example Use Case** |
| --- | --- | --- | --- |
| **Symbolic Representations** | **Logic-Based** | Uses formal logic (e.g., First-Order Logic) to represent knowledge. | Automated reasoning, expert systems. |
|  | **Rule-Based Systems** | Knowledge is stored as IF-THEN rules. | Production systems, decision support. |
|  | **Semantic Networks** | Represents knowledge as a graph of interconnected concepts. | Conceptual modeling, knowledge graphs. |
|  | **Frames** | Uses structured templates to store entity attributes. | Natural language understanding, AI planning. |
|  | **Ontology-Based** | Hierarchical representation of domain-specific concepts. | Semantic web, linked data, biomedical informatics. |
| **Subsymbolic Representations** | **Neural Networks** | Learns implicit knowledge through weighted connections. | Deep learning, image and speech recognition. |
|  | **Embeddings** | Represents entities as continuous vectors in high-dimensional space. | NLP (word embeddings), recommender systems. |
| **Graph-Based Methods** | **Knowledge Graphs** | A structured graph with entities as nodes and relationships as edges. | Search engines, question answering, fraud detection. |
|  | **Bayesian Networks** | Probabilistic graphical models representing dependencies. | Decision-making under uncertainty, risk assessment. |
| **Mathematical & Statistical** | **Markov Logic Networks (MLN)** | Combines logic with probabilities for uncertain reasoning. | AI-driven decision-making, NLP. |
|  | **Tensor-Based Representation** | Uses multi-dimensional arrays to encode structured data. | Signal processing, AI knowledge bases. |
| **Linguistic Approaches** | **Latent Semantic Analysis (LSA)** | Captures relationships between words in a document corpus. | Topic modeling, document retrieval. |
|  | **Transformers (e.g., BERT, GPT)** | Contextual representation of text for deep NLP. | Chatbots, translation, summarization. |