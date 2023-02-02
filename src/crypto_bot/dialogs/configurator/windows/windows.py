from typing import List

from aiogram_dialog import Window

from src.crypto_bot.dialogs.configurator.windows.api_key import api_key
from src.crypto_bot.dialogs.configurator.windows.api_passphrase import api_passphrase
from src.crypto_bot.dialogs.configurator.windows.api_secret import api_secret
from src.crypto_bot.dialogs.configurator.windows.buy_mode import buy_mode
from src.crypto_bot.dialogs.configurator.windows.crypto_exchange import crypto_exchange
from src.crypto_bot.dialogs.configurator.windows.no_account import no_account
from src.crypto_bot.dialogs.configurator.windows.period import period
from src.crypto_bot.dialogs.configurator.windows.usd import usd


def get_windows() -> List[Window]:
    return [
        buy_mode,
        crypto_exchange,
        no_account,
        period,
        usd,
        api_key,
        api_secret,
        api_passphrase,
    ]
