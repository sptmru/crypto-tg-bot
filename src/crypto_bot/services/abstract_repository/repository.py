from abc import ABC

from src.crypto_bot.services.abstract_repository.user_repository import UserRepository


class Repository(ABC):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_repository(self) -> UserRepository:
        return self.user_repository
