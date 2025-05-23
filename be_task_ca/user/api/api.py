import hashlib
from fastapi import APIRouter, Depends, status, HTTPException
from ..repos.repository import UserRepo
from ..interfaces.user_interface import UserInterface
from ..api.schema import CreateUserRequest, CreateUserResponse
from ..usecases.usecases import create_user
from ..entities.user import User

user_router = APIRouter(
    prefix="/users",
    tags=["user"],
)

def get_user_repository() -> UserInterface:
    return UserRepo()

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
