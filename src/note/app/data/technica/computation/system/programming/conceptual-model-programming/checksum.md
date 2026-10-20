# Checksum


> A **checksum** is a calculated value derived from a data set, used to verify the integrity of that data by detecting errors during transmission or storage, allowing for the identification of alterations or corruption.
> 

## Uses

> In computer science, **checksums** fall under several related topics, including:
> 
1. **Data Integrity**: Ensuring that data is accurate and unaltered during storage or transmission.
2. **Error Detection and Correction**: Techniques used to identify and correct errors in data.
3. **Networking**: Protocols that ensure reliable data transmission over networks, such as TCP/IP.
4. **Cryptography**: Techniques for secure communication, where checksums can be used alongside cryptographic methods for data validation.
5. **File Storage and Systems**: Methods for verifying the integrity of files stored on disks or transmitted over networks.

## Methods

> 

| **Method** | **Description** | **Advantages** | **Use Cases** |
| --- | --- | --- | --- |
| **Parity Bit** | Adds a single bit to the data to ensure even or odd parity. | Simple and low overhead. | Basic error detection in data storage. |
| **Checksum (Simple Sum)** | Adds the binary values of data segments and takes the modulo. | Easy to compute and implement. | Basic error detection in network protocols. |
| **CRC (Cyclic Redundancy Check)** | Uses polynomial division to detect changes in data. | Highly effective at detecting burst errors. | Network communications, file storage. |
| **MD5 Checksum** | Produces a 128-bit hash value from data for integrity checks. | Fast and widely used, but vulnerable to collisions. | File verification, checksums in software downloads. |
| **SHA-1/SHA-256** | Produces a cryptographic hash for secure data integrity checks. | Stronger security and resistance to collisions. | Secure file transfers, digital signatures. |
| **Adler-32** | Combines checksum and CRC principles for fast error detection. | Faster than CRC, suitable for small data sizes. | File integrity checks in compression formats. |
| **Fletcher's Checksum** | Computes a two-dimensional checksum to detect errors. | More reliable than simple checksums, detects more errors. | Network packet error checking. |
| **HMAC (Hash-based Message Authentication Code)** | Combines a hash function with a secret key for data integrity and authentication. | Provides both integrity and authenticity. | Secure communication protocols (e.g., HTTPS). |

## References

- [Cryptography](https://app.notion.com/p/Cryptography-766587784d42445b9480fac1333fd42b?pvs=21)
- https://en.wikipedia.org/wiki/Checksum