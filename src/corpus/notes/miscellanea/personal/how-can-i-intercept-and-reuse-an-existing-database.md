---
tags: [note, como]
---

# How can I intercept and reuse an existing database connection file descriptor in a running process?


> TODO:  Create a concrete example using transactions add this example to https://github.com/csiglab/cs-analyst-labs.
> 

## Use a Proxy Process (IPC Approach)

```python
# server
import socket
import cx_Oracle

conn = cx_Oracle.connect("user/password@host:port/service_name")  # Maintain a single connection
cursor = conn.cursor()

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind("/tmp/oracle_db_socket")
server.listen(5)

while True:
    client, _ = server.accept()
    query = client.recv(1024).decode()
    cursor.execute(query)
    result = cursor.fetchall()
    client.send(str(result).encode())
    client.close()
```

```python
## client
import socket

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect("/tmp/oracle_db_socket")
client.send("SELECT * FROM employees".encode())

response = client.recv(4096).decode()
print(response)
```
