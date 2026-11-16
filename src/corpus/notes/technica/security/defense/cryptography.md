---
tags: [note, security, defense, cryptographic]
---

# Cryptography

> Related: [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md)

> A **cryptography model** refers to the theoretical and mathematical framework that defines the principles and techniques used in cryptographic systems.

> A **cryptography system** is the practical implementation of cryptographic techniques to secure information and communication.

> La palabra “criptografía” proviene del griego antiguo “kryptos”, que significa “oculto” o “secreto”, y “graphein”, que significa “escribir”.

> Cryptography is the practice of securing communication and data through the use of mathematical techniques such as encryption, hashing, and digital signatures.

> A Cryptographic System is a set of algorithms, protocols, and procedures designed to secure communication, protect data integrity, and ensure confidentiality between two or more parties.

QA:

- Where linux stores the TSL Certificates?
- Where does the digital signature is store?

## Goals

- **Confidentiality [C]**: To ensure that data and information remain private and only accessible to authorized parties. Cryptographic techniques like encryption are used to protect sensitive data from unauthorized disclosure.
- **Data Integrity [IG]**: To maintain the accuracy and completeness of data during transmission and storage. Cryptographic hash functions and digital signatures are used to detect any unauthorized modifications or data tampering.
- **Non-Repudiation [R]**: To prevent parties from denying their involvement in a communication or transaction. Digital signatures provide evidence of the origin and approval of data, making it difficult for a sender to disown their actions.
- **Authentication [A]**: To verify the identity of users, devices, or entities involved in a communication or transaction. **Digital signatures** and **certificates** are used to establish trust and ensure the authenticity of participants.

## Uses

- **Digital Signature**: The process of generating a digital signature by applying a cryptographic hash function to a message and then encrypting the resulting hash with a private key. Digital signatures provide **authentication** and **non-repudiation**.
- **Ciphers**: Ciphers are algorithms used in cryptography to transform plaintext (original, readable data) into ciphertext (encrypted, unintelligible data) and vice versa. They provide **privacy**.
- **Hashing**: The application of a hash function to a piece of data to produce a fixed-size hash value. Hashing is used for **data integrity** and to generate **unique representations of data**.
- **Digital Certificate / Public Key Certificate / Identity Certificate**: A **digital certificate**, also known as a , is an **electronic document** used to verify the authenticity and identity of an entity in a digital communication environment. Digital certificates play a crucial role in establishing secure communication and trust over the internet and other computer networks.

## References

- See `openssl`
- See `openssh`
- See `tsl`
- See  `repr/crypto`
- [Steganography](https://en.wikipedia.org/wiki/Steganography)
- [Standard Model (Cryptography)](https://en.wikipedia.org/wiki/Standard_model_(cryptography))
- [How are ssl certificates verified?](https://stackoverflow.com/questions/188266/how-are-ssl-certificates-verified)
- [SoK: SSL and HTTPS: Revisiting past challenges and evaluating certificate trust model enhancements](https://css.csail.mit.edu/6.858/2020/readings/sok-ssl-https.pdf)
- [Analysis of the SSL 3.0 protocol](https://css.csail.mit.edu/6.858/2020/readings/ssl-analysis.pdf)
- [The Transport Layer Security (TLS) Protocol](https://datatracker.ietf.org/doc/html/rfc5246)
- [Handshake (computing)](https://en.wikipedia.org/wiki/Handshake_(computing))
- [Implementing a toy version of TLS 1.3](https://jvns.ca/blog/2022/03/23/a-toy-version-of-tls/)
- [The Illustrated TLS 1.3 Connection](https://tls13.xargs.org/)
- [TLS in the kernel](https://lwn.net/Articles/666509/)
- [OpenSSL](https://www.wikiwand.com/en/OpenSSL)
- [SSL: it’s hard to do right](https://recompilermag.com/issues/issue-1/ssl-its-hard-to-do-right)
- [How to encrypt and decrypt a string/text in shell (linux environment)](https://stackoverflow.com/questions/33718005/how-to-encrypt-and-decrypt-a-string-text-in-shell-linux-environment)
- [OpenSSL](https://www.openssl.org/)
- [Bad SSL](https://badssl.com/)
- [Lets Encrypt](https://letsencrypt.org/)
- [What is the criteria on which Chrome shows available certificates for client authentication](https://superuser.com/questions/1688418/what-is-the-criteria-on-which-chrome-shows-available-certificates-for-client-aut)
- [Mutual Authentication](https://www.wikiwand.com/en/Mutual_authentication)
- [Optimizing TLS for High–Bandwidth Applications in FreeBSD](https://people.freebsd.org/~rrs/asiabsd_2015_tls.pdf)
- [Transparent SSL/TLS interception](https://github.com/droe/sslsplit/)
- [Applicative Protocol Multiplexer (e.g. share SSH and HTTPS on the same port)](https://github.com/yrutschle/sslh/)
- [The GnuTLS Transport Layer Security Library](https://www.gnutls.org/)
- [How to debug SSL handshake using cURL?](https://stackoverflow.com/questions/17742003/how-to-debug-ssl-handshake-using-curl)
- [How to test TLS handshake process?](https://security.stackexchange.com/questions/118112/how-to-test-tls-handshake-process)
- [Public-Key Infrastructure (X.509) (pkix)](https://datatracker.ietf.org/wg/pkix/about/)
- [Cryptography](https://textbook.cs161.org/crypto/)
- [RSA (cryptosystem)](https://www.wikiwand.com/en/RSA_(cryptosystem))
- [Public-key cryptography](https://www.wikiwand.com/en/Public-key_cryptography)
- [Parser](https://8gwifi.org/PemParserFunctions.jsp)
- [Certificate authority](https://www.wikiwand.com/en/Certificate_authority)
- [Certificates for localhsot](https://news.ycombinator.com/item?id=17358339)
- [Public key certificate](https://en.wikipedia.org/wiki/Public_key_certificate)
- [X.509](https://www.wikiwand.com/en/X.509)
- [Public Key Certificate](https://en.wikipedia.org/wiki/Public_key_certificate)
- [Digital signature](https://en.wikipedia.org/wiki/Digital_signature)
- [Electronic signature](https://en.wikipedia.org/wiki/Electronic_signature)
- [Client certificate](https://www.wikiwand.com/en/Client_certificate)
- [Dissecting an SSL certificate](https://jvns.ca/blog/2017/01/31/whats-tls/)
- [Certificates](https://wizardzines.com/comics/certificates/)
- [Some list of openssl commands for check and verify your keys](https://gist.github.com/Hakky54/b30418b25215ad7d18f978bc0b448d81)
- [curl TSL](https://curl.se/docs/sslcerts.html)
- [How SSL Certificate Validation Works](https://embeddedcomputing.com/technology/security/software-security/how-ssl-certificate-validation-works)
- [Applied Cryptography Protocols, Algorithms, and Source Code in C](https://www.schneier.com/books/applied-cryptography)
- [Secure Multi Party Computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation)
- [awesome-cryptography](https://github.com/sobolevn/awesome-cryptography)
- [Comparison of cryptography libraries](https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries)
