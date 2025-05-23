import pytest
from fastapi.testclient import TestClient

from be_task_ca.app import app

@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    return client


def test_create_user(
    client
):
    response = client.post(
        "/users/",
        headers={
            "Content-Type": "application/json",
        },
        json={
            "first_name": "test",
            "last_name": "test",
            "email": "test@example.com",
            "password": "password",
            "shipping_address": "shipping_address",
        }
    )
    assert response.status_code == 201