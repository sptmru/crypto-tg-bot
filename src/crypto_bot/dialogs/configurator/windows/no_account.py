from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row, Url
from aiogram_dialog.widgets.text import Const, Format

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.models.crypto_exchange import CryptoExchanges


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "no_account": messages.no_account(),
    }


def get_crypto_exchanges_keyboard() -> Group:
    group = Group(
        Row(
            Url(
                Const(CryptoExchanges.binance.exchange),
                Const(CryptoExchanges.binance.url),
            ),
            Url(
                Const(CryptoExchanges.kucoin.exchange),
                Const(CryptoExchanges.kucoin.url),
            ),
        ),
        Row(
            Url(
                Const(CryptoExchanges.huobi.exchange), Const(CryptoExchanges.huobi.url)
            ),
            Url(
                Const(CryptoExchanges.bybit.exchange), Const(CryptoExchanges.bybit.url)
            ),
        ),
        Button(
            Const(messages.continue_button()), id="no_account_next", on_click=next_click
        ),
    )
    return group


no_account = Window(
    Format("{no_account}"),
    get_crypto_exchanges_keyboard(),
    get_back_cancel_keyboard(window_name="no_account", on_back=back_click),
    state=ConfiguratorDialog.no_account,
    getter=get_data,
)
