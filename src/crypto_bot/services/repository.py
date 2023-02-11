from src.crypto_bot.services.abstract_repository.configuration import (
    ConfigurationRepository,
)
from src.crypto_bot.services.abstract_repository.user import UserRepository
from src.crypto_bot.services.mongodb_repository.repository import (
    Repository as MongoDBRepository,
)


class Repository:
    def __init__(self, client):
        self.repository = MongoDBRepository(client)

    async def init_db(self, admin_id: int):
        await self.repository.init_db(admin_id)

    def get_user_repository(self) -> UserRepository:
        return self.repository.get_user_repository()

    def get_configuration_repository(self) -> ConfigurationRepository:
        return self.repository.get_configuration_repository()
