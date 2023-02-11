from abc import ABC, abstractmethod

from src.crypto_bot.models.user import User


class UserRepository(ABC):
    @abstractmethod
    async def insert_user(self, user: User) -> int:
        raise NotImplementedError()

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def update_user(self, user: User) -> int:
        raise NotImplementedError()

    @abstractmethod
    async def delete_user(self, user_id: int) -> int:
        raise NotImplementedError()
