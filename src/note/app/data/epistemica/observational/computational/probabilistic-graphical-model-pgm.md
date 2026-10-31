---
tags: [distribution, probability]
---

# Probabilistic Graphical Model (PGM)


> Aka. **`Structured Probabilistic Model`**: Capture complex probability distribution.
> 

> A probabilistic graphical model (PGM) is a framework for representing and reasoning about the probabilistic relationships among a set of random variables. It provides a visual structure that encodes the joint probability distribution of the variables, capturing both their dependencies and independencies.
> 

## Definition

> There are two main components of a probabilistic graphical model:
> 
1. **Nodes**: Each node in the graph represents a random variable, which can be discrete or continuous.
2. **Edges**: The edges between the nodes represent probabilistic dependencies between the variables. An edge from node A to node B indicates that A directly influences B in terms of conditional probability.

## Representation

> 
- **Joint Probability Distribution**: A PGM encodes a joint probability distribution over all the random variables it represents. The graph structure helps break down this distribution into smaller, more manageable conditional probabilities.
- **Conditional Independence**: PGMs make explicit the conditional independencies between variables. For example, if two variables are conditionally independent given a third, the graph structure will show no direct path (edge) between those two variables once the third variable is known. This is a powerful way to simplify complex systems.
- **Probabilistic Inference**: Once the model is constructed, PGMs allow for efficient inference. You can compute the probability of certain variables given observed data, make predictions, and perform decision-making under uncertainty.

## Evaluation

> 

## Optimization

> 

## Uses

> 

A **probabilistic graphical model (PGM)** can be used to represent various types of data that involve uncertainty and probabilistic dependencies. Here are some examples of the types of data that can be represented by PGMs:

1. **Medical Data**:

- **Diagnosis**: A PGM can model the relationships between various symptoms, diseases, test results, and patient history. For ecfxample, it can represent how certain diseases are related to specific symptoms, and how test results (e.g., blood pressure, glucose levels) influence the likelihood of disease.
- **Treatment Outcomes**: It can model the effect of different treatments on patient recovery, considering factors like medication, lifestyle changes, and genetic predisposition.
- **Genomic Data**: PGMs can be used to represent gene expression levels and the probabilistic relationships between different genes, diseases, and environmental factors.

2. **Sensor Data**:

- **IoT Systems**: In systems with sensors (e.g., smart homes, industrial IoT), PGMs can represent the probabilistic relationships between sensor readings, environmental conditions, and system states. For example, sensor data might indicate whether a machine is malfunctioning based on various environmental conditions like temperature, vibration, etc.
- **Time-Series Data**: PGMs can represent dependencies between time-dependent variables, such as stock prices, weather conditions, or sensor measurements over time.

3. **Natural Language Processing (NLP)**:

- **Language Models**: In NLP, PGMs can be used to represent the probabilistic relationships between words or phrases in a sentence, capturing the dependencies of word choices based on context. This is commonly seen in **hidden Markov models (HMMs)** or **conditional random fields (CRFs)** for tasks like named entity recognition (NER) or part-of-speech tagging.
- **Topic Modeling**: In text data, PGMs like **Latent Dirichlet Allocation (LDA)** are used to model the relationship between documents and topics, where each document is assumed to be a mixture of topics, and each topic is represented as a distribution over words.

4. **Financial Data**:

- **Risk Analysis**: PGMs can model the relationships between different financial variables (e.g., asset prices, interest rates, market indicators) to assess risk and make investment decisions.
- **Credit Scoring**: In credit scoring models, PGMs can represent the probabilistic relationship between a person’s financial history, current financial status, and the likelihood of loan default.

5. **E-commerce and Recommendation Systems**:

- **User Preferences**: PGMs can represent the relationships between users, products, ratings, and preferences. For example, a recommendation system can use a PGM to infer a user’s likelihood of purchasing a particular product based on previous behavior and the behavior of similar users.
- **Click-Through Rate (CTR) Prediction**: In online advertising, PGMs can model the relationship between user attributes, advertisement characteristics, and the likelihood of a user clicking on an ad.

6. **Social Network Data**:

- **Influence Models**: PGMs can represent how individuals in a social network influence each other’s behavior or opinions. For instance, they can model the spread of information or the likelihood of someone adopting a new product based on their connections.
- **Community Detection**: PGMs can be used to infer latent communities within a network, where users are more likely to be influenced by or interact with other users in the same community.

7. **Computer Vision**:

- **Object Recognition**: In computer vision, PGMs can model the relationships between different features of images (e.g., color, texture, shape) and the objects being detected. **Markov random fields (MRFs)** are often used in image segmentation tasks.
- **Pose Estimation**: PGMs can represent the probabilistic relationships between body parts and their positions in the image, useful in human pose estimation or action recognition.

8. **Robotics and Autonomous Systems**:

- **Localization and Mapping**: PGMs are used in **SLAM (Simultaneous Localization and Mapping)**, where robots estimate their position relative to a map while updating the map with sensory data. The dependencies between sensor measurements and the robot’s position are represented probabilistically.
- **Planning**: PGMs can model the uncertainty in the robot’s environment and the consequences of actions, allowing it to make decisions under uncertainty.

9. **Climate and Environmental Data**:

- **Weather Prediction**: PGMs can represent the relationships between meteorological variables (e.g., temperature, humidity, wind speed) and weather conditions, allowing for probabilistic forecasting.
- **Environmental Modeling**: In ecological studies, PGMs can model the impact of factors such as pollution levels, habitat conditions, and animal migration patterns on ecosystem health.

10. **Supply Chain and Operations**:

- **Inventory Management**: PGMs can represent the probabilistic relationships between supply chain variables such as demand, stock levels, and delivery times, aiding in decision-making processes like restocking and inventory optimization.
- **Production Systems**: In manufacturing, PGMs can model dependencies between machine performance, raw materials, and production outcomes to optimize operations.

11. **Game Theory and Strategy**:

- **Strategic Decision Making**: PGMs can model the probabilistic relationships between different strategies in a game, considering the uncertainty of opponent moves and outcomes.
- **Multi-Agent Systems**: In multi-agent systems, PGMs can represent the uncertain relationships between agents, actions, and states in competitive or cooperative environments.

12. **Supply and Demand Systems**:

- **Market Predictions**: PGMs can be used to model how supply, demand, and pricing are interrelated under uncertain conditions, aiding in market forecasting and decision-making.

13. **Human Behavior Modeling**:

- **Psychological Studies**: PGMs can model the relationships between different psychological factors (e.g., stress, motivation, mood) and behaviors (e.g., decision-making, health outcomes).

## Taxonomy

| **Graphical Model** | **Description** | **Applications** |
| --- | --- | --- |
| **Bayesian Networks** | Directed acyclic graphs (DAGs) representing conditional dependencies among variables. | Risk analysis, medical diagnosis, AI systems |
| **Markov Random Fields (MRFs)** | Undirected graphical models represent dependencies between variables without explicit direction. | Image processing, spatial statistics |
| **Conditional Random Fields (CRFs)** | A discriminative model for structured prediction, where the conditional probabilities are modeled. | Natural language processing, computer vision |
| **Factor Graphs** | Bipartite graphs where nodes represent variables and factors, showing how variables are related. | Error correction, probabilistic inference |
| **Hidden Markov Models (HMMs)** | Models with hidden states and observable outputs are represented as a type of probabilistic graphical model. | Speech recognition, sequence analysis |
| **Dynamic Bayesian Networks (DBNs)** | Extensions of Bayesian networks that model temporal processes with dependencies over time. | Time-series analysis, speech recognition |
| **Graphical Models for Latent Variables** | Models, where latent (hidden) variables are used to explain observed data, are often visualized with graphs. | Clustering, dimensionality reduction |
| **Influence Diagrams** | Graphical representations combining decision-making elements with probabilistic relationships. | Decision analysis, strategic planning |
| **Relational Graphical Models** | Extend graphical models to handle structured and relational data, such as entities and their relations. | Social network analysis, knowledge graphs |
| **Gaussian Graphical Models** | Models where variables are jointly Gaussian and the precision matrix represents dependencies. | Financial modeling, bioinformatics |
| **Graphical Models for Temporal Dependencies** | Represent sequences or time-series data with dependencies across time steps. | Forecasting, sequence prediction |
| **Kalman filters** | … | … |
| **Ising models** | … | … |

## References

- [Graphical model](https://en.wikipedia.org/wiki/Graphical_model)
- [Markov random field](https://en.wikipedia.org/wiki/Markov_random_field)
- [Probabilistic Graphical Models](https://ermongroup.github.io/cs228-notes/)
- https://pgmpy.org/index.html#
