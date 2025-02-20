import socket
import time

# Server details
SERVER_IP = "35.170.185.50"
SERVER_PORT = 9999

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = "ping"
        client.sendto(message.encode(), (SERVER_IP, SERVER_PORT))  # Send ping request

        # Receive response
        data, _ = client.recvfrom(1024)
        print(f"Server Response: {data.decode()}")

        time.sleep(1)  # Wait 1 second before sending the next ping

except KeyboardInterrupt:
    print("\nClient stopped.")
    client.close()
