
from ..interfaces.user_interface import UserInterface
from ..entities.user import User


def create_user(user: User, interface: UserInterface) -> User:
    if interface.get_user_by_email(user.email):
        raise Exception(f"Can't create account, {user.email} already exists.")
    return interface.create_user(user)


# def add_item_to_cart(user_id: int, cart_item: AddToCartRequest, db: Session) -> AddToCartResponse:
#     user: User = get_user_by_id(user_id, db)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User does not exist")
#
#     item: Item = get_item_by_id(cart_item.item_id, db)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item does not exist")
#     if item.quantity < cart_item.quantity:
#         raise HTTPException(status_code=409, detail="Not enough items in stock")
#
#     item_ids = [o.item_id for o in user.cart_items]
#     if cart_item.item_id in item_ids:
#         raise HTTPException(status_code=409, detail="Item already in cart")
#
#     new_cart_item: CartItem = CartItem(
#         user_id=user.id, item_id=cart_item.item_id, quantity=cart_item.quantity
#     )
#
#     user.cart_items.append(new_cart_item)
#
#     save_user(user, db)
#
#     return list_items_in_cart(user.id, db)
#
#
# def list_items_in_cart(user_id, db):
#     cart_items = find_cart_items_for_user_id(user_id, db)
#     return AddToCartResponse(items=list(map(cart_item_model_to_schema, cart_items)))
#
#
# def cart_item_model_to_schema(model: CartItem):
#     return AddToCartRequest(item_id=model.item_id, quantity=model.quantity)
