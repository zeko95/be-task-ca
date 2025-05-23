from typing import Optional, List
from dataclasses import dataclass, field
from uuid import UUID

from be_task_ca.user.entities.cart_item import CartItem


@dataclass
class User:
    name: str
    last_name: str
    email: str
    password: str
    address: str
    id: Optional[UUID] = None
    cart_items: List[CartItem] = field(default_factory=list)