from typing import Optional, List
from uuid import UUID
from abc import ABC, abstractmethod

from ..entities.cart_item import CartItem
from ..entities.user import User

class UserInterface(ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, id: UUID) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def save_cart_item(self, cart_item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def get_cart_items_by_user_id(self, user_id: UUID) -> List[CartItem]:
        pass