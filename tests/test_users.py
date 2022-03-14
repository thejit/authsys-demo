from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestUserRegistration:
    """TestUserRegistration test /users/register"""

    def test_get_request_return_405(self):
        """registration endpoint does only expect a post request"""
        response = client.get("/users/register")
        assert response.status_code == 405

    def test_post_request_without_body_return_422(self):
        """body should have username, password and fullname"""
        response = client.post("/users/register")
        assert response.status_code == 422

    def test_post_request_with_improper_body_returns_422(self):
        """all of username, password and fullname is required"""
        response = client.post("/users/register", json={"username": "jeong"})
        assert response.status_code == 422

    def test_post_request_with_proper_body_returns_201(self):
        response = client.post(
            "/users/register", json={"username": "jeongh", "password": "qweqwe123", "fullname": "lee"}
        )
        assert response.status_code == 201
