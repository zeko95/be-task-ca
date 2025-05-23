import pytest
from fastapi.testclient import TestClient
from be_task_ca.app import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com",
            "password": "securepassword",
            "shipping_address": "123 Testing Lane",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["email"] == "jane@example.com"


def test_add_item_to_cart_and_get_cart(client):
    user_response = client.post(
        "/users/",
        json={
            "first_name": "Cart",
            "last_name": "Tester",
            "email": "cart@example.com",
            "password": "securepassword",
            "shipping_address": "Cart St 1",
        },
    )
    assert user_response.status_code == 201

    item_response = client.post(
        "/items/",
        json={
            "name": "Test Item",
            "price": 9.99,
            "description": "Item for cart testing",
            "quantity": 5,
        },
    )
    assert item_response.status_code == 201