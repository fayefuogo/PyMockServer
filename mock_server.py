import http.server
import socketserver
import logging


class MockRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # HTTP status code for success
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Mock server response")

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Post request received"}')


def start_mock_server():
    logging.info("Starting mock server...")

    # Set up the server to listen on the loopback address and port 8080
    handler = MockRequestHandler
    server = socketserver.TCPServer(("127.0.0.1", 8080), handler)

    logging.info("Mock server is running on http://127.0.0.1:8080")

    try:
        server.serve_forever()  # Run the server forever
    except KeyboardInterrupt:
        logging.info("Shutting down mock server...")
        server.server_close()


if __name__ == "__main__":
    start_mock_server()

