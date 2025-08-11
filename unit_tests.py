import requests

def test_get_request():
    response = requests.get("http://127.0.0.1:8080")
    assert response.status_code == 200
    assert response.text == "Mock server response"

def test_post_request():
    response = requests.post("http://127.0.0.1:8080")
    assert response.status_code == 200
    assert response.json() == {"message": "Post request received"}
