from typing import List

from aiogram_dialog import Window

from src.crypto_bot.dialogs.configurator.windows.api_key import api_key
from src.crypto_bot.dialogs.configurator.windows.api_passphrase import api_passphrase
from src.crypto_bot.dialogs.configurator.windows.api_secret import api_secret
from src.crypto_bot.dialogs.configurator.windows.buy_mode import buy_mode
from src.crypto_bot.dialogs.configurator.windows.company_buy import company_buy
from src.crypto_bot.dialogs.configurator.windows.company_next_action import (
    company_next_action,
)
from src.crypto_bot.dialogs.configurator.windows.crypto_exchange import crypto_exchange
from src.crypto_bot.dialogs.configurator.windows.enter_kpi import enter_kpi
from src.crypto_bot.dialogs.configurator.windows.enter_usd_value import enter_usd_value
from src.crypto_bot.dialogs.configurator.windows.no_account import no_account
from src.crypto_bot.dialogs.configurator.windows.period import period
from src.crypto_bot.dialogs.configurator.windows.start_enter_kpi import start_enter_kpi
from src.crypto_bot.dialogs.configurator.windows.usd import usd


def get_windows() -> List[Window]:
    return [
        buy_mode,
        company_buy,
        start_enter_kpi,
        enter_kpi,
        enter_usd_value,
        company_next_action,
        crypto_exchange,
        no_account,
        period,
        usd,
        api_key,
        api_secret,
        api_passphrase,
    ]
