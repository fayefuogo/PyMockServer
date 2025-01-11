import requests

def test_get_request():
    # Send a GET request to your mock server
    response = requests.get("http://127.0.0.1:8080")
    # Assert the response status code and content
    assert response.status_code == 200
    assert response.text == "Mock server response"

def test_post_request():
    # Send a POST request to your mock server
    response = requests.post("http://127.0.0.1:8080")
    # Assert the response status code and JSON content
    assert response.status_code == 200
    assert response.json() == {"message": "Post request received"}
