from uuid import UUID

from be_task_ca.item.repos.repository import ItemRepo
from be_task_ca.item.repos.model import Item


def test_save_item_assigns_id_and_saves():
    repo = ItemRepo()
    item = Item(name="Laptop", description="Gaming Laptop", price=1200)

    saved_item = repo.save_item(item)

    assert saved_item.id is not None
    assert saved_item in repo.item
    assert isinstance(saved_item.id, UUID)


def test_get_item_by_name_returns_correct_item():
    repo = ItemRepo()
    item = Item(name="Phone", description="Smartphone", price=800)
    repo.save_item(item)

    result = repo.get_item_by_name("Phone")

    assert result is not None
    assert result.name == "Phone"


def test_get_item_by_name_returns_none_if_not_found():
    repo = ItemRepo()

    result = repo.get_item_by_name("Tablet")

    assert result is None


def test_get_all_items_returns_all_saved_items():
    repo = ItemRepo()
    item1 = Item(name="Mouse", description="Wireless Mouse", price=50)
    item2 = Item(name="Keyboard", description="Mechanical Keyboard", price=150)
    repo.save_item(item1)
    repo.save_item(item2)

    all_items = repo.get_all_items()

    assert len(all_items) == 2
    assert item1 in all_items
    assert item2 in all_items


def test_get_item_by_id_returns_correct_item():
    repo = ItemRepo()
    item = Item(name="Monitor", description="4K Monitor", price=300)
    saved = repo.save_item(item)

    result = repo.get_item_by_id(saved.id)

    assert result == saved


def test_get_item_by_id_returns_none_if_not_found():
    repo = ItemRepo()
    result = repo.get_item_by_id(UUID("00000000-0000-0000-0000-000000000000"))
    assert result is None
