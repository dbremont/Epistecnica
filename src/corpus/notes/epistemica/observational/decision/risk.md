---
tags: [note, risk, decision, uncertainty, probability]
qa:
 - Is the probability in "risk = probability × consequence" a frequency, a degree of belief, or a market price — and does the answer change the number?
 - Does a risk that no one dreads and a risk everyone dreads of the same expected magnitude belong in the same register?
 - If Knight is right that uncertainty is unmeasurable, what exactly is being measured by a risk model?
---

# Risk

> **Risk** is exposure to an outcome that is not certain and that matters — the possibility of loss, damage, or failure, together with the chance that it occurs. The word names a *relation* between an action or a situation and an uncertain future, not a thing in the world: the same flood is a risk to the house, an opportunity to the boatbuilder, and a variable in the insurer's model.

> Two different quantities travel under the same word, and the corpus must keep them apart. **Risk** in the decision-theoretic sense is a probability distribution over outcomes — measurable, comparable, and priceable. **Uncertainty** in Knight's sense is the part that cannot be assigned a probability at all: the outcome space is not known, or the situation has no repeatable reference class. Most practical "risk management" is the attempt to move the second into the first — to make the unmeasurable measurable enough to act on — and the attempt is always partly a construction.

## Formulation

**What epistemic element type does this risk instance belong to?** A `Concept` — a determinable feature of decisions and situations, not an event. It is predicated over a state-trajectory: risk attaches to what might happen, and it is carried by the agent that chooses, owns, or suffers the outcome. The corpus files the *instances* elsewhere (`country-risk`, a firm's risk register, an insurer's book) and keeps the general concept here, at the root of the decision shelf.

**What is this risk instance?** The exposure relation between an agent, a hazard, and an uncertain consequence, read at the level of a decision. It has three components that are routinely confused:

| Component | Question it answers | Example |
| --- | --- | --- |
| **Hazard** | What could do harm? | A pathogen, a flood, a leveraged position, a supplier with one plant |
| **Exposure** | Who or what is in its path, and how much? | The population downstream, the notional held, the days of inventory |
| **Vulnerability** | How much harm does the exposure convert into? | Building codes, capital buffers, substitutable inputs |

Risk is the composition of the three. A hazard with no exposure is not a risk; exposure with no vulnerability is a nuisance. This decomposition is why the same hazard produces different risks in different places, and why "the risk is high" without naming the exposure is not a statement about anything.

**Is the type unambiguous?** No, and the ambiguity is productive. Read as **epistemic**, risk is a probability distribution and a decision rule over it; read as **social**, it is an institution — insurance, regulation, liability, the risk register — that distributes the consequences; read as **natural**, it is a property of a physical situation (a slope, a storm, a pathogen). The three readings are the same situation under three descriptions, and the corpus keeps them separate rather than choosing one.

## Risk and uncertainty

Frank Knight's distinction (*Risk, Uncertainty and Profit*, 1921) is the founding move: **risk** is a known probability distribution over known outcomes — insurable, because a reference class exists; **uncertainty** is the residual, where no distribution can be assigned and the outcome is genuinely novel. Profit, on Knight's account, is the reward for bearing the second, not the first.

The distinction has been refined rather than settled. **Ambiguity** (Ellsberg, 1961) is uncertainty about the probabilities themselves — the decision-maker knows the outcomes but not their weights, and behaves differently from a decision-maker who does. **Model uncertainty** is uncertainty about the structure that generates the outcomes, which no parameter distribution captures. **Black swans** (Taleb) name the tail where the reference class fails altogether. In each case the practical question is the same: which part of the situation has been made measurable, by what warrant, and what was assumed away to make it so.

## Measurement

Risk is quantified in three families, and they answer different questions:

- **Expected loss** — $\mathbb{E}[L] = \sum_i p_i L_i$ over the loss distribution. The long-run average, and the number that prices insurance. It is silent about the tail: two portfolios with identical expected loss can differ in the probability of ruin.
- **Dispersion** — variance or standard deviation of the loss. Treats upside and downside symmetrically, which is why it is a poor fit for risk that only hurts.
- **Tail measures** — value at risk (VaR), the loss not exceeded with probability $1-\alpha$, and expected shortfall (CVaR), the average loss conditional on exceeding it. VaR is the regulatory convention and is blind beyond its threshold; CVaR is coherent but needs the tail modelled, which is exactly where the data are thinnest.

The choice of measure is not technical. It determines which risks are visible to the institution that uses it, and every measure makes some risks invisible by construction.

## Risk perception and the social reading

Objective frequency and perceived risk diverge systematically. Slovic's psychometric work found that dread (involuntary, catastrophic, uncontrollable) and unknown (unobservable, delayed, unfamiliar) predict perceived risk better than annual fatality counts: nuclear power and pesticides rank high, driving and domestic accidents low, in inverse proportion to their tolls. The divergence is not public irrationality to be corrected — it is a different question being answered. A community asked "how bad is this?" answers about agency, control, and fairness, not about expected deaths.

This is why risk is an institution as much as a quantity. Insurance pools and prices it; regulation sets acceptable levels and allocates the duty to reduce it; liability moves the cost to the party that can bear or prevent it; the risk register makes it visible to an organisation that would otherwise ignore it. - [Insurance](/view.html?p=notes/technica/business/toolkit/risk/insurance.md) for the pooling mechanism and [Safety](/view.html?p=notes/social/good/safety.html) for the hazard-class reading of consumer products.

## In the corpus

- [Country Risk](/view.html?p=notes/social/observation/state/country-risk.md) — the sovereign instance: default, expropriation, currency and political risk priced into cross-border capital.
- [RD 1.0 Dominican Risk Management System](/view.html?p=notes/social/koinomia/collective/polity/instance/dom/security/risk.md) — a national risk-management *system* as an institutional instance.
- [Decision Making](/view.html?p=notes/epistemica/observational/decision/decision-making.md) · [Decision Problem](/view.html?p=notes/epistemica/observational/decision/decision-problem.md) — the setting in which risk is evaluated.
- [Expected Value](/view.html?p=notes/epistemica/observational/probability/expected-value.md) — the expectation the expected-loss measure is built on.

## References

- Knight, F. H. (1921). *Risk, uncertainty and profit*. Houghton Mifflin. — the distinction the concept turns on: measurable risk versus unmeasurable uncertainty.
- Kornai, J. (1980). *Economics of shortage*. North-Holland. — the soft budget constraint as an institutional risk transfer, and the shortage economy as its consequence.
- Slovic, P. (1987). Perception of risk. *Science*, 236(4799), 280–285. — dread and unknown as the dimensions of perceived risk.
- Ellsberg, D. (1961). Risk, ambiguity, and the Savage axioms. *The Quarterly Journal of Economics*, 75(4), 643–669. — ambiguity aversion: the probability itself can be uncertain.
- Beck, U. (1986). *Risikogesellschaft: Auf dem Weg in eine andere Moderne* [Risk society: Towards a new modernity]. Suhrkamp. — risk as a produced, distributed and politicised social good.
- ISO 31000:2018. *Risk management — Guidelines*. International Organization for Standardization. — the standard definition: risk as the effect of uncertainty on objectives, explicitly including upside.
- [Risk — Wikipedia](https://en.wikipedia.org/wiki/Risk)
