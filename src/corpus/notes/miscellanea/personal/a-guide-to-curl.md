---
tags: [note, guia]
---

# A Guide To Curl


> curl is a command-line tool for making HTTP requests to web servers, allowing data retrieval and interaction with web resources from the terminal.
> 

> curl is a versatile and powerful command-line tool used to perform a wide range of operations involving web resources, primarily focused on making HTTP requests to servers. It supports various protocols, including HTTP, HTTPS, FTP, FTPS, SCP, SFTP, LDAP, and more. curl is designed to work in terminal environments and provides extensive options for customization, making it a popular choice for debugging, testing, automation, and data retrieval tasks. It allows users to specify request methods, headers, data payloads, authentication details, and other parameters, and can be used to download/upload files, interact with APIs, perform benchmarking, and more.
> 

## Protocols

> curl supports a variety of protocols for making requests to different types of resources.
> 

Here are some of the protocols that `curl` can work with:

1. **HTTP/HTTPS**: The most common protocol for retrieving resources from the web.
2. **FTP/FTPS**: For transferring files using the File Transfer Protocol, with or without SSL/TLS encryption.
3. **SCP/SFTP**: Securely copy files between hosts using the Secure Copy Protocol or the SSH File Transfer Protocol.
4. **LDAP/LDAPS**: Query and manage information stored in LDAP directories, with or without SSL/TLS encryption.
5. **SMTP/SMTPS**: Send emails using the Simple Mail Transfer Protocol, with or without SSL/TLS encryption.
6. **IMAP/IMAPS**: Access and manage emails on remote servers using the Internet Message Access Protocol, with or without SSL/TLS encryption.
7. **POP3/POP3S**: Retrieve emails from a remote server using the Post Office Protocol, with or without SSL/TLS encryption.
8. **TELNET**: Connect to remote hosts using the Telnet protocol (less commonly used due to security concerns).
9. **RTMP/RTMPS**: Stream audio and video content using the Real-Time Messaging Protocol, with or without SSL/TLS encryption.
10. **Gopher**: Access resources on Gopher servers, an older protocol used for information retrieval.
11. **DICT**: Query dictionary definitions from dictionary servers.
12. **FILE**: Access local files on the filesystem using a file URL.

## Modifiers / Options / Flags

The main modifiers in the `curl` command allow you to customize and control various aspects of the HTTP request:

1. `X, --request <command>`: Specifies the HTTP request method (GET, POST, PUT, DELETE, etc.).
2. `H, --header <header>`: Adds custom headers to the request.
3. `d, --data <data>`: Sends data in the request body (for POST or PUT requests).
4. `F, --form <name=content>`: Sends form data as a multipart POST request.
5. `u, --user <user:password>`: Specifies username and password for basic authentication.
6. `-url <URL>`: Specifies the URL to send the request to.
7. `A, --user-agent <string>`: Sets the User-Agent header in the request.
8. `i, --include`: Includes the response headers in the output.
9. `-head`: Sends a HEAD request instead of GET.
10. `-data-raw <data>`: Sends data without processing (useful for custom POST requests).
11. `G, --get`: Converts the request to a GET request (with query parameters).
12. `b, --cookie <name=data>`: Sends cookies in the request.
13. `c, --cookie-jar <file>`: Stores cookies in the specified file.
14. `-compressed`: Requests compressed response.
15. `-data-urlencode <data>`: URL-encodes data and sends it in the request.
16. `L, --location`: Follows redirects.
17. `-max-time <seconds>`: Sets the maximum time allowed for the request.
18. `-output <file>`: Writes the response to the specified file.
19. `s, --silent`: Silences progress and error messages.
20. `v, --verbose`: Provides detailed information about the request and response.
21. `-insecure`: Disables SSL certificate verification.

These modifiers enable you to customize your `curl` requests based on your specific use case and interaction with web resources.

## References

- [Curl Converter](https://curlconverter.com/)
- [Curl](https://curl.se/)
- [Curl exercises](https://news.ycombinator.com/item?id=20811829)
- [Mastering the Curl Command Line | daniel.haxx.se](https://daniel.haxx.se/blog/2023/08/08/mastering-the-curl-command-line/)
- Curl HTTP/3 Performance
[https://news.ycombinator.com/item?id=39163948](https://news.ycombinator.com/item?id=39163948)
