import socket

# Create a socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost on port 8080
server_socket.bind(("127.0.0.1", 8080))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening on port 8080...")

while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive HTTP request
    request = client_socket.recv(1024).decode()
    print(f"Request:\n{request}")

    # Simple HTTP response
    response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\n<h1>Hello, Khalid!</h1>"
    
    # Send response
    client_socket.sendall(response.encode())

    # Close connection
    client_socket.close()
