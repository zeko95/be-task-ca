from typing import List

from ..entities.item import Item
from ..interfaces.item_interface import ItemInterface


def create_item(item: Item, interface: ItemInterface) -> Item:
    if interface.get_item_by_name(item.name):
        raise Exception(f"An item with this name {item.name} already exists.")
    return interface.save_item(item)


def get_all(interface: ItemInterface) -> List[Item]:
    items = interface.get_all_items()
    return items
