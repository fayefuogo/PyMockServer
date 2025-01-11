import subprocess
import time
import socket

# Start the server in a separate process
server_process = subprocess.Popen(["python", "server.py"])

# Give the server some time to start
time.sleep(10)

# Then run the tests (e.g., test server responses)
def test_server_get_response():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))
    client_socket.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
    response = client_socket.recv(1024).decode()
    assert "200 OK" in response
    client_socket.close()

def test_invalid_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))
    client_socket.send(b"NONSENSE REQUEST\r\n\r\n")
    response = client_socket.recv(1024).decode()
    assert "400 Bad Request" in response
    client_socket.close()

# Terminate the server after tests
server_process.terminate()
