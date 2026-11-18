---
tags: [note, production]
---

# An Essay on Air Conditioning

> In this essay, we explore house climatization from a user’s perspective, with an emphasis on `air-conditioning technologies`.

## Terminology

| Term                                                  | Meaning                                                                                                             | Tag(s)         |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------- |
| **Climatization**                                     | The set of techniques and technologies used to regulate indoor temperature, humidity, and air quality.              | General        |
| **Passive Cooling**                                   | Non-mechanical strategies for thermal comfort, such as shading, ventilation, and insulation.                        | Cooling Method |
| **Active Cooling**                                    | Mechanically powered systems, primarily air conditioners and heat pumps, that regulate indoor conditions.           | Cooling Method |
| **Heat Pump**                                         | A device that transfers heat from one place to another using thermodynamic cycles (can both cool and heat).         | System Type    |
| **Cooling Capacity**                                  | The total heat energy an air conditioner can remove per hour, typically expressed in BTU/h or kW.                   | Performance    |
| **Cooling Load**                                      | The total heat energy that must be removed from a space to maintain the desired temperature.                        | Performance    |
| **BTU (British Thermal Unit)**                        | A unit of heat energy; in air conditioning, it measures cooling capacity (1 BTU ≈ 0.293 Wh).                        | Unit           |
| **BTU/h (British Thermal Units per hour)**            | Standard unit of cooling capacity; 12,000 BTU/h ≈ 3.52 kW.                                                          | Unit           |
| **kW (Kilowatts)**                                    | SI unit of power; often used alongside BTU/h for cooling/heating capacity.                                          | Unit           |
| **Tonnage (TR)**                                      | 1 ton of cooling = 12,000 BTU/h ≈ 3.52 kW. Used in sizing larger systems.                                           | Unit           |
| **Sensible Heat Ratio (SHR)**                         | Fraction of total cooling used to reduce air temperature (as opposed to removing humidity).                         | Performance    |
| **Latent Load**                                       | Portion of cooling used to remove moisture from the air (dehumidification).                                         | Performance    |
| **CFM (Cubic Feet per Minute)**                       | Volume of air moved by the system; measures airflow rate.                                                           | Airflow        |
| **Static Pressure**                                   | Resistance to airflow within ducts; affects fan and system efficiency.                                              | Airflow        |
| **Air Changes per Hour (ACH)**                        | Number of times the air in a space is replaced per hour; key for ventilation.                                       | Airflow        |
| **COP (Coefficient of Performance)**                  | Ratio of cooling (or heating) output to electrical input, in consistent energy units (Watts/Watt). Higher = better. | Efficiency     |
| **EER (Energy Efficiency Ratio)**                     | Ratio of cooling capacity (BTU/h) to electrical input (W) under fixed indoor/outdoor conditions.                    | Efficiency     |
| **SEER (Seasonal Energy Efficiency Ratio)**           | Seasonal average of EER, reflecting variable outdoor conditions and part-load performance.                          | Efficiency     |
| **IEER (Integrated Energy Efficiency Ratio)**         | Refined version of SEER for commercial systems; weights part-load efficiencies more accurately.                     | Efficiency     |
| **ESEER (European Seasonal Energy Efficiency Ratio)** | Similar to SEER, used in European standards for cooling.                                                            | Efficiency     |
| **HSPF (Heating Seasonal Performance Factor)**        | Seasonal heating efficiency for heat pumps; analogous to SEER but for heating.                                      | Efficiency     |
| **SCOP (Seasonal Coefficient of Performance)**        | European metric for heating efficiency; heating-season analog to SEER.                                              | Efficiency     |
| **Setpoint Temperature**                              | Desired indoor temperature maintained by the thermostat.                                                            | Control        |
| **Duty Cycle**                                        | Percentage of time the compressor runs in a given period.                                                           | Control        |
| **Inverter Technology**                               | Variable-speed compressor control that adjusts output continuously for energy efficiency.                           | Control        |
| **VRF / VRV (Variable Refrigerant Flow / Volume)**    | System that modulates refrigerant flow to multiple indoor units for precise zonal control.                          | System Type    |
| **Zoning**                                            | Ability to condition different rooms independently for comfort and efficiency.                                      | Control        |
| **Smart Control / AI Optimization**                   | Algorithms and sensors that adjust operation based on occupancy, temperature, and humidity patterns.                | Control        |
| **Voltage**               | Electrical potential difference supplied to the system; typically in volts (V).                      | Electrical  |
| **AC / DC**               | Type of electrical current: Alternating Current (AC) or Direct Current (DC).                         | Electrical  |
| **Split System**          | Air conditioning system with separate indoor and outdoor units, connected by refrigerant lines.      | System Type |
| **Mini Split / Ductless** | Split system without ducts; each indoor unit independently controlled, connected to an outdoor unit. | System Type |

## Technology Space

| Technology               | Description                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Vapor-Compression System | The most common cooling technology, using a compressor, condenser, expansion valve, and evaporator.                  |
| Inverter Technology      | Variable-speed compressors that adjust output to maintain stable temperatures efficiently.                           |
| Split System             | A configuration dividing indoor and outdoor units for better performance and noise reduction.                        |
| Smart Control            | Integration of sensors and automation systems to optimize energy use and user comfort.                               |
| Refrigerant              | The working fluid responsible for heat transfer; modern systems use low-GWP (Global Warming Potential) refrigerants. |

## Energy Consumption

> > What determies the erngy cmsupiotno of a given Air Conditionign Technical object?

| Criterion                     | Description                                                                                                   | Energy Impact                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Efficiency (EER/SEER/COP)** | Measures how much cooling you get per unit of electricity. Higher = better.                                   | Directly reduces energy use.                                 |
| **Compressor Type**           | Inverter or variable-speed compressors adjust output to match the exact cooling demand.                       | 30–50% less electricity than old fixed-speed types.          |
| **Refrigerant**               | Modern low-GWP refrigerants (e.g., R-32) transfer heat more efficiently than older ones (e.g., R-410A, R-22). | Improves thermodynamic efficiency by 5–10%.                  |
| **Heat-Exchanger Design**     | Micro-channel or enhanced fin designs improve heat transfer.                                                  | Reduces compressor workload → lower energy.                  |
| **Smart Controls**            | Sensors, motion detection, and adaptive thermostats optimize runtime.                                         | Cuts wasted operation hours.                                 |
| **Zoning / VRF Systems**      | Deliver cooling only where needed.                                                                            | Major energy savings in multi-room homes.                    |
| **Humidity Control**          | Systems that manage latent heat more precisely (e.g., inverter + variable airflow).                           | Better comfort at higher temperatures → less cooling needed. |

## Evaluation

| **Metric**                                   | **Description**                                                                                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Cooling Capacity (BTU/h)**                 | Amount of heat removed per hour; determines if the unit can handle the room size.                                  |
| **SEER (Seasonal Energy Efficiency Ratio)**  | Measures energy efficiency over a cooling season — higher SEER = less energy use per cooling output.               |
| **Power Input (kW)**                         | Electrical power drawn when the unit is operating at full load.                                                    |
| **Energy Consumption (kWh/month)**           | Estimated monthly electricity use, based on cooling hours and SEER.                                                |
| **Electricity Rate (USD/kWh)**               | Cost of electricity used to estimate operating expense (varies by region).                                         |
| **Monthly Operating Cost (USD)**             | Expected electricity cost per month of use.                                                                        |
| **Unit Price (USD)**                         | Purchase and installation cost of the HVAC unit.                                                                   |
| **Lifetime Energy Cost (USD)**               | Total cost of electricity over the expected lifetime (e.g. 10 years of operation).                                 |
| **Total Ownership Cost (USD)**               | Unit price + lifetime energy cost; reflects real cost of the system.                                               |
| **Payback Period (months)**                  | Time required for energy savings (vs a baseline model) to offset the higher purchase price.                        |
| **Noise Level (dB)**                         | Sound level during operation — relevant for comfort in small rooms.                                                |
| **Cooling Load Match (%)**                   | Degree to which unit capacity matches the calculated cooling requirement of the space.                             |
| **COP (Coefficient of Performance)**         | Ratio of cooling output to electrical input in consistent units; used especially for reversible (heat pump) units. |
| **Maintenance Requirement**                  | Frequency and complexity of cleaning or servicing (filters, coils, refrigerant checks).                            |
| **Durability / Warranty (years)**            | Expected lifetime and coverage period; influences long-term cost and reliability.                                  |
| **Environmental Impact (Refrigerant / GWP)** | Type of refrigerant and its Global Warming Potential; affects sustainability assessment.                           |
| **Smart / Control Features**                 | Integration with sensors, thermostats, or energy-saving modes.                                                     |
| **Brand Reliability Index**                  | Qualitative measure of brand performance, service availability, and failure rates.                                 |

## Economic Profile

> An estimate for an air conditioner serving a space of approximately 9 $m^2$ (≈ 10×10 ft), operating 15 hours per day in a tropical climate.

### Comparison

> Note: Make a graph with Use (By Year) - Total Cost (Equiment + ... + Energy Use).

> SEER 18 gives nearly minimum cost; SEER 20 or 25 adds little savings because higher price offsets reduced energy use.

Assumptions:

| **Variable**            | **Value**    | **Notes**                                   |
| ----------------------- | ------------ | ------------------------------------------- |
| **Cooling Load**        | 12,000 BTU/h | ≈ 1 ton of cooling capacity                 |
| **Operating Hours/Day** | 15 hours     | Typical for tropical climates               |
| **Energy Rate**         | $0.18 /kWh   | Dominican Republic average residential rate |
| **System Lifetime**     | 8 years      | Economic evaluation horizon                 |
| **Days/Year**           | 365          | Continuous yearly operation assumption      |
| **Noise Level**         | 19–45 dB(A)  | Typical range for indoor/outdoor AC units   |
| **Voltage** | |


| SEER | Unit Price (USD) | 8-Year Energy Cost | **Total 8-Year Cost** |
| ---- | ---------------- | ------------------ | --------------------- |
| 13   | 450              | 3 624              | **4 074**             |
| 16   | 600              | 2 944              | **3 544**             |
| 18   | 750              | 2 616              | **3 366** ✅          |
| 20   | 950              | 2 352              | **3 302**             |
| 25   | 1 400            | 1 880              | **3 280**             |

### Product Space

| Firm           | Technology                    | Example product (model / typical size)                  |                      SEER (advertised) |   Typical US price (approx.) | Quick quality evaluation                                                                                                   |
| -------------- | ----------------------------- | ------------------------------------------------------- | -------------------------------------: | ---------------------------: | -------------------------------------------------------------------------------------------------------------------------- |
| **Midea**      | DC-inverter mini-split        | Midea 9,000 BTU single-zone (Hyper-heat / smart models) |     **~19–28 SEER2** (model dependent) | **~USD $700–1,200** (varies) | Very good value for $; high-SEER models available; decent warranty; good budget choice. |
| **LG**         | Dual-inverter mini-split      | LG 9,000 BTU single-zone (DUAL Inverter / ThinQ)        |                       **~21–27 SEER2** |        **~USD $1,100–1,900** | Strong reliability, modern features (Wi-Fi/ThinQ), long warranties on some models; mid-to-high tier.|
| **Daikin**     | Inverter mini-split           | Daikin 9,000 BTU Entra / 17-series                      | **~17–18 SEER (some models SEER2 18)** |        **~USD $1,000–1,300** | Premium engineering, quiet, reliable; often slightly premium pricing; very common installer choice.|
| **Mitsubishi** | Inverter mini-split (premium) | Mitsubishi 9,000 BTU wall-mount                         |                        **~16–20 SEER** |             **~USD $1,300+** | Excellent long-term reliability and dealer network; higher upfront cost; top tier quality.|

## Maintenance

> What are the maintenance requirements of an air-conditioning system?

> **Maintenance Schedule:**  
> • **Monthly:** Clean or replace filters; inspect return and supply vents; check for abnormal noise or vibration.  
> • **Quarterly:** Clean evaporator and condenser coils; inspect condensate drain and tray; check thermostat calibration.  
> • **Biannual (Cooling/Heating Season Start):** Verify refrigerant charge; inspect electrical connections; test blower motor and fan belts; clean outdoor unit surroundings.  
> • **Annual:** Full system performance audit; pressure testing; lubrication of motors and bearings (if applicable); inspection of duct integrity; overall safety check.

> **Maintenance Type:**  
> • **Preventive Maintenance:** Regular cleaning, inspection, calibration, and component checks to preserve efficiency and avoid failures.  
> • **Corrective Maintenance:** Repair or replacement of faulty components such as capacitors, contactors, fan motors, sensors, or refrigerant leaks.  
> • **Predictive Maintenance (Advanced Systems):** Monitoring performance metrics (temperature delta, compressor load, energy consumption) to anticipate failures and optimize operation.  
> • **Seasonal Maintenance:** Configuration and checks specific to cooling or heating seasons (in HVAC heat-pump systems).

### Filter Maintenance

> How to maintain the filter?

- Remove the filter panel and inspect for dust accumulation.
- Clean reusable filters with mild soap and water; allow them to dry completely before reinstalling.
- For disposable filters, replace with the manufacturer-specified MERV rating.
- Ensure proper seating and sealing of the filter to avoid bypass airflow.
- Verify airflow after reinstalling and reset any filter-change indicators (if present).

### Evaporator Maintenance

> How to maintain the evaporator?

- Turn off power before servicing.
- Remove access panels and inspect coil fins for dust, mold, or obstruction.
- Clean using a non-corrosive coil cleaner or gentle brushing.
- Check the condensate drain line for clogs and flush it to prevent overflow.
- Verify insulation on refrigerant lines and ensure proper airflow across the coil.

### Condenser Maintenance

> How to maintain the condenser?

- Disconnect power to the outdoor unit.
- Clear debris around the condenser within a 1–2 meter radius.
- Remove the top grille and rinse the coil from the inside out using low-pressure water.
- Straighten bent fins using a fin comb.
- Inspect the fan motor, fan blades, and electrical contacts; clean and tighten if necessary.
- Ensure no objects obstruct the exhaust airflow of the condenser.

## QA

### Does an 'Split' System improves SERR?

### What i th best predictor of energy compsiotion by a air condition?

## References

- [Air conditioning](https://en.wikipedia.org/wiki/Air_conditioning)
- [Heating, ventilation, and air conditioning](https://en.wikipedia.org/wiki/Heating,_ventilation,_and_air_conditioning)
- [A comprehensive evaluation of the most suitable HVAC system for an industrial building by using a hybrid building energy simulation and multi criteria decision making framework](https://www.sciencedirect.com/science/article/abs/pii/S2352710221000097)
