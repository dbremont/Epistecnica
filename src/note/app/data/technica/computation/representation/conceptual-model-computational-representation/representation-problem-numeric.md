---
tags: [domain]
---

# Representation Problem: Numeric


> **Representation of Numeric Data** refers to the encoding of numerical values in a computational system using fixed or variable-length binary structures, adhering to formats such as **integer (two’s complement, sign-magnitude, or unsigned representation), floating-point (IEEE 754 single, double, or extended precision), fixed-point, or arbitrary-precision encoding**, where precision, range, and rounding behavior are dictated by hardware architecture, compiler optimizations, and language-specific data type implementations.
> 

> Precision: …
> 

> Limited Precision:  …
> 

> Arbitrary precision: …
> 

> Numerical System: …
> 

Terminology: 

- Number Based:
- Expanded Based Representation: `0.3`
- Compact  - Non Expanded Representation: `1/3`

## Digital Representation System

> **Representing numerical** values using various formats, such as integers, floating-point numbers, and complex numbers. Different bit-lengths and representations (e.g., two’s complement for signed integers) are used for efficient storage and calculations.
> 

> Note: All of this representations are **digital.**
> 

> **Unsigned Integer: Is the Vanilla Representation.**
> 

> How to map one representation to another? How  do we evaluate the **result representation**?
> 

> What is the role of the processor in supporting this number types? …
> 

| **Representation System** | **Encoding Method** | **Bit-Level Format** | **Precision & Range** | **Tag(s)** | **Use Cases** |
| --- | --- | --- | --- | --- | --- |
| **Unsigned Integer** | Direct binary encoding | Fixed-width binary | 0 to 2^n − 1 | integer, discrete | Addressing, indexing, counters |
| **Signed Integer (Two’s Complement)** | Negation via bit inversion + 1 | Fixed-width binary | −2^(n−1) to 2^(n−1)−1 | integer, discrete, arithmetic | Arithmetic, memory offsets |
| **Signed Integer (Sign-Magnitude)** | MSB as sign bit, rest as magnitude | Fixed-width binary | −(2^(n−1)−1) to 2^(n−1)−1 | integer, discrete, legacy | Historical use, floating-point mantissa |
| **Signed Integer (One’s Complement)** | Negation via bit inversion | Fixed-width binary | −(2^(n−1)−1) to 2^(n−1)−1 | integer, discrete, legacy | Legacy systems |
| **Fixed-Point Representation** | Integer-like, with an implicit scaling factor | Fixed-width binary | User-defined precision; range depends on scaling | fixed-point, arithmetic | DSP, financial computing |
| **Floating-Point (IEEE 754 Half-Precision)** | Sign + Exponent + Mantissa | 1-bit sign, 5-bit exponent, 10-bit mantissa | Approx. 6 × 10^−8 to 6.55 × 10^4 | floating-point, approximate, 16-bit | Graphics, ML accelerators, embedded |
| **Floating-Point (IEEE 754 Single-Precision)** | Sign + Exponent + Mantissa | 1-bit sign, 8-bit exponent, 23-bit mantissa | Approx. 1.18 × 10^−38 to 3.4 × 10^38 | floating-point, approximate, 32-bit | Scientific computing, graphics |
| **Floating-Point (IEEE 754 Double-Precision)** | Sign + Exponent + Mantissa | 1-bit sign, 11-bit exponent, 52-bit mantissa | Approx. 2.23 × 10^−308 to 1.8 × 10^308 | floating-point, approximate, 64-bit | Scientific computing, simulations |
| **Floating-Point (IEEE 754 Extended Precision)** | Wider exponent/mantissa | Typically 80-bit or variable | Greater than double precision; implementation-defined | floating-point, extended, high-precision | High-precision computing |
| **Arbitrary-Precision Integer (BigInt)** | Variable-length encoding | Dynamically allocated | Limited only by memory | integer, arbitrary-precision | Cryptography, symbolic computing |
| **Arbitrary-Precision Floating-Point** | Mantissa + Exponent (software-based) | Dynamically allocated | Limited only by memory | floating-point, arbitrary-precision | High-precision math, symbolic computation |
| **BCD (Binary-Coded Decimal)** | 4-bit binary per decimal digit | Packed or unpacked | Fixed precision; exact decimal representation | decimal, fixed-point, exact | Financial calculations, legacy systems |
| **Logarithmic Number System (LNS)** | Logarithmically encoded values | Exponent-only representation | High dynamic range; multiplication/division simplified, addition/subtraction complex | numeric, logarithmic, specialized | DSP, AI accelerators |
| **Residue Number System (RNS)** | Modular arithmetic with prime bases | Parallel modular representations | Application-specific; no unique ordering | numeric, modular, parallel | Cryptography, fault-tolerant computing |
| **IEEE 854 (Generalized Floating-Point Arithmetic)** | Sign + Exponent + Mantissa | Implementation-defined; generalizes IEEE 754 | Depends on implementation; supports radix other than 2 | floating-point, generalized | Scientific and high-precision computing |
| Fractional Binary Number (Full Representation) |  |  |  |  |  |
|  |  |  |  |  |  |

## Binary → Numeric Conversion

> Converting a binary sequence into a numeric value requires interpreting the bits according to the representation system.
> 

| **Binary Representation** | **Conversion Method** | **Case** |
| --- | --- | --- |
| Unsigned Integer | Sum of 2^i × bit_i | `1011₂` → 1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 = 11 |
| Two’s Complement | MSB as sign, invert & add 1 for negatives | `11110101₂` (8-bit) → −11 |
| Sign-Magnitude | MSB as sign, remaining as magnitude | `10001011₂` → −11 |
| One’s Complement | MSB as sign, invert bits for negative | `11110100₂` → −11 |
| Fixed-Point | Integer × 2^(−fractional_bits) | `1101.101₂` (Q3.4) → 13.625 |
| IEEE 754 Floating-Point | Decode sign, exponent (bias), mantissa | `0 10000010 10100000000000000000000₂` → 5.25 |
| BCD | Each 4-bit group → decimal digit | `0001 0010 1001₂` → 129 |
| LNS | Exponentiate the value of the stored logarithm | `log2(8)₂` → 8 |
| RNS | Reconstruct via Chinese Remainder Theorem | Modular values combined → original integer |

## Numeric Conversion → Binary

> Converting a numeric value into its binary representation requires encoding according to the target representation system, including considerations for sign, scaling, and precision.
> 

| **Binary Representation** | **Conversion Method** | **Case** |
| --- | --- | --- |
| Unsigned Integer | Divide repeatedly by 2, record remainders | `11 → 1011₂` |
| Two’s Complement | If negative, take absolute value → binary → invert bits → add 1; if positive, simple binary | `−11 → 10110101₂` (8-bit) |
| Sign-Magnitude | MSB = 0 (positive) / 1 (negative), rest = magnitude in binary | `−11 → 10001011₂` (8-bit) |
| One’s Complement | If negative, invert bits of positive binary | `−11 → 11110100₂` (8-bit) |
| Fixed-Point | Multiply by 2^(fractional_bits) → convert to integer → binary | `13.625` in Q3.4 → `1101.101₂` |
| IEEE 754 Floating-Point | 1. Determine sign bit; 2. Normalize number; 3. Encode exponent (with bias); 4. Encode mantissa | `5.25 → 0 10000010 01010000000000000000000₂` (single-precision) |
| Arbitrary-Precision Integer | Convert integer to binary; store in variable-length memory | `123456789 → 111010110111100110100010101₂` |
| Arbitrary-Precision Floating-Point | Split into mantissa + exponent; convert both to binary dynamically | `12345.6789 → mantissa + exponent binary` |
| BCD | Convert each decimal digit → 4-bit binary | `129 → 0001 0010 1001₂` |
| Logarithmic Number System (LNS) | Compute logarithm (usually base 2), encode exponent as binary | `8 → log2(8)=3 → 11₂` |
| Residue Number System (RNS) | Compute modulo with each chosen base | `29, bases = {3,5,7} → {2,4,1}` |

## Case Study

> 

## QA

- How to serialize numeric data?
- How to design the data storage / loading interaction?
- What is the representation capacity of a given encoding?
- What is the performance of the computations with the  given data representations?

## References

- https://en.wikipedia.org/wiki/Unum_(number_format)
- https://en.wikipedia.org/wiki/Floating-point_arithmetic
- https://en.wikipedia.org/wiki/Half-precision_floating-point_format
- https://en.wikipedia.org/wiki/Minifloat
- https://en.wikipedia.org/wiki/Bfloat16_floating-point_format
- https://en.wikipedia.org/wiki/TensorFloat-32
- https://en.wikipedia.org/wiki/Microsoft_Binary_Format
- https://en.wikipedia.org/wiki/IBM_hexadecimal_floating-point
- https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
- https://en.wikipedia.org/wiki/Tapered_floating_point
- https://en.wikipedia.org/wiki/Logarithmic_number_system
- https://en.wikipedia.org/wiki/Symmetric_level-index_arithmetic
- https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format
- https://en.wikipedia.org/wiki/Extended_precision
- https://en.wikipedia.org/wiki/Fixed-point_arithmetic
- https://en.wikipedia.org/wiki/List_of_arbitrary-precision_arithmetic_software
- https://en.wikipedia.org/wiki/Computable_number
- https://github.com/openjdk-mirror/jdk7u-jdk/blob/master/src/share/classes/java/math/BigDecimal.java
- https://stackoverflow.com/questions/10655254/how-bigdecimal-is-implemented
- [‣](https://app.notion.com/p/2b2598edb79080179c52c3dfbecbb5ce?pvs=21)
- [‣](https://app.notion.com/p/289598edb79080359cb0e8e7f900da96?pvs=21)
- [Numeric System](https://app.notion.com/p/Numeric-System-1d6c0f5171ec80899160d6587a6a9e3e?pvs=21)
- https://www.h-schmidt.net/FloatConverter/IEEE754.html
- Java BigDecimal