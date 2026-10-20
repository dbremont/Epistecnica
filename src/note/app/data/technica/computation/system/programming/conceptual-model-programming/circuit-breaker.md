---
tags: [design-idiom]
---

# Circuit Breaker

- [Technique](note.html?n=technica/computation/system/programming/conceptual-model-programming/technique.md)

> A **Circuit Breaker** is a resilience design pattern that monitors for failures and, upon detecting a threshold of faults in a remote service or subsystem, transitions into an open state to short-circuit subsequent calls, thereby preventing cascading failures and enabling fault recovery via a reset or timeout mechanism.
> 

QA:

- When to close the **circuit breaker**?
- How do you determine an optimal failure threshold and timeout duration for a circuit breaker in a high-throughput microservices environment?
- What are the trade-offs between using a rolling window failure rate vs. a fixed consecutive failure count for triggering the circuit breaker?
- How can circuit breakers be composed or cascaded effectively in a distributed call graph to prevent systemic cascading failures?
- Describe how to implement an adaptive circuit breaker that dynamically adjusts thresholds based on service latency and error patterns.
- How do you integrate circuit breaker state management with persistent distributed stores to handle failover and restarts?
- What patterns or techniques can be combined with circuit breakers to handle partial failures and maintain system availability?
- Explain how the half-open state can be safely implemented to avoid thundering herd problems during recovery attempts.
- How would you design a circuit breaker to handle multi-tenant or multiservice scenarios with varying SLAs and error tolerances?
- Discuss the implications of false positives and false negatives in failure detection on system reliability and how to mitigate them.
- In a reactive or asynchronous programming model, how do circuit breakers interact with backpressure and event-driven streams?
- What monitoring and telemetry are critical for diagnosing and tuning circuit breaker behavior in production systems?
- How can circuit breakers be integrated with service mesh architectures, and what challenges arise in that context?
- What are security considerations when implementing circuit breakers that expose fallback behaviors or error responses?
- Explain the role of circuit breakers in conjunction with retry policies, and how to coordinate their behavior for optimal fault tolerance.
- How would you test a circuit breaker implementation to validate correct state transitions and resilience under simulated failure conditions?

## Signature

- **Design aspect:** It structures how components interact in a distributed system to improve reliability. It defines **how service calls are encapsulated** to prevent cascading failures.
- **Control aspect:** It manages **execution flow** dynamically—deciding when to allow requests, when to fail fast, or when to retry.

## Semantics

> 

| **Term / State** | **Description** | **Behavior** | **Typical Action / Transition** |
| --- | --- | --- | --- |
| **Closed** | Normal state where requests are allowed to pass through. | Requests are sent to the remote service; failures increment the failure count. | If failures exceed threshold → transition to Open. |
| **Open** | Circuit is tripped; requests are blocked or fail-fast to prevent further load on failing service. | Requests are rejected immediately without calling the remote service. | After a timeout or manual reset, transition to Half-Open. |
| **Half-Open** | Trial state to test if the remote service has recovered. | Allows a limited number of requests to pass through and monitors their success or failure. | If trial requests succeed → transition to Closed; if fail → back to Open. |
| **Failure Count** | Counter that tracks consecutive failures or failure rate within a window. | Incremented on failed requests; reset on successful requests or state transitions. | Crossing threshold triggers Open state. |
| **Success Count** | Counter to track successes during Half-Open state to determine recovery. | Incremented on successful trial requests. | Enough successes → transition to Closed. |
| **Timeout** | Duration to keep the circuit in open state before allowing retries (Half-Open). | Prevents retry flood; ensures a wait period for service recovery. | After timeout expires → transition to Half-Open. |
| **Fail-fast** | Behavior of immediately rejecting requests while circuit is open. | Improves responsiveness and prevents cascading failures. | Return error or fallback without remote call. |
| **Reset** | Action to clear counters and return the circuit breaker to closed state. | Typically manual or automatic after successful recovery. | Resets failure and success counts. |
| **Fallback** | Alternative action taken when requests are blocked or fail. | Can be a default value, cached response, or degraded functionality. | Invoked on Open or failure states. |

## Case Study

```bash
import static org.junit.jupiter.api.Assertions.*;
import org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker;
import org.junit.jupiter.api.Test;

class ThresholdCircuitBreakerTest {

    @Test
    void testThresholdCircuitBreaker() {
        final long threshold = 10L;
        ThresholdCircuitBreaker breaker = new ThresholdCircuitBreaker(threshold);

        // Initially closed: count = 0
        assertTrue(breaker.isClosed(), "Should start CLOSED");

        // Increment below threshold
        assertTrue(breaker.incrementAndCheckState(5L), "5 < 10 → still CLOSED");
        assertTrue(breaker.isClosed());

        // Increment reaching threshold exactly
        assertFalse(breaker.incrementAndCheckState(5L), "Total = 10 → OPEN");
        assertTrue(breaker.isOpen(), "Should be OPEN now");

        // Once open, no further increments will close it until reset
        assertFalse(breaker.incrementAndCheckState(1L));
        assertTrue(breaker.isOpen());

        // Close explicitly
        breaker.close();
        assertTrue(breaker.isClosed(), "Close resets counter and re-CLOSE");
        assertTrue(breaker.incrementAndCheckState(9L), "9 < 10 → CLOSED");

        // Edge case: threshold 0 = always OPEN
        ThresholdCircuitBreaker alwaysOpen = new ThresholdCircuitBreaker(0L);
        assertFalse(alwaysOpen.isClosed());
        assertFalse(alwaysOpen.incrementAndCheckState(0L));
    }
}
```

## References

- https://github.com/resilience4j/resilience4j
- https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern
- https://github.com/apache/commons-lang/blob/master/src/test/java/org/apache/commons/lang3/concurrent/ThresholdCircuitBreakerTest.java