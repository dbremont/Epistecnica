---
tags: [note, production]
---

# Semiconductor Industry

> The Semiconductor Industry designs, fabricates, and packages integrated circuits (ICs) and microelectronic components essential to all modern electronic systems. It is a core subindustry of the Electronics and Electrical Equipment Manufacturing Industry and a strategic segment of high-technology and advanced manufacturing.


**Industry**: A set of firms designing and manufacturing semiconductor devices, primarily integrated circuits (ICs) or "chips," which process, store, and transmit digital information.
**Market**: The global ecosystem of buyers (e.g., electronics manufacturers, automotive companies, cloud providers) and sellers (e.g., chip designers, foundries, equipment makers) of semiconductors and related intellectual property.


### Meta (Fundamental Understanding)

*   **How to model the industry?** The semiconductor industry is best modeled as a complex, global, and highly cyclical innovation ecosystem. It can be evaluated using its "flywheel effect": R&D investment → technological advancement → higher performance/demand → revenue → R&D investment. Disruptions to this cycle (e.g., demand shocks, supply constraints) cause high volatility.
*   **Fundamental essence of the product:** Semiconductors are the foundational building blocks of the digital world. They process information (CPUs, GPUs), store data (memory), control power, and interface with the physical world (sensors). They address the need for computation, data storage, and control in virtually all modern electronics.
*   **Could the problem disappear?** The fundamental need for computation and data processing is growing, not disappearing. However, the *form* of the solution could evolve. Quantum computing, neuromorphic computing, or advanced photonics could eventually supplement or replace traditional silicon-based transistors for specific tasks, but a full displacement is a long-term prospect.
*   **Emerging substitutes:** As above, nascent technologies like quantum computing pose a long-term threat. More immediately, the rise of specialized architectures (e.g., domain-specific accelerators for AI) is disrupting the dominance of general-purpose CPUs.
*   **Social/Cultural trends influence:** The demand for chips is directly fueled by trends like remote work (requiring cloud infrastructure and PCs), AI/ML (requiring powerful training and inference chips), electrification of vehicles (more chips per car), and the Internet of Things (billions of connected sensors and devices).

### Production Chain & Operations

*   **Main stages:**
    1.  **Design:** Creating the chip's blueprint using specialized EDA software.
    2.  **Front-End (Fabrication):** Processing pure silicon into wafers containing hundreds of chips. This involves complex processes like lithography, etching, and doping.
    3.  **Back-End (Assembly, Test, and Packaging - ATP):** Slicing the wafer into individual dies, testing them, and packaging them for protection and connection to a circuit board.
*   **Connections & Dependencies:** The chain is tightly coupled. A flaw in design renders fabrication useless. Advanced fabrication capabilities enable more complex designs. Packaging is critical for performance and thermal management.
*   **Standardized vs. Specialized:** ATP is relatively standardized. Design and Fabrication are highly specialized.
*   **Modular vs. Integrated:** The industry has largely **dis-integrated** into three main models:
    *   **Integrated Device Manufacturers (IDMs):** Design and manufacture their own chips (e.g., Intel, Samsung).
    *   **Fabless Companies:** Design chips but outsource manufacturing to foundries (e.g., Qualcomm, NVIDIA, AMD).
    *   **Pure-Play Foundries:** Manufacture chips for fabless companies (e.g., TSMC, GlobalFoundries).
*   **Bottlenecks & Critical Inputs:**
    *   **Extreme Ultraviolet (EUV) Lithography Machines:** Produced almost exclusively by ASML. A critical bottleneck for leading-edge nodes.
    *   **Specialty Gases & Chemicals:** e.g., Neon, Helium, C4F6.
    *   **Ultra-Pure Silicon Wafers.**
    *   **Geographic Concentration:** Over 90% of the world's most advanced (<10nm) chip manufacturing capacity is located in Taiwan (TSMC) and South Korea (Samsung).
*   **Sensitive Stages:** Fabrication is extremely sensitive. Fabs run 24/7; any disruption (earthquake, power outage, geopolitical conflict) halts billions of dollars of production.
*   **Quantitative Value Add:** The value is heavily concentrated. For a high-end processor:
    *   **Design & IP:** ~30-40% of value.
    *   **Front-End Fabrication:** ~40-50% of value (especially at advanced nodes).
    *   **Back-End ATP:** ~10-20% of value.

### Technology & Processes

*   **Key Technologies:** At fabrication, the core technology is **photolithography**, currently using EUV light. Other key processes include chemical vapor deposition, ion implantation, and plasma etching.
*   **Technology Evolution:** The industry is driven by **Moore's Law** (the observation that the number of transistors on a chip doubles roughly every two years). This requires constant advancement in lithography, materials science, and transistor design (e.g., moving to Gate-All-Around transistors).
*   **Disruptive Innovations:**
    *   **Chiplet Design:** Breaking a large die into smaller "chiplets" and connecting them in a package to improve yield and cost.
    *   **Advanced Packaging:** e.g., 3D stacking, which allows for denser and faster connections between chips.
    *   **New Materials:** e.g., Gallium Nitride (GaN) for power electronics, Silicon Carbide (SiC) for electric vehicles.
*   **Technological Dependencies:** The entire industry depends on a handful of equipment suppliers (ASML, Applied Materials, Lam Research, Tokyo Electron). ASML's EUV machines are a single point of failure for advancing beyond 7nm.
*   **Quantitative Adoption:** Adoption of a new technology node (e.g., 3nm) follows an S-curve. It takes 2-3 years from first production at a leading foundry to become mainstream for high-performance chips. Not all chips need the latest node; many applications (automotive, IoT) use mature nodes (>28nm).

### Market Structure & Dynamics

*   **Buyers & Sellers:**
    *   **Upstream:** Equipment/IP sellers (ASML, ARM) sell to...
    *   **Midstream:** Foundries/IDMs (TSMC, Intel) who sell to...
    *   **Downstream:** Electronics manufacturers (Apple, Dell, Ford, Huawei).
*   **Market Concentration:**
    *   **Foundry Market:** Highly concentrated. TSMC has ~55-60% market share.
    *   **Equipment Market:** Oligopolistic (ASML in lithography, Applied Materials in deposition).
    *   **Fabless Design:** Concentrated in specific segments (NVIDIA in AI GPUs, Qualcomm in mobile SoCs).
*   **Pricing:** A mix of **cost-based** (for mature nodes) and **value-based** (for leading-edge nodes, where performance premium allows high margins).
*   **Key Dynamics:** High **switching costs** between foundries (designs are optimized for a specific process). Strong **network effects** in design ecosystems (ARM architecture, CUDA software platform for NVIDIA).
*   **Regulatory Influence:** Heavily influenced by export controls (e.g., US-China tech war), environmental regulations (use of PFAS, energy/water consumption), and massive government subsidies (US CHIPS Act, EU Chips Act).
*   **Macroeconomic Sensitivity:** Highly cyclical and correlated with GDP. Demand for end-products (PCs, smartphones) drives chip orders. High inventory can lead to "chip gluts" after periods of shortage.

### Firm Dynamics

*   **Firm Size Distribution:** Bifurcated. A few giant firms (Intel, Samsung, TSMC, NVIDIA) coexist with thousands of small and medium-sized enterprises (SMEs) in design, specialized equipment, and materials.
*   **Differentiation:**
    *   **Technology/Performance:** (e.g., NVIDIA's AI GPUs, Apple's M-series CPUs).
    *   **Cost Leadership:** (e.g., manufacturers of mature-node chips).
    *   **Brand & Ecosystem:** (e.g., Intel's "Intel Inside," NVIDIA's CUDA).
*   **Barriers to Entry:** Extremely high.
    *   **Capital:** A new advanced fab costs $10-$20 billion.
    *   **Know-How:** Requires decades of accumulated process knowledge.
    *   **IP:** Dense thickets of patents protect designs and processes.
*   **Rate of Innovation:** Extremely high. Firms spend 15-25% of revenue on R&D to keep pace.
*   **Strategic Alliances:** Common. Examples include the IBM-led Sematech in the past, and today's R&D alliances for next-generation packaging and materials.
*   **Profitability Profile:**
    *   **High Margins:** For leading fabless (NVIDIA ~60% gross margin) and foundries (TSMC ~50% gross margin).
    *   **Capital Intensity:** Extremely high (CapEx can be 30-40% of revenue for a foundry).
*   **Growth Strategies:**
    *   **Organic:** Investing in next-generation process technology.
    *   **Diversification:** e.g., Intel moving into foundry services.
    *   **Internationalization:** Building fabs in new geographies for supply chain resilience (e.g., TSMC in Arizona, Intel in Germany).

### Value Capture & Profitability

*   **Where is value captured?** Value capture has shifted over time. Historically, IDMs captured most value. Today, it is split between:
    1.  **Firms with "Unassailable Moats":** TSMC (manufacturing leadership), ASML (equipment monopoly), NVIDIA (software-hardware ecosystem for AI).
    2.  **Firms with Dominant IP/Design:** ARM (architecture), Qualcomm (wireless patents).
*   **Activities Contributing to Advantage:** R&D, manufacturing process control, and ecosystem/software lock-in (e.g., CUDA).
*   **Shifting Value Capture:** The rise of chiplets and advanced packaging may shift value from front-end fabrication toward design and packaging expertise.
*   **Scale Advantages:** Massive scale is essential to amortize enormous R&D and CapEx costs.

### Innovation & R&D

*   **R&D Intensity:** One of the most R&D-intensive industries globally. R&D spending typically ranges from **15% to 25% of revenue**.
*   **Type of Innovation:**
    *   **Incremental:** Shrinking transistor sizes (Moore's Law).
    *   **Radical:** EUV lithography, new transistor architectures (FinFET, GAA).
    *   **Architectural:** The shift to fabless/foundry model, chiplet-based design.
*   **Patent Activity:** Patents are extremely dense and highly concentrated among the largest firms and a few specialized IP companies (like ARM and Qualcomm).
*   **Innovation Diffusion:** Diffusion is rapid among competitors at the same stage (e.g., fabless companies quickly adopt a new TSMC process) but slow across the chain (new equipment takes years to develop).
*   **Open Innovation & Consortia:** Universities are fundamental for basic materials and physics research. Startups drive innovation in novel chip architectures (e.g., RISC-V) and AI-specific designs. Consortia like IMEC (Belgium) are critical for pre-competitive R&D.
*   **Cycle Time:** From initial research to high-volume manufacturing can take 5-10 years for a fundamental new technology (like EUV).

### Risks & Vulnerabilities

*   **Critical Vulnerabilities:**
    *   **Geographic Concentration:** Taiwan Strait geopolitical risk.
    *   **Single-Source Suppliers:** ASML for EUV.
    *   **Complex Supply Chain:** Susceptible to disruptions (e.g., COVID-19, drought in Taiwan).
*   **Resilience:** The industry has low short-term resilience due to capital intensity and complexity. Rebuilding a disrupted supply chain would take years and trillions of dollars.
*   **Single Points of Failure:** ASML; TSMC's advanced fabs.
*   **Legal/Environmental Risks:** IP litigation is common. Environmental risks include high water and energy consumption, and use of hazardous chemicals.

### External Forces

*   **Macroeconomic:** Chip demand is a leading indicator for global economic health. Recession leads to immediate order cancellations and inventory corrections.
*   **Geopolitical:** The US-China tech war is fragmenting the global market, creating separate tech spheres. Export controls are reshaping supply chains.
*   **Environmental/Sustainability:** Pressure to reduce water/energy usage and carbon footprint. The EU's Carbon Border Adjustment Mechanism (CBAM) is a future concern.
*   **Demographic/Cultural:** Aging populations in key manufacturing countries (Japan, Taiwan, South Korea) pose a long-term labor challenge.

### Government Forces

*   **Policies & Incentives:** Massive subsidies are being deployed to onshore manufacturing (US CHIPS Act: $52B, EU Chips Act: €43B). These directly influence where new fabs are built.
*   **Taxation & Trade:** R&D tax credits are critical. Export controls are a primary tool of industrial policy (e.g., restricting advanced chip and equipment sales to China).
*   **Upcoming Changes:** Expect continued regulatory focus on supply chain security, antitrust scrutiny (e.g., on the NVIDIA-ARM acquisition attempt), and new rules around data sovereignty that influence chip design (e.g., secure enclaves).

---

### Product Space

| Product                      | Description                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| Microprocessors (CPU/GPU)    | The "brains" of computers and servers; GPUs are specialized for parallel processing (AI). |
| Memory (DRAM/NAND)           | DRAM for temporary working memory; NAND Flash for permanent storage.                    |
| Analog Chips                 | Process real-world signals like sound, temperature, and power.                          |
| Mixed-Signal Chips           | Convert between analog and digital signals.                                             |
| Microcontrollers (MCUs)      | Small, self-contained computers for embedded control in cars, appliances, etc.          |
| Sensors & MEMS               | Measure physical phenomena like motion, pressure, and light.                            |
| Discrete Semiconductors      | Single-function devices like transistors and diodes, often for power management.        |

### Techno-Productive Matrix

| **Technical Object (Constitutive Technique)** | **Constitutive Technique**       | **Operating Technique**                              | **Product(s)**                          |
| --------------------------------------------- | -------------------------------- | ---------------------------------------------------- | --------------------------------------- |
| Silicon Wafer                                 | Czochralski Process              | Photolithography, Etching, Doping                    | Integrated Circuit (CPU, Memory, etc.)  |
| Electronic Design Automation (EDA) Software   | Algorithmic Design & Simulation  | Place-and-Route, Verification                        | Chip Design (GDSII file)                |
| EUV Light Source                              | Laser-Produced Plasma            | Precision Optics & Masking                           | Patterned Features on a Silicon Wafer   |

### Related Industry(s)

| Industry                | Description                                                                 | NAICS Code        |
| ----------------------- | --------------------------------------------------------------------------- | ----------------- |
| Semiconductor Machinery | Manufacturing the equipment used to make semiconductors.                    | 333242, 333249    |
| Electronic Components   | Production of other components (resistors, capacitors) used on circuit boards. | 334419            |
| Software Development    | Creating the operating systems and applications that run on the hardware.   | 511210, 541511    |
| Telecommunications      | Network infrastructure that relies on semiconductors for data transmission. | 517               |

## References

- [A Guide to Profile an Industry](/view.html?p=notes/technica/general/breviarium/a-guide-to-profile-an-industry.md)
