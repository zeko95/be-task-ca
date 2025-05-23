from typing import Optional
from uuid import UUID, uuid4
from .model import User
from ..interfaces.user_interface import UserInterface


class UserRepo(UserInterface):
    def __init__(self):
        self.users = []

    def get_user_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self.users if u.email == email), None)

    def get_user_by_id(self, id: UUID) -> Optional[User]:
        return next((u for u in self.users if u.id == id), None)

    def create_user(self, user: User) -> User:
        user.id = uuid4()
        self.users.append(user)
        return user