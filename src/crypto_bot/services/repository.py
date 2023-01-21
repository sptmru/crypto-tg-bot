from src.crypto_bot.services.abstract_repository.user_repository import UserRepository
from src.crypto_bot.services.mongodb_repository.repository import (
    Repository as MongoDBRepository,
)


class Repository:
    def __init__(self, client):
        self.repository = MongoDBRepository(client)

    def get_user_repository(self) -> UserRepository:
        return self.repository.get_user_repository()
