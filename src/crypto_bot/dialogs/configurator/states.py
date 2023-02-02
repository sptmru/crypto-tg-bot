from aiogram.dispatcher.filters.state import State, StatesGroup


class ConfiguratorDialog(StatesGroup):
    buy_mode = State()
    crypto_exchange = State()
    no_account = State()
    period = State()
    usd = State()
    api_key = State()
    api_secret = State()
    api_passphrase = State()
