from uuid import uuid4
from be_task_ca.user.repos.model import User, CartItem
from be_task_ca.user.repos.repository import UserRepo


def test_create_user():
    repo = UserRepo()
    user = User(
        id=None,
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        hashed_password="secret",
        shipping_address="123 Main St"
    )

    created_user = repo.create_user(user)

    assert created_user.id is not None
    assert created_user.email == "john@example.com"
    assert len(repo.users) == 1


def test_get_user_by_email():
    repo = UserRepo()
    user = User(
        id=None,
        first_name="Alice",
        last_name="Smith",
        email="alice@example.com",
        hashed_password="pass123",
        shipping_address="456 Maple Ave"
    )
    repo.create_user(user)

    found = repo.get_user_by_email("alice@example.com")
    not_found = repo.get_user_by_email("not@exist.com")

    assert found is not None
    assert found.email == "alice@example.com"
    assert not_found is None


def test_get_user_by_id():
    repo = UserRepo()
    user = User(
        id=None,
        first_name="Bob",
        last_name="Brown",
        email="bob@example.com",
        hashed_password="abc123",
        shipping_address="789 Oak Lane"
    )
    created = repo.create_user(user)

    found = repo.get_user_by_id(created.id)
    not_found = repo.get_user_by_id(uuid4())

    assert found is not None
    assert found.id == created.id
    assert not_found is None


def test_save_cart_item():
    repo = UserRepo()
    user_id = uuid4()
    item_id = uuid4()

    cart_item = CartItem(user_id=user_id, item_id=item_id, quantity=2)
    saved = repo.save_cart_item(cart_item)

    assert saved.user_id == user_id
    assert saved.quantity == 2
    assert len(repo.cart_items) == 1


def test_get_cart_items_by_user_id():
    repo = UserRepo()
    user1 = uuid4()
    user2 = uuid4()

    repo.save_cart_item(CartItem(user_id=user1, item_id=uuid4(), quantity=1))
    repo.save_cart_item(CartItem(user_id=user1, item_id=uuid4(), quantity=3))
    repo.save_cart_item(CartItem(user_id=user2, item_id=uuid4(), quantity=5))

    items_user1 = repo.get_cart_items_by_user_id(user1)
    items_user2 = repo.get_cart_items_by_user_id(user2)
    items_none = repo.get_cart_items_by_user_id(uuid4())

    assert len(items_user1) == 2
    assert len(items_user2) == 1
    assert items_none == []
