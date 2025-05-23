from fastapi import APIRouter, Depends, status, HTTPException
from be_task_ca.item.api.schema import CreateItemRequest, CreateItemResponse, AllItemsResponse
from ..usecases.usecases import create_item, get_all
from ..entities.item import Item
from ..interfaces.item_interface import ItemInterface
from ..repos.repository import ItemRepo

item_router = APIRouter(
    prefix="/items",
    tags=["item"],
)

def get_item_repository() -> ItemInterface:
    return ItemRepo()

@item_router.post("/", status_code=status.HTTP_201_CREATED)
async def post_item(
    dto: CreateItemRequest,
    repo: ItemInterface = Depends(get_item_repository)
) -> CreateItemResponse:
    item = Item(
        name=dto.name,
        description=dto.description,
        price=dto.price,
        quantity=dto.quantity
    )
    try:
        item = create_item(item, repo)
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e)) from e

    return CreateItemResponse(
        id=item.id,
        name= item.name,
        description= item.description,
        price= item.price,
        quantity= item.quantity
    )


@item_router.get("/")
async def get_items(
    repo: ItemInterface = Depends(get_item_repository)
) -> AllItemsResponse:
    items = get_all(repo)
    return AllItemsResponse(
        items=[
            CreateItemResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                price=item.price,
                quantity=item.quantity
            ) for item in items
        ]
    )
