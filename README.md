# UDP Ping Server

## Overview
This project implements a **UDP Ping Server** that listens for incoming ping requests and responds with a timestamp. A client script is also provided to send ping requests to the server at a fixed interval (every 1 minute).

## Features
- Listens on a specified UDP port for incoming ping requests.
- Responds with a timestamp when a ping request is received.
- Client script sends pings every 60 seconds and logs responses.

## Prerequisites
- An AWS EC2 instance (Ubuntu or Amazon Linux recommended)
- Python 3 installed on both server and client machines

## Installation
### 1️⃣ Set Up the Server
#### **Install Python**
```sh
sudo apt update && sudo apt install python3 -y
```

#### **Create the UDP Ping Server**
Create a file named `udp_ping_server.py`:
```python
import socket
from datetime import datetime

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 9999  # UDP Port

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"UDP Ping Server listening on port {PORT}")

while True:
    data, addr = server.recvfrom(1024)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Received '{data.decode()}' from {addr} at {timestamp}")
    server.sendto(f"PONG {timestamp}".encode(), addr)
```

#### **Run the UDP Server**
```sh
python3 udp_ping_server.py
```

### 2️⃣ Set Up the Client
Create a file named `udp_ping_client.py`:
```python
import socket
import time
from datetime import datetime

SERVER_IP = "<EC2_PUBLIC_IP>"  # Replace with your EC2 public IP
SERVER_PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"PING {timestamp}"
    client.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    try:
        client.settimeout(5)
        response, addr = client.recvfrom(1024)
        print(f"Server Response: {response.decode()}")
    except socket.timeout:
        print("No response from server!")
    
    time.sleep(60)  # Ping every 60 seconds
```

#### **Run the UDP Client**
```sh
python3 udp_ping_client.py
```

## Verifying the Server
To check if the server is running and listening on **port 9999**:
```sh
sudo netstat -tulnp | grep 9999
```

To capture UDP traffic on the server:
```sh
sudo tcpdump -i any udp port 9999
```

## Firewall Configuration
Ensure that **UDP port 9999** is open in the **AWS Security Group**:
1. Go to the **AWS EC2 Dashboard**.
2. Select your instance and go to **Security Groups**.
3. Edit the **Inbound rules** and **Allow UDP traffic on port 9999**.

## License
This project is open-source and available under the **MIT License**.

---


