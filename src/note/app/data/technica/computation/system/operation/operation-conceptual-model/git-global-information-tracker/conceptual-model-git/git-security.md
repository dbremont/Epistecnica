# GIT: Security


## Security

Git has several security features built-in to protect the confidentiality, integrity, and availability of your code and repositories:

- **Authentication and Authorization**: Git supports multiple authentication and authorization methods, including SSH keys, HTTPS credentials, and OAuth tokens. This helps ensure that only authorized users can access and modify your repositories.
- **Cryptographic Integrity Checking**: Git uses cryptographic hashes to ensure the integrity of your code and repositories. Each commit is identified by a unique hash value, which makes it difficult for attackers to modify your code without detection.
- **Secure Transport Protocols**: Git supports several secure transport protocols, including SSH and HTTPS. These protocols encrypt all data transmitted between clients and servers, protecting your code from interception and tampering.
- **Access Controls**: Git provides several control mechanisms to restrict who can access and modify your repositories. For example, you can use branch permissions to prevent unauthorized changes to critical branches.
- **Auditing and Logging**: Git provides detailed audit logs and activity feeds to help you monitor and track changes to your repositories. This enables you to detect and respond to security incidents promptly.
- **Commit Signing** is a security practice used in Git to verify the authenticity and integrity of commits made to a Git repository. It helps ensure that commits have not been tampered with and were created by a trusted source.