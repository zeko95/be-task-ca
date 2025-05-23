from typing import Optional
from dataclasses import dataclass
from uuid import UUID

@dataclass
class User:
    name: str
    last_name: str
    email: str
    password: str
    address: str
    id: Optional[UUID] = None