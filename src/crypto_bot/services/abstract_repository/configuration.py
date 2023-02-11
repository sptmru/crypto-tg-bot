from abc import ABC, abstractmethod

from src.crypto_bot.models.configuration import Configuration


class ConfigurationRepository(ABC):
    @abstractmethod
    async def insert_configuration(self, configuration: Configuration) -> int:
        raise NotImplementedError()

    @abstractmethod
    async def get_configuration(self, configuration_id: int) -> Configuration:
        raise NotImplementedError()

    @abstractmethod
    async def update_configuration(self, configuration: Configuration) -> int:
        raise NotImplementedError()

    @abstractmethod
    async def delete_configuration(self, configuration_id: int) -> int:
        raise NotImplementedError()
