import socket
import datetime

# Server setup
HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"UDP Ping Server listening on port {PORT}")

while True:
    data, addr = server.recvfrom(1024)  # Receive ping request
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Received '{data.decode()}' from {addr} at {timestamp}")

    response = f"PONG {timestamp}"
    server.sendto(response.encode(), addr)  # Send response
