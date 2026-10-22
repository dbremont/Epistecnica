# LLM System Modelling

> Let’s model LLMs.
> 

> What to do not to fall in love with effective models of **LLMs** behavior?
> 

> One impressive element about LLMs is that they can perform tasks like summarization remarkably well, despite the fact that we do not yet fully understand why these capabilities emerge so effectively. This phenomenon may provide valuable insight into human cognition and certain cognitive processes, making it, quite frankly, deeply interesting.
> 

> There have a be a simple way to explain llms - inner mechanisms - they should be a locus of meaning - and dynamics a simple thing.
> 

DOING:

- How stable are capabitlies? That is ounce a capablity has been shown in a  llm - does similar task - that exercise the capalbity - will produce the right result?
- What is the orignie of the capblity? Data, Optimization Dynamics, Inference Dynamics - a combination of the them.
- let say - we have thousand of specilized slm - how do we route task to them?  so having a thousand small moden - is not better than one giant model probably?
- How to think computation superposition? One Layer Many Computations?
    - One can understand compositionality - as  conditional computation application on state -
    - (How to induced compression) Compression → Abstraction
    - This seems to make clear - that llms - are powerful imitators - not innovators - take for example can this systems - generate let’s quanting mechanims - from XIX century physics -probably not - because it’s an abductive jump - not  a hill climign  - combinatorial thing.
    - Streamly good ad induction - streamly weak ad abduction?
    - Is question making more akin to induction, or abduction?
    - Note: **Compositionality** → combination.
    - **Compositionality = compression + conditional computation**
    - Imitator Innovation (Combination) vs Oringal Innovation (Abduction)
    - I think this sort of sheear light - into the inabilty of llm - to learn from descriptiosn - they need to be train - on task direclty - so you just don’t give it a book about let say - x- and extped to peak those skills - they need to be t rain - on the task samples.
        - Also it sheear light on the stream learning ineeficinecy
    - Is question making more **abduction or induction**?
    - So in order to list the capbilties of a llm - one need to look at th edat - but is even mroe ientresting - because predictin ght enovel combinations - yilend sophisitcate comopsed computatonis -is not easy either - this is way this systems - are crazy genious.
    - How can this go with that llms can learn programming lets say from a spec? Without previous enrourmous amoudn of training? (Weak Generalization)
- Why should gradient descent produce representations that become increasingly task-specific and concrete?
- Can use the idea of self-organizing to understand llm’s
- Twofundamental problems with llm (**Production Technical Element Set  (PTES)**):
    - Inability  to use - what is ‘data’ ( a book of programming) into programming skills? Skills and capabilities emerges - trhougth  - process liek data (example of performing  the task)
    - Online learning (how to change the wheigt  - online) - This is not that hard - just expensive - as it right know.
        - There is also one share model for all.
- If data is the key driver of progress, what kinds of new data are the frontier models released in 2026 being trained on that the leading models from 2025 were not? It seems that the **2025 models had already ingested a large fraction of the high-quality publicly** available text on the Internet. So where does the additional training signal come from? Are the gains primarily due to new types of data (e.g., synthetic data, reasoning traces, multimodal data, interactive data), or are they mostly the result of improvements in training methods, architectures, and post-training?
    - I would argue that every major category of training data used by frontier models in 2026 was already available in 2025. Web pages, books, code, scientific papers, images, videos, multimodal data, reasoning traces, and even synthetic data all existed before the latest generation of models. If there are no fundamentally new categories of training data, what explains the improvements in capability? Are the gains primarily due to better data curation, higher-quality synthetic data, improved training algorithms, reinforcement learning, architectural innovations, inference-time reasoning, or something else?
    - Can bad data downgroud model performance? How sensitive is the model to **bad training data**?
    - Fact: Paris is the capital of France.
    - **Process**:  Given these premises, derive the conclusion step by step.
    - It seems that **Process -** oriented data - is the key.
    - Which are the limits of this?  All this problems seems to be solved with **continual learning**.
    - Let’s take and advanced model- let’s take its based model - can the based model behave the same as the adavnced model - given that the cot of the advanced model is ust in the prmopt?
        - Genarlly no, models do omre tha nthey can tell they do - so called j-scape - or latent computation.
    - Speakign of this - can you post train a smal model 27b - or something in  a narrow complex task - let say write article - like hackdr news types - to surpass trrillosn param models - [https://xcancel.com/i/article/2075619939780874440](https://xcancel.com/i/article/2075619939780874440)
        - How is tiis possible? is the ianblity - to learn procedure (task pability) from let;s say non task oriented - and descriptiosn - that big?
        
        ![image.png](../assets/hy3-announcement-tweet.png)
        
- …
- A **logistic regression probe** is a technique used in machine learning and mechanistic interpretability to determine whether specific concepts, traits, or information are encoded in the internal representations (hidden states or activations) of a complex neural network.
- How to explain the inner dialog? How to think about it from the te chnical and eneingerng iperstive - fronm the poitn of view of a llm designer?
- What is the context needed to guarantee the correctness of the continuation? Is training data key - in order to some capability to emerge? What is the relations of the number of layers and the **abstract representations** that the **network is able to learn**?
- (Type of Question) What explain the emergence of certain capability?
- Is quality tokens reality important?
- What explains the performance of current llms systems?  In a table of techniques, mechanisms? Is intermediate tokens generation (”reasoning”) so important?
    - I have taken reasoning traces of advanced GLM Model 5.2, and send them to 4.7 and  the result was vastly better.
    - …
- (Generalization) How to think about this  - a model that was ‘learn’ to generate code - presuamalby has master procedural — pattern - but is unable to apply that to certain problems like the nested logical evaluations, etc? How to think about generalization in LLMs Models?
- One of the deepest and most interesting behaviors of llms sems to be - that they know when to stop.
- What explain let say ‘x behavior - capacity’? How structure the explanation? Technique, Mechanism, Ingredient (Data, etc).
- How to explain goal - identification, and validation?
- How can the idea of constraint propagation helps to to understand this?
- Which have this scatfold spect (data, training, etc), and the product (llm blob)? What capabitlies should we expect? How to predict capabitilies?
    - **What kinds continuations can I trigger?** Is the role of prompts - or even the internal dialog of the model - will always be decieviced? Will the models learn - how to ask question? Will they learn - to learn - what they don’t know? What it’s missing? Is this even teachable? Is this habilty will ever going to emerged?
    - Model vs Capability Potential
    - A Modle of 1b what cpabitlies can emerged?
    - 0.1 B What kinds of capabilities can emerged?
    - Can to much promp brake a llm? Can a promp induced vastly differnt behavior in a non speciry dimensio? Take for example i have a specification for web app, for a bank- will the design an aesthetics field autmatically like  a bank app? What explaisn this, the internal dialog, etc?
- Limitations of statistical models - take the case of the term emergence - the term - tries to serve a function - type a set of behavior in the real world - a sophisticated human being - weill probably even question the term - but a trainign llm will be induced to used and mimic the term effectuvly - not to futher develop a depper understanding and even rejecting and improving the and finding a better solution - to the problem that the term is trying to solved?
    - Can a good llm orchestractor (hardness) fix this?
    - Is this kinds of recursion - fixable?
- 

## Index

- What is an **Activation Pattern**? What is ‘**Representation Space’**?
    - activation space = geometry
    - features = directions in that geometry
    - tokens = points in that space
    - **“Activation”** = alignment with directions that trigger downstream computation patterns
        - An activation - is just the output of  the layer - but  let’s say `a activation` to be certain **dynamic - or process**.
    - meaning is not stored as objects, but as **geometry that biases future computation**
    - Case:
        - “Company feature” = learned direction in representation space
        - “Activation” = projection onto that direction
        - “Tesla activates company features” = Tesla’s representation aligns with those directions strongly enough to influence downstream generation
- What do we actually mean by a **concept in a transformer**? ….
- What is composition at the mechanistic level? Can this compositions be always useful?  How  this composition emerge? Are they latent?
    - An state can be extreamly rich - and superpose - and activate rich dynamics - which is condition and superpose (it can do many things at one pass) - based on the input state.
    - The richness of the state get’s refined throught the layers - and - recurrence, etc.
    - The richness of the state - and it’s transformation types - etc - are not known - this extreamly  basic ‘capabilities’ - and the chain of them - presumebly from less abstract - to most abstract - in network - is where the deep magic comes from  - but when you have this computational graph of trillions of nodes, and connections - making sense of this - is almost  a task that requires some great strategy - because the  problem is almost intractable.
- Is the role of CoT to enrich the representation, to better constraint - and facciliate the mapping to a output representaiton?
- Which are the level of abstract notions - That I can use to think about LLMs? …
    - ….
- How to think deeply about composition of operators?
    - Superposition
    - Composition = interacting circuits writing/reading shared state
    - What is a transformation pattern?
    - Transformation pattern = a recurrent, parameterized mapping from one hidden-state configuration to another, triggered under certain contexts and implemented by a distributed set of weights (attention heads + MLPs).
- Is translation a universal way on how to think bout llm? Input → Output.
    - Structured manifold translation
    - …
- How to think about the LLM in capacity - to reason deeply and find incosistencies - in let say representation?
    - It’s like a dedicated idiot - know everyfind - but questiosn nothing.
    - Plausible continuatio rather than: Rigorous adversarial verification
- How to think about compositionaly  …?
- Take a Set of Type Prompts - And See If your model can explain - how the llm handle them?
    - Question - Answer,
    - Problem Solving,
    - Question Formulation,
    - Instruction,
    - How to **think about terms**? How to think about tokens? Can tokens **forms concepts**? How to think about the **interaction of terms**?
    - How to to think about the meaning of the term model, representation? What does it mean to have a representation let say - of the concept of  a function?
    - How to think about representation and representation mapping?
- One impressive element about LLMs is that they can perform tasks like summarization remarkably well, despite the fact that we do not yet fully understand why these capabilities emerge so effectively. This phenomenon may provide valuable insight into human cognition and certain cognitive processes, making it, quite frankly, deeply interesting.
- How to think about few-shot behavior in llm?
- What to do not to fall in love with effective models of **LLMs behavior**?
- Which are the limits of **representation spaces induces by text**?
- How to used cognitive science ideas - effectly and does not imposed them naivly to the llms study?
- How does LLMs know when to stop?
- How many weights - parameters - does a LLM MLP layers ussualy have?
- Knowledge (??? Is this even a good term here ???)
    - Is there is a notion of knowledge quantifation in thie systems?
    - What do we even mean when we say a - llm knows x?
    - Which are the methods used to ‘extract knowledge’?
- Is the notion ‘ a llm - understand the spec (as a it’s able to have a representation of it) to generate a plausible continuation useful?
- Does the attention mechanism - add tokens - that is enrich the tokens - or just masasage the state in order to add information …?
    - **Attention does not add new tokens.**
    - It **re-weights and mixes information from existing tokens into the current token’s state** , effectively *enriching its representation.*
- How to think deeply about the **idea of representation**?
- How to reason - about llms conceptual combinations - using the translation and manifold approach?
    - How **many firms** does `Elon` have? This requires combination - in order to answer this?
    - 'How many firms does Elon have? This requires combination - in order to answer this?' what is teh operators tha tinduces the dynamis here - mnay firms? or waht- that induces the posuble target representation space?
    - How is the information about elon musk store?
    - How composition between operators works?
    - How to think abotu even the dynamics- is the represntation space already there or just the result of the **operators combinations**?
    - How to think about this operators?
- LLMs seems to have different representations mechanisms or schemes in some layers - and maybe compatible between others.
- How to thinka bout the roles of  the layers?
    - What dropping layers can do?
- How to conduct experimetns - how to gather data?
- Which are the notions used in mechanismlaty interpretabilty to model llms?

**Guiding questions:**

- **How should an LLM (Transformer) be modeled conceptually and technically?**
- **How should we think about LLMs, their capabilities, limitations, and task-specific performance?**
    - **Induced Dynamics:** An LLM can be understood as a high-dimensional dynamical system whose behavior is conditioned by prompts, internal representations, and learned token-transition structures.
    - **Model-Based Interpretation:** LLMs learn deep, compressed, and richly structured latent models from large-scale text corpora; prompts function as computational operators that activate, constrain, or traverse specific regions of this learned representational space.
    - Simulation Based Interrpetation: …
    - Representation Transductor: …
    - Dynamical Systems + Manifold Translation: ….
    - Context-Conditioned Representational Dynamical System
    - Probabilistic Semantic Manifold Translator
    - **Capability Estimation:** Performance on a given task depends on:
        - Representational overlap between training distributions and target task structure
        - Prompt-induced computational alignment
        - Reasoning depth requirements
        - Context length and memory demands
        - Precision requirements
        - Tool augmentation or external system integration
    - **Predictive Framework:** LLM performance can be estimated by analyzing:
        - Task abstraction complexity
        - Distributional familiarity
        - Required symbolic rigor
        - Multi-step dependency depth
        - Error tolerance
        - Need for grounded external knowledge
- **How can we formalize LLMs as computational systems?**
    - Probabilistic sequence models
    - Approximate world-model constructors
    - Neural inference engines
    - Context-sensitive symbolic simulators
    - Emergent meta-learning systems
- **How should we characterize their operational boundaries?**
    - Statistical generalization
    - Pattern induction
    - Approximate reasoning
    - Contextual synthesis
    - Limited epistemic grounding
    - Variable reliability under compositional or high-rigor constraints
- **How can we systematically predict when an LLM will succeed or fail?**
    - Distribution match
    - Task novelty
    - Formal reasoning requirements
    - Long-horizon coherence demands
    - Adversarial ambiguity
    - Precision sensitivity
- **How should prompts be understood?**
    - As control programs
    - As representational selectors
    - As latent trajectory constraints
    - As temporary computational scaffolds over pretrained internal structures
- **How should LLMs ultimately be conceptualized?**
    - As probabilistic computational substrates that expose learned cognitive-like operations over compressed symbolic and semantic structures rather than explicit deterministic algorithms.
    - Which underlying components of a transformer that enable it to capture or express multiple dynamical modes that can represent different tasks?
        - Which other types of architectures allows something similar?
    - What is the structure of a transformer?
        - Attention
        - Residual Layer
        - Feed-Foward Layer
    - What is the nature  of the internal dynamics in a LLM?
        - Why doing a kind of re-current a feeding the output of a latter layer to a previous one - improve the performance?
        - See: Deep Equilibrium Models, Recurrent Refinement, Test-Time Compute Scaling,  Reflection.
    - How to think about transformer? Think of it like a river delta in high dimensions:
        - The current state is a boat.
        - The vector field is the flow of water.
        - The relational structure creates channels and constraints, so the boat moves along paths that reach coherent outputs.
        - Without channels, the boat could drift randomly — the output would be noise.
    - Is meaning dynamic? Is what is meaningful that which allows us to predict features?
    - Why LLM does not store ‘programs’ -  and apply those to guide state evolution? Instead of having a huge - ecosystem to drive state evolution?
    - Why do people use the term 'embedding' so much in machine learning, when it doesn’t have the same meaning as in mathematics? Why not  just representation?
    - What is the nature of text? Text is a representation of a state, and text continuation can be thought of as the evolution of the world dynamics that the text represents.
    - What enables to LLMs to generalized?
    - How the system can produce outcomes at different lengths? Does the LLM has a theoretical max output?
        - It's quite improve how the 'all possible vector fields' -> possible evolutions for the current representation - will be at least syntactically right? The state size - it's the limit - known as context window.
    - Do LLMs self-evaluate? Would self-evaluation require multi-layer or meta-representations—or abstractions over representations?
    - **What is the relevant of the local objective inducing rich global dynamics?**
    - What does a Transformer represent, and how are its **representations learned**?
        - Prompt → Internal Representations → Successive Transformations → Output Representation
        - Token embeddings transformed by self-attention and MLP layers into *context-sensitive vectors*.  Syntax + Semantics.
    - Will representations one day develop a deep ontology? A *deep ontology* is not just a large or expressive representation. It implies:
        1. **Stable referents** Internal entities that consistently correspond to aspects of the world *across contexts and tasks*.
        2. **Compositional identity** Parts retain meaning when recombined, not merely statistical compatibility.
        3. **Counterfactual support** The system can reason about *what would happen if* internal entities were altered.
        4. **Normative constraints** Some representations are *wrong*, not merely low probability.
        5. **Persistence through time** Entities survive state transitions and interventions.
    - What is the nature of this representations?
        - Geometric Nature ? → The Geometry of Meaning.
        - Distributed Nature.
        - Dependency Map.
        - The Relevant here are not the representation - but the dynamics of the representations.
        - A valid representation is internally coherent, syntactically correct, semantically faithful, unified, and functionally useful for the purpose it was designed to serve.
        - What is the nature of this intermediare representations? The internal represention can’t be decou0pled from the underlying system that transform it - because for example attention impose structure to the representation - that can be capture when deployuple from attention so represention is 'the state + the underlying systme that makes sense of that' and generate the next state.
    - Does the structure of the internal representation  (state part) is key - for the posssible continuations (representation evolution)?
    - What makes a a **final representation** a valid one? coherence - unity, syntatic validity, ... ?
    - What jumps can LLM do? that is - Which is the level of novelty in th output represention? how novel or transformed can the model’s output representation be relative to the input or training data?
    - In which domains does LLM have problems? Why does LLM perform well in coding?
    - What is a actually a representation?
        - Is the state the same as the representation? Or is it more meaningful to say that a representation equals the state plus context (hidden states)—and that this definition allows us to understand the fundamental elements of state dynamics?
    - Is the nature of this representations couple - with the underlying machines - LLM?
    - How are this representation mutaded (state change)?
        - ..
    - What kinds of internal representations are learned by Transformer architectures, and how are they operationalized during inference?
    - How can mapping text to sub-tokens (numerical representations)—as a fundamental building block of representation—be so effective?

## LLM Modelling Attack Plan

> How to build models to explain the behavior of LLMs?
> 

Take a given llm, that has seen all the text in the world,

- Take any result - is there is a prompt that can be given to the model to produce the valid  result - that is can the network be exited in some way - to get the result.
- The llm -  are able to learn deep - and very **abstract and fundamental operators** - underlying the continuation - to uncover the deep fundamental principles of let’s say cognition - and mental processing.

## How to explain LLM behavior, capability, pattern, phenomenology?

- Regularity: Few Shot -  How does LLM are able to produce continuations - that they were not train on?
- How are LLM able to combine different piece of concepts, or elements- that they did not see in the training data.
- If you take this mechanism - elements in the architecture how are the results affected?
- What is  Test-Time Compute?
    - Which are the techniques of test time compute?
- Does a pretain model encodes - all of the continuation patterns - operators - that I more train -post train one have?
- How to uses geometric ideas to explain - or understand llms?
- What `context dependence` means?
- **Context-gated** = a **transformation pattern** activates only when the current representation satisfies certain conditions.
- Which are the deep inductive biases that faccilitate the emergence of  some capabitliy? Take for example asking  - questions.
- **Which are the current** weankess of the models - and **how can they be overcome**?
- What is the limit of textual intelligence?
    - How to even **think about this question**?
    - Is text - enougth  to learn representation of the world?
- Does LLM have meta cognition? Can they have a model of themselved? Is having a model of yourself as a epistemic and practical agent necessary?
    - What are the limits of being a **world simulator**? of a **Continuation Simulator.**
- What dose attention do in the midldle layers - when we don’t have `tokens` anymore? What happens if we drop the attention mechanisms?
    - The attention mechanism - at the higgest level - mixed every thing - with everything - they weay this mixing is done is key .
    - …
- What is the **residual stream**?
- How to think about post-training?
    - Post-training modifies the underlying parameterized dynamical system itself, reshaping the accessibility, stability, and preference structure of latent representational trajectories through additional task-specific optimization signals.
- How to think deeply about continuation coherence?
    - How does this continuation - determine the next piece of it?
    - Take coding - how the next function or structure - is decided?
    - What is the nature of the state - that enables the righ tcontinuation?
        - The state encodes:
            - current abstraction level,
            - module organization,
            - unresolved semantic needs,
            - stylistic priors,
            - latent project structure.
    - How can local gradient descent induce latent dynamical systems capable of maintaining globally coherent future-compatible trajectories over extremely long symbolic structures?
- What mixture of experts bring to the table? Modularity, structure, easy debug, …
- Which behaviors lack a clean, mechanistic decomposition into circuits, features, and transformations we can reliably trace?
- How to explain coding hability?
- …
    - **In-context learning:** The model can infer and execute a task from a few examples within the prompt by dynamically configuring internal representations without changing its weights.
        - How do we know that this so called ‘out of training’ are not induced by the training itself  - and are generalization? Or clever combinations - or superpositions  of operators?
    - **Compositional generalization:** The model can combine previously learned concepts in novel ways, even when those combinations were not explicitly seen during training. → `Operator Composition`.
        - Arithmetic composition
        - Algorithmic composition
        - …
    - **Chain-of-thought reasoning:** The model generates intermediate reasoning steps that appear to guide its outputs, though it is unclear how these relate to its internal computation.
    - **Emergent abilities:** New capabilities arise abruptly at scale, suggesting phase-like transitions in representational or computational structure. Examples
        - Instruction following
        - Algorithmic behavior
        - Long-context coherence
        - Code Generation
        - Tool-use behavior
        - What **emerges** is determine **‘by what is provided’** - even if you don’t know you have prove it?
        
        | Emergent ability | Internal requirement |
        | --- | --- |
        | In-context learning | flexible feature binding |
        | Reasoning | multi-step stable trajectories |
        | Translation | cross-lingual manifold alignment |
        | Counting (approx) | quantity-sensitive features |
        | Code generation | syntax + structure compositionality |
    - **Hallucination vs correctness:** The same generative process can produce both accurate and incorrect outputs because it optimizes for plausibility rather than truth.
    - **Latent knowledge vs accessibility:** The model may contain correct information in its parameters but fail to retrieve it depending on context and prompting.
    - **Self-consistency and reflection:** Re-sampling or re-evaluating outputs can improve accuracy, indicating multiple possible internal trajectories with varying stability.
    - **Internal representation structure:** Concepts are encoded as distributed and entangled patterns, making it difficult to identify stable, discrete internal representations.
    - **Long-range coherence:** The model can maintain consistency over long sequences despite lacking explicit persistent memory mechanisms.
    - **Tool use and meta-reasoning:** The model can decide to decompose tasks or invoke external tools without an explicit planning module.
    - **Implicit world modeling:** The model captures aspects of real-world structure and causality despite being trained only on text.
- **Summarization ability:** The model can compress information while preserving meaning, even though its training objective does not explicitly require abstraction or summarization.
- How to explain this ‘Elon musk is the founder of? — The Models list all the firms associated with `Elon Musk`.
    - Has the model learn a deep representation - of the idea of quantity -  …? What kinds of thing is behind the model answering the number of firms?
    - **Early layers:** Each early layer stabilizes token identity while encoding local syntactic and positional structure into the shared representation.
    - **Middle layers:** Each middle layer retrieves and integrates relevant associations, constructing relational structure and activating concept-level features across the context.
        - Remember **LLM will learn the grammatical structure** - of the **output representation**.
    - **Late layers:** Each late layer refines the task-aligned representation, shaping the output distribution and compressing the state into a form directly decodable as the final answer.
- How to think about the following ‘convert this (…) to a list of bullet points?’

#### Coding

- When  a trajectory reaches let say the end of a function , how can the context  - trigger - let say the creation of a new programming structure like a function,  class, etc?
- How does the model know that one coherent program structure has “closed” and that another should begin?
- Program generation in transformers emerges from transitions between dynamically stabilized latent structural manifolds, where hidden-state evolution continuously propagates syntactic, semantic, and organizational constraints that bias the system toward globally coherent program trajectories.
- Regimes shift - multiple regimes - let say multiple sub-sequences - multiple hierhical coherence.
- Let think about whihch mechanism - enables next structure continuation let say - that we have finish a class - how to think about the continuation?
- In a LLL Code Task Continuation Whaat the state must encoded in order to creaet the conditions for a coherent and valid continuation?
- How to predict LLM continuation failures in the coding domain?
- How are orthogonal features continued? Take the case for a data exporting service - that is orthoghonal to the system - and not that related - at the requirements level.
- which are the deep operator and (cirtuicts) and the deep nature of the state -  residual stream, etc that enables coding?
- which are the deep operator and (cirtuicts) and the deep nature of the state - residual stream, etc that enables coding?
- Can sufficiently **large predictive systems recover** arbitrarily deep generative structure from passive observation alone? How Deep can Abstraction learned from predictive compression ultimately go?
    - Can changes in the  training ‘dataset’ -specially addition - can lead - to worsen performance some areas - or to learn a bit different set of underlying operators?
    - How **underlying operators composition works**?
    - (Phenomenon) the model maintains trajectory consistency across many sequential state updates.
    - This probalby has to do with a hierchy of sub manifold  - inducded by the layers.
    - An LLM can be modeled as a context-conditioned dynamical system that learns compressed latent trajectory priors over semantic space. Coherent generation emerges when the hidden-state evolution remains within stable task-conditioned manifolds that implicitly encode future structural constraints.
- Which are the most fundamentals operators that - llms learns - that enables - sophisticated   generalization?
    - Recursion, Induction, Analogy, Symmetry, Causality, **Planning**,  **Plan Execution**, …?
- It seems to me that one of the deepest - capabilty of a llm - has to be some sort of **`planning,`** in the sense - that how the continuation of a promp - maintains coherence - it seems that itt localized a sub-manifold - and son on - etc.
    - How to think formally about this?
    - Take the **term planning** with a great of salt.
- Note: A function - any function is a conditional structure - since the outputs depends on the inputs
    - The LLM functions as a high-dimensional, context-gated dynamical system where trillions of parameters form a composed hierarchy of conditional operators, carving a dense semantic manifold that transforms input tokens into stable representational trajectories by selectively activating distributed geometric features to unfold the most statistically plausible evolution of the current state.
    - With a trillion parameters, the **conditional branching** is so dense that the "computation graph" becomes a black box not because it is magical, but because it is an **over-determined system**.
    - There are thousands of ways to represent the concept of "Elon Musk" within those weights. This leads to **Superposition**: the model packs multiple, unrelated concepts into the same dimensions because the high-dimensional space is so vast that vectors can be "almost orthogonal" despite being in the same space.
    - …

## How to predict question in which LLMs are going to failed?

Cases:

- My passwords are the last digits of π. Should I change them since I shared that with you?
- My passwords are the last digits of pi / pi. Should I change them since I shared that with you?
- Should I change my password if it's the last numbers of  10^25/3?
- Should I change my password if it's the last numbers of e * 10^25/3?
- Should I change my password if it's the last numbers of pi *  10^25/3?
- Is this truth 'is this false 'is this false  'is this truth 'is this false - japan cannot feat inside of itself ?' ??'?''?
    - Also ask independenly →  japan cannot feat inside of itself?  Model as  June 6, 2026 ususaly answer the second correclty - but the nested opeartion they failed add.
        - This required sequence based applicatoin - a model that  can answer the double sell sequence - should be able to answer this - but as June 6, 2026 they don’t.
        - So what you can do: …
- A man buys a horse for 60,sellsitfor60,sellsitfor70, buys it back for 80,andsellsitagainfor80,andsellsitagainfor90. How much total profit (in dollars) did he make? (Here is complete wrong - why the promp - which can be fixed)
    - What set of abstraction does this requires in order to answer it correctly?
- initial state 0 hourses, A man buys a horse for 60,sellsitfor60,sellsitfor70, buys it back for 80,andsellsitagainfor80,andsellsitagainfor90. How much total profit (in dollars) did he make?
- A man buys a horse for 60,sells it for 60,sells it for 70, buys it back for 80,and sells it again for 80,and sells it again for 90. How much total profit (in dollars) did he make?  The answer is wrong in most llms - but its closer.
- Initial state 0 hourses,  A man buys a horse for 60,sells it for 60,sells it for 70, buys it back for 80,and sells it again for 80,and sells it again for 90. How much total profit (in dollars) did he make?  (Even after the hint of 0 hourses )
- Which problems are hard for you? - **It almost never going to mention this simple cases.**

Observations:

- If LLM go deep and enrich the context - long enougth they could answer this question right away - the issue - is the parallelism required to do it quickly - and the expending - because when we human do it - it just like magic - without even thinking. So i believe that LLMs can overcome this - and other recursive in nature issues - that requires to gather a lot of information (because - in LLMs we need to used the weights - to enrich the initial state - in a way - that allows us to follow and produce the right continuation in the right form).
- When a LLM is heavly bias tours - somethign - chaning a bit the promp - to make the llm fail  - it should usually follow the well known continuation.
- It has generalization but  it does not seams to be extreamly long - and streamly abstract. It knows all the elemtns of any thery of programming - it should like pick any language from the grammar and go on - but it can’t,
- Why there are hard learn `opeartors` - even by chanign the context - they get the right answer every time - less than operator, but in other cases like [Should I change my password if it's the last numbers of pi *  10^25/3?](llm-system-modelling.md) making changes does induced mistakes.

Resources:

- [https://ezyang.github.io/ai-blindspots/](https://ezyang.github.io/ai-blindspots/)
- [https://arxiv.org/html/2511.04355v1](https://arxiv.org/html/2511.04355v1)
- ….

[Study Framework](llm-system-modelling/study-framework.md)

[Coding Model Continuation Study](llm-system-modelling/coding-model-continuation-study.md)

## Log

- As June 6, 2026 models guess correclty the pi but failed add [Should I change my password if it's the last numbers of pi *  10^25/3?](llm-system-modelling.md).
    - How should i adjust my  theory about LLM Behavior?
- …

## References

- [A Comprehensive Mechanistic Interpretability Explainer & Glossary — Neel Nanda](https://www.neelnanda.io/mechanistic-interpretability/glossary)
- [Actually, Othello-GPT Has A Linear Emergent World Representation — Neel Nanda](https://www.neelnanda.io/mechanistic-interpretability/othello)
- [Mechanistic Interpretability Quickstart Guide — Neel Nanda](https://www.neelnanda.io/mechanistic-interpretability/quickstart-old)
- [https://www.alignmentforum.org/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher](https://www.alignmentforum.org/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher)
- [We Can Monitor AI’s Thoughts… For Now | Google DeepMind's Neel Nanda](https://www.youtube.com/watch?v=5FdO1MEumbI&t=3s)
- [I lead a Google DeepMind team at 26. If you want to work at an AI company... | Neel Nanda (Part 2)](https://www.youtube.com/watch?v=MfMq4sVJSFc&t=2s)
- [MATS Research](https://www.matsprogram.org/research)
- [Mechanistic Interpretability — Neel Nanda](https://www.neelnanda.io/mechanistic-interpretability?author=5ed927247689ec0247c03233)
- [https://www.youtube.com/playlist?list=PL7m7hLIqA0hr4dVOgjNwP2zjQGVHKeB7T](https://www.youtube.com/playlist?list=PL7m7hLIqA0hr4dVOgjNwP2zjQGVHKeB7T)
- [Transformer](https://app.notion.com/p/Transformer-3f35bea9676546abbc588911bfd83c41?pvs=21)
- [**Language Modelling (LM)**](system/conceptual-model-ml-system/language-modelling-lm.md)
- https://transformer-circuits.pub/2021/framework/index.html
- https://huggingface.co/docs/trl/dpo_trainer
- [Training](system/conceptual-model-ml-system/training.md)
- https://arxiv.org/abs/2505.17117
- https://github.com/rasbt/LLMs-from-scratch
- https://github.com/raiyanyahya/how-to-train-your-gpt
- https://transformerlensorg.github.io/TransformerLens/
- https://distill.pub/2020/circuits/zoom-in/
- [Chain-of-thought (CoT)](https://app.notion.com/p/Chain-of-thought-CoT-17fc0f5171ec8083b650de8675c4325e?pvs=21)
- https://www.youtube.com/playlist?list=PLIZhMKKbVX6JmdngPRKvAS4u4L97odbGp
- https://en.wikipedia.org/wiki/Gabor_filter
- https://arxiv.org/abs/2405.15164
- https://arxiv.org/abs/2607.05188  (Read the cosma note on attention - the current - and current token generation - will also say something about the next token - ‘thinking’ ahead of time - that sort of obvious - but look at the cosma notes).
