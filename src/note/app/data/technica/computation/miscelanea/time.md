---
tags: [model-of-computation, computer-system, coordination]
---

# Time

- [Timestamping](note.html?n=technica/computation/miscelanea/timestamping.md), [Calendar](note.html?n=technica/computation/miscelanea/calendar.md)

> Time (clock): A technology to index events.
> 

> Time, in a technical sense, is a continuous, measurable quantity used to track and quantify the progression of events. It is typically defined using standardized units like seconds, minutes, and hours, and can be measured using various technologies such as **atomic clocks** (for precision timekeeping) and **synchronization protocols** (such as **NTP** or **GPS**). In computing, **time** is often tracked in terms of **timestamps** or **epoch time**, counting seconds since a reference point (e.g., January 1, 1970 for Unix time). It is an essential parameter for coordinating systems, scheduling tasks, and synchronizing processes in both physical and digital systems.
> 

> A model of time in the context of distributed systems refers to a framework or conceptual representation used to manage and reason about the temporal aspects of events occurring within the system. In distributed systems, where multiple independent processes or nodes operate concurrently and asynchronously, establishing a consistent understanding of time is crucial for ensuring correct behavior, coordination, and consistency.
> 

> Standard Time Model → Local Time Model;   this mapping geneartes so many problems.
> 

> Human societies follow calendar systems, usually to track the seasons. They measure time relative to the seasons, so civilian time standards also account for them.
> 

> In Physics we defines things in reference to some standard.
> 

> **Time Reference System**:  ..,.
> 

QA:

- What is a time-zone?
- What is High Precision Time Measure? [What is High Precision Time Measure?](note.html?n=technica/computation/miscelanea/time.md)
- How long does it take for the Earth to orbit the Sun?  [How long does it take for the Earth to orbit the Sun?](note.html?n=technica/computation/miscelanea/time.md)
- How to know if a Year is  a leap Year?
- How UTC handles keeps tracks of the tropical  year?
- What are the requirements for a good clock and time standard?
- How a computing system Language System + OS System handles times?
- What is a leap second? How to handle leap seconds? What is a leap year?
- How to synchronize clocks? What happens when clocks have **different precision**?
- Which are the most common problems in **time management in computing systems**?
- How do synchronization protocols handle transmission delays when syncing clocks? [How do synchronization protocols handle transmission delays when syncing clocks?](note.html?n=technica/computation/miscelanea/time.md)
- What factors lead to discrepancies between a local clock and UTC, and what methods are used to maintain synchronization?
- What is the difference between date and time? …

## Uses

1. **Ordering:** A time model provides mechanisms for ordering events relative to each other. This includes determining which events precede others and establishing causal relationships between events.
2. **Synchronization:** The model addresses the issue of clock synchronization among distributed nodes, ensuring that different processes have a consistent notion of time despite operating with independent clocks and experiencing variable network latencies.
3. **Consistency:** It defines rules or constraints to maintain the consistency of data and operations across distributed nodes, even in the presence of concurrency, failures, or network partitions.
4. **Granularity:** The model may specify the granularity of time units representing temporal information, such as milliseconds, microseconds, logical ticks, or physical clock cycles.
5. **Uncertainty and Error Handling:** It addresses uncertainties and errors associated with time measurement, clock drift, message delays, and varying clock resolutions in distributed environments.
6. **Concurrency Control:** The model may incorporate concurrency control mechanisms to manage conflicting updates and ensure the correctness of concurrent operations performed by distributed processes.

## **Time Reference System**

> A **Time Reference System (TRS)** is a framework or set of conventions that defines the measurement and standardization of time within a given context, relying on specific reference points or periodic phenomena. It establishes the **unit of time**, the **method of measurement**, and the **origin of time** for a particular system, ensuring consistency in timekeeping and synchronization across systems or processes.
> 

> Time Standard and “Time Reference System” are almost the same idea but the name “Time Reference System” is better.
> 

### List of **Time Reference System (TRS)**

| **Time Reference System (TRS)** | **Definition** | **Measurement Mechanism** | **Reference Point / Epoch** | **Precision** | **Uses** |
| --- | --- | --- | --- | --- | --- |
| **Universal Time  / Astronomical (UT)** | Time based on Earth's rotation relative to distant stars. | Earth's rotation, astronomical observations. | Vernal equinox (for UT1) or arbitrary fixed points for others (e.g., midnight UTC). | Millisecond to second-level precision (subject to irregularities in Earth's rotation). | Astronomy, celestial navigation, and some scientific observations. |
| **Coordinated Universal Time (UTC)** | The standard time used globally, combining atomic time with Earth’s rotation (adjusted by leap seconds). | Atomic clocks (TAI) and Earth’s rotation (leap seconds). | Epoch of January 1, 1970 (Unix epoch). | High precision (nanosecond-level), adjusted by leap seconds. | Civil timekeeping, global communications, networks, computing systems. |
| **International Atomic Time (TAI)** | Continuous time scale based purely on atomic clock measurements. | Cesium or rubidium atomic clocks. | 1958, starting from a reference of 0 s at the beginning of the year. | Extremely precise (nanosecond-level). | High-precision scientific research, GPS, time synchronization in telecommunications. |
| **Terrestrial Time (TT)** | Time scale used in geodesy and celestial mechanics. | Based on Earth’s motion relative to celestial bodies, adjusted for relativity. | Reference: J2000.0 epoch (January 1, 2000, 12:00 TT). | Nanosecond precision (including relativistic effects). | Space missions, astronomical observations, and orbital mechanics. |
| **Barycentric Dynamical Time (TDB)** | Time scale used for calculations of the Solar System's dynamics. | Calculations accounting for gravitational forces, relativistic effects. | J2000.0 epoch. | High precision (nanosecond-level). | Orbital dynamics, astronomical simulations. |
| **Geocentric Coordinate Time (TCB)** | Time scale used for the geocentric reference frame, considering relativistic effects. | Gravitational effects and relativistic corrections. | J2000.0 epoch. | High precision (nanosecond-level). | Space exploration, satellite navigation, and astronomical simulations. |
| **GPS Time** | Time system used by GPS satellites. | Atomic clocks on satellites, based on TAI. | January 6, 1980 (Epoch of GPS time). | Extremely precise (nanosecond-level), but no leap seconds. | Navigation, geolocation, and time synchronization for systems worldwide. |
| **Sidereal Time** | Time system based on the Earth's rotation relative to distant stars. | Earth's rotation and astronomical observations. | Sidereal day starts from the vernal equinox. | Millisecond-level precision. | Astronomical observations, telescope alignment. |
| **Ephemeris Time (ET)** | Time scale used in older celestial mechanics, prior to TDB. | Earth's orbital motion and celestial mechanics. | January 1, 1950, 0h UT. | High precision for celestial mechanics. | Early space missions, astronomical observations. |

### Alternatives Time References Systems

| **Clock Type** | **Description** |
| --- | --- |
| **System Clock** | The system clock, or real-time clock (RTC), is integrated into a computer's motherboard. It tracks the current date and time, referencing time-related operations in the OS and software applications. |
| **Logical Clocks** | Abstract models are used in distributed systems to order events and maintain a partial ordering of events across different processes or nodes without necessarily representing real-time. |
| **Vector Clocks** | Track causal relationships and order events in distributed systems. This ensures consistent views of events across multiple nodes and aids in synchronization and conflict resolution. |
| **Lamport Timestamps** | Logical clocks that order events in a distributed system maintain causality between events and determine the global order across distributed nodes. |
| **Monotonic Clocks** | Provide a continuous, ever-increasing time value unaffected by system clock changes or synchronization adjustments. It is commonly used for measuring time intervals and scheduling tasks. |
| **Wall Clocks** | Represent the real-world time, typically provided by the system clock. Display the current date and time to users and timestamp events. |

References:

- https://www.ibm.com/docs/en/watsonx/saas?topic=analysis-time-reference-system
- https://science.nasa.gov/learn/basics-of-space-flight/chapter2-3/
- [Clock](note.html?n=technica/computation/concurrency/conceptual-model-coordination/clock.md)

## Calendar System

> **Calendar System**: A structured framework for organizing and measuring time based on astronomical cycles (e.g., solar, lunar, lunisolar) using a set of rules to define units (days, months, years) and intercalation adjustments to maintain alignment with celestial events.
> 

> **Gregorian Calendar System**: A solar-based calendar system introduced in 1582, refining the Julian calendar by defining a 400-year leap year rule (leap years occur in years divisible by 4, except for century years not divisible by 400) to maintain the **tropical year**'s alignment with **seasonal equinoxes**.
> 

> **Human societies** have traditionally structured their calendars around the cycles of the seasons, which are driven by Earth's orbit around the Sun. This is why most civilian time standards incorporate adjustments like leap years and daylight saving time to keep them aligned with seasonal changes.
> 

> See more in [Calendar](note.html?n=technica/computation/miscelanea/calendar.md).
> 

The underlying reason is that agricultural, economic, and cultural activities have historically depended on predictable seasonal shifts. For example:

- **Solar calendars** (e.g., the Gregorian calendar) are designed to keep the months aligned with the seasons by approximating Earth's orbit.
- **Lunisolar calendars** (e.g., the Chinese or Hebrew calendars) use the Moon's phases but periodically insert leap months to stay in sync with the solar year.
- **Sidereal time** is sometimes used in specialized fields (like astronomy) to track time based on distant stars rather than the Sun.

References

- https://en.wikipedia.org/wiki/Calendar
- https://en.wikipedia.org/wiki/Gregorian_calendar
- [Calendar](note.html?n=technica/computation/miscelanea/calendar.md)

## Leap Second

> A **leap second** is an adjustment made to **Coordinated Universal Time (UTC)**
to account for the slight difference between atomic time (measured by highly accurate atomic clocks) and astronomical time (based on the Earth's rotation).
> 

> **Atomic Time (TAI):**  Atomic clocks measure time based on the vibrations of atoms (usually cesium-133) and are extremely precise.
> 

> **Astronomical Time (UT1)**:  Astronomical time is based on the Earth's rotation relative to celestial bodies (e.g., the Sun). The Earth's rotation is not perfectly constant; it can slow down or speed up due to factors like tidal friction, gravitational interactions, and changes in the Earth's core.
> 

> Correction:  Over time, the Earth's rotation slows down very slightly, **causing astronomical time (UT1) to drift away from atomic time (TAI)**. → To keep UTC (which is based on atomic time) in sync with the Earth's rotation, leap seconds are added.
> 

> **Who Decides on Leap Seconds?**  The **International Earth Rotation and Reference Systems Service (IERS)** monitors the Earth's rotation and determines when a leap second is needed.
> 

**Why Leap Seconds Matter:**

> Leap seconds ensure that UTC remains aligned with the Earth's rotation, which is important for
applications that rely on precise timekeeping, such as:
> 
- **Astronomy** (tracking celestial objects).
- **Navigation systems** (e.g., GPS).
- **Communication networks** (e.g., synchronization of data transmission).
- **Financial systems** (e.g., timestamping transactions).

**Controversy and Future of Leap Seconds:**

- Leap seconds can cause issues for computer systems and networks that rely on precise
timekeeping, as they require manual adjustments and can lead to errors
if not handled properly.
- Some organizations, including the **International Telecommunication Union (ITU)**, have proposed abolishing leap seconds and allowing UTC to drift slightly from astronomical time over long periods.
- As of now, leap seconds are still in use, but their future is under discussion.

References

- https://www.youtube.com/watch?v=WkhrL8NMycU

## **Clocks Models**

> 

## **Time Standard**

> **Time Standard** is a formally defined system for measuring time based on a specific physical realization and a defined timescale. It consists of:
> 
1. **Reference Clock** – A precise physical process that defines the unit of time (e.g., atomic oscillations in Cesium-133 for TAI).
2. **Timescale Algorithm** – A mathematical model that integrates reference clock readings into a continuous time representation (e.g., UTC, TAI).
3. **Dissemination Protocols** – Methods for distributing time information to users (e.g., NTP, PTP, GPS).

| **Time Standard** | **Abbreviation** | **Description** |
| --- | --- | --- |
| **Coordinated Universal Time** | **UTC** | The primary time standard used worldwide. It is maintained using atomic clocks and is adjusted with leap seconds to stay in sync with Earth's rotation. |
| **Greenwich Mean Time** | **GMT** | The mean solar time at the Prime Meridian (0° longitude). Historically used as the world's time reference before UTC. |
| **International Atomic Time** | **TAI** | A continuous time standard based on atomic clocks, running without leap seconds. It is ahead of UTC by a number of leap seconds. |
| **Universal Time (UT1)   /Astronomical Time**  | **UT1** | A version of Universal Time adjusted for the Earth's irregular rotation, making it more accurate than GMT. |
| **Universal Time (UT0, UT1, UT2)** | **UT0, UT1, UT2** | Variants of Universal Time: UT0 (raw astronomical observations), UT1 (corrected for polar motion), UT2 (historically corrected for seasonal effects). |
| **Solar Time** | **Apparent Solar Time** / **Mean Solar Time** | Based on the position of the Sun in the sky; varies slightly due to Earth's elliptical orbit and axial tilt. |
| **Dynamical Time (TT, TDB, TCB, TCG)** | **TT, TDB, TCB, TCG** | Used in astronomy to describe planetary motions more accurately than atomic time. |
| **Terrestrial Time** | **TT** | A theoretical time standard for ephemeris calculations, close to TAI + 32.184 seconds. |
| **Barycentric Dynamical Time** | **TDB** | A time standard used in planetary motion calculations, correcting for relativistic effects near the Sun. |
| **Geocentric Coordinate Time** | **TCG** | Similar to TT but accounts for relativistic effects in Earth's gravitational field. |
| **Barycentric Coordinate Time** | **TCB** | Similar to TDB but adjusted for the gravitational influence of the entire solar system. |
| **Unix Time (POSIX Time)** | **Epoch Time** | Counts seconds since **January 1, 1970, 00:00:00 UTC**, ignoring leap seconds. Used in computing. |
| **GPS Time** | **GPST** | Used in GPS systems, running ahead of UTC by leap seconds but synchronized with TAI. |
| **Sidereal Time** | **GMST, LMST** | Measures time based on the rotation of the Earth relative to distant stars, instead of the Sun. Used in astronomy. |
| **Julian Date (JD, MJD)** | **JD, MJD** | A continuous count of days since **January 1, 4713 BCE**, used in astronomy. The **Modified Julian Date (MJD)** is JD - 2400000.5. |

## Local Time

> Usually some reference time + time zones + some local rules like (light saving …) …
> 

### Clock

> A clock refers to a timing mechanism that generates a sequence of regular, periodic signals, known as clock pulses, which synchronize the operations of a computer's components, particularly in coordinating the execution of instructions and data transfer between hardware components.
> 

> In computer science, a "clock" is an internal mechanism that tracks time, often based on a specific source like the system clock, hardware clock, or a software-implemented logical clock. "Time" refers to temporal ordering and duration, represented as real-world time (wall-clock), logical time (e.g., Lamport timestamps), or system-specific units used for scheduling and coordination.
> 

### Local Clocks

> 

| **Type of Clock** | **Description** | **Accuracy** | **Typical Applications** |
| --- | --- | --- | --- |
| **Quartz Crystal Clock** | Uses the vibrations of a quartz crystal to keep time. | Moderate (seconds per month) | Consumer electronics (watches, computers, phones) |
| **Atomic Clock** | Uses the vibrations of atoms (e.g., cesium or rubidium) for extreme precision. | Extremely high (nanoseconds) | Scientific research, GPS satellites, data centers |
| **GPS Clock** | Synchronizes with atomic clocks on GPS satellites. | High (microseconds) | Telecommunications, power grids, navigation |
| **Radio Clock** | Receives time signals from radio broadcasts (e.g., WWVB, DCF77). | High (milliseconds) | Wall clocks, alarm clocks, industrial systems |
| **Network Time Protocol (NTP) Clock** | Synchronizes with remote servers over the internet using NTP. | High (milliseconds) | Computers, servers, networked devices |
| **Precision Time Protocol (PTP) Clock** | Synchronizes with a master clock using PTP (IEEE 1588). | Very high (microseconds) | Industrial automation, financial trading, telecom |
| **Real-Time Clock (RTC)** | A low-power clock that keeps time when the device is off. | Low to moderate (minutes per month) | Embedded systems, IoT devices, motherboards |
| **Software Clock** | Relies on the device's operating system to keep time. | Low (depends on hardware) | General-purpose computing, smartphones |

### Timezones

> Timezones: UTC Clock → Local Time.
> 

> A **time zone** is a region of the Earth's surface where the **legal or civil time** is defined by a fixed offset from **Coordinated Universal Time (UTC)**, often incorporating **daylight saving time (DST) rules**.
> 

> **Representation in Computing** – In systems, time zones are managed using **IANA Time Zone Database (tzdata)**, which includes historical and future time rules (e.g., "America/New_York" rather than "UTC-5").
> 

## **ISO 8601**

> 

## **Network Time Protocol (NTP)**

> **NTP** is one of the most widely used protocols for synchronizing clocks over networks.
> 

> NTP uses multiple servers and statistical algorithms to filter out inconsistent data and improve accuracy.
> 

> Synchronization protocols use **filtering algorithms** (e.g., **Kalman filters**) to smooth out variations caused by network jitter and delays. 😊
> 

It accounts for transmission delays by using a **round-trip time (RTT)** calculation:

1. The client sends a request to the time server and records the time $T_1$.
2. The server receives the request at $T_2$ and sends a response at $T_3$.
3. The client receives the response at $T_4$.

The **offset** between the client and server clocks is calculated using the formula:  $\text{Offset} = \frac{(T_2 - T_1) + (T_3 - T_4)}{2}$.

The **delay** is calculated as: $\text{Delay} = (T_4 - T_1) - (T_3 - T_2)$ - 

## **Precision Time Protocol (PTP)**

- **PTP** (IEEE 1588) is used for highly precise synchronization, often in industrial and scientific applications.
- It works by exchanging timestamped messages between a **master clock** and **slave clocks**.
- PTP accounts for transmission delays by measuring the **propagation delay** between devices and adjusting the clocks accordingly.
- It achieves sub-microsecond accuracy, making it suitable for applications like financial trading and telecommunications.

## **GPS Timing**

- **GPS satellites** broadcast highly accurate time signals based on atomic clocks.
- Devices with GPS receivers can synchronize their clocks directly to these signals, bypassing network delays.
- GPS timing is often used in critical systems like power grids and telecommunications networks.

## Relativistic Effects

Relativistic effects in time measurement arise from **Albert Einstein's theory of relativity**, which fundamentally altered our understanding of time and space. There are two key aspects of relativity that affect time measurement:

1. **Special Relativity**: Time dilation occurs as an object approaches the speed of light. According to special relativity, a clock moving at high speeds relative to an observer will tick slower than a clock at rest. This effect is most noticeable at velocities approaching the speed of light.
2. **General Relativity**: Gravitational time dilation occurs in the presence of strong gravitational fields. Time runs slower near massive objects (like planets, stars, or black holes) compared to regions with weaker gravitational fields.

Practical Implications:

- **GPS Systems**: Satellites orbiting Earth experience weaker gravitational fields and move at high velocities, so their clocks run faster than those on the surface of the Earth. Engineers account for both special and general relativistic time dilation to ensure GPS systems are accurate.
- **Atomic Clocks**: Precision time measurement, such as in atomic clocks, is affected by relativity. The difference in time between clocks on the ground and those at altitude or in motion must be corrected.
- **Cosmology**: Relativity also plays a role in measuring the age of the universe and in understanding phenomena like black holes or the expansion of space.

## How long does it take for the Earth to orbit the Sun?

> It’s takes a “**Sidereal Year” a  concept that denotes**  the time that it takes the Earth to Orbit the Sun.
> 

> It’s  a variable quantity but  it usually takes  **365.25636 days ≈ 31,558,149.8 seconds.**
> 

This is the time it takes for Earth to return to the same position relative to distant stars, unaffected by seasonal shifts or calendar adjustments.

Atomic clocks confirm that this period is not perfectly constant—it changes due to:

- **Gravitational perturbations** from other planets (especially Jupiter and Venus).
- **General relativity effects**, which cause tiny shifts in Earth's orbit over time.
- **The Sun’s mass loss**, which slightly increases Earth's orbital period as the Sun radiates energy.

## What are the different concepts of a year used in calendar systems, and how do they relate to Earth's orbit and astronomical events?

- **Tropical Year (**~365.24219 days):  The time from one **vernal equinox** to the next, which governs our **calendar system**.
- **Anomalistic Year (**~365.25964 days):  The time between two successive perihelion passages (when Earth is closest to the Sun).
- **Draconic Year** (~346.6201 days): The time it takes for the Earth to return to the same node of its orbit, important for predicting eclipses.

Referemces

- https://www.youtube.com/watch?v=mKCvqzCrZfA

## How do we identify when the Earth has completed a full orbit around the Sun?

Earth completes **one full orbit** around the Sun when it returns to the same position in its **heliocentric trajectory**, meaning:

- It has traveled **approximately 940 million km** (its full orbital path).
- Its **orbital longitude (mean anomaly)** has returned to the same value.
- The **orbital period**, as defined by Kepler’s laws and Newtonian mechanics, has elapsed.

**Methods to Determine Orbit Completion**

1. **Heliocentric Coordinates (Barycentric Reference Frame)**
    - Earth’s position is tracked using **ephemerides** based on precise gravitational models.
    - We can calculate when Earth returns to the **same position** in its elliptical path relative to the Sun in a barycentric (solar-system-centered) frame.
2. **Kepler’s Third Law & Orbital Period**
    - Earth’s mean orbital period, computed from Newtonian mechanics, is **31,558,149.8 seconds (~365.25636 days)**.
    - Using this period, we can predict when Earth has completed a full revolution around the Sun.
3. **Atomic Clock and Doppler Measurements**
    - Modern space missions use **Doppler tracking and radio signals** (e.g., from DSN – Deep Space Network) to measure Earth’s velocity and position with respect to the Sun.
    - Any deviations due to perturbations (from planets, relativistic effects) can be accounted for in precise orbit determination.
4. **Solar System Dynamics & N-body Simulations**
    - Using **numerical integrations** of planetary motion (such as those done by NASA’s JPL Horizons system), we can track Earth's motion and identify the exact moment it returns to its starting position.

References

- https://en.wikipedia.org/wiki/Earth%27s_orbit
- [**Earth**](https://app.notion.com/p/Earth-1bfc0f5171ec8021893ad56b46fe2044?pvs=21)

## What is the point of origin used to account for an orbit?

> The **point of origin** for counting an orbit depends on the chosen reference frame and definition of a complete revolution. Here are the key technical choices:
> 

**1. Heliocentric (Solar-Centered) Reference Frame**

- In an **inertial frame** (e.g., with respect to distant stars), the **starting point** can be defined as Earth’s position at a particular time, such as **J2000.0 epoch** (January 1, 2000, 12:00 TT).
- A full orbit is completed when Earth returns to the same **longitude in its elliptical path**.
- This method aligns with the **sidereal year** (~365.25636 days).

**2. Vernal Equinox as the Starting Point**

- The **tropical year** (~365.24219 days) is defined by Earth's return to the same **equinox position** (where the Sun crosses the celestial equator).
- The equinox shifts due to **axial precession**, meaning this reference frame is non-inertial.
- Used in calendars and for seasonal consistency.

**3. Perihelion as the Starting Point**

- The **anomalistic year** (~365.25964 days) is measured between successive **perihelion passages** (when Earth is closest to the Sun).
- Due to planetary perturbations, perihelion shifts over time (~1 day per 58 years).

**4. Barycentric Dynamical Time (TDB) and Ephemerides**

- If using precise ephemeris data, an orbit can be measured from any arbitrary **epoch** (e.g., J2000.0 or real-time astronomical observations).
- This method is used in spacecraft navigation and deep-space tracking.

## How UTC handles keeps tracks of the Tropical Year?

> UTC keeps track Astronomical Time not Tropical  Year.
> 

> UTC does not explicitly track the **Tropical Year**, but leap seconds help keep it aligned with Earth's rotation, ensuring that over time, **midnight on January 1st remains close to the same point in the seasonal cycle**.
> 

## How do synchronization protocols handle transmission delays when syncing clocks?

> **Transmission delays** are a common challenge when synchronizing clocks across networks or systems. These delays can occur due to factors like network latency, packet loss, and varying distances between devices.
> 

Review the specific protocols  and sync tools to see how they manage these challenges:

- [**Network Time Protocol (NTP)**](note.html?n=technica/computation/miscelanea/time.md)
- [ **Precision Time Protocol (PTP)**](note.html?n=technica/computation/miscelanea/time.md)
- [**GPS Timing**](note.html?n=technica/computation/miscelanea/time.md)

## What factors lead to discrepancies between a local clock system and UTC, and what methods are used to maintain synchronization?

> 

- **Clock Drift:**
    - Local clocks, especially those based on quartz oscillators, can drift over time due to temperature changes, aging, or manufacturing imperfections.
    - This drift can cause the local clock to run faster or slower than UTC.
- **Environmental Factors**: Temperature fluctuations, humidity, pressure, and even electromagnetic interference can cause clocks to drift.
- **Software Overheads:** The time taken by software to process and apply synchronization updates can introduce small but cumulative errors.
- **Hardware Limitations:**  Low-precision hardware clocks (e.g., in consumer devices) may not maintain accurate time over long periods.
- **Leap Seconds:**  The occasional addition of leap seconds to UTC can cause temporary mismatches if the local clock does not account for them.
- Time Zone or Configuration Errors:      Incorrect time zone settings or misconfigured synchronization protocols can lead to discrepancies.
- Relativistic Effects:  As mentioned earlier, **special relativity** (due to high velocities) and **general relativity** (due to differences in gravitational fields) affect the passage of time.   For example, clocks at higher altitudes (weaker gravity) or moving at high velocities (like satellites) will tick at different rates compared to clocks on Earth's surface.

## What is High Precision Time Measure?

> Aka. Time Resolution - Time Slices
> 

> Here’s a **comprehensive and detailed** table of time measurement units, including their definitions, equivalents, and **specific use cases**—with additions like *high-frequency trading (HFT)*, cosmic scales, and scientific applications.
> 

| **Unit** | **Description** | **Equivalent To** | **Key Uses & Applications** |
| --- | --- | --- | --- |
| **Millennium** | 1,000 years | 10 centuries | Long-term climate modeling, civilization studies, deep future planning. |
| **Century** | 100 years | 10 decades | Historical eras, infrastructure projects (e.g., dams, cities). |
| **Decade** | 10 years | ~3,652 days | Economic trends, technology adoption, demographic shifts. |
| **Year** | Earth’s orbital period | 365.25 days (approx.) | Financial reporting, agriculture, astronomy, academic years. |
| **Quarter** | 3 months | ~91 days | Corporate earnings reports, fiscal planning, seasonal business cycles. |
| **Month** | ~1/12 of a year | 28–31 days | Payroll cycles, lunar calendars, subscription billing. |
| **Week** | 7-day cycle | 168 hours | Work schedules, sprint planning (Agile), TV show releases. |
| **Day** | Earth’s rotation | 24 hours | Daylight cycles, medicine dosing, circadian biology. |
| **Hour** | 1/24 of a day | 60 minutes | Work shifts, time zones, cooking, transportation schedules. |
| **Minute** | 1/60 of an hour | 60 seconds | Meetings, short tasks, sports periods (e.g., soccer halves). |
| **Second** | SI base unit | 1,000 milliseconds | Clocks, physics experiments, GPS timing, everyday measurements. |
| **Millisecond (ms)** | 1/1,000 of a second | 1,000 microseconds | **High-frequency trading (HFT)**, audio processing, camera exposure. |
| **Microsecond (μs)** | 1/1,000,000 of a second | 1,000 nanoseconds | Radar, nuclear reactions, network latency testing. |
| **Nanosecond (ns)** | 1/1,000,000,000 of a second | 1,000 picoseconds | **HFT order execution**, DRAM access, light travel (~30 cm per ns). |
| **Picosecond (ps)** | 1/1,000,000,000,000 of a second | 1,000 femtoseconds | Quantum computing, laser physics, semiconductor testing. |
| **Femtosecond (fs)** | 10⁻¹⁵ seconds | 1,000 attoseconds | Molecular bond dynamics, ultrafast lasers (e.g., Nobel-winning spectroscopy). |
| **Attosecond (as)** | 10⁻¹⁸ seconds | 1/1,000 femtosecond | Electron motion imaging, atomic-scale reactions. |
| **Planck Time** | Smallest measurable time (~5.39×10⁻⁴⁴ s) | Quantum scale | Theoretical physics (quantum gravity, Big Bang models). |
| … | … | … | … |

## References

- https://es.wikipedia.org/wiki/Tiempo_Unix
- [Logical Physical Clocks and Consistent Snapshots in Globally Distributed Databases](https://cse.buffalo.edu/tech-reports/2014-04.pdf)
- https://news.ycombinator.com/item?id=19922062
- https://en.wikipedia.org/wiki/ISO_8601
- https://cr.yp.to/proto/utctai.html
- https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/
- https://www.creativedeletion.com/2015/03/19/persisting_future_datetimes.html
- https://blog.miguelgrinberg.com/post/it-s-time-for-a-change-datetime-utcnow-is-now-deprecated
- https://z.vandillen.dev/articles/unix-time-bad.md/
- http://yellerapp.com/posts/2015-01-12-the-worst-server-setup-you-can-make.html
- https://www.ucolick.org/~sla/leapsecs/
- http://www.leapsecond.com/java/gpsclock.htm
- https://zachholman.com/talk/utc-is-enough-for-everyone-right
- https://gist.github.com/timvisee/fcda9bbdff88d45cc9061606b4b923ca
- https://unix4lyfe.org/time/?v=1
- https://www.unixtimestamp.com/
- https://en.wikipedia.org/wiki/Year_2038_problem
- https://en.wikipedia.org/wiki/Time_formatting_and_storage_bugs
- https://www.youtube.com/watch?v=-5wpm-gesOY
- https://www.bipm.org/en/
- https://medium.com/@BlueTaslem/time-is-hard-for-computers-programmers-14ef2a7ece77
- [International Astronomical  Union](https://www.iau.org/)
- [‣](https://app.notion.com/p/fe6e9732f0ce4104b49c95bc3e106a70?pvs=21)
- [Frequency (Periodicity)](https://app.notion.com/p/Frequency-Periodicity-1c3c0f5171ec80c79de4e2520c7f3e51?pvs=21)
- [‣](https://app.notion.com/p/1c3c0f5171ec80a2b079c779bc1d140d?pvs=21)
- https://news.ycombinator.com/item?id=46368177