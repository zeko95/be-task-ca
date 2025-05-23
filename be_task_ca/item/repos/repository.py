from typing import Optional, List
from uuid import uuid4, UUID

from be_task_ca.item.interfaces.item_interface import ItemInterface
from be_task_ca.item.repos.model import Item


class ItemRepo(ItemInterface):
    def __init__(self):
        self.item = []

    def save_item(self, item: Item) -> Item:
        item.id = uuid4()
        self.item.append(item)
        return item

    def get_item_by_name(self, name: str) -> Optional[Item]:
        return next((item for item in self.item if item.name == name), None)

    def get_all_items(self) -> List[Item]:
        return self.item

    def get_item_by_id(self, id: UUID) -> Item:
        return next((item for item in self.item if item.id == id), None)
