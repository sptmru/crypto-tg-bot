from typing import Callable, Dict

from src.crypto_bot.models.user import User
from src.crypto_bot.services.abstract_repository.user import (
    UserRepository as AbstractUserRepository,
)
from src.crypto_bot.services.exceptions import DBError


def exception_handler(func: Callable):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as exc:
            raise DBError() from exc

    return wrapper


class UserRepository(AbstractUserRepository):
    def __init__(self, collection):
        self.collection = collection

    @exception_handler
    async def insert_user(self, user: User) -> int:
        query = user_to_dict(user)
        inserted = await self.collection.insert_one(query)
        return inserted.inserted_id

    @exception_handler
    async def get_user(self, user_id: int) -> User:
        query = {"user_id": user_id}
        user_dict = await self.collection.find_one(query)
        if user_dict is None:
            user = User()
        else:
            user_dict.pop("_id", None)
            user = user_from_dict(user_dict)
        return user

    @exception_handler
    async def update_user(self, user: User) -> int:
        query = {"user_id": user.user_id}
        new_values = {"$set": user_to_dict(user=user, with_user_id=False)}
        updated = await self.collection.update_one(query, new_values)
        return updated.modified_count

    @exception_handler
    async def delete_user(self, user_id: int) -> int:
        query = {"user_id": user_id}
        deleted = await self.collection.delete_one(query)
        return deleted.deleted_count


def user_from_dict(user_dict: Dict) -> User:
    user = User(
        user_id=user_dict["user_id"],
        sent_request=user_dict["has_sent_request"],
        access=user_dict["has_access"],
        configured=user_dict.get("configuration") is not None,
        configured_date_ts=user_dict["configured_date_ts"],
        next_date_ts=user_dict["next_date_ts"],
        last_date_ts=user_dict["last_date_ts"],
    )
    return user


def user_to_dict(user: User, with_user_id: bool = True) -> Dict:
    user_dict: Dict = {
        "has_sent_request": user.sent_request,
        "has_access": user.access,
        "configured_date_ts": user.configured_date_ts,
        "next_date_ts": user.next_date_ts,
        "last_date_ts": user.last_date_ts,
    }
    if with_user_id:
        user_dict["user_id"] = user.user_id
    return user_dict
