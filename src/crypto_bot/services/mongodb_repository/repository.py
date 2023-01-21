from src.crypto_bot.services.abstract_repository.repository import (
    Repository as AbstractRepository,
)
from src.crypto_bot.services.mongodb_repository.user_repository import UserRepository


class Repository(AbstractRepository):
    def __init__(self, client):
        db = client.crypto
        super().__init__(
            user_repository=UserRepository(collection=db.users),
        )
        self.client = client
