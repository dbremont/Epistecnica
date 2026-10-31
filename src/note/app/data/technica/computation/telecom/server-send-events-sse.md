---
tags: [computer-network, protocol]
---

# Server Send Events (SSE)


Server-sent events (SSE) is a protocol for sending real-time updates or events from a server to a client over a single HTTP connection. It is often used to push real-time data, notifications, or updates from the server to web browsers and applications. SSE is based on a simple and efficient protocol that consists of plain text messages sent from the server to the client.

Here’s an overview of the Server-Sent Events protocol:

1. **Connection Initialization:**
    - The client initiates an SSE connection by creating an `EventSource` object in JavaScript. The client specifies the URL of the SSE endpoint it wants to connect to.
    
    ```jsx
    const eventSource = new EventSource('/sse-endpoint');
    ```
    
    - The client sends an HTTP GET request to the specified SSE endpoint on the server. The server acknowledges this request and begins preparing to send events.
2. **Server-to-Client Event Messages:**
    - Once the SSE connection is established, the server can send event messages to the client.
    - Each event message consists of a plain text string with the following structure:
    
    ```
    event: <event-name>
    data: <event-data>
    ```
    
    - The `event` field is optional and specifies the type or name of the event. It allows clients to differentiate between different types of events if needed.
    - The `data` field contains the payload or data associated with the event.
    
    Example SSE event message:
    
    ```
    event: update
    data: {"message": "A new update is available."}
    ```
    
    - Event messages are separated by a double newline (`\n\n`) to indicate the end of one event and the start of the next.
3. **Client-Side Event Handling:**
    - On the client side, JavaScript code can listen for incoming events and handle them using event listeners.
    - The `event` field in the event message defines event listeners. If the `event` field is omitted, the event is treated as a generic event.
    
    ```jsx
    eventSource.addEventListener('update', (event) => {    const eventData = JSON.parse(event.data);    // Handle the 'update' event});
    ```
    
4. **Connection Keep-Alive:**
    - SSE connections are designed to be long-lived and are kept open by the server. The server periodically sends a heartbeat or comment line to keep the connection alive.
    
    ```
    :keep-alive
    ```
    
    - The `:keep-alive` comment line ensures that the connection remains open even if there is no data to send.
5. **Error Handling:**
    - SSE connections can handle errors and connection interruptions gracefully. If the connection is lost, the client can automatically attempt to reconnect.
    
    ```jsx
    eventSource.onerror = function(event) {    console.error('SSE error:', event);    eventSource.close(); // Close the connection};
    ```
    
6. **Connection Termination:**
    - The connection can be terminated by either the client or the server.
    - Clients can close the connection using `eventSource.close()`.
    - Servers can close the connection by closing the underlying HTTP connection or by sending a special event message:
    
    ```
    event: goodbye
    data: {"message": "Server is closing the connection."}
    ```
    

Server-sent events provide a straightforward and efficient way to send real-time updates from the server to the client without complex libraries or frameworks. They are particularly well-suited for scenarios where the server needs to push updates to web clients in a unidirectional manner.

## Server

```python
from flask import Flask, Responsefrom flask_cors import CORSimport timeapp = Flask(__name__)# Enable CORS for your entire Flask appcors = CORS(app, resources={r"/*": {"origins": "*"}})  # Replace "*" with your allowed origins# A list to store connected clients (you might want to use a more robust data structure in a production environment).clients = []@app.route('/')def hello_world():    return jsonify(message="Hello, CORS is enabled!")@app.route('/sse')def sse():    def event_stream():        clients.append("Client")  # Add the client to the list        try:            while True:                data = "Pedro Server Time: " + str(time.time())                yield f"data: {data}\n\n"  # Send the data as an SSE event                time.sleep(1)  # Simulate updates every 1 second        except GeneratorExit:            clients.remove("Client")  # Remove the client from the list when they disconnect    return Response(event_stream(), content_type='text/event-stream')if __name__ == '__main__':    app.run(debug=True)
```

## Client (Browser)

```html
<!DOCTYPE html><html><head>    <title>SSE Client</title></head><body>    <div id="sse-data"></div>    <script>        const eventSource = new EventSource('http://127.0.0.1:5000/sse');        eventSource.onmessage = function(event) {            const sseData = document.getElementById('sse-data');            sseData.innerHTML = event.data;        };        eventSource.onerror = function(event) {            console.error('SSE error:', event);            eventSource.close();        };    </script></body></html>
```

## Client (C)

```c
#include <stdio.h>#include <stdlib.h>#include <string.h>#include <unistd.h>#include <arpa/inet.h>#include <netinet/in.h>#include <netdb.h>#define SSE_ENDPOINT "http://127.0.0.1:5000/sse"void handleSSEData(const char *data) {    // Handle the incoming SSE data here    printf("Received SSE data: %s\n", data);}int main() {    // Parse the SSE_ENDPOINT URL    char hostname[128];    char path[256];    int port = 80;    if (sscanf(SSE_ENDPOINT, "http://%127[^:/]:%d/%255[^\n]", hostname, &port, path) != 3) {        printf("Invalid SSE_ENDPOINT format\n");        return 1;    }    // Create a socket    int sockfd = socket(AF_INET, SOCK_STREAM, 0);    if (sockfd < 0) {        perror("Error creating socket");        return 1;    }    struct hostent *server = gethostbyname(hostname);    if (server == NULL) {        perror("Error resolving hostname");        return 1;    }    struct sockaddr_in server_addr;    memset(&server_addr, 0, sizeof(server_addr));    server_addr.sin_family = AF_INET;    server_addr.sin_port = htons(port);    memcpy(&server_addr.sin_addr.s_addr, server->h_addr, server->h_length);    // Connect to the server    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {        perror("Error connecting to server");        return 1;    }    // Send the HTTP GET request    char request[256];    snprintf(request, sizeof(request), "GET /%s HTTP/1.1\r\nHost: %s:%d\r\nAccept: text/event-stream\r\n\r\n", path, hostname, port);    write(sockfd, request, strlen(request));    // Read and process SSE data    char buffer[1024];    ssize_t bytesRead;    while ((bytesRead = read(sockfd, buffer, sizeof(buffer))) > 0) {        buffer[bytesRead] = '\0';        // Split SSE events (lines separated by '\n')        char *line = strtok(buffer, "\n");        while (line != NULL) {            if (strlen(line) > 0) {                handleSSEData(line);            }            line = strtok(NULL, "\n");        }    }    // Close the socket and exit    close(sockfd);    return 0;}
```

## References

[Server Send Events (SSE)](https://en.wikipedia.org/wiki/Server-sent_events)