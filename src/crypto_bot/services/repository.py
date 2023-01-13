from typing import List

from src.crypto_bot.services.user_repository import UserRepository


class Repository:
    def __init__(self, access_ids: List[int]):
        self.user_repository = UserRepository(access_ids)

    def get_user_repository(self) -> UserRepository:
        return self.user_repository
