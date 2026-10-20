# Database Record Identifier Models


> 

| Strategy | Description | Example |
| --- | --- | --- |
| Sequential Numeric ID | Assigns a unique identifier to each record in sequential order, typically incremented by one for each new record. | 1, 2, 3, 4, ... |
| Timestamps | Uses a timestamp value (e.g., Unix or database-specific timestamp) as a unique identifier, often combined with other attributes for uniqueness. | 1615323522 (Unix timestamp) |
| Random Alphanumeric IDs | Generates random alphanumeric strings of a specified length to serve as unique identifiers for database records. | "aB5Rt8qX", "K2jP3l5d", ... |
| Prefixed Hashids | Utilizes Hashids (a cryptographic hash function) to generate unique, reversible, and shorter identifiers, often prefixed with a specific string for context. | "user_1X6z", "order_2J8y", ... |
| Hashids | Generates unique, reversible, and shorter identifiers using a cryptographic hash function based on one or more input values (e.g., primary key values). | "o89xW7B", "m3EjR9k", ... |
| Semantic Keys | Constructs identifiers based on meaningful attributes or properties of the record, such as a combination of customer name and birth date for a customer record. | "JohnDoe1985", "AliceSmith1978", ... |
| UUIDs (Universally Unique Identifiers) | Generates unique 128-bit identifiers using standardized algorithms, typically represented as a 32-character hexadecimal string separated by hyphens. | "550e8400-e29b-41d4-a716-446655440000", "f47ac10b-58cc-4372-a567-0e02b2c3d479", ... |