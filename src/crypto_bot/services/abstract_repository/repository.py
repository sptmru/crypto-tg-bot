from abc import ABC

from src.crypto_bot.services.abstract_repository.configuration import (
    ConfigurationRepository,
)
from src.crypto_bot.services.abstract_repository.user import UserRepository


class Repository(ABC):
    def __init__(
        self,
        user_repository: UserRepository,
        configuration_repository: ConfigurationRepository,
    ):
        self.user_repository = user_repository
        self.configuration_repository = configuration_repository

    def get_user_repository(self) -> UserRepository:
        return self.user_repository

    def get_configuration_repository(self) -> ConfigurationRepository:
        return self.configuration_repository
