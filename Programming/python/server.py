import socket
import threading

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Connected with {address}")

    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            print(f"Connection with {address} closed")
            break
        print(f"Received message from {address}: {message}")

        # Broadcast message to all clients
        for c in clients:
            c.send(message.encode())

    client_socket.close()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind(("localhost", 9999))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening for connections...")

clients = []

while True:
    # Accept a new connection
    client_socket, address = server_socket.accept()
    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
