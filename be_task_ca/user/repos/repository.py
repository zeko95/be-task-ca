from typing import Optional, List
from uuid import UUID, uuid4
from .model import User, CartItem
from ..interfaces.user_interface import UserInterface


class UserRepo(UserInterface):
    def __init__(self):
        self.users = []
        self.cart_items = []

    def get_user_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self.users if u.email == email), None)

    def get_user_by_id(self, id: UUID) -> Optional[User]:
        return next((u for u in self.users if u.id == id), None)

    def create_user(self, user: User) -> User:
        user.id = uuid4()
        self.users.append(user)
        return user

    def save_cart_item(self, cart_item: CartItem) -> CartItem:
        self.cart_items.append(cart_item)
        return cart_item

    def get_cart_items_by_user_id(self, user_id: UUID) -> List[CartItem]:
        return [cart_item for cart_item in self.cart_items if cart_item.user_id == user_id]