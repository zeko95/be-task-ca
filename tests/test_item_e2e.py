import pytest
from fastapi.testclient import TestClient

from be_task_ca.app import app

@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    return client


def test_create_item(
    client
):
    response = client.post(
        "/items/",
        headers={
            "Content-Type": "application/json",
        },
        json={
            "name": "test",
            "description": "test",
            "price": 100,
            "quantity": 1,
        }
    )
    assert response.status_code == 201