from aiogram.dispatcher.filters.state import State, StatesGroup


class ConfiguratorDialog(StatesGroup):
    buy_mode = State()
    company_buy = State()
    start_enter_kpi = State()
    enter_kpi = State()
    enter_usd_value = State()
    company_next_action = State()
    crypto_exchange = State()
    no_account = State()
    period = State()
    usd = State()
    api_key = State()
    api_secret = State()
    api_passphrase = State()
