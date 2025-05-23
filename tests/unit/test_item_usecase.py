import pytest
from uuid import uuid4
from be_task_ca.item.entities.item import Item
from be_task_ca.item.usecases.usecases import create_item, get_all


class FakeItemInterface:
    def __init__(self):
        self.saved_items = []
        self.existing_item = None

    def get_item_by_name(self, name: str):
        return self.existing_item if self.existing_item and self.existing_item.name == name else None

    def save_item(self, item: Item):
        self.saved_items.append(item)
        item.id = uuid4()
        return item

    def get_all_items(self):
        return self.saved_items


def test_create_item_success():
    interface = FakeItemInterface()
    new_item = Item(name="Test Item", price=10.0, description="Test description", quantity=2)

    saved_item = create_item(new_item, interface)

    assert saved_item.name == "Test Item"
    assert saved_item in interface.saved_items
    assert saved_item.id is not None


def test_create_item_raises_if_name_exists():
    existing = Item(name="Existing", price=10.0, description="Existing item", quantity=1)
    interface = FakeItemInterface()
    interface.existing_item = existing

    new_item = Item(name="Existing", price=15.0, description="Another item",  quantity=2)

    with pytest.raises(Exception) as e:
        create_item(new_item, interface)

    assert "already exists" in str(e.value)


def test_get_all_items_returns_saved_items():
    interface = FakeItemInterface()
    item1 = Item(name="Item1", price=5.0, description="Desc1",  quantity=1)
    item2 = Item(name="Item2", price=6.0, description="Desc2",  quantity=2)
    interface.save_item(item1)
    interface.save_item(item2)

    items = get_all(interface)

    assert len(items) == 2
    assert item1 in items
    assert item2 in items
