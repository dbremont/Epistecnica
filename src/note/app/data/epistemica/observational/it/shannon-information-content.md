---
tags: [information]
---

# Shannon Information Content

> Shannon information content — self-information or surprisal — is the amount of uncertainty removed when a single outcome is observed: the rarer the outcome, the more information it carries.

It is the atom of Shannon's theory. Entropy averages it over a distribution; joint, conditional, and mutual information recombine it; divergence and cross-entropy price it under a wrong model. The [Information Theory Atlas](data/epistemica/observational/it/atlas.html) lets each of these quantities be played with directly.

## Formulation

### What is this epistemic instance?

Shannon information content is a quantitative epistemic construction: a concept that maps an event's probability to the surprise its occurrence carries. Given an outcome $x$ with probability $P(x)$, the information content is

$$I(x) = -\log_b P(x).$$

The minus sign turns the inverse relation between probability and surprise into a positive quantity; the logarithm makes information additive for independent events, since $P(x,y) = P(x)P(y)$ implies $I(x,y) = I(x) + I(y)$. The base $b$ chooses the unit: $b = 2$ gives bits, $b = e$ gives nats, $b = 10$ gives hartleys.

The concept is a companion of [Shannon Information Theory](note.html?n=epistemica/observational/shannon-information-theory.md) and the probabilistic realisation of [Entropy](note.html?n=epistemica/observational/entropy.md); its averaged form is [Shannon Entropy](note.html?n=epistemica/observational/shannon-entropy.md).

### What epistemic element type does this epistemic instance belong to?

An **Epistemic Construction** — specifically a concept that operationalises a target (the surprisal of an outcome) into a computable quantity. Read at a second remove it is a **quantitative Model**: a formula whose predictions (bits per outcome) can be compared against a source's actual statistics.

### Is the type of this `epistemic element instance` ambiguous?

The primary reading is unambiguous: it is a concept/construction, not an ontic entity and not a physical process. The secondary reading — a model — is legitimate but derivative, because the concept is applied through a probability model rather than being one. What is *not* licensed is reading it as a measure of semantic content or meaning: Shannon information is defined over probabilities alone and is silent about what an outcome signifies.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: this table decomposes one epistemic instance — the concept of Shannon information content — into its definition, its probability input, its surprisal measure, and its direct extensions. Base/unit choices, single-outcome examples, and limit cases are treated in the formulation above.
>
> Stopping rule: a row is terminal when it names a concrete epistemic construction; the extensions are not decomposed further here.
>
> Identity: Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique.
>
> Typing: the decomposition is read under the Epistemic Order; the root type is `Epistemic Construction`, and the instances are concepts, models, and theories built on self-information.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Construction` → Shannon Information Content | The concept as an epistemic construction: a map from an outcome's probability to its surprisal. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Self-Information Definition | The definitional construction: $I(x) = -\log_b P(x)$. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Probability Model | The probabilistic model supplying $P(x)$; the single input the measure consumes. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Surprisal Measure | The graded model: the negative logarithm with a chosen base (bits, nats, hartleys). |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Shannon Entropy | The averaged model: $H(X) = \mathbb{E}[I(x)]$. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Joint Entropy Model | The joint model over pairs. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Conditional Entropy Model | The residual model after conditioning. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → Cross-Entropy Model | The comparative model: expected surprisal under a wrong distribution. |
| `Epistemic Construction` → Shannon Information Content → `Epistemic Construction` → KL Divergence Model | The comparative model: directed cost of a wrong distribution. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

The concept is exact and minimal: one input (probability), one operation (negative logarithm), and one unit choice — and from it the whole architecture of the theory follows. Its additivity over independent events is what makes entropy a sum and channel capacity a rate rather than an arbitrary score.

Its limits are equally sharp. It is defined only for non-zero probabilities, so it does not assign information to impossible events. It is observer- and meaning-independent by construction — a point that is a strength for communication engineering and a defect when one wants a notion of *semantic* content. And because it is a function of a probability model, any disagreement about the model propagates into the measure: self-information is only as well-grounded as the probabilities fed to it.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Shannon Information Theory](note.html?n=epistemica/observational/shannon-information-theory.md)
- [Shannon Entropy](note.html?n=epistemica/observational/shannon-entropy.md)
- [Entropy](note.html?n=epistemica/observational/entropy.md)
- [Information Theory Atlas](data/epistemica/observational/it/atlas.html)
- Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27, 379–423.
- Cover, T. M. & Thomas, J. A. (1999). *Elements of Information Theory*. Wiley.
