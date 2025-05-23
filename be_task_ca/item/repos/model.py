from dataclasses import dataclass
from uuid import UUID, uuid4
from sqlalchemy.orm import Mapped, mapped_column
from be_task_ca.database import Base


@dataclass
class Item(Base):
    __tablename__ = "items"

    description: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4(),
        index=True,
    )
    name: Mapped[str] = mapped_column(unique=True, index=True)