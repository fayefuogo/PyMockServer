# PyMockServer

**PyMockServer** is a small Python project demonstrating two approaches to building and testing simple HTTP servers:

1. **Raw Socket Server (`server.py`)** – Implements a minimal HTTP server using Python’s `socket` module.
2. **Mock HTTP Server (`mockserver.py`)** – Uses Python’s built-in `http.server` to quickly spin up a mock server for testing.

The project also includes two styles of testing:
- **Low-level socket tests** (direct TCP communication)
- **High-level HTTP client tests** (via `requests`)

---

## Project Structure

| File              | Description |
|-------------------|-------------|
| **mockserver.py** | Simple mock HTTP server supporting `GET` and `POST` with fixed responses. |
| **server.py**     | Basic TCP socket HTTP server handling simple `GET` requests and rejecting invalid ones. |
| **test_server.py**| Integration tests for the raw socket server using direct TCP socket communication. |
| **unit_test.py**  | Unit tests for the mock HTTP server using the `requests` library. |




will complete later
