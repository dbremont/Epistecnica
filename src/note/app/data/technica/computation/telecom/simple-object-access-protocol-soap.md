# Simple Object Access Protocol (SOAP)


SOAP (Simple Object Access Protocol) is a protocol specification for exchanging structured information to implement web services. It defines a set of rules for structuring messages, encoding data types, and exchanging messages between web services and clients. SOAP is often used for communication between applications running on different platforms and written in other programming languages. Below is an overview of the SOAP specification:

**SOAP Message Structure:** A SOAP message is an XML document consisting of the following elements:

1. **Envelope**: The top-level element that encloses the entire SOAP message. It contains mandatory namespaces for specifying the SOAP version.
2. **Header (optional)**: The `<Header>` element contains optional header information, such as security tokens or routing instructions. It is typically used for adding application-specific or transport-specific information.
3. **Body**: The `<Body>` element contains the actual SOAP message payload, which consists of one or more XML elements representing the data to be transmitted.
4. **Fault (optional)**: The `<Fault>` element is used to report errors or exceptions that occurred during the processing of the message. It contains a `<faultcode>`, `<faultstring>`, and `<detail>` element.

**SOAP Encoding Rules:** SOAP defines rules for encoding data types within the message. It supports various data types, including integers, strings, arrays, and complex types. The encoding can be based on XML Schema or other encoding standards.

**SOAP Binding:** SOAP messages can be transmitted using different transport protocols, such as HTTP, SMTP, and more. The SOAP binding defines how SOAP messages are encapsulated within the chosen transport protocol. For example, SOAP over HTTP uses HTTP headers and POST requests to transport SOAP messages.

**SOAP Versions:** There are two major versions of SOAP:

1. **SOAP 1.1**: This was the original version of SOAP and is still in use today, although it has been largely superseded by SOAP 1.2.
2. **SOAP 1.2**: SOAP 1.2 introduced several improvements and clarifications to the SOAP specification. It is backward compatible with SOAP 1.1 but provides better support for internationalization and more precise rules.

**WS-Security:** WS-Security is an extension to the SOAP specification that provides a framework for adding security features to SOAP messages. It defines how to sign, encrypt, and authenticate SOAP messages, making it suitable for secure communication over untrusted networks.

**Usage of SOAP:** SOAP is used in various scenarios, including:

- Web services: SOAP-based web services provide a standardized way for applications to communicate over the internet.
- Remote procedure calls (RPC): SOAP can invoke remote procedures or methods on a server.
- Enterprise service buses (ESB): SOAP is often used in ESBs to facilitate communication between different organizational components and systems.
- Messaging systems: SOAP can be used for asynchronous messaging between systems.
- B2B (business-to-business) communication: SOAP is used for secure and structured data exchange between businesses.

SOAP is a well-established protocol, and its specifications are maintained by standards organizations like the World Wide Web Consortium (W3C) and the Organization for the Advancement of Structured Information Standards (OASIS). It has played a significant role in enabling interoperability between heterogeneous systems in web services.

## SOAP API SPEC (WSDL)

> WSDL is a specification used in web services to describe the functionality of a web service and the methods it exposes.
> 

Here’s an overview of the **WSDL** specification:

**WSDL (Web Services Description Language):**

**Purpose**: - **WSDL** is an XML-based language that provides a standardized way to describe web services. - It defines the structure of SOAP (Simple Object Access Protocol) messages that are exchanged between service providers and consumers.

**Service Description**: - **WSDL** documents provide a comprehensive description of a web service, including the location of the service, the operations it supports, the format of input and output messages, and the data types used.

**Elements in a WSDL Document**:

- `<definitions>`: The root element of a WSDL document, which contains all other elements.
- `<types>`: Defines the data types used in the web service, often based on XML Schema.
- `<message>`: Describes the format of input and output messages for operations.
- `<portType>`: Defines a set of operations, including their names, input and output messages, and the order in which they are invoked.
- `<binding>`: Specifies how a port type’s operations are bound to a specific protocol, such as SOAP over HTTP.
- `<service>`: Describes the location of the service, including its endpoint URL.

**Message Exchange Patterns**: - **WSDL** supports various message exchange patterns, including one-way, request-response, and notifications.

**Data Types**: - **WSDL** allows the definition of complex data types, including structures and enumerations, using XML Schema.

**Version**: - There are two major versions of WSDL: - **WSDL** 1.1: The original version of **WSDL**. - **WSDL** 2.0: An updated version with improved support for complex messaging patterns and description of services.

**Tool Support**: - **WSDL** documents are often used to generate client-side code, server-side code, and documentation. - Various development tools and platforms, such as Apache Axis, WCF (Windows Communication Foundation), and Java EE, provide support for working with WSDL.

**Interoperability**: - **WSDL** plays a crucial role in achieving interoperability between different platforms and languages by providing a standardized way to describe services.

**WSDL Extensions**: - **WSDL** can be extended using various extensions, such as WS-Security for adding security information to the service description, and WS-Policy for specifying policies related to the service.

In summary, **WSDL** is a specification used in web services to provide a structured and standardized way of describing the functionality and capabilities of a service. It serves as a contract between service providers and consumers, ensuring that both parties understand how to interact with the service. **WSDL** is a fundamental component in the world of web services, enabling seamless integration and communication between different systems and platforms.

## References

- [xjc](https://stackoverflow.com/questions/6267478/how-to-disable-java-naming-conventions-in-xjc?rq=4)
- [SOAP Spec](https://www.w3.org/TR/soap/)
- [Web Services Description Language (WSDL) 1.1](https://www.w3.org/TR/wsdl.html)