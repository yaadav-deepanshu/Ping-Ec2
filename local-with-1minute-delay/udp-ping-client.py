
import socket
import time
from datetime import datetime

SERVER_IP = "35.170.185.50"  # Replace with your EC2 IP
SERVER_PORT = 9999

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Send a "PING" message
    message = f"PING {timestamp}"
    client.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    # Receive response from server
    try:
        client.settimeout(5)  # Wait for max 5 seconds
        response, addr = client.recvfrom(1024)
        print(f"Server Response: {response.decode()}")
    except socket.timeout:
        print("No response from server!")

    # Wait for 60 seconds before sending the next ping
    time.sleep(60)
