import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print(f"Received message from {address}: {data}")

        # Echo the received data back to the client
        client_socket.send(data.encode())

    # Close the connection with the client
    client_socket.close()
    print(f"Connection with {address} closed")

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 connections

    print(f"Server is listening on {host}:{port}")

    while True:
        # Accept a new connection
        client_socket, address = server_socket.accept()

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 5555

    start_server(HOST, PORT)
