# Random Number Generator (RNG)


> A **Random Number Generator** is a computational or physical device/system that produces a sequence of numbers or symbols that lack any predictable pattern, i.e., appear random.
> 

Improve this note:

| Aspect | Recommendation |
| --- | --- |
| Definition | Use more precise, formal language about randomness, unpredictability, and statistical indistinguishability. |
| QA | Clarify/remove off-topic questions, expand on entropy and cryptographic unpredictability concepts. |
| PRNG Descriptions | Add rigorous detail on parameter selection, period, quality, and theoretical foundations. |
| CSPRNG | Add cryptographic security properties (e.g., next-bit unpredictability). |
| TRNG | Discuss entropy extraction and bias removal rigorously. |
| References | Add authoritative textbooks and standards for rigor and further reading. |
| Reproducibility | Emphasize importance and mechanisms to ensure reproducibility in simulations and testing. |
| Security | Add formal treatment of forward/backward secrecy and state compromise. |

QA:

- How to implement the “Linear Congruential Generator (LCG)“
- How to spot a Computer Scientist?
- What is a seed?
- What are the mathematical foundations behind common PRNG algorithms like Linear Congruential Generators and Mersenne Twister?
- How do you evaluate the statistical quality of an RNG? Which tests and metrics are standard?
- What makes a PRNG cryptographically secure, and how do CSPRNGs differ internally from non-secure PRNGs?
- How do you securely seed a CSPRNG, and what are the risks of poor seeding?
- Can you explain the concept of entropy and how it is measured and extracted in TRNGs?
- What are common sources of hardware entropy for TRNGs, and what are their advantages and disadvantages?
- How do you prevent RNG output prediction or state compromise attacks in cryptographic systems?
- What are the trade-offs between speed, security, and randomness quality when selecting an RNG for an application?
- How do you design and implement RNGs for parallel or distributed computing environments?
- Can RNG failures cause security vulnerabilities? Can you give examples of real-world incidents?
- How do you test RNG implementations for compliance with standards such as NIST SP 800-90 or FIPS 140-2?
- What is the role of post-processing (whitening) in RNGs, and when is it necessary?
- How do you handle RNGs in virtualized or containerized environments where hardware entropy sources may be limited?
- What are the best practices for maintaining RNG state and reseeding in long-running applications?
- Can you explain the difference between forward secrecy and backward secrecy in RNGs?
- How does quantum randomness differ from classical RNG methods, and what are current challenges in practical quantum RNG deployment?
- How do RNGs influence the reproducibility of simulations, and what strategies ensure consistent results across platforms?
- What cryptographic primitives are commonly used inside CSPRNG constructions?
- How do you evaluate and mitigate bias or correlation in RNG output streams?
- Can RNGs be backdoored? How can such backdoors be detected or prevented?

## Pseudorandom Number Generator (PRNG)

> 

| **PRNG** | **Description** | **Use Cases** |
| --- | --- | --- |
| **Linear Congruential Generator (LCG)** | One of the oldest and simplest PRNGs, defined by the recurrence relation: $X_{n+1} = (aX_n + c) \mod m$. | Simple simulations, embedded systems, early computing. |
| **Mersenne Twister** | A widely used PRNG with a very long period and high-quality output. | Simulations, Monte Carlo methods, gaming, scientific computing. |
| **Xorshift** | A family of fast PRNGs based on bitwise XOR and shift operations. | Gaming, lightweight applications, embedded systems. |
| **Multiply-with-Carry (MWC)** | An improvement over LCGs, combining multiplication and carry operations. | Simulations, general-purpose applications. |
| **PCG (Permuted Congruential Generator)** | A modern PRNG combining LCGs with permutation functions for improved quality. | Gaming, simulations, cryptography (lightweight). |
| **Blum Blum Shub** | A cryptographically secure PRNG based on quadratic residues. | Cryptography, secure communications. |
| **Fortuna** | A cryptographically secure PRNG designed for high security. | Cryptography, secure systems. |
| **WELL (Well Equidistributed Long-period Linear)** | A family of PRNGs designed to improve on the Mersenne Twister. | High-quality simulations, scientific computing. |
| **Middle Square Method** | A historical PRNG that squares a number and takes the middle digits as the next number. | Historical interest, educational purposes. |
| **Lehmer Random Number Generator** | A variant of LCGs, often used in early computing. | Early computing, simple simulations. |

### **Linear Congruential Generator (LCG)**

> A simple and fast pseudorandom number generator defined by the recurrence relation: $X_{n+1} = (a X_n + c) \mod m$ where $a$, $c$, and $m$ are integer parameters, and $X_0$ is the seed.
> 

> LCGs are widely used due to their simplicity but suffer from short periods and poor randomness quality for some applications.
> 

### **Cryptographically Secure PRNGs (CSPRNGs)**

> Pseudorandom number generators designed to be computationally infeasible to predict or reproduce without knowledge of the internal state.
> 
> 
> They use cryptographic primitives such as block ciphers or hash functions to produce output suitable for security-sensitive tasks like key generation and encryption.
> 

---

### **True Random Number Generator (TRNG)**

> A device or system that generates randomness from a physical, non-deterministic process, such as electronic noise, radioactive decay, or photon behavior.
> 
> 
> TRNGs provide genuinely unpredictable random numbers, unlike deterministic PRNGs, but often at slower speeds and with more complexity in extraction and processing.
> 

### **Cryptographically Secure PRNGs (CSPRNGs)**

> Pseudorandom number generators designed to be computationally infeasible to predict or reproduce without knowledge of the internal state.
> 

> They use cryptographic primitives such as block ciphers or hash functions to produce output suitable for security-sensitive tasks like key generation and encryption.
> 

## True Random Number Generator (TRNG)

> A device or system that generates randomness from a physical, non-deterministic process, such as electronic noise, radioactive decay, or photon behavior.
> 
> 
> TRNGs provide genuinely unpredictable random numbers, unlike deterministic PRNGs, but often at slower speeds and with more complexity in extraction and processing.
> 

## ✅ Checklist

> How to use properly RNG?
> 

| **Category** | **Checklist Item** |
| --- | --- |
| **Setup & Initialization** | Selected appropriate RNG type (PRNG / CSPRNG / TRNG) |
|  | Seeded properly with high-entropy source |
|  | Seed fixed and documented (if reproducibility is needed) |
| **RNG Source & Implementation** | Using a trusted library (e.g., Python `random`, C++ `<random>`, Java `SecureRandom`) |
|  | Avoiding outdated or weak RNGs (`rand()`, `java.util.Random` for crypto) |
|  | Custom RNG tested with tools (e.g., Dieharder, TestU01) |
| **Security Considerations** | Using cryptographically secure RNG where needed |
|  | Output used for secrets/keys/passwords |
|  | OS entropy source is used and trusted |
|  | Secure RNG outputs not reused improperly |
| **Distribution & Transformation** | Using correct distribution/transformation (e.g., `uniform`, `normal`) |
|  | Avoiding modulo bias (no `random() % n`) |
|  | Using built-in tools for sampling ranges |
| **Concurrency & Reusability** | Using thread-local RNG or synchronized access |
|  | Reusing RNG instances only when intentional and safe |
| **Reproducibility & Logging** | Seed stored or logged for reproducibility |
|  | Behavior (deterministic or not) is clearly documented |
| **Testing & Validation** | Statistical properties of output tested or validated |
|  | Reproducibility verified when seed is fixed |

## ⚠️ Common RNG Pitfalls and Better Practices

| **Pitfall** | **Why It’s a Problem** | **Better Practice / Fix** |
| --- | --- | --- |
| Using `rand()` in C/C++ | Poor randomness, low period, platform-dependent | Use `std::mt19937`, `random_device`, or a proper library RNG |
| Using PRNGs for cryptographic tasks | Easily predictable, insecure | Use CSPRNGs like `SecureRandom` (Java), `secrets` (Python), or `crypto` API |
| Using `random() % n` | Causes **modulo bias** if `RAND_MAX + 1` isn’t divisible by `n` | Use proper range sampling like `randint(a, b)` or `uniform_int_distribution` |
| Forgetting to seed the PRNG | Leads to same output on every run (especially with old PRNGs) | Seed with time or entropy source: `srand(time(NULL))` |
| Reseeding PRNG in a loop | Can reduce randomness or produce repeated values | Seed once at the start; reuse the PRNG |
| Using low-entropy seed (e.g., `srand(1)`) | Makes the sequence predictable | Use high-entropy seed sources (`random_device`, OS entropy) |
| Misunderstanding uniform distribution | Leads to skewed or non-uniform sampling | Use built-in uniform functions or carefully map to desired distribution |
| Sharing PRNGs between threads unsafely | Causes race conditions and correlated values | Use thread-local RNGs or mutexes |
| Assuming TRNGs are fast and always available | TRNGs are slow, hardware-dependent, and sometimes block | Use TRNGs only when necessary; buffer entropy or use hybrid approach |
| Using outdated or homebrew PRNGs | Usually have bad statistical properties | Use well-vetted algorithms (e.g., PCG, xoshiro256**, Mersenne Twister) |
| Ignoring reproducibility in scientific code | Makes results non-repeatable and hard to debug | Allow user-defined seed and log it |
| Using floating-point randoms for indexing | Can cause rounding issues and index errors | Use integer-based RNGs for indices |

## Decision Model

> **Note:** This is a rough first draft of the **decision model** generated by ChatGPT and may need improvement.
> 

When choosing a random number generator (RNG), consider the purpose of randomness required:

- For **cryptographic applications**, use a cryptographically secure RNG (CSPRNG) that is resistant to prediction and attacks.
- For **simulations, modeling, or games**, a high-quality pseudorandom number generator (PRNG) with a long period and good statistical properties is sufficient.
- For **reproducibility**, ensure the RNG supports seeding to recreate the same sequence if needed.
    
    Evaluate trade-offs between randomness quality, reproducibility, and resource usage based on the application’s needs.
    

## Security

RNGs used in security-sensitive contexts must be resistant to reverse engineering and prediction.

- Avoid using standard PRNGs like linear congruential generators for cryptographic purposes.
- Use hardware entropy sources or operating system-provided cryptographic RNGs.
- Regularly reseed the RNG with fresh entropy to maintain unpredictability.
- Validate the RNG output against known statistical tests to detect failures or attacks.
- Securely manage seeds and internal states to prevent leakage or replay attacks.

## Performance

> **Note:** This is a rough first draft of the **performance section** generated by ChatGPT and may need improvement.
> 

RNG performance depends on the algorithm complexity and source of entropy:

- PRNGs are generally faster and consume less CPU than CSPRNGs but are less secure.
- Hardware RNGs can offer high throughput but may have availability or cost constraints.
- Consider the overhead of seeding and reseeding, especially in high-frequency or real-time applications.
- Use batch generation or buffering strategies to reduce performance bottlenecks.
- Profile RNG performance in the target environment to ensure it meets latency and throughput requirements.

## Uses

| **Use Case** | **Description** | **Example Applications** | **Notes** |
| --- | --- | --- | --- |
| **Simulation & Modeling** | Generate random variables to model real-world processes | Monte Carlo simulations, physics models | Requires statistically good randomness, reproducibility useful |
| **Cryptography** | Secure key generation, nonce creation, random padding | SSL/TLS keys, digital signatures | Must use cryptographically secure RNGs (CSPRNG) |
| **Gaming & Gambling** | Random outcomes for fairness in games | Video games, lotteries, slot machines | Needs good randomness and unpredictability |
| **Random Sampling** | Selecting random samples from datasets | Surveys, randomized controlled trials | Requires unbiased, uniform sampling |
| **Procedural Generation** | Create content algorithmically | Terrain generation in games, textures | Requires reproducible RNG for consistency |
| **Testing & Debugging** | Generate random test data or inputs | Software testing, fuzz testing | Reproducibility via seed is important |
| **Load Balancing** | Distribute requests randomly | Server load balancing, network routing | Simple PRNGs often sufficient |
| **Security Tokens** | Generate session IDs, OTPs, password salts | Multi-factor authentication | Requires secure RNG to prevent predictability |
| **Machine Learning** | Initialize model parameters, shuffle datasets | Neural network weight initialization | Statistical quality important for training effectiveness |
| **Art & Creative Tools** | Generate random patterns, music, or art | Generative art, algorithmic music | Often combined with procedural generation |
| **….** | **…** | **…** | **…** |

## QA

### What is a seed?

> A **seed** is an initial value or input used to start a process that generates pseudo-random numbers.
> 

### Does a true random number generator require a seed?

> No, **True Random Number Generators (TRNGs)** typically **do not require seeds** because they rely on inherently unpredictable physical processes (like radioactive decay, thermal noise, or atmospheric noise) to generate randomness.
> 

## References

- https://en.wikipedia.org/wiki/Pseudorandom_generator
- https://en.wikipedia.org/wiki/Pseudorandom_number_generator
- https://en.wikipedia.org/wiki/Hardware_random_number_generator
- Random Numbers Fall Mainly in the Planes -  (PNAS, 1968)
- "Mersenne Twister: A 623-Dimensionally Equidistributed Uniform Pseudo-Random Number Generator" (1998)
- "PCG: A Family of Simple Fast Space-Efficient Statistically Good Algorithms for Random Number Generation" (2014)
- "A Simple Unpredictable Pseudo-Random Number Generator" (SIAM J. Comput., 1986)
- SP 800-90A: Recommendation for Random Number Generation Using Deterministic Random Bit Generators (NIST, 2015)
- Analysis and Design of Random Number Generators (Various papers on RNG security)
- RFC 4086: Randomness Requirements for Security (IETF, 2005)