# Java BigDecimal

> 

> 
> 
> 
> BigDecimal is a numeric representation system based on finite base-10 decimal expansions. When representing values such as  `1/3` , which are rational numbers but have non-terminating decimal expansions in base 10 (0.3333…), BigDecimal must enforce finiteness by truncating or rounding the infinite expansion to a fixed precision (scale).
> 

> Note: One cool thing is that the decimal 1/3 can have a finite representation in other based like based `3`.
> 

BigDecimal:

- Use
- Representation
- Performance
- Pitfalls
- Observation

## Formulation

| Category | Type | Fact |
| --- | --- | --- |
| Representation | Representation | Value = unscaledValue × 10^(-scale) |
| Representation | Internal structure | Stores `BigInteger` (unscaled value) + `int` scale |
| Representation | Numeric model | Exact base-10 decimal (not binary floating point) |
| Object Model | Mutability | Immutable (operations return new instances) |
| Construction | Construction (String) | Exact decimal representation preserved |
| Construction | Construction (double) | Uses IEEE-754 binary approximation (may introduce error) |
| Construction | Construction (valueOf(double)) | Converts via string → safe and stable |
| Construction | Construction (BigInteger) | Always scale = 0 |
| Precision | Precision | No fixed default precision (arbitrary precision) - depends on the instance construction |
| Precision | Precision control | Only via `Java MathContext` |
| Scale | Scale definition | Number of digits after decimal point |
| Scale | Scale default | Derived from input representation, not fixed |
| Scale | Scale normalization | Not automatic |
| Arithmetic | Addition/Subtraction | Exact after scale alignment |
| Arithmetic | Multiplication | Exact; scales are added |
| Arithmetic | Division | May require rounding context or throws exception |
| Arithmetic | Division failure case | Throws `ArithmeticException` if non-terminating and no context |
| Arithmetic | Arithmetic engine | Operates on unscaled `BigInteger` values |
| Rounding | Rounding system | Controlled via `RoundingMode` |
| Rounding | Default rounding | None (must be explicitly specified) |
| Rounding | Rounding triggers | Division, scaling, `MathContext` usage |
| Comparison | equals() behavior | Strict (value + scale must match) |
| Comparison | compareTo() behavior | Numeric only (ignores scale) |
| Comparison | 1.0 vs 1.00 (equals) | false |
| Comparison | 1.0 vs 1.00 (compareTo) | equal |
| Performance | Performance | Slower than primitive floating-point types |
| Performance | Cost drivers | Division and large integer arithmetic |
| Reliability | Determinism | Only guaranteed if construction + context are consistent |
| Representation | Canonical form | Not enforced automatically |
| Application | Typical use cases | Finance, billing, accounting systems |
| Design Intent | Core design intent | Exact decimal arithmetic without binary floating-point error |

## QA

- Which problems do java BigDecimal has?

```bash
BigDecimal a = new BigDecimal("1.2345");
BigDecimal b = new BigDecimal("2.3456");
BigDecimal result = a.multiply(b); // Precision may exceed expectations
```

## References

- https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.htmlx
- https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/math/BigDecimal.html
- https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/math/BigDecimal.java
- [Number](https://app.notion.com/p/Number-1dec0f5171ec809d8838c20764714d52?pvs=21)