import hashlib
from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..repos.repository import UserRepo
from ..interfaces.user_interface import UserInterface
from ..api.schema import CreateUserRequest, CreateUserResponse, AddToCartRequest, AddToCartResponse, CartItemResponse
from ..usecases.usecases import create_user, add_item_to_cart, get_items_in_cart
from ..entities.user import User
from ..entities.cart_item import CartItem
from ...item.api.api import get_item_repository
from ...item.interfaces.item_interface import ItemInterface

user_router = APIRouter(
    prefix="/users",
    tags=["user"],
)

def get_user_repository() -> UserInterface:
    return UserRepo()

user_repo_instance = UserRepo()

@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(
    dto: CreateUserRequest,
    repo: UserInterface = Depends(get_user_repository)
) -> CreateUserResponse:
    user = User(
        name=dto.first_name,
        last_name=dto.last_name,
        email=dto.email,
        password=hashlib.sha512(
            dto.password.encode("UTF-8")
        ).hexdigest(),
        address=dto.shipping_address,
    )
    try:
        user = create_user(user, repo)
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e)) from e
    # TODO
    """  Make DTOs -pydantic- to skip this amount of mappings"""
    return CreateUserResponse(
        id=user.id,
        first_name=user.name,
        last_name=user.last_name,
        email=user.email,
        shipping_address=user.address
    )

@user_router.post("/{user_id}/cart", status_code=status.HTTP_201_CREATED)
async def post_cart(
    user_id: UUID, dto: AddToCartRequest,
    user_repo: UserInterface = Depends(get_user_repository),
    item_repo: ItemInterface = Depends(get_item_repository)
) -> Response:
    cart_item = CartItem(
        user_id= user_id,
        item_id= dto.item_id,
        quantity= dto.quantity
    )
    try:
        add_item_to_cart(cart_item, user_repo, item_repo)
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e)) from e
    return Response(status_code=status.HTTP_201_CREATED)

@user_router.get("/{user_id}/cart", status_code=status.HTTP_200_OK)
async def get_cart(
    user_id: UUID,
    repo: UserInterface = Depends(get_user_repository)
) -> AddToCartResponse:
    cart_items = get_items_in_cart(user_id, repo)
    return AddToCartResponse(
        items=[
            CartItemResponse(
                item_id=item.item_id,
                quantity=item.quantity,
            )
            for item in cart_items
        ]
    )