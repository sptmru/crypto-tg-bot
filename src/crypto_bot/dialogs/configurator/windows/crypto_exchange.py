from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row
from aiogram_dialog.widgets.text import Const

from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import cancel, exception_handler


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.update({"crypto_exchange": call.data})
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


crypto_exchange = Window(
    Const("Выберите биржу:"),
    Group(
        Row(
            Button(Const("Binance"), id="binance", on_click=next_click),
            Button(Const("Kucoin"), id="kucoin", on_click=next_click),
        ),
        Row(
            Button(Const("Huobi"), id="huobi", on_click=next_click),
            Button(Const("Bybit"), id="bybit", on_click=next_click),
        ),
    ),
    Button(Const("Нет аккаунта"), id="crypto_exchange_no_account", on_click=no_account),
    Row(
        Button(Const("Назад"), id="api_secret_back", on_click=back_click),
        Button(Const("Отмена"), id="api_secret_cancel", on_click=cancel),
    ),
    state=ConfiguratorDialog.crypto_exchange,
)
