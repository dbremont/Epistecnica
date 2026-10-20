---
tags: [representation]
---

# Binary Representation


> ¡ El Esquema Universal de Representatión !
> 

> Representing data using a base-2 number system, where each digit (bit) is either 0 or 1. Binary is fundamental to digital computing and used to represent numbers, text, and other data types.
> 

> A binary file is a file format that stores data in specific format (not a text encoding).
> 

> **Binary Representation**: Representing data using a base-2 number system, where each digit (bit) is 0 or 1. Binary is fundamental to digital computing and represents numbers, text, and other data types.
> 

> Br : Dx → (0|1)*: Donde Dx (Dominio X).
> 

Here are some common types of binary files:

- **Executable files**: These are files that contain machine code and instructions that a computer’s processor can execute. Examples include programs, applications, and scripts.
- **Object files**: These are files that contain compiled code and data that is not yet linked into an executable file. A compiler usually generates object files and can be linked together to create an executable file.
- **Library files**: These are files that contain reusable code and data that can be shared by multiple programs. Examples include dynamic link libraries (DLLs) and shared object files (SOs).
- **Archive files**: These are files that contain multiple other files, often used for distribution or backup purposes. Examples include zip files, tarballs, and ISO images.
- **Data files**: These are files that contain data in binary format, such as images, videos, audio files, and database files.
- **Configuration files**: These are files that contain configuration settings for a program or system. Examples include INI files, XML files, and JSON files.
- **Cryptographic files**: These are files that contain encrypted data or keys used for encryption and decryption.
- **Virtual machine files**: These are files that contain a complete virtual machine environment, including operating system, applications, and data. Examples include VMware virtual machine files and VirtualBox disk images.

## Representing Binary

> Representing binary data is essential for transmitting and storing cryptographic information securely.
> 
- **Base64 Encoding**: A method that encodes binary data using 64 printable ASCII characters. Each 6 bits of binary data is represented by a single character, making it suitable for transferring binary data over text-based protocols.
- **Hexadecimal Representation**: Binary data can be represented using hexadecimal (base-16) notation. Each 4 bits of binary data is represented by a single hexadecimal digit (0-9, A-F).
- **Octal Representation**: A single octal digit represents 3 bits of binary data (0-7). Octal representation is rarely used in modern cryptographic systems.
- **Bitstrings**: Binary data can be represented directly as a sequence of 0s and 1s, with each bit having a specific meaning or position within the data.
- **Byte Arrays**: Binary data is often represented as arrays of bytes, each containing 8 bits.
- **Network Byte Order (Big-endian or Little-endian)**: Multi-byte binary data (e.g., integers, IP addresses) can be represented in different byte orders to ensure consistent interpretation across different platforms.
- **Object Serialization**: Binary data can be represented by serializing objects or data structures into a binary format, such as pickle in Python or protobuf (Protocol Buffers).
- **DER (Distinguished Encoding Rules) Format**: This is a binary format used to encode cryptographic elements like X.509 certificates and public keys.
- **ASN.1 (Abstract Syntax Notation One)**: A standard notation and set of rules for describing the structure and encoding of data in a platform-independent way. It is often used in combination with DER.

## References

- [Binary File](https://en.wikipedia.org/wiki/Binary_file)
- How to view a binary file?://unix.stackexchange.com/questions/282215/how-to-view-a-binary-file
- Byte [https://en.wikipedia.org/wiki/Byte](https://en.wikipedia.org/wiki/Byte)