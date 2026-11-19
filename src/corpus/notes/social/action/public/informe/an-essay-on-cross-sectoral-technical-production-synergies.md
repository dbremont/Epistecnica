---
tags: [note, industrial-policy, diversification, technology, production]
---

# An Essay on Cross-Sectoral Technical-Production Synergies: Technical Overlap over the Product Space

> The standard theory of diversification is a theory of **nearness in a space of traded goods**. A country makes what it is close to making, and closeness is inferred from what it already exports together. That map is useful, and it has a blind spot: the product space is built from an **outcome** — co-export — so it cannot tell a shared *market* from a shared *technique*. Two goods can sit next to each other because they travel through the same distributors, or because the same cleanroom, the same vacuum pump and the same process vocabulary make them.

> This essay argues for a different coordinate: the **technical-production overlap** between two sectors — the equipment, process steps, metrology, standards and skills they share — and takes one case where the difference is stark. Semiconductor equipment and solar-panel equipment are different products in different markets, sitting far apart in the trade statistics, and built with an unusually large share of the same capital stock and the same know-how. If the product space is the better map, this case should look improbable. It is not improbable. It is what the industry did.

**Core questions**

- What does the product space measure, and what does it systematically miss?
- What is technical-production overlap, and how is it measured?
- Why did the semiconductor equipment base transfer into solar, and why did it not transfer back?
- If overlap predicts diversification, why did so many of the overlapping firms fail?
- What does a policy that targets overlap do differently from one that targets related products?

## The Product Space and Its Blind Spot

> The product space of Hidalgo and Hausmann places every traded product in a network whose edges measure **proximity**: the conditional probability that a country exporting one good also exports the other, adjusted for how ubiquitous each good is. The empirical finding is that countries move along those edges — diversification is path-dependent, and the path runs through what the country already does.

The construction has three virtues that keep it in use. It is **measurable** from trade data alone, it **predicts** the direction of subsequent diversification with real success, and it produces the useful complement — economic complexity — that explains income differences better than the volume of trade. It also has three limits that matter for the question this essay asks.

| Limit | What it means |
| --- | --- |
| **Co-export is an outcome, not a cause** | Two goods are proximate because they are made or sold together, which may be for reasons of technique, of market, of raw material, or of a chance historical bundle |
| **The space is national and static** | It describes what a country has already assembled, not what an existing plant could be reconfigured to make |
| **The classification hides the plant** | Trade codes classify the *good*; the capability lives in the **equipment and the process**, which the codes do not name |

> The third limit is the one that this essay presses. A country that exports semiconductors and a country that exports solar panels may appear distant because their exports are different goods with different buyers. But the question of whether the second can be built from the first is not a question about goods at all. It is a question about whether the same furnaces, the same deposition tools, the same cleanroom discipline and the same process engineers can be pointed at a different product.

## What Technical Overlap Is

> **Technical-production overlap** is the share of the production stack that two products have in common. The stack has five layers, and overlap can be assessed layer by layer — which is what makes the concept operational rather than metaphorical.

| Layer | What is shared | Semiconductor device | Solar cell |
| --- | --- | --- | --- |
| **Capital equipment** | Furnaces, deposition, etch, vacuum, wet benches, laser tools | Diffusion, CVD/PVD/ALD, plasma etch, CMP, lithography, implant | Diffusion, PECVD, sputter, wet processing, laser scribing/edge isolation |
| **Process know-how** | The vocabulary of the steps: clean, deposit, dope, pattern, anneal, measure | Nanometre tolerances, many mask layers | Micrometre tolerances, few patterning steps |
| **Metrology and quality regime** | How the product is measured and the process controlled | Ellipsometry, CD-SEM, yield analysis, SPC | Sheet resistance, ellipsometry, IV/luminescence, SPC |
| **Contamination and environment** | Cleanroom class, gas and chemical purity, particle control | Very strict, front-end grades | Strict but tolerant of a coarser class in many steps |
| **Skills and standards** | Process engineers, equipment maintenance, automation, certification | Deep specialisation, SEMI standards | The same roles, a different product specification |

> The essential point is that overlap is a property of the **plant**, not of the good. It can be large between two products that no trade statistic places near each other, and small between two products that share a code family — two goods can be in the same HS chapter and share no equipment at all. This is why the product space and the technical overlap can disagree, and why the disagreement is informative.

> The direction of transfer is also asymmetric, and this is the second essential point. Precision flows **downward** more easily than upward: a plant and a workforce built to nanometre tolerances can be relaxed into micrometre work, while the reverse requires buying the precision that the cheaper plant never had. Overlap, in other words, is not symmetric between two sectors even when it looks symmetric on a list of equipment.

## Semiconductors into Solar

> The case is the one that makes the concept visible, because it is large, recent, and documented in the order books of the equipment makers rather than in a policy document.

### What transfers

- **Deposition.** PECVD for silicon nitride antireflection coatings and for thin-film silicon; sputtering for transparent conductive oxides and metal contacts. These are the same tool families, with different recipes and a much larger substrate.
- **Diffusion and annealing.** Tube furnaces for dopant diffusion and oxidation, in both industries, with the same handling discipline.
- **Wet processing.** Cleaning, texturing and etching benches — different chemistry, same architecture and same chemical-hygiene requirements.
- **Vacuum and gas delivery.** Pumps, abatement, gas cabinets, leak checking — a substantial share of the plant, and the layer with the highest overlap in cost terms.
- **Laser processing.** Scribing and edge isolation in thin-film solar; dicing and annealing in semiconductors.
- **Metrology and control.** Sheet resistance, ellipsometry, photoluminescence and IV testing on the solar side; the same measurement culture, SPC and yield analysis, and the same MES layer that schedules the line.
- **Cleanroom and facilities.** The building, the contamination discipline, the utility plant.

### What does not transfer

| Dimension | Semiconductor | Solar |
| --- | --- | --- |
| **Tolerance** | Nanometres; overlay and critical dimension are the product | Micrometres to millimetres; area and uniformity matter more than feature size |
| **Cost logic** | Performance-priced: the customer pays for speed and yield | Commodity-priced in $/W: the customer buys the cheapest watt |
| **Throughput** | Wafers per hour through a complex route | Square metres per minute through a short route |
| **Market and certification** | Design houses, foundries, long qualification cycles | Project developers, utilities, bankability and warranty regimes |
| **Patterning** | Lithography is the core competence and the capital bottleneck | Screen printing and laser scribing replace it; lithography is mostly absent |

> The overlap is therefore real and partial at the same time: the **furniture** of the plant transfers — the deposition, the furnaces, the vacuum, the metrology culture — while the **purpose** of the line changes completely, from precision to area and from performance to cost.

### Who shows the overlap

> The equipment makers are the evidence. Firms that had built their business on semiconductor or display tools sold turnkey photovoltaic lines and process equipment in the 2000s: Applied Materials with its thin-film SunFab line, centrotherm and Manz in Germany, Meyer Burger in Switzerland, Von Ardenne and others in the German and Japanese Vacuum cluster. On the producer side, several of the large Chinese photovoltaic manufacturers began as semiconductor silicon or electronics firms, and the display industry — amorphous-silicon thin-film transistor lines — supplied both the process know-how and, in several cases, the people.

> This is the strongest form of the evidence, because it is the **supply side** revealing the overlap: an equipment maker sells the same competence into both markets, and the decision to do so is a commercial judgement that the overlap is real.

### Why the overlap did not save the overlapping firms

> The honest part of the case is the aftermath. Applied Materials exited thin-film solar in 2010; centrotherm went through insolvency in 2012; Meyer Burger has been restructuring through the 2020s. The equipment overlap was real and the businesses still failed, for reasons the overlap could not address: a collapse in module prices driven by Chinese scale, a capex cycle that punished anyone holding photovoltaic capacity, and a customer base that could not pay for precision it did not need.

> That is the essay's central caution. **Overlap is necessary and not sufficient.** It tells you that a capability can be pointed at a second product; it says nothing about whether the second product's market will pay for the capability. A theory of diversification built only on overlap would have predicted the entry and missed the exit.

## Why the Overlap Matters for Policy

> If the production stack is the right unit, then three policy conclusions follow, and each of them contradicts a habit of product-space thinking.

**Map the stack, not the classification.** A target sector should be described as a list of equipment, process steps, metrology and skills, not as a trade code. The exercise is unglamorous and it is the one that answers the question: which of these layers exists here, and which must be imported, bought or built?

**Relatedness is a hypothesis, not a measurement.** Co-export proximity is a statistical proxy for a capability relation that can be checked directly — by looking at the equipment, the firms and the labour flows. Skill-relatedness measures, which infer relatedness from worker mobility between industries, are a better proxy than trade for exactly this reason, and they point at the same object: the people and the tools, not the goods.

**The missing link is usually one layer, not the whole stack.** In the semiconductor-to-solar case the missing layers were screen printing, the cost discipline and the market access; the deposition, furnaces and metrology were present. Policy that treats a target as a monolith spends on what already exists and underinvests in the one layer that decides the outcome. The test is to name the missing layer explicitly, and then to decide whether it can be bought, partnered for, or must be built — three very different budgets.

> There is also a caution for the cluster literature. A cluster is a geographic concentration of a production stack, which is precisely why it is the natural vehicle for cross-sectoral transfer: the equipment, the technicians and the metrology laboratory are all in one place, and the second product can be tried without moving them. The cluster is not a location effect that happens to industries; it is the physical form of the overlap.

## A Test, Not a Map

> The essay's practical residue is a five-column frame, applied to a candidate product before any incentive is designed.

| Column | Question | Semiconductor-to-solar example |
| --- | --- | --- |
| **Equipment** | Which tool families does the product need, and which exist here? | Deposition, furnaces, vacuum and wet benches — present; screen printer — missing |
| **Process** | Which steps are the same, and which are new? | Clean, dope, deposit, measure — same; metallisation by printing — new |
| **Metrology** | Can the product be measured and the process controlled here? | Same measurement culture; new IV and luminescence tests — cheap to add |
| **Skills** | Who can run the line, and where do they come from? | Process engineers and maintenance technicians transfer; printing specialists do not |
| **Missing link** | Which one layer decides the outcome? | Cost engineering and market access, not technology |

> The output of the test is not a score but a **sentence**: this product is reachable from this stack if we acquire *this* layer, and the case rests on *that*. A policy that cannot write the sentence is not doing overlap analysis; it is renaming an aspiration.

## Conclusion

> The product space is a shadow of the production system, and a shadow is a useful thing until it is mistaken for the object. What a country can make next is determined by the equipment it owns, the processes its engineers have run, and the metrology culture it has built — and those are properties of plants and people, not of export codes. Semiconductor equipment into solar panel equipment is the clean case: two products that the trade statistics separate and the factory floor does not.

> The lesson is not that overlap guarantees success. The equipment makers that made the transfer mostly did not survive the market that followed it, which is the strongest evidence that overlap answers only half the question. It tells you what is *possible* to build from what exists. The other half — whether anyone will buy it at a price that pays for the plant — is not answered by the production stack at all, and a policy that confuses the two will be right about the capability and wrong about the outcome.

## References

- [Economic Complexity](/view.html?p=notes/epistemica/complexity/economic-complexity.md) — the complexity index and the product-space frame this essay argues beside
- [Economic Diversification](/view.html?p=notes/social/action/problem/dimension/production/diversification/economic-diversification.md) — diversification policy and its smart-specialisation variant
- [Cluster](/view.html?p=notes/social/action/problem/dimension/production/cluster/cluster.md) — the cluster as the physical form of a production stack
- [Productive Policy](/view.html?p=notes/social/action/public/productive-policy.md) — the policy frame the test belongs to
- [A Defense of Industrial Policy](/view.html?p=notes/miscellanea/unclassified/a-defense-of-industrial-policy.md) — the case for intervention the overlap test has to serve
- [The Defense Industry as Catalyst of General Technical Progress](/view.html?p=notes/social/action/public/informe/the-defense-industry-as-catalyst-of-general-technical-progress.md) — the companion essay on capability transfer through procurement
- [Semiconductor Fabrication](/view.html?p=notes/technica/production/industry/semiconductor-fabrication.md) — the process route whose equipment is half of the overlap
- [Semiconductor](/view.html?p=notes/nature/semiconductor.md) — the material and device reading
- [Solar Energy](/view.html?p=notes/nature/solar-energy.md) — the conversion the photovoltaic line performs
- Hidalgo, C. A., & Hausmann, R. (2009). The building blocks of economic complexity. *PNAS*, 106(26), 10570–10575.
- Hidalgo, C. A., et al. (2018). *The Atlas of Economic Complexity*. MIT Press.
- Neffke, F., & Henning, M. (2013). Skill relatedness and firm diversification. *Strategic Management Journal*, 34(3), 297–316.
- Boschma, R. (2017). Related diversification and smart specialisation. In *Advances in the Theory and Practice of Smart Specialisation*.
- Perez, C. (2002). *Technological Revolutions and Financial Capital*. Edward Elgar.
