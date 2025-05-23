import pytest
from uuid import uuid4
from unittest.mock import MagicMock

from be_task_ca.user.entities.user import User
from be_task_ca.user.entities.cart_item import CartItem
from be_task_ca.item.entities.item import Item
from be_task_ca.user.usecases import usecases


def test_create_user_success():
    user = User(
        id=None,
        name="Alice",
        last_name="Smith",
        email="alice@example.com",
        password="pass123",
        address="Wonderland"
    )

    mock_interface = MagicMock()
    mock_interface.get_user_by_email.return_value = None
    mock_interface.create_user.return_value = user

    result = usecases.create_user(user, mock_interface)

    assert result == user
    mock_interface.create_user.assert_called_once_with(user)


def test_create_user_duplicate_email():
    user = User(
        id=None,
        name="Bob",
        last_name="Smith",
        email="bob@example.com",
        password="abc123",
        address="Nowhere"
    )

    mock_interface = MagicMock()
    mock_interface.get_user_by_email.return_value = user

    with pytest.raises(Exception, match="bob@example.com already exists"):
        usecases.create_user(user, mock_interface)


def test_add_item_to_cart_success():
    user_id = uuid4()
    item_id = uuid4()

    cart_item = CartItem(user_id=user_id, item_id=item_id, quantity=1)

    mock_user = MagicMock()
    mock_user.get_user_by_id.return_value = User(
        id=user_id,
        name="Test",
        last_name="User",
        email="test@example.com",
        password="pass",
        address="Mars",
        cart_items=[]
    )

    mock_item = MagicMock()
    mock_item.get_item_by_id.return_value = Item(
        id=item_id,
        name="Book",
        description="Test book",
        price=12.99,
        quantity=1
    )

    response = usecases.add_item_to_cart(cart_item, mock_user, mock_item)

    assert response == 201
    mock_user.save_cart_item.assert_called_once_with(cart_item)


def test_add_item_to_cart_user_not_found():
    cart_item = CartItem(user_id=uuid4(), item_id=uuid4(), quantity=1)

    mock_user = MagicMock()
    mock_user.get_user_by_id.return_value = None

    mock_item = MagicMock()

    with pytest.raises(Exception):
        usecases.add_item_to_cart(cart_item, mock_user, mock_item)


def test_add_item_to_cart_item_not_found():
    user_id = uuid4()
    item_id = uuid4()
    cart_item = CartItem(user_id=user_id, item_id=item_id, quantity=1)

    mock_user = MagicMock()
    mock_user.get_user_by_id.return_value = User(
        id=user_id,
        name="Test",
        last_name="User",
        email="test@example.com",
        password="pass",
        address="Moon",
        cart_items=[]
    )

    mock_item = MagicMock()
    mock_item.get_item_by_id.return_value = None

    with pytest.raises(Exception):
        usecases.add_item_to_cart(cart_item, mock_user, mock_item)


def test_add_item_to_cart_duplicate_item():
    user_id = uuid4()
    item_id = uuid4()
    cart_item = CartItem(user_id=user_id, item_id=item_id, quantity=1)

    mock_user = MagicMock()
    mock_user.get_user_by_id.return_value = User(
        id=user_id,
        name="Jane",
        last_name="Doe",
        email="jane@example.com",
        password="secure",
        address="Sun",
        cart_items=[{"item_id": item_id}]
    )

    mock_item = MagicMock()
    mock_item.get_item_by_id.return_value = Item(
        id=item_id,
        name="Lamp",
        description="Shiny lamp",
        price=9.99,
        quantity=1
    )

    with pytest.raises(Exception):
        usecases.add_item_to_cart(cart_item, mock_user, mock_item)


def test_get_items_in_cart_success():
    user_id = uuid4()

    expected_items = [
        CartItem(user_id=user_id, item_id=uuid4(), quantity=2),
        CartItem(user_id=user_id, item_id=uuid4(), quantity=1),
    ]

    mock_repo = MagicMock()
    mock_repo.get_cart_items_by_user_id.return_value = expected_items

    result = usecases.get_items_in_cart(user_id, mock_repo)

    assert result == expected_items
    mock_repo.get_cart_items_by_user_id.assert_called_once_with(user_id)
