import socket
import logging

logging.basicConfig(level=logging.INFO, filename="server.log", filemode="a",
                    format="%(asctime)s - %(message)s")



def start_server():
    logging.info("Server is starting...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8080))
    server_socket.listen(5)

    while True:
        client_socket, address = server_socket.accept()
        print(f"The address of the client is {address}")
        message = client_socket.recv(1024).decode()
        print(f"The sent message is {message}")
        if message.startswith("GET "):
            response = "HTTP/1.1 200 OK\n\nGET request received"
        else:
            response = "HTTP/1.1 400 Bad Request\n\nInvalid Request"
        client_socket.send(response.encode())
        client_socket.close()


if __name__ == "__main__":
    start_server()

