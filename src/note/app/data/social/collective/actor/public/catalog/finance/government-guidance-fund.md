---
tags: [guidance-fund, china, industrial-policy, capital, actor]
---

# Government Guidance Fund

> A **Government Guidance Fund** (GGF, 政府引导基金) is a state-seeded investment fund that guides private capital into state-selected priority sectors — the financial vehicle of Chinese industrial policy since 2005, typically structured as a fund of funds.

## Formulation

### What social element type does this social instance belong to?

**Government Guidance Fund belongs to the `Capital / Labor` social element type — a multi-layer economic operator pooling resources and directing productive capacity.**

It is a capital pool with a policy compass: governments (central and local) commit seed capital that leverages a multiple of social capital, managed with private venture partners toward sectors the state prioritizes. Its layer is read twice — **Ontic** as the committed pool and legal entity, **Synontic** as the recognized claim and sector signal markets act upon — which is why it types as a Multi operator rather than a plain fund. Its facet is economic. A guidance fund is not a `Firm` (it guides rather than operates) and not a `Policy` (it is the capitalized instrument, not the rule itself).

### What is this social instance?

> A guidance fund fixes *where directed capital goes*: the state commits seed money, private partners multiply it, and the combined pool is steered into priority sectors — semiconductors, emerging industries, small enterprises — that struggle to secure market funding. Deployed by China from 2005 to accelerate technological catch-up; by 2021 more than 1,800 GGFs carried an estimated $1.52 trillion in target capital, though only about 26 per cent had met their targets — the ambition/implementation gap (Wei/Ang/Jia).

### What is the recursive instance decomposition of this social instance?

> Boundary: one generic Government Guidance Fund — mechanism plus exemplar funds only.
>
> Stopping rule: a row is terminal when it names a mechanism component or an exemplar fund.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| Capital / Labor `(→ Part)` Government Guidance Fund | State-seeded fund guiding private capital into priority sectors. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Part)` Price / Asset | Grouping: capital components of the fund. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Part)` Price / Asset `(→ Part)` Seed Capital | Fiscal commitment anchoring the fund and signaling state priority. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Part)` Price / Asset `(→ Part)` Leveraged Social Capital | Private multiple raised on the seed through fund-of-funds structures. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Component)` Institution | Grouping: rules stabilizing the fund's operation. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Component)` Institution `(→ Component)` Sector Mandate | Policy rule bounding which sectors the fund may enter. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Part)` Social Relation / Network | Grouping: ties binding the fund to its partners. |
| Capital / Labor `(→ Part)` Government Guidance Fund `(→ Part)` Social Relation / Network `(→ Part)` Venture Partnership Web | Ties to private VC managers executing the investments. |

## QA

### Which government guidance funds operate in China?

> - **National Integrated Circuit Industry Investment Fund ("Big Fund")** — the flagship: Phase I (2014, ¥138.7bn), Phase II (2019, ¥204bn), Phase III (2024, ¥344bn / ~$47.5bn) into semiconductors, from equipment and materials to DRAM; financed SMIC, Hua Hong, Yangtze Memory.
> - **Shenzhen Venture Capital Guidance Fund** — local-exemplar: municipal seed guiding venture capital into Shenzhen's startups.
> - **National Emerging Industry Venture Capital Guidance Fund** — central-level fund steering venture capital into strategic emerging industries.
> - **National SME Development Fund** — central-level fund broadening capital access for small and medium enterprises.
>
> *Observation: not all of these are pure fund of funds. The Big Fund takes direct operating stakes — equity in SMIC, Hua Hong, Yangtze Memory (per the Taipei Times/Fortune references below) — while Shenzhen-style vehicles work through sub-funds and VC managers. The type spans a spectrum from pure fund-of-funds allocation to direct operating investment, and any classification of a given GGF must state where on that spectrum it sits.*

## References

- Wei, Ang, Jia, "The Promise and Pitfalls of Government Guidance Funds" (SSRN, 2022) — instrument definition (2005), scale (1,800+ GGFs, $1.52T target), implementation gap
- [State Council: six banks invest in Big Fund III](https://english.www.gov.cn/news/202405/29/content_WS66569746c6d0868f4e8e7987.html) (Phase III ¥344bn capital, bank shares)
- [Fortune: Big Fund III $47.5B](https://fortune.com/asia/2024/05/28/more-confident-china-doubling-down-big-fund-iii-semiconductors-development-us-controls) (doubling-down reading)
- [Nikkei Asia: Big Fund III spending](https://asia.nikkei.com/business/tech/semiconductors/china-s-3rd-semiconductor-big-fund-starts-spending-47bn-war-chest) (outside-capital attraction)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [China](note.html?n=social/collective/actor/public/polity/chn/prc/china.md) (State R&D finance row: the policy lineage)
- [Market](note.html?n=social/coordinator/market/market.md) (arena guided capital enters)
- Graph nodes of the same names: `government-guidance-fund`, `reality.market` (Social Space, dataset `social`); instance stubs: `National Integrated Circuit Industry Investment Fund (Big Fund)`, `Shenzhen Venture Capital Guidance Fund`
