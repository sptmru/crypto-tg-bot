from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row
from aiogram_dialog.widgets.text import Const, Format

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.models.configuration import Configuration
from src.crypto_bot.models.crypto_exchange import CryptoExchange


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    configuration: Configuration = manager.current_context().dialog_data[
        "configuration"
    ]
    configuration.crypto_exchange = CryptoExchange(button.widget_id)
    await manager.update({"configuration": configuration})
    await manager.dialog().switch_to(ConfiguratorDialog.period)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.buy_mode)


@exception_handler
async def no_account(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.no_account)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "crypto_exchange": messages.crypto_exchange(),
    }


def get_crypto_exchanges_keyboard() -> Group:
    group = Group(
        Row(
            Button(
                Const(CryptoExchange.BINANCE.value),
                id=CryptoExchange.BINANCE.value,
                on_click=next_click,
            ),
            Button(
                Const(CryptoExchange.KUCOIN.value),
                id=CryptoExchange.KUCOIN.value,
                on_click=next_click,
            ),
        ),
        Row(
            Button(
                Const(CryptoExchange.HUOBI.value),
                id=CryptoExchange.HUOBI.value,
                on_click=next_click,
            ),
            Button(
                Const(CryptoExchange.BYBIT.value),
                id=CryptoExchange.BYBIT.value,
                on_click=next_click,
            ),
        ),
        Button(
            Const(messages.no_account_button()),
            id="crypto_exchange_no_account",
            on_click=no_account,
        ),
    )
    return group


crypto_exchange = Window(
    Format("{crypto_exchange}"),
    get_crypto_exchanges_keyboard(),
    get_back_cancel_keyboard(window_name="crypto_exchange", on_back=back_click),
    state=ConfiguratorDialog.crypto_exchange,
    getter=get_data,
)
