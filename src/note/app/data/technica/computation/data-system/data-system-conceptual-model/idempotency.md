# Idempotency


> **Idempotency** is a property of certain operations in computing where performing the same action multiple times results in the same outcome as performing it once.
> 

> In other words, an idempotent operation can be repeated without changing the final result beyond the initial application.
> 

### Key Characteristics of Idempotency:

- **Repeatable without side effects**: Repeated execution of the operation does not produce any additional changes after the first execution.
- **Ensures consistency**: Useful in distributed systems where network failures or retries might cause an operation to be executed more than once.
- **Fault-tolerant**: Protects against duplicate requests or accidental retries by ensuring the system remains in a consistent state.

### Example in Real Life:

- **HTTP PUT Method**: The HTTP `PUT` method is idempotent because sending the same `PUT` request multiple times will not change the resource more than sending it once. For example, updating a user's profile with a `PUT` request to set their name to "John" will always result in the name being "John", regardless of how many times the request is sent.
- **Database Insert with Idempotency Key**: Imagine you're processing payments. If you accidentally submit the same payment request twice, an idempotent system would check whether that payment has already been processed using an idempotency key (like a unique transaction ID), and if so, avoid double charging the user.

### Idempotency in Message Delivery:

In **distributed systems**, idempotency is crucial for **at-least-once** delivery semantics, where messages might be delivered more than once. If the receiving system's operations are idempotent, even if a message is delivered twice, the system will only process it once, avoiding unintended side effects like double processing, charging, or state changes.

### Benefits:

- **Reduces complexity** in handling retries and failure recovery.
- **Increases fault tolerance** by ensuring operations can be safely retried without unwanted side effects.

### Non-idempotent Operations:

Operations that **do** change the system's state each time they are executed (e.g., **incrementing a counter** or **adding a record** to a database) are **non-idempotent**. These require special handling in distributed systems to avoid unintended duplicates or state changes.