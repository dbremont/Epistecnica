---
tags: [human, cognition, development, learning]
---

# Learning

> Learning is **the process of**  acquiring (training / changing your brain) to incorporate new knowledge, skills, behaviors, or understanding **through** study, experience, or teaching. Learning is a  **heterogeneous** phenomena - many **types of learning process** (not generic way to learn everything).
>

> The **skill of learning things** fast is a multiplier, it has an exponential impact in other activities. Humans process meta-cognition so they can alter and improve the learning process (also we  have R&D / Science).
>

> **Learning**: The process by which we acquire new knowledge or skills through experience, observation, or instruction,
>

## Index

## Formulation

> **Learning** is a **computationally mediated, experience-dependent modification** of an **agent’s internal representational structures** and **functional mappings (a fancy way to say operate better)**, occurring through neurobiological or symbolic substrate updates, which result in **non-random, adaptive changes** in the system’s ability to predict, infer, decide, or act within a given environment.
>

Formally, let an agent be described by a tuple $A = \langle R, M, P, U \rangle$, where:

- $R$ is a representational space (e.g., beliefs, models, schemas);
- $M$ is a set of mechanisms (e.g., neural networks, symbolic rules) for information processing;
- $P$ is a performance function $P: R \times E \rightarrow \mathbb{R}$, mapping representations and environments $E$ to performance;
- $U$ is an update function $U: R \times E \times O \rightarrow R$, where $O$ is the set of observed outcomes.

Then **learning** occurs when: $\exists \, t_1, t_2 \in \mathbb{T}, \, t_1 < t_2 \; \text{such that} \; R_{t_1} \neq R_{t_2} \; \text{and} \; P(R_{t_2}, E) > P(R_{t_1}, E)$ under the constraint that changes in $R$ are due to updates from $U$ driven by interaction with $E$, not by random noise.

## Learning Research

> Learning research is a multidisciplinary field within cognitive science, psychology, neuroscience, and education that explores how individuals acquire, process, and retain knowledge and skills. It examines cognitive mechanisms, environmental influences, and instructional methods that impact learning.
>

- [ ]  **Core Theories of Learning**
- **Behaviorism** – Learning as conditioned responses (e.g., Pavlov, Skinner).
- **Cognitivism** – Learning as information processing, memory encoding, and retrieval (e.g., Piaget, Atkinson-Shiffrin model).
- **Constructivism** – Knowledge is actively built through experiences (e.g., Vygotsky, Bruner).
- **Connectivism** – Learning in a digital age via networks and technology (e.g., Siemens, Downes).

- [ ]  **Cognitive Mechanisms of Learning**
- **Memory Systems** – Sensory, short-term, and long-term memory.
- **Attention & Cognitive Load** – How working memory capacity affects learning efficiency.
- **Metacognition** – Self-awareness and regulation of learning strategies.
- **Transfer of Learning** – How knowledge is applied across different contexts.

- [ ]  **Learning Modalities & Styles**
- **Visual, Auditory, Kinesthetic** – Individual preferences in absorbing information.
- **Experiential Learning** – Learning through reflection and experience (e.g., Kolb’s Learning Cycle).
- **Adaptive Learning** – AI-driven personalized instruction based on learner behavior.

- [ ]  **Research Methods in Learning Science**
- **Experimental Studies** – Controlled tests of learning interventions.
- **Neuroscientific Approaches** – EEG, fMRI studies on brain activity during learning.
- **Big Data & Learning Analytics** – Tracking digital learning patterns in education.

- [ ]  **Applications of Learning Research**
- **Education** – Curriculum design, adaptive learning systems.
- **Workforce Training** – Upskilling strategies, corporate e-learning.
- **Artificial Intelligence** – Machine learning models inspired by human learning.

## Learning Research Datasets

> …
>

| **Category** | **Dataset** | **Description** |
| --- | --- | --- |
| **Education & Student Learning** | **ASSISTments Dataset** | Online tutoring data tracking student problem-solving and learning progress. |
|  | **EdNet (Korea University)** | Large-scale student learning dataset from AI-powered education platforms. |
|  | **KDD Cup 2010 Educational Data** | Student interactions with an online learning system, useful for knowledge tracing research. |
|  | **Open University Learning Analytics Dataset (OULAD)** | Data from an online university, including student demographics, activities, and success rates. |
| **Memory & Cognitive Processes** | **Learning and Forgetting Dataset** | Studies memory retention over time using experimental recall data. |
|  | **PIRLS (Progress in International Reading Literacy Study)** | Large-scale dataset tracking reading comprehension in students worldwide. |
|  | **EEG Learning Dataset** | Brain activity recordings of individuals during learning tasks, useful for neurocognitive studies. |
| **Skill Development & Adaptive Learning** | **MOOC Learning Analytics Dataset** | Data from online courses (e.g., Coursera, edX) tracking student engagement and performance. |
|  | **CogSci Cognitive Skill Learning Dataset** | Experimental data on how individuals acquire complex cognitive skills over time. |
|  | **Workplace Learning & Skill Development (XAPI Data)** | Corporate learning data collected using Experience API (xAPI) for tracking employee training. |

## **Aspects of Learning**

| Aspect | Working Definition | Typical Measures |
| --- | --- | --- |
| Working Memory Load | Amount of consciously maintained information during learning | Dual-task cost, n-back accuracy |
| Attentional Focus | Selective processing of task-relevant stimuli | Eye-tracking, ERP (P3) amplitude |
| Encoding Strength | Initial trace fidelity | Immediate free-recall score |
| Consolidation Rate | Speed of hippocampal-to-cortical transfer | Sleep-spindle density, overnight gains |
| Procedural Fluency | Speed & accuracy of low-level components | RT slope, error variability |
| Transfer Distance | How far knowledge generalizes | Novel-isomorph accuracy |
| Generativity | Ability to create new examples or procedures | Divergent-production tasks |
| Causal Coherence | Explicit grasp of cause-effect links | Causal-chain diagrams, “why” probes |
| Metacognitive Accuracy | Monitoring & control of one’s own cognition | Confidence-accuracy gamma |
| Cognitive Load (NASA-TLX) | Subjective effort & resource expenditure | 0–100 composite score |
| Distraction Resilience | Performance under concurrent interference | Dual-task decrement |
| Error-Recovery Time | Latency to self-correct after mistake | Time-to-first-fix |
| Retention Slope | Forgetting rate over delay | Savings or relearning speed |
| Neural Signature | Dominant brain circuits | fMRI/EEG patterns (HC vs. PFC vs. motor cortex) |
| Acquiring Information | Process of selecting and registering new data | Initial recall accuracy, study-time allocation |
| Adaptation | Adjustments in strategy or representation with experience | Strategy-shift frequency, learning-rate change |
| Experience | Accumulated episodes and their statistical structure | Trial history entropy, pattern stability |
| Memory | Persistent internal representation of prior events | Recognition d′, recall probability |
| Behavioral Changes | Observable modifications in performance or strategy | RT delta, error-rate reduction |
| Problem-Solving | Goal-directed search through problem space | Solution latency, number of sub-goal steps |
| Retention | Long-term accessibility of learned material | Delayed recall, forgetting half-life |

## Theories of Learning

| **Category** | **Theory** | **Core Idea in One Sentence** | **Key Proponent(s) & Year** |
| --- | --- | --- | --- |
| **Behavioral** | Classical Conditioning | Organism learns to associate two stimuli so that one elicits a response previously produced only by the other. | Pavlov, 1890s |
|  | Operant Conditioning | Behavior is shaped by its consequences (reinforcement or punishment). | Skinner, 1938 |
|  | Law of Effect | Responses followed by satisfying states become more likely to recur. | Thorndike, 1905 |
|  | Drive-Reduction Theory | Learning occurs when drives are reduced by satisfying responses. | Hull, 1943 |
|  | Contiguity Theory | Any stimulus contiguous with a response becomes associated with it. | Guthrie, 1935 |
|  | Social Learning Theory | Learning occurs through observation and imitation of modeled behaviors. | Bandura, 1977 |
|  | Premack Principle | High-probability behaviors can reinforce low-probability behaviors. | Premack, 1959 |
|  | Behavioral Systems Analysis | Learning is analyzed as interactions of organism–environment systems. | Baer, Wolf & Risley, 1968 |
| **Cognitivist( Information Processing)** | Information-Processing Model | Human cognition resembles a computer: encode → store → retrieve. | Atkinson & Shiffrin, 1968 |
|  | Levels of Processing | Deeper, semantic processing yields more durable memory traces. | Craik & Lockhart, 1972 |
|  | Multi-Store Model | Memory consists of sensory, short-term, and long-term stores. | Atkinson & Shiffrin, 1968 |
|  | Working Memory Model | Limited-capacity system for temporary storage and manipulation of information. | Baddeley & Hitch, 1974 |
|  | Modal Model | Memory flow: sensory → short-term → long-term with rehearsal. | Waugh & Norman, 1965 |
|  | Sternberg Memory Scanning | Retrieval involves serial, exhaustive scanning of short-term items. | Sternberg, 1966 |
|  | Encoding Specificity | Retrieval success depends on match between encoding and retrieval cues. | Tulving & Thomson, 1973 |
|  | Transfer-Appropriate Processing | Memory is best when processing at test matches processing at study. | Morris et al., 1977 |
|  | Cognitive Load Theory | Instructional design should manage intrinsic, extraneous, and germane load. | Sweller, 1988 |
|  | Cognitive Theory of Multimedia Learning | People learn better from words + pictures when design reduces extraneous processing. | Mayer, 2001 |
| **Constructivist** | Genetic Epistemology | Cognitive development proceeds through assimilation & accommodation via stages. | Piaget, 1936 |
|  | Sociocultural Theory | Learning is mediated by tools and social interaction within the zone of proximal development. | Vygotsky, 1934 |
|  | Cognitive Apprenticeship | Expert models & scaffolds skills in authentic contexts. | Collins, Brown & Newman, 1991 |
|  | Situated Cognition | Knowing and learning are inseparable from context and activity. | Brown, Collins & Duguid, 1989 |
|  | Communities of Practice | Learning occurs via legitimate peripheral participation in social groups. | Lave & Wenger, 1991 |
|  | Radical Constructivism | Knowledge is individually constructed without objective reality. | von Glasersfeld, 1984 |
|  | Discovery Learning | Learners construct understanding through exploration & problem solving. | Bruner, 1961 |
|  | Anchored Instruction | Learning is anchored in realistic, complex problems. | CTGV, 1990 |
| **Schema & Semantic Network** | Schema Theory | Pre-existing knowledge structures guide encoding & retrieval. | Bartlett, 1932 |
|  | Semantic Network Model | Concepts are nodes; retrieval time ∝ associative path length. | Collins & Quillian, 1969 |
|  | ACT-R | Unified cognitive architecture combining symbolic and subsymbolic levels. | Anderson, 1983 |
|  | Scripts Theory | Stereotyped event sequences stored as knowledge structures. | Schank & Abelson, 1977 |
| **Dual-Coding & Multimodal** | Dual-Coding Theory | Information coded verbally and visually yields richer traces. | Paivio, 1971 |
|  | Cognitive Flexibility Theory | Advanced learning requires multiple representations of complex material. | Spiro et al., 1988 |
| **Connectionist** | Parallel Distributed Processing (PDP) | Knowledge is patterns of activation across neuron-like units. | Rumelhart & McClelland, 1986 |
|  | Backpropagation Learning Rule | Network weights adjusted by error signal propagated backward. | Rumelhart, Hinton & Williams, 1986 |
|  | Hebbian Learning | Neurons that fire together wire together. | Hebb, 1949 |
|  | Self-Organizing Maps | Competitive learning creates topology-preserving maps. | Kohonen, 1982 |
|  | Adaptive Resonance Theory (ART) | Self-regulating networks for stable category learning. | Grossberg, 1976 |
|  | Hopfield Networks | Recurrent networks that settle into energy minima for associative recall. | Hopfield, 1982 |
| **Symbolic** | General Problem Solver (GPS) | Means-ends analysis for rule-based problem solving. | Newell & Simon, 1972 |
|  | Soar Architecture | Unified cognitive architecture using production rules & chunking. | Laird, Newell & Rosenbloom, 1987 |
|  | Production System Models | Cognitive performance modeled as IF-THEN rules. | Anderson, 1976 |
|  | Explanation-Based Learning | Generalizes rules from single example + domain theory. | Mitchell et al., 1986 |
|  | Analogical Transfer | Solving new problems via mapping from prior examples. | Gentner, 1983 |
| **Bayesian (Probabilistic)** | Bayesian Brain Hypothesis | Brain computes probabilistic inferences under uncertainty. | Knill & Pouget, 2004 |
|  | Predictive Coding | Cortex minimizes prediction error via hierarchical Bayesian updates. | Friston, 2005 |
|  | Rational Analysis of Memory | Memory performance predicted by optimal Bayesian adaptation to environment. | Anderson & Schooler, 1991 |
|  | Ideal Observer Models | Optimal statistical inference models for perceptual learning. | Geisler, 1989 |
| **Embodied & Ecological** | Embodied Cognition | Mind arises from bodily interaction with environment. | Varela, Thompson & Rosch, 1991 |
|  | Enactive Approach | Cognition is enacted through action, not represented. | Maturana & Varela, 1980 |
|  | Ecological Psychology / Affordances | Learning entails perceiving action possibilities directly. | Gibson, 1979 |
|  | Dynamic Systems Theory | Behavior emerges from coupled nonlinear brain-body-environment dynamics. | Thelen & Smith, 1994 |
|  | 4E Cognition | Embodied, Embedded, Enactive, Extended cognition. | Clark, 1997 |
| **Neurobiological / Plasticity** | Synaptic Plasticity & LTP/LTD | Long-term potentiation/depression as cellular basis of memory. | Bliss & Lømo, 1973 |
|  | Spike-Timing-Dependent Plasticity (STDP) | Synaptic change depends on precise spike timing. | Markram et al., 1997 |
|  | Neurogenesis Theory | Adult hippocampal neurogenesis supports new memory formation. | Gould et al., 1999 |
|  | Systems Consolidation | Gradual reorganization from hippocampal to neocortical storage. | McClelland et al., 1995 |
|  | Homeostatic Plasticity | Synaptic scaling maintains network stability after plastic changes. | Turrigiano & Nelson, 2004 |
| **Stage / Taxonomic** | Bloom’s Taxonomy | Six hierarchical levels of cognitive learning objectives. | Bloom, 1956 |
|  | Gagné’s Conditions of Learning | Five types of learned capabilities with different internal/external conditions. | Gagné, 1965 |
|  | Stages of Skill Acquisition | Cognitive → associative → autonomous phases. | Fitts & Posner, 1967 |
|  | Dreyfus Model of Skill Development | Novice → advanced beginner → competent → proficient → expert. | Dreyfus & Dreyfus, 1980 |
|  | Kolb’s Experiential Learning Cycle | Concrete experience → reflective observation → abstract conceptualization → active experimentation. | Kolb, 1984 |
| **Metacognitive & Self-Regulation** | Metacognitive Monitoring & Control | Learners monitor accuracy and control study strategies. | Flavell, 1979 |
|  | Self-Regulated Learning (SRL) | Cyclical forethought → performance → self-reflection phases. | Zimmerman, 1989 |
|  | Self-Determination Theory | Intrinsic motivation driven by autonomy, competence, relatedness. | Deci & Ryan, 1985 |
| **Motivational & Affective** | Expectancy-Value Theory | Achievement choices depend on expectancy of success & subjective task value. | Wigfield & Eccles, 2000 |
|  | Achievement Goal Theory | Mastery vs. performance goals influence learning strategies. | Dweck, 1986 |
|  | Flow Theory | Optimal learning occurs in states of challenge-skill balance. | Csikszentmihalyi, 1990 |

## QA

### What  are the different cognitive states archieve after learning?

| State | Key Cognitive Signature | Typical Time Scale | Observable Markers |
| --- | --- | --- | --- |
| Initial Encoding | High working-memory load, fragile explicit trace | Seconds–minutes | Can reproduce only with hints; frequent errors |
| Early Consolidation | Hippocampal replay, trace stabilization | Minutes–hours | Performance drops sharply if disrupted by new tasks |
| Proceduralization / Component-Fluency | Compiled routines, reduced error rate | Hours–days | Faster RT, fewer errors, less verbal mediation |
| Explicit-to-Implicit Transition | Declarative → implicit conversion | Days | “Know how” without “know what”; difficult to verbalize steps |
| Schema Formation & Generalization | Higher-order mental models | Days–weeks | Successful transfer to isomorphic problems |
| Automaticity | Minimal attention demand, dual-task resistant | Weeks | Task runs in parallel; Stroop-like interference vanishes |
| Metacognitive Awareness | Accurate self-monitoring & study strategies | Weeks–months | Self-pacing study, error detection without feedback |
| Adaptive Expertise | Deep, conditionalized, flexible knowledge | Months–years | Innovates procedures; solves novel problems |
| Expert Intuition | Rapid pattern recognition | Years | Immediate “gut” answers; high accuracy under time pressure |
| Long-Term Retention / Permastore | Neocortical storage, hippocampal independence | Years–decades | Retrieval after years with little relearning; low forgetting slope |

### How people Consumes Information?

> Approaches and patterns by which individuals or organizations access, process, and utilize information from diverse sources and formats.
>
- **[Exposition] Linear/Feed/Personalized/Curated/Discovery Model (Stuff Get Push To Me) (Indirected) :** These models involve the delivery or discovery of information in a structured, predetermined manner (linear or feed), tailored to individual preferences (personalized), handpicked by experts (curated), or serendipitously encountered (discovery).
- **[Necesity] On-Demand/Interactive/Search-Based Model (I Look It Up) (Directed):** These models emphasize user-driven access to information, allowing users to request specific content as needed (on-demand), engage with content interactively (interactive), or actively search for data using queries (search-based).

## References

- [Human Memory](note.html?n=nature/human-memory.md)
- Keshav, S., Cheriton, D. R. (2007). How to Read a Paper.
- Leubepin, F. (2013). How to Read (and Understand) a Social Science Journal Article.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., Willingham, D. T. (2013). Improving Students’ Learning With Effective Learning Techniques.
- Burger, E. B., Starbird, M. (2012). The 5 elements of effective thinking. Princeton University Press.
- Richards, C. (2020). Boyd’s OODA loop. 5(1), 142–165.
- [Curious Inquiry and Rigorous Training](https://www.lesswrong.com/posts/RDD6dbd2xXudJLxYd/curious-inquiry-and-rigorous-training)
- [Check OK, babble-read, optimize (how I read textbooks)](https://www.lesswrong.com/posts/5hZybLna6oktgKyFK/check-ok-babble-read-optimize-how-i-read-textbooks)
- [Augmenting Human Intellect: A Conceptual Framework](https://www.dougengelbart.org/pubs/papers/scanned/Doug_Engelbart-AugmentingHumanIntellect.pdf)
- [Brandolini Law](https://www.wikiwand.com/en/Brandolini%27s_law)
- Classical conditioning: Pavlov, I. P. (1927). Conditioned reflexes: An investigation of the physiological activity of the cerebral cortex. London: Oxford University Press.
- Operant conditioning: Skinner, B. F. (1938). The behavior of organisms: An experimental analysis. New York: Appleton-Century-Crofts.
- Cognitive apprenticeship: Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), Knowing, learning, and instruction: Essays in honor of Robert Glaser (pp. 453-494). Hillsdale, NJ: Erlbaum.
- Information processing model: Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. In K. W. Spence & J. T. Spence (Eds.), The psychology of learning and motivation: Advances in research and theory (Vol. 2, pp. 89-195). New York: Academic Press.
- Constructivist models: Piaget, J. (1970). Science of education and the psychology of the child. New York: Orion Press.
- Murphy. G. Chaps. 9 and 10 in The Big Book of Concepts.
- Shanks, D. R. “Is Human Learning Rational?” The Quarterly Journal of Experimental Psychology 48A (2) (1995): 257-279.
- Berwick, R. C. “Learning From Positive-only Examples: The Subset Principle and Three Case Studies.” Machine Learning 2 (1986): 625- 645. (The section on phonology can be skipped. Just read the applications to conceptual hierarchies and syntax.)
- Bruner, Jerome S., Jacqueline J. Goodnow, and George Austin. A Study in Thinking. Somerset, NJ: Transaction Publishers, 1986. ISBN: 0887386563.
- Mitchell, Thomas M. Machine Learning. New York, NY: McGraw-Hill, 1997, chapter 2. ISBN: 0070428077.
- Feldman, J. “Minimization of Boolean Complexity in Human Concept Learning.” Nature 407 (2000): 630-633.
- Buy at MIT Press Kearns, Michael J., and Umesh V. Vasirani. An Introduction to Computational Learning Theory. Cambridge, MA: MIT Press, 1994, pp. 1-7. ISBN: 0262111934.
- Winston, P. H., ed. “Learning Structural Descriptions from Examples.” In The Psychology of Computer Vision. New York, NY: McGaw-Hill, 1975, pp. 157-209. ISBN: 0070710481.
- Gunstone, Richard. Encyclopedia of science education. Springer Reference, 2015.
- Chi, M. T. H., Bassock, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. Cognitive Science, 15, 145–182.
- Kort, B. (2009, May 10). Cognition, affect, and learning: The role of emotions in learning. Retrieved March 13, 2010, from http:// knol.google.com/k/cognition-affect-and-learning
- Ohlsson, S. (2008). Computational models of skill acquisition. In R. Sun (Ed.), The Cambridge handbook of computational psychology (pp. 359–395). New York: Cambridge University Press.
- Sinatra, G. M., & Pintrich, P. R. (Eds.). (2003). Intentional conceptual change. Mahwah: Erlbaum.
- VanLehn, K. (1996). Cognitive skill acquisition. Annual Review of Psychology, 47(1), 513–539.
- VanLehn, K. (1999). Rule-learning events in the acquisition of complex skill: An evaluation of C
- Armstrong, P. (2010). Bloom’s Taxonomy. Vanderbilt University Center for Teaching. https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/
- Sharma, Aman. “Learning: meaning, nature, types and theories of learning.” (2016).
- [Future-Proof with Learning Hacks](https://modelthinkers.com/playbook/future-proof-with-learning-hacks)
- https://www.youtube.com/watch?v=-IzWIf4dAjg

## Related

- [Space Repetition](note.html?n=human/cognitive/conceptual-model-cognition/space-repetition.md)
- [Practice](note.html?n=human/cognitive/conceptual-model-cognition/practice.md)

## Provenance

- Notion export: `Modelo/Human/Cognitive/Conceptual Model Cognition/Learning 8efe193bd36b4787b764a36a5b6d54d1.md`
