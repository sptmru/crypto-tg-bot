from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from src.crypto_bot.models.crypto_exchange import CryptoExchange


class BuyMode(Enum):
    PERSONAL = "personal"
    COMPANY = "company"


@dataclass
class KPIUsd:
    kpi: Decimal
    usd: Decimal


@dataclass
class Configuration:
    user_id: int = -1
    buy_mode: Optional[BuyMode] = None
    kpi_usd_values: List[KPIUsd] = field(default_factory=list)
    crypto_exchange: Optional[CryptoExchange] = None
    period: int = -1
    usd: Decimal = Decimal(-1)
    api_key: str = ""
    api_secret: str = ""
    api_passphrase: Optional[str] = None
