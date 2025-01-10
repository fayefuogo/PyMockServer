import socket


def start_server():
    # This specifies the address family used by our server. This case it uses IPV4
    # This specifies the protocol used by the server in transmission of data across the web.
    # Our server uses TCP as opposed to UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This is a loopback address. This is the address of our server. It runs on our local machine.
    # 8080 is the listening port for HTTP communications
    server_socket.bind(("127.0.0.1", 8080))
    # Listens for a client to make a request
    server_socket.listen(5)

    while True:
        # Set up a connection between a client and our server.
        client_socket, address = server_socket.accept()
        # Print the address of our client
        print(f"The address of the client is {address}")
        # Get the first 1024 bytes of the sent information and decode it
        message = client_socket.recv(1024).decode()
        # Print the message to screen
        print(f"The sent message is {message}")
        if message.startswith("GET "):
            response = "HTTP/1.1 200 OK\n\nGET request received"
        else:
            response = "HTTP/1.1 400 Bad Request\n\nInvalid Request"
        # Create the response we send for every message
        client_socket.send(response.encode())
        # Close the setup connection
        client_socket.close()


if __name__ == "__main__":
    start_server()
