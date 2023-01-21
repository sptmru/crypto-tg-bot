from typing import Callable

from src.crypto_bot.services.abstract_repository.user_repository import (
    UserRepository as AbstractUserRepository,
)
from src.crypto_bot.services.exceptions import DBError


def exception_handler(func: Callable):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as exc:
            raise DBError() from exc

    return wrapper


class UserRepository(AbstractUserRepository):
    def __init__(self, collection):
        self.collection = collection

    @exception_handler
    def has_user_access(self, user_id: int) -> bool:
        query = {"user_id": user_id}
        user = self.collection.find_one(query)
        if user is None:
            return False
        return True

    @exception_handler
    def provide_access(self, user_id: int) -> None:
        query = {"user_id": user_id}
        self.collection.insert_one(query)

    @exception_handler
    def revoke_access(self, user_id: int) -> None:
        query = {"user_id": user_id}
        self.collection.delete_one(query)
