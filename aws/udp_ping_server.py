import socket
import datetime

# Server configuration
HOST = "0.0.0.0"
PORT = 9999

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"UDP Ping Server listening on port {PORT}...")

while True:
    data, addr = server.recvfrom(1024)  # Receive ping request
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get timestamp
    print(f"Received '{data.decode()}' from {addr} at {timestamp}")

    if data.decode().strip().lower() == "ping":
        response = f"PONG {timestamp}"
        server.sendto(response.encode(), addr)  # Send response
