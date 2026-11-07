---
tags: [note, mathematics, rule, number]
---

# Rounding

> ...

## Formulation

### What kind of epistemic element is `rounding`?

> A `Transformation Rule` — a `<<Constitutive Element>>` of the `Constitutive Substrate` of the `Numeral System`, reached through the `Epistemic Representation` lane of `Arithmetic`: the licence that rewrites a well-formed numeral into a representable neighbour at the stated precision (`3.46 ↦ 3.5` at one decimal place). The schema is owned by the canonical [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md), whose Arithmetic case is the worked reference; the rewrite licences carried by the mathematical representational systems are catalogued in [Transformation Rule](../transformation.md).

> Settled by the guide's test, and by exclusion: **not an `Epistemic Act`** — an operation specifies a result, never an order of acts, so the act that fires the rule is the `Computation` that writes the rounded numeral; **not an `Epistemic Method`** — a method is the reproducible order of acts, so the "Rounding Method"s above (round half up, round half to even, …) are selection disciplines fixing *which* value results, not routines fixing *what is done when*; **not a glyph** — `≈` and the format specifier are inert marks that say which rule fires and are themselves never transformed, while `3.5` is the product the `Computation` leaves behind; **not ontic** — the deviation of a measured quantity from its recorded value is read in the naturalis grammar, never here. Two roundings are two sittings and one rule, so it is not an `Epistemic Activity` either.

> `readable as` a `Convention` when attention falls on the halfway-case and precision choices — the guide types those as `Convention`s of the same substrate — and as an `Epistemic Error` when attention falls on the deviation the rewrite introduces (`Rounding Error` below).

### What is the recursive instance decomposition of this `epistemic instance`?

> The path below follows the guide's Arithmetic case: the rule is reached from the practice through the representation lane, and it lives nowhere else. The four rounding schemes of the tables above are four instances of the rule type; the halfway-case and precision choices are `Convention`s of the same substrate; the deviation the rewrite introduces is an `Epistemic Error` of the practice.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic | The practice whose notation rounding constitutes: reckoning over positional numerals at a stated precision. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` | Grouping: representations of number. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System | The positional system of signs with place rules whose numerals rounding rewrites. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` | Grouping: rules and structures constituting the system. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` | Grouping: rewrite licences selecting the representable value at the stated precision. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Nearest-Value Rounding Rule | Rewrite licence: the representable neighbour — `3.46 ↦ 3.5` at one decimal place; halfway cases deferred to the Tie-Breaking Convention. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Directed Rounding Rule | Rewrite licence: the neighbour in the prescribed direction — `2.3 ↦ 3` toward positive infinity, `2.7 ↦ 2` toward negative infinity or toward zero, `-2.3 ↦ -3` away from zero. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Stochastic Rounding Rule | Rewrite licence: a neighbour drawn by relative position — `3.2 ↦ 3` with probability 0.8, `3.2 ↦ 4` with probability 0.2. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Truncation Rule | Rewrite licence: discard digits beyond the stated precision without adjusting the retained ones — `3.49 ↦ 3.4`. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: stabilized notational choices completing the rewrite. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Tie-Breaking Convention | The halfway-case choice: half up, half down, half to even, half to odd, half away from zero, half toward zero. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Precision Convention | The retained places fixed for a body of work — decimal places and significant figures: one place turns `3.46` into `3.5`. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Rounded Numeral | The rewritten token the act leaves behind — `3.5` standing for `3.46` at one decimal place. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` | Grouping: assessments of rounding. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Error` (→ Instance) Rounding Error | The deviation of the rounded numeral from the value it stands for — `|3.46 - 3.5| = 0.06`, bounded by half the last retained place. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) IEEE 754 Rounding Standard | The norm floating-point rounding is judged against: prescribed formats, the four direction rules, and `roundTiesToEven` as the default tie-break. |

## Terminology

| Concept | Description |
|---|---|
| Rounding | Replacing a numerical value with another value at a specified level of numerical precision. |
| Rounding Precision | The positional or decimal precision to which a number is rounded. |
| Rounding Method | A specific procedure for determining the rounded value. Examples: rounding half up, rounding half to even, rounding toward zero. |
| Rounding Scheme | A system of rounding conventions that specifies the applicable rounding methods, precision requirements, and tie-breaking rules. |
| Rounding Rule | A rule determining which representable value is selected for a given input. |
| Rounding Direction | The direction in which a value is approximated. |
| Rounding Error | The difference between the original and rounded values. |
| Significant Figures | Digits used to express the precision of a numerical value. |
| Tie-Breaking Rule | The convention used when two candidate rounded values are equally close. |
| Truncation | Discarding digits without adjusting the last retained digit. |

## What Are the Rounding Schemes and Methods?

| Rounding Scheme | Description | Case | Methods Set |
|---|---|---|---|
| **Nearest-Value Rounding** | Selects the representable value closest to the original value. | \(3.46 \rightarrow 3.5\), to one decimal place. | Round Half Up; Round Half Down; Round Half to Even; Round Half to Odd; Round Half Away from Zero; Round Half Toward Zero. |
| **Directed Rounding** | Selects a representable value according to a specified direction, rather than minimizing the absolute rounding error. | \(3.41 \rightarrow 4\), toward positive infinity. | Round Toward Positive Infinity (Ceiling); Round Toward Negative Infinity (Floor); Round Toward Zero; Round Away from Zero. |
| **Stochastic Rounding** | Selects between neighboring representable values according to probabilities determined by the original value's relative position between them. | \(3.2 \rightarrow 3\) or \(4\), with probabilities \(0.8\) and \(0.2\), respectively. | Probabilistic Neighbor Selection. |
| **Truncation** | Discards digits beyond the specified precision without adjusting the retained digits. | \(3.49 \rightarrow 3.4\), to one decimal place. | Decimal Truncation; Integer Truncation. |

## What Are the Rounding Methods?

| Method | Description | Case |
|---|---|---|
| Round Half Up | Selects the nearest value; halfway cases are rounded up in magnitude for positive numbers. | \(2.5 \rightarrow 3\) |
| Round Half Down | Selects the nearest value; halfway cases are rounded toward zero. | \(2.5 \rightarrow 2\) |
| Round Half to Even | Halfway cases are rounded to the nearest value with an even last retained digit. | \(2.5 \rightarrow 2;\ 3.5 \rightarrow 4\) |
| Round Half to Odd | Halfway cases are rounded to the nearest value with an odd last retained digit. | \(2.5 \rightarrow 3;\ 3.5 \rightarrow 3\) |
| Round Half Away from Zero | Halfway cases are rounded away from zero. | \(2.5 \rightarrow 3;\ -2.5 \rightarrow -3\) |
| Round Half Toward Zero | Halfway cases are rounded toward zero. | \(2.5 \rightarrow 2;\ -2.5 \rightarrow -2\) |
| Round Toward Positive Infinity | Selects the smallest representable value greater than or equal to the original value. | \(2.3 \rightarrow 3\) |
| Round Toward Negative Infinity | Selects the largest representable value less than or equal to the original value. | \(2.7 \rightarrow 2\) |
| Round Toward Zero | Discards the fractional part, moving toward zero. | \(2.7 \rightarrow 2;\ -2.7 \rightarrow -2\) |
| Round Away from Zero | Selects the next representable value away from zero. | \(2.3 \rightarrow 3;\ -2.3 \rightarrow -3\) |
| Stochastic Rounding | Selects one of the two neighboring representable values probabilistically, according to their relative distances from the original value. | \(2.3 \rightarrow 2\) (70%) or \(3\) (30%). |
| Round to Odd | For inexact conversions, selects a representable value with an odd least significant digit. | \(2.3 \rightarrow 3\), at integer precision. |
| Truncation | Discards digits beyond the specified precision without adjusting the retained digits. | \(2.9 \rightarrow 2\). |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) — the `<<Constitutive Element>>` slot, the Arithmetic case study, and the §QA "Is multiplication an `Epistemic Act`, an `Epistemic Method`, or a constituent of the representation?"
- [Transformation Rule](../transformation.md) — the rewrite-licence catalogue the rounding rules are members of
- [Rounding](https://en.wikipedia.org/wiki/Rounding)
- National Institute of Standards and Technology. (2019). IEEE standard for floating-point arithmetic (IEEE Std 754-2019). IEEE. IEEE 754-2019
- Higham, N. J. (2002). Accuracy and stability of numerical algorithms (2nd ed.). Society for Industrial and Applied Mathematics.
- Barlow, R. (1989). Statistics: A guide to the use of statistical methods in the physical sciences. John Wiley & Sons.

