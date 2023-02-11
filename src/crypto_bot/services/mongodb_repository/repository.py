from src.crypto_bot.models.user import User
from src.crypto_bot.services.abstract_repository.repository import (
    Repository as AbstractRepository,
)
from src.crypto_bot.services.mongodb_repository.configuration import (
    ConfigurationRepository,
)
from src.crypto_bot.services.mongodb_repository.user import UserRepository


class Repository(AbstractRepository):
    def __init__(self, client):
        db = client.crypto
        super().__init__(
            user_repository=UserRepository(collection=db.users),
            configuration_repository=ConfigurationRepository(collection=db.users),
        )
        self.client = client

    async def init_db(self, admin_id: int):
        db_names = await self.client.list_database_names()
        if "crypto" not in db_names:
            users = self.client.crypto.users
            users.create_index("user_id")
            user = User(user_id=admin_id, access=True)
            await self.user_repository.insert_user(user)
