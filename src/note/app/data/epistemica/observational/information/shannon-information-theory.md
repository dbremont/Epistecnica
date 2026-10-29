---
tags: [information]
---

# Shannon Information Theory

 : Information Geometry (Information%20Geometry%209e8f47513e9c4b8ba9e9450c52dced78.md), Information (Information%2017ac0f5171ec813d813ff6055c98fe7d.md), Probability (Probability%204210c322839242cd8cc944b9b1e7c27f.md)

> In this note, we introduce Shannon Information Theory—not in terms of everyday notions of information, but as a formal theory of **Rarity = Novelty**, where information quantifies **how unlikely an outcome is**.
> 

> Shannon’s Information Theory is the mathematical theory of the representation, transmission, and compression of signals or data, quantifying information as the reduction of uncertainty, independent of meaning.
> 

> Information Theory uses probability to build a **set of abstractions** that quantify uncertainty, information content, and the limits of communication, independent of meaning.
> 

> **Shannon Information Theory** is a **mathematical tool to study communication systems**, quantify information, and set limits on transmission. It **does not by itself transmit messages** or implement encoders/decoders — those are practical applications inspired by the theory.
> 

> Shannon’s Information Theory builds a tower of abstractions to study the properties of communication systems. It abstracts away meaning and physical implementation, focusing instead on probabilities, uncertainty, and the fundamental limits of transmitting information reliably.
> 

> Shannon entropy  is given this Probability Model,  how capable are we of reducing the space - in which an outcome fall in?
> 

> Probability quantifies uncertainty and the range of possible outcomes, and Shannon Information builds on this to formalize the related concept of unpredictability.
> 

Doing:

- [ ]  Is Shannon’s information theory a theory of communication efficiency, that is, of compression and reliability?
    - [ ]  **Compression** (source coding) and  → What is the minimum number of bits needed to represent the message?
    - [ ]  **Reliability** (channel coding)  → How can we send the message perfectly across a noisy channel?
    - [ ]  Source-channel Separation Theorem.
- [ ]  We need examples of encoding schemes.

## Problem Formulation

> Data →  (**Encoding)** Representation → **(Decoding)** Recovered Data.
> 

> (**Reconstruction Fidelity**) Suppose we are given some data $d$ to transmit. What encoding $E_d$ of $d$ would ensure that $d$ can be reliably and unambiguously reconstructed from its encoded form ($E_d$) — that is, such that $\text{decoded}(E_d) ≈ d$?
> 

> (**Informational Content**) In other contexts, suppose the original data $d$ is unknown, but we are given its encoding $E_d$. How much information does $E_d$ convey? That is, how many distinct interpretations of $E_d$ are possible? The fewer the interpretations, the more informative $E_d$ it is.
> 

> **Data is transformed** into a **latent representation**. Through a sequence of Yes/No questions (a decision process), we aim to **uncover the set of possible values** that the **latent representation encodes** or corresponds to **upon materialization**.
> 

## Formulation

> **Event → Shannon Information → Entropy → Mutual Information → Channel Capacity → Coding**
> 

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
> 

> In Shannon’s framework, an event is treated as a symbol or signal whose occurrence has a probability $P(x)$ and contributes Shannon information $I(x) = -\log P(x)$.
> 

> Events are the basic units from which entropy, mutual information, and other measures are calculated.
> 

### Shannon Information

> **Shannon information** (also called **self-information**) is a measure of the **amount of uncertainty reduced** when an event occurs. It is **quantitative**, not semantic—it doesn’t measure meaning —  **unpredictability** of an outcome.
> 

> Formally, if an event $X = x$ has probability $P(x)$, the **Shannon information** associated with that event is: $I(x) = -\log_b P(x)$.
> 

> Why it’s it called self-information?
> 

> Is surprisal → rarity? Why -logb and not log?   Why log at all? How to think about different measure of surprisal? Why not P(x)? Isn just surprisal an interpretation? P(x) high non surprising, P(x) small surprising.
> 

> What kind of element is this? Technical, Epistemic, or What?
> 

> See the dedicated note on [Shannon Information Content](note.html?n=epistemica/observational/information/shannon-information-content.md) and the [Information Theory Atlas](data/epistemica/observational/information/atlas/atlas.html) for its operational quantities.

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
> 

## Uses

> See [Entropy Realization](entropy.md).
> 

## Limitations

> **'Information,' as captured in Shannon's theory**, is its measure of 'surprise' or unpredictability. However, this definition is quite narrow, as it does not account for meaning, relevance, or contextual significance. While Shannon entropy quantifies uncertainty reduction in a system, other dimensions of information—such as its semantic content, pragmatic use, and its role in knowledge formation—go beyond mere statistical encoding.
> 

## QA

- Ho  do we get the probability distribution for the Alphabet of Symbols?

## References

- [**Entropy**](entropy.md)
- Li, Ming, John Tromp, and Paul Vitányi. “Sharpening Occam’s razor.” Information Processing Letters 85.5 (2003): 267-274.
- https://computationstructures.org/lectures/info/info.html
- https://en.m.wikipedia.org/wiki/Noisy-channel_coding_theorem
- http://bactra.org/notebooks/information-theory.html
- http://bactra.org/notebooks/algorithmic-information-theory.html
- https://www.lesswrong.com/w/information-theory
- https://arxiv.org/abs/quant-ph/0405005
- http://bactra.org/notebooks/mdl.html
- https://en.m.wikipedia.org/wiki/Information_flow_(information_theory)
- [Data Compression Explained](http://mattmahoney.net/dc/dce.html)
- https://arxiv.org/abs/cs/0410002
- [An Introduction to Kolmogorov Complexity and Its Applications](https://homepages.cwi.nl/~paulv/kolmogorov.html)
- https://www.hutter1.net/
- [Information Theory From Coding to Learning](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf)
- [Mutual Information](https://www.youtube.com/@Mutual_Information/videos)
- [Lossless Image Compression in O(n) Time](https://phoboslab.org/log/2021/11/qoi-fast-lossless-image-compression)
- https://www.youtube.com/watch?v=XYugyhoohhY
- Wallace, Chris S., and David L. Dowe. “Minimum message length and Kolmogorov complexity.” The Computer Journal 42.4 (1999): 270-283.
- Oliver, JONATHAN J., David L. Dowe, and C. S. Wallace. “Inferring decision graphs using the minimum message length principle.” Proceedings of the 5th Australian Joint Conference on Artificial Intelligence. Singapore: World Scientific, 1992.
- [**Statistics and Information Theory]** [https://web.stanford.edu/class/stats311/lecture-notes.pdf](https://web.stanford.edu/class/stats311/lecture-notes.pdf)
- Balduzzi, David. “Information, learning and falsification.” arXiv preprint arXiv:1110.3592 (2011).
- [‣](https://app.notion.com/p/27c598edb79080acbdb7e481c007c38a?pvs=21)
- https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/
- https://www.coursera.org/learn/information-theory
