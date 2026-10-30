---
tags: [information]
qa: 
 - What is the nature of the term `theory`  on 'Shannon Information Theory'?
 - ...
---

# Shannon Information Theory

> In this note, we introduce Shannon Information Theory—not in terms of everyday notions of information, but as a formal theory of **Rarity = Novelty**, where information quantifies **how unlikely an outcome is**.

> Shannon’s Information Theory is the mathematical theory of the representation, transmission, and compression of signals or data, quantifying information as the reduction of uncertainty, independent of meaning.

> Information Theory uses probability to build a **set of abstractions** that quantify uncertainty, information content, and the limits of communication, independent of meaning.

> **Shannon Information Theory** is a **mathematical tool to study communication systems**, quantify information, and set limits on transmission. It **does not by itself transmit messages** or implement encoders/decoders — those are practical applications inspired by the theory.

> Shannon’s Information Theory builds a tower of abstractions to study the properties of communication systems. It abstracts away meaning and physical implementation, focusing instead on probabilities, uncertainty, and the fundamental limits of transmitting information reliably.

> Shannon entropy  is given this Probability Model,  how capable are we of reducing the space - in which an outcome fall in?

> Probability quantifies uncertainty and the range of possible outcomes, and Shannon Information builds on this to formalize the related concept of unpredictability.

Doing:

- [ ]  Is Shannon’s information theory a theory of communication efficiency, that is, of compression and reliability?
    - [ ]  **Compression** (source coding) and  → What is the minimum number of bits needed to represent the message?
    - [ ]  **Reliability** (channel coding)  → How can we send the message perfectly across a noisy channel?
    - [ ]  Source-channel Separation Theorem.
- [ ]  We need examples of encoding schemes.

## Problem Formulation

> Data →  (**Encoding)** Representation → **(Decoding)** Recovered Data.

> (**Reconstruction Fidelity**) Suppose we are given some data $d$ to transmit. What encoding $E_d$ of $d$ would ensure that $d$ can be reliably and unambiguously reconstructed from its encoded form ($E_d$) — that is, such that $\text{decoded}(E_d) ≈ d$?

> (**Informational Content**) In other contexts, suppose the original data $d$ is unknown, but we are given its encoding $E_d$. How much information does $E_d$ convey? That is, how many distinct interpretations of $E_d$ are possible? The fewer the interpretations, the more informative $E_d$ it is.

> **Data is transformed** into a **latent representation**. Through a sequence of Yes/No questions (a decision process), we aim to **uncover the set of possible values** that the **latent representation encodes** or corresponds to **upon materialization**.

## Formulation

### What is this epistemic instance?

Shannon information theory is the mathematical theory of the representation, transmission, and compression of messages. It abstracts away meaning and implementation: a source is a probability distribution over an alphabet of symbols, a channel is a conditional distribution over received symbols, and information is the reduction of uncertainty that an outcome or a message produces. From those two distributions it builds a tower of quantities — self-information, entropy, joint and conditional entropy, mutual information, channel capacity — and derives from them the limits that make the theory operational: the shortest average code a source admits, and the fastest rate a noisy channel carries reliably.

This note develops the theory and its atom together. The atom — Shannon information content, the surprisal of a single outcome — is developed in [Shannon Information Content](#sec-shannon-information); its type, decomposition, and evaluation are answered here, in the shared formulation. The [Information Theory Atlas](data/epistemica/observational/information/atlas/atlas.html) makes every quantity in the tower playable.

### What epistemic element type does this epistemic instance belong to?

An **Aggregate**: an organized inquiry whose orientation, target, representation, constructions, and coding operations form a coherent epistemic whole.

Its atom, Shannon information content, is an **Epistemic Construction** — a concept that operationalises a target (the surprisal of an outcome) into a computable quantity. Read as the value it produces, the same atom is an **Epistemic Representation**: the quantity $I(x)$ inside a quantitative probability representation. The theory's models and theorems are constructions; its coding practice is an operation.

### Is the type of this `epistemic element instance` ambiguous?

The theory's reading as an `Aggregate` is not in doubt: it is an organized inquiry, not a single model. Two boundaries are genuinely ambiguous and are handled explicitly.

Its **outer boundary**: probability theory supplies the distributions the theory consumes, and algorithmic information theory (Kolmogorov) supplies a competing, representation-relative notion of content. Shannon's theory is neither, and it must not be read as a theory of meaning — the ambiguity is resolved by the `Limitations` section and by the meaning-independence property in the decomposition.

Its **atom's type**: Shannon information content is a construction when read as a concept and a representation when read as a quantity. Both readings are legitimate, so the decomposition carries both — the concept under `Epistemic Construction`, the value under `Epistemic Representation` — instead of choosing one and losing the other.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: this table decomposes one epistemic instance — Shannon information theory — as an organized inquiry: its orientation, target, quantitative representation, constructions, and coding operations. Agency, access, communication, infrastructure, context, worked applications, and the two coding theorems' proofs are outside its scope.
>
> Stopping rule: a row is terminal when it names a concrete purpose, question, quantity, unit, model, assumption, property, act, practice, or theorem; the branches are not decomposed further here.
>
> Identity: every path is unique and complete from the root; instance rows are Title Case; type groupings are backticked; no type terminates a branch.
>
> Typing: the root type is `Aggregate` — the declared epistemic element type of the theory read as an organized inquiry. The concept `Shannon Information Content` is an `Epistemic Construction` inside it; its value is read as an `Epistemic Representation`; coding is the `Epistemic Operation`.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Shannon Information Theory | The organized inquiry into uncertainty, compression, and reliable transmission independent of meaning: its questions, target, representation, constructions, and coding operations. |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` | Grouping: the purposes and questions that direct the theory. |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: what the theory is for. |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` → `Epistemic Purpose` → Communication Limit Purpose | Telos: the minimum description length for a source and the maximum reliable rate over a channel. |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` → `Epistemic Question` | Grouping: the questions the theory answers. |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` → `Epistemic Question` → Outcome Information Question | How much information does a single outcome carry? |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` → `Epistemic Question` → Compression Question | What is the shortest code for a source? |
| `Aggregate` → Shannon Information Theory → `Epistemic Orientation` → `Epistemic Question` → Reliable Transmission Question | At what rate can a noisy channel carry a message reliably? |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` | Grouping: what the theory ranges over. |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` → `Target Element` | Grouping: the units of the target. |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` → `Target Element` → Event | The outcome whose occurrence the theory prices. |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` → `Target Element` → Source Alphabet | The finite set of symbols a source emits. |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` → `Target Element` → Noisy Channel | The medium modeled by the conditional probability $P(M' \mid M)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` → `Observable` | Grouping: what is registered from the target. |
| `Aggregate` → Shannon Information Theory → `Epistemic Target` → `Observable` → Emitted Symbol | The symbol occurrence registered from the source. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` | Grouping: the theory read as a quantitative representation. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` | Grouping: the sign system in which information is expressed. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation | Probabilities on a logarithmic scale — the system the theory works in. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Representation Element` | Grouping: the combinable constituents of the representation. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Representation Element` → Outcome Probability | $P(x)$: the measure the source assigns to an outcome. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Representation Element` → Shannon Information Quantity | $I(x) = -\log_b P(x)$: the surprisal the outcome carries, read as a quantity. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Representation Element` → Bit | The unit fixed by base 2; nats at base $e$, hartleys at base 10. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` | Grouping: the structures and rules constituting the representation. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` → Probability Model | The distribution over outcomes that supplies $P(x)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` → Independence Assumption | $P(x,y) = P(x)P(y)$ for independent events — what makes information additive. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` → Logarithmic Scale Convention | The base choice that fixes the unit. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` → `Property` | Grouping: properties of the representation. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` → `Property` → Additivity Property | Independent events add their information: $I(x,y) = I(x) + I(y)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Representation` → `Representational System` → Quantitative Probability Representation → `Constitutive Substrate` → `Property` → Meaning Independence Property | The measure is defined over probabilities alone and is silent about significance. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` | Grouping: the theory's constructions. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Shannon Information Content | The atom concept: a map from an outcome's probability to the surprisal it carries. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Shannon Information Content → Self-Information Definition | The identity $I(x) = -\log_b P(x)$ that fixes the concept. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Shannon Information Content → Surprisal Measure | The graded reading of the negative logarithm with a chosen base. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Shannon Entropy Model | The averaged model: $H(X) = \mathbb{E}[I(x)]$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Joint Entropy Model | Uncertainty over pairs: $H(X,Y) = -\sum_{x,y} P(x,y) \log P(x,y)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Conditional Entropy Model | Residual uncertainty after conditioning: $H(X \mid Y) = H(X,Y) - H(Y)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Mutual Information Model | Information shared by two variables: $I(X;Y) = H(X) - H(X \mid Y)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Channel Capacity Model | The maximum mutual information over input distributions: $C = \max_{P(X)} I(X;Y)$. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Source Coding Theorem | Entropy as the compression limit of a source. |
| `Aggregate` → Shannon Information Theory → `Epistemic Construction` → Channel Coding Theorem | Capacity as the reliable-rate limit of a noisy channel. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` | Grouping: the theory read as coding operation. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` → `Action` | Grouping: the primitive acts of transmission. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` → `Action` → Encoding Act | Mapping source symbols to code words. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` → `Action` → Decoding Act | Recovering source symbols from code words. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` → `Organization` | Grouping: the organized practices of coding. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` → `Organization` → Source Coding Practice | Compression practice that approaches the entropy limit. |
| `Aggregate` → Shannon Information Theory → `Epistemic Operation` → `Organization` → Channel Coding Practice | Error-correction practice that approaches capacity. |

### What Is a critical conceptual evaluation of Shannon Information Theory?

The theory is precised as the one that assigns to each outcome $x$ of a probabilistic source the information $I(x) = -\log_b P(x)$ and derives entropy, mutual information, channel capacity, and the coding limits from it.

Verdicts: Conceptual Identification **strong**; Definitional Clarity **strong**; Conceptual Determinacy **strong** within the probabilistic setting and **weak** at the theory's outer boundary; Internal Consistency **strong**; Representational Adequacy **strong** for the quantities and the limits; Purpose Adequacy **strong** for communication engineering and **inadequate** for semantic or pragmatic content.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Strong | The theory is distinguished from probability theory, which supplies the distributions, and from algorithmic information theory, which relativizes content to a description language. |
| Definitional Clarity | Strong | Source, channel, event, entropy, mutual information, and capacity each carry an explicit probabilistic definition. |
| Conceptual Determinacy | Strong within scope, weak at the boundary | Every quantity is determined by the distributions; what counts as "information" outside a probabilistic source is not. |
| Internal Consistency | Strong | Event → Self-Information → Entropy → Mutual Information → Capacity derive in one framework; no quantity contradicts another. |
| Representational Adequacy | Strong | The quantities capture uncertainty, its reduction, and the exponential limits of coding; they do not capture semantic content, and do not claim to. |
| Purpose Adequacy | Strong for engineering, inadequate for meaning | The theory is fit for compression and reliable transmission; it is silent about significance, relevance, and knowledge. |

### What Is a critical conceptual evaluation of Shannon Information Content?

The concept is precised as the map $I(x) = -\log_b P(x)$ from an outcome's probability to the surprisal its occurrence carries.

Verdicts: Conceptual Identification **strong**; Definitional Clarity **strong**; Conceptual Determinacy **strong**; Internal Consistency **strong**; Representational Adequacy **strong** under a known model and **weak** when the model is contested; Purpose Adequacy **strong** for coding and **inadequate** for meaning.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from entropy, its average, and from mutual information, its recombination over two variables. |
| Definitional Clarity | Strong | One input $P(x)$, one operation $-\log_b$, one unit choice; no hidden parameter. |
| Conceptual Determinacy | Strong | Defined for every outcome with $P(x) > 0$; impossible events are excluded rather than assigned a value. |
| Internal Consistency | Strong | Additivity over independent events follows from $P(x,y) = P(x)P(y)$ and makes entropy a sum. |
| Representational Adequacy | Strong under a known model, weak under a contested one | The value is exact given the model; it inherits every defect of the probabilities fed to it. |
| Purpose Adequacy | Strong for coding, inadequate for meaning | It measures surprise, not significance; reading it as semantic content is a category error. |

## Shannon Theory Toolbox

> **Event → Shannon Information → Entropy → Mutual Information → Channel Capacity → Coding**


> **Noise:** Uncertainty introduced by the channel that can corrupt messages.
> 

> **Redundancy:** Extra bits added to mitigate errors.
> 

> **Source coding:** Efficient representation of messages (compression).
> 

> **Channel coding:** Adding structured redundancy to protect against noise (error correction).
> 

Let the alphabet be: $\mathcal{A} = \{a_1, a_2, \dots, a_n\}$:

- Each symbol $a_i$ has a probability  $P(a_i)$ of being chosen by the source.
- These probabilities define the **source distribution**.
- A message (M) is a **sequence of symbols** from the alphabet:  M = ($a_{i_1}, a_{i_2}, \dots, a_{i_L}$)

**Transmission**: Let the channel introduce **errors**, modeled by a conditional probability: $P(M'|M)$

- (M') = received message.
- Example: each symbol is transmitted correctly with probability (p), or replaced by another symbol with probability (1-p) (uniformly).
- This defines a **noisy channel**, which is the basis for computing conditional and mutual information.
- **Entropy H(X)** → average uncertainty per symbol.
- **Noisy channel P(M'|M)** → models transmission errors.
- **Conditional entropy H(M|M')** → remaining uncertainty after reception.
- **Mutual information I(M;M')** → information successfully transmitted.
- **Channel capacity (C)** → maximum reliable information rate.

### **Event**

> A specific outcome or set of outcomes from a random **process or source**.

> In Shannon’s framework, an event is treated as a symbol or signal whose occurrence has a probability $P(x)$ and contributes Shannon information $I(x) = -\log P(x)$.

> Events are the basic units from which entropy, mutual information, and other measures are calculated.

### Shannon Information

> **Shannon information** (also called **self-information**) (also called Shannon Information Content)  is a measure of the **amount of uncertainty reduced** when an event occurs. It is **quantitative**, not semantic—it doesn’t measure meaning —  **unpredictability** of an outcome.

> Why it’s it called self-information?

> Is surprisal → rarity? Why -logb and not log?   Why log at all? How to think about different measure of surprisal? Why not P(x)? Isn just surprisal an interpretation? P(x) high non surprising, P(x) small surprising.

> The concept itself — its definition, its typing, its decomposition, and its evaluation — is developed in [Shannon Information Content](#sec-shannon-information). The [Information Theory Atlas](data/epistemica/observational/information/atlas/atlas.html) makes its operational quantities playable.

> Shannon information content — self-information or surprisal — is the amount of uncertainty removed when a single outcome is observed: the rarer the outcome, the more information it carries.

It is the atom of Shannon's theory. Entropy averages it over a distribution; joint, conditional, and mutual information recombine it; divergence and cross-entropy price it under a wrong model. The [Information Theory Atlas](data/epistemica/observational/information/atlas/atlas.html) lets each of these quantities be played with directly.

Given an outcome $x$ with probability $P(x)$, the information content is

$$I(x) = -\log_b P(x).$$

The minus sign turns the inverse relation between probability and surprise into a positive quantity; the logarithm makes information additive for independent events, since $P(x,y) = P(x)P(y)$ implies $I(x,y) = I(x) + I(y)$. The base $b$ chooses the unit: $b = 2$ gives bits, $b = e$ gives nats, $b = 10$ gives hartleys.

The concept is the atom of the theory developed above: the probabilistic realisation of [Entropy](note.html?n=epistemica/observational/information/entropy.md), whose averaged form is [Shannon Entropy](note.html?n=epistemica/observational/information/shannon-entropy.md). Its type, decomposition, and evaluation are answered in the shared [Formulation](#sec-formulation): the concept is the `Epistemic Construction` path, its value the `Epistemic Representation` path, and its evaluation the second table under the critical-evaluation question.

![image.png](../assets/note/epistemica/observational/shannon-information-theory/image.png)

### Entropy

> aka. Average Uncertantity.
> 

> Suppose I have a probability model and encounter an unseen outcome. How difficult will it be to guess this outcome? How large is the **space of possibilities I must consider**?
> 

For a discrete random variable (X) with possible outcomes (${x_1, x_2, \dots, x_n}$) and probabilities $P(x_i)$: 

$H(X) = \sum_{i=1}^{n} p_i I(a_i) = - \sum_{i=1}^{n} p_i \log_2 p_i$

Where:

- $H(X)$ = entropy of (X)
- $P(x_i)$ = probability of outcome ($x_i$)
- (b) = logarithm base (2 → bits, (e) → nats)

> The averaged quantity itself is developed in [Entropy](note.html?n=epistemica/observational/information/entropy.md) and [Shannon Entropy](note.html?n=epistemica/observational/information/shannon-entropy.md).

### **Joint Entropy**

> Measures the total uncertainty of a pair of random variables (X) and (Y).
> 

> Formula: $H(X,Y) = - \sum_{x,y} P(x,y) \log P(x,y)$.
> 

> Captures how unpredictable both variables are together.
> 

### **Conditional Entropy**

> Measures the uncertainty remaining in (X) given that (Y) is known.
> 

> Formula: $H(X|Y) = H(X,Y) - H(Y)$
> 

> Useful for understanding how much information one variable provides about another.
> 

### **Mutual Information**

> Quantifies the amount of **information shared** between (X) and (Y).
> 

> Formula:  $I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$
> 

> Indicates how much knowing one variable reduces uncertainty about the other.
> 

### **Channel Capacity (C)**

> Maximum rate at which information can be transmitted **reliably** over a communication channel.
> 

> Formula: $C = \max_{P(X)} I(X;Y)$
> 

> Sets the theoretical limit for error-free communication given channel noise.
> 



## Information System

> An **information system** is a system that collects, processes, stores, and transmits information. An information system can be thought of as a communication system that transfers information from a source to a destination.
> 

> The features of a communication channel encompass characteristics such as bandwidth, latency, signal quality, noise, and reliability that collectively influence the effectiveness of data transmission and communication.
> 

> **Shannon’s Communication Model:** Claude Shannon’s groundbreaking work introduced the communication model, which consists of an information source, a transmitter, a channel, a receiver, and a destination. This model is still widely used to understand communication systems.
> 

The **main components of an information system** are:

- **Source**: The source is the originator of the information, which generates messages that are to be transmitted through the system. The source can be a human, a machine, or a natural system.
- **Channel**: The channel is the medium through which the information is transmitted from the source to the destination. The channel can be a physical medium, such as a wire or a radio wave, or it can be a logical channel, such as a computer network.
- **Encoder**: The encoder is the device that converts the messages from the source into a form that can be transmitted through the channel. The encoder can use a variety of techniques, such as modulation, coding, and compression, to convert the messages into a form that is suitable for transmission.
- **Decoder**: The decoder is the device that converts the transmitted signal back into the original message at the destination. The decoder uses techniques such as demodulation, decoding, and decompression to recover the original message from the transmitted signal.
- **Receiver**: The receiver is the destination of the information, which receives the messages transmitted through the channel and processes them according to the intended purpose.

## Compression

> **Rate-Distortion Theory**: Studies the trade-off between the compression rate and the distortion (loss of information) in lossy data compression.

## Limitations

> **'Information,' as captured in Shannon's theory**, is its measure of 'surprise' or unpredictability. However, this definition is quite narrow, as it does not account for meaning, relevance, or contextual significance. While Shannon entropy quantifies uncertainty reduction in a system, other dimensions of information—such as its semantic content, pragmatic use, and its role in knowledge formation—go beyond mere statistical encoding.
> 

## QA

### Why Is Shannon Information Called Self-Information?

> Shannon information is called **Self-Information** because it quantifies the information associated with the occurrence of an individual outcome, based on the probability assigned to that outcome. It captures the information associated with the event \(X=x\), denoted by \(I(X=x)\).

> Mathematically: $I(X=x)=-\log_2 P(X=x)$

> The term *self* emphasizes that the quantity concerns an individual outcome rather than the relationship between two variables (as in mutual information).

### How to Think about Shannon Information?

| Intuitive Notion | Central Question | Relationship to Shannon Information |
|---|---|---|
| **Possible Worlds** | What are the possible states in which the world could be? | Defines the set of possible outcomes under consideration. |
| **Possibility** | Which outcomes remain possible given the available constraints? | Establishes the space of alternatives that could occur. |
| **Contingency** | What could have happened differently? | Captures the existence of alternative outcomes that could have occurred instead. |
| **Variability** | How much do the possible outcomes differ or vary? | Concerns the distribution and dispersion of possible outcomes. |
| **Unpredictability** | How difficult is it to anticipate which outcome will occur? | Relates to the uncertainty associated with the probability distribution. |
| **Surprise** | How unexpected is a particular realized outcome? | Quantifies the information associated with an individual outcome through its probability. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Entropy](note.html?n=epistemica/observational/information/entropy.md)
- [Shannon Entropy](note.html?n=epistemica/observational/information/shannon-entropy.md)
- [Coding](note.html?n=epistemica/observational/information/coding.md)
- [Huffman Coding](note.html?n=epistemica/observational/information/huffman-coding.md)
- [Error-Correcting Code](note.html?n=epistemica/observational/information/error-correcting-code.md)
- [Information Theory Atlas](data/epistemica/observational/information/atlas/atlas.html)
- Nyquist, H. (1924). Certain factors affecting telegraph speed. *Bell System Technical Journal*, 3(2), 324–346.
- Hartley, R. V. L. (1928). Transmission of information. *Bell System Technical Journal*, 7(3), 535–563.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423; 27(4), 623–656.
- Shannon, C. E. (1949). Communication in the presence of noise. *Proceedings of the IRE*, 37(1), 10–21.
- Hamming, R. W. (1950). Error detecting and error correcting codes. *Bell System Technical Journal*, 29(2), 147–160.
- Kullback, S., & Leibler, R. A. (1951). On information and sufficiency. *Annals of Mathematical Statistics*, 22(1), 79–86.
- Shannon, C. E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal*, 30(1), 50–64.
- Huffman, D. A. (1952). A method for the construction of minimum-redundancy codes. *Proceedings of the IRE*, 40(9), 1098–1101.
- Shannon, C. E. (1956). The bandwagon. IRE Transactions on Information Theory, 2(1), 3. https://doi.org/10.1109/TIT.1956.1056774.
- Jaynes, E. T. (1957). Information theory and statistical mechanics. *Physical Review*, 106(4), 620–630.
- Shannon, C. E. (1959). Coding theorems for a discrete source with a fidelity criterion. *IRE National Convention Record*, 7(4), 142–163.
- Ziv, J., & Lempel, A. (1977). A universal algorithm for sequential data compression. *IEEE Transactions on Information Theory*, 23(3), 337–343.
- Rissanen, J. (1978). Modeling by shortest data description. *Automatica*, 14(5), 465–471.
- Verdú, S. (1998). Fifty years of Shannon theory. *IEEE Transactions on Information Theory*, 44(6), 2057–2078.
- Tishby, N., Pereira, F. C., & Bialek, W. (1999). The information bottleneck method. In *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing* (pp. 368–377).
- Paninski, L. (2003). Estimation of entropy and mutual information. *Neural Computation*, 15(6), 1191–1253.
- Kraskov, A., Stögbauer, H., & Grassberger, P. (2004). Estimating mutual information. *Physical Review E*, 69(6), 066138.
- Shannon, C. E., & Weaver, W. (1949). *The Mathematical Theory of Communication*. University of Illinois Press.
- Khinchin, A. I. (1957). *Mathematical Foundations of Information Theory*. Dover.
- Kullback, S. (1959). *Information Theory and Statistics*. Wiley.
- Fano, R. M. (1961). *Transmission of Information: A Statistical Theory of Communications*. MIT Press.
- Gallager, R. G. (1968). *Information Theory and Reliable Communication*. Wiley.
- Berger, T. (1971). *Rate Distortion Theory: A Mathematical Basis for Data Compression*. Prentice-Hall.
- Dretske, F. I. (1981). *Knowledge and the Flow of Information*. MIT Press.
- Gray, R. M. (1990). *Entropy and Information Theory*. Springer.
- MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press. https://www.inference.org.uk/mackay/itila/
- Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley.
- Grünwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press.
- Li, M., & Vitányi, P. (2008). *An Introduction to Kolmogorov Complexity and Its Applications* (3rd ed.). Springer. https://homepages.cwi.nl/~paulv/kolmogorov.html
- Csiszár, I., & Körner, J. (2011). *Information Theory: Coding Theorems for Discrete Memoryless Systems* (2nd ed.). Cambridge University Press.
- Floridi, L. (2011). *The Philosophy of Information*. Oxford University Press.
- Polyanskiy, Y., & Wu, Y. (2024). *Information Theory: From Coding to Learning*. Cambridge University Press. https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf
- [Information Theory (6.441) — MIT OpenCourseWare](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/)
- [Statistics and Information Theory — Stanford Stats 311 lecture notes](https://web.stanford.edu/class/stats311/lecture-notes.pdf)
- [Information and Entropy — Computation Structures](https://computationstructures.org/lectures/info/info.html)
- [Data Compression Explained](http://mattmahoney.net/dc/dce.html)
- [Information Theory course — Coursera](https://www.coursera.org/learn/information-theory)
- [Mutual Information — YouTube channel](https://www.youtube.com/@Mutual_Information/videos)
- [Introduction to Information Theory — Edward Witten (Institute for Advanced Study)](https://www.youtube.com/watch?v=XYugyhoohhY)
- [Noisy-channel coding theorem — Wikipedia](https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem)
- [Information flow (information theory) — Wikipedia](https://en.wikipedia.org/wiki/Information_flow_(information_theory))
- [Lossless Image Compression in O(n) Time](https://phoboslab.org/log/2021/11/qoi-fast-lossless-image-compression)
- Li, M., Tromp, J., & Vitányi, P. (2003). Sharpening Occam's razor. *Information Processing Letters*, 85(5), 267–274.
- Wallace, C. S., & Dowe, D. L. (1999). Minimum message length and Kolmogorov complexity. *The Computer Journal*, 42(4), 270–283.
- Oliver, J. J., Dowe, D. L., & Wallace, C. S. (1992). Inferring decision graphs using the minimum message length principle. In *Proceedings of the 5th Australian Joint Conference on Artificial Intelligence*. World Scientific.
- [Algorithmic information theory — Hutter](https://www.hutter1.net/)
- [Information theory — bactra](http://bactra.org/notebooks/information-theory.html)
- [Algorithmic information theory — bactra](http://bactra.org/notebooks/algorithmic-information-theory.html)
- [Minimum description length — bactra](http://bactra.org/notebooks/mdl.html)
- Grünwald, P. D., & Vitányi, P. M. B. (2004). Shannon information and Kolmogorov complexity. *arXiv:cs/0410002*. https://arxiv.org/abs/cs/0410002
- Adami, C. (2004). The physics of information. *arXiv:quant-ph/0405005*. https://arxiv.org/abs/quant-ph/0405005
- Balduzzi, D. (2011). Information, learning and falsification. *arXiv:1110.3592*.
- [Information theory — LessWrong](https://www.lesswrong.com/w/information-theory)
- Golan, A., & Harte, J. (2022). Information theory: A foundation for complexity science. Proceedings of the National Academy of Sciences, 119(33), e2119089119. https://doi.org/10.1073/pnas.2119089119
- Rhee, A., Cheong, R., & Levchenko, A. (2012). The application of information theory to biochemical signaling systems. Physical Biology, 9(4), 045011. https://doi.org/10.1088/1478-3975/9/4/045011
- Timme, N. M., & Lapish, C. (2018). A tutorial for information theory in neuroscience. eNeuro, 5(3), ENEURO.0052-18.2018. https://doi.org/10.1523/ENEURO.0052-18.2018
- Information theory: Deep ideas, wide perspectives, and various applications. (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC7922818/
- [Variety](https://en.wikipedia.org/wiki/Variety_(cybernetics))
- [Solomon Kullback](https://en.wikipedia.org/wiki/Solomon_Kullback)
- Cover, T. M., & Thomas, J. A. (2006). *Elements of information theory* (2nd ed.). Wiley.
- Kullback, S. (1959). *Information theory and statistics*. John Wiley & Sons.
- Fisher, R. A. (1925). Theory of statistical estimation. Mathematical Proceedings of the Cambridge Philosophical Society, 22(5), 700–725. https://doi.org/10.1017/S0305004100009580 Cambridge University Press
- [Bandwagon Effect](https://en.wikipedia.org/wiki/Bandwagon_effect)
