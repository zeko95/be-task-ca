from typing import Optional
from uuid import UUID
from abc import ABC, abstractmethod
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
