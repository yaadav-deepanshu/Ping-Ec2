import socket
import time

SERVER_IP = "35.170.185.50"
SERVER_PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = "ping"
        client.sendto(message.encode(), (SERVER_IP, SERVER_PORT))  # Send ping request
        data, _ = client.recvfrom(1024)  # Receive response
        print(f"Server Response: {data.decode()}")  # Print response
        time.sleep(1)  # Wait 1 second before sending the next ping

except KeyboardInterrupt:
    print("\nClient stopped.")
    client.close()
