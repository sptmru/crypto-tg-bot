from decimal import Decimal
from typing import Callable, Dict, List

from src.crypto_bot.models.configuration import BuyMode, Configuration, KPIUsd
from src.crypto_bot.models.crypto_exchange import CryptoExchange
from src.crypto_bot.services.abstract_repository.configuration import (
    ConfigurationRepository as AbstractConfigurationRepository,
)
from src.crypto_bot.services.exceptions import DBError


def exception_handler(func: Callable):
    async def wrapper(*args):
        try:
            return await func(*args)
        except Exception as exc:
            raise DBError() from exc

    return wrapper


class ConfigurationRepository(AbstractConfigurationRepository):
    def __init__(self, collection):
        self.collection = collection

    @exception_handler
    async def insert_configuration(self, configuration: Configuration) -> int:
        query = {"user_id": configuration.user_id}
        new_values = {"$set": {"configuration": configuration_to_dict(configuration)}}
        updated = await self.collection.update_one(query, new_values)
        return updated.modified_count

    @exception_handler
    async def get_configuration(self, configuration_id: int) -> Configuration:
        query = {"user_id": configuration_id}
        user_dict = await self.collection.find_one(query)
        configuration = configuration_from_dict(user_dict)
        return configuration

    @exception_handler
    async def update_configuration(self, configuration: Configuration) -> int:
        print(configuration)
        query = {"user_id": configuration.user_id}
        new_values = {"$set": {"configuration": configuration_to_dict(configuration)}}
        updated = await self.collection.update_one(query, new_values)
        return updated.modified_count

    @exception_handler
    async def delete_configuration(self, configuration_id: int) -> int:
        query = {"user_id": configuration_id}
        new_values = {"$unset": "configuration"}
        updated = await self.collection.update_one(query, new_values)
        return updated.modified_count


def configuration_from_dict(user_dict: Dict) -> Configuration:
    if user_dict is None:
        configuration = Configuration()
    else:
        configuration_dict = user_dict.get("configuration", None)
        if configuration_dict is None:
            configuration = Configuration()
        else:
            configuration = Configuration(
                user_id=user_dict["user_id"],
                buy_mode=BuyMode(configuration_dict["buy_mode"]),
                crypto_exchange=CryptoExchange(configuration_dict["crypto_exchange"]),
                period=configuration_dict["period"],
                usd=Decimal(configuration_dict["usd"]),
                kpi_usd_values=get_kpi_usd_values(configuration_dict["kpi_usd_values"]),
                api_key=configuration_dict["api_key"],
                api_secret=configuration_dict["api_secret"],
                api_passphrase=configuration_dict["api_passphrase"],
            )
    return configuration


def configuration_to_dict(configuration: Configuration) -> Dict:
    configuration_dict: Dict = {
        "buy_mode": configuration.buy_mode.value,  # type: ignore
        "crypto_exchange": configuration.crypto_exchange.value,  # type: ignore
        "period": configuration.period,
        "usd": str(configuration.usd),
        "usd_kpi_values": get_kpi_usd_values_list(configuration.kpi_usd_values),
        "api_key": configuration.api_key,
        "api_secret": configuration.api_secret,
        "api_passphrase": configuration.api_passphrase,
    }
    return configuration_dict


def get_kpi_usd_values_list(kpi_usd_values: List[KPIUsd]) -> List:
    kpi_usd_list = []
    for kpi_usd in kpi_usd_values:
        kpi_usd_list.append(
            {
                "kpi": str(kpi_usd.kpi),
                "usd": str(kpi_usd.usd),
            }
        )
    return kpi_usd_list


def get_kpi_usd_values(kpi_usd_values_list: List) -> List[KPIUsd]:
    kpi_usd_values = []
    for kpi_usd in kpi_usd_values_list:
        kpi_usd_values.append(
            KPIUsd(
                kpi=Decimal(kpi_usd["kpi"]),
                usd=Decimal(kpi_usd["usd"]),
            )
        )
    return kpi_usd_values
