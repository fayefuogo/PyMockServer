import socket


# Test what response does our server return
def test_server_get_response():
    # Creates the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connects to the server at that particular address and with that particular port
    client_socket.connect(("127.0.0.1", 8080))
    # Information to send to server
    client_socket.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
    response = client_socket.recv(1024).decode()
    assert "200 OK" in response
    client_socket.close()


# What does it show if I send something terrible
def test_invalid_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))
    client_socket.send(b"NONSENSE REQUEST\r\n\r\n")
    response = client_socket.recv(1024).decode()
    assert "400 Bad Request" in response
    client_socket.close()