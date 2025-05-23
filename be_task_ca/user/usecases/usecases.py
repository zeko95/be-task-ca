from typing import List
from uuid import UUID

from ..interfaces.user_interface import UserInterface
from ..entities.user import User
from ...item.entities.item import Item
from ...item.interfaces.item_interface import ItemInterface

from ...user.entities.cart_item import CartItem


def create_user(user: User, interface: UserInterface) -> User:
    if interface.get_user_by_email(user.email):
        raise Exception(f"Can't create account, {user.email} already exists.")
    return interface.create_user(user)


def add_item_to_cart(
        cart: CartItem,
        user: UserInterface,
        item: ItemInterface
):
    get_user: User = user.get_user_by_id(cart.user_id)

    if get_user is None:
        raise Exception(f"User doesn't exists.")

    get_item: Item = item.get_item_by_id(cart.item_id)
    if get_item is None:
        raise Exception(f"Item doesn't exists.")

    items_in_cart = next((c for c in get_user.cart_items if c["item_id"] == cart.item_id), None)
    if items_in_cart:
        raise Exception(f"No items in cart.")
    user.save_cart_item(cart)

    return 201


def get_items_in_cart(user_id: UUID, user_repo: UserInterface) -> List[CartItem]:
    return user_repo.get_cart_items_by_user_id(user_id)