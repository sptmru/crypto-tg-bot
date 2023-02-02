from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row, Url
from aiogram_dialog.widgets.text import Const

from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import cancel, exception_handler


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


no_account = Window(
    Const("Регистрация аккаунта:"),
    Group(
        Row(
            Url(Const("Binance"), Const("https://binance.com")),
            Url(Const("Kucoin"), Const("https://kucoin.com")),
        ),
        Row(
            Url(Const("Huobi"), Const("https://huobi.com")),
            Url(Const("Bybit"), Const("https://bybit.com")),
        ),
    ),
    Button(Const("Продолжить"), id="no_account_next", on_click=next_click),
    Row(
        Button(Const("Назад"), id="no_account_back", on_click=back_click),
        Button(Const("Отмена"), id="api_key_cancel", on_click=cancel),
    ),
    state=ConfiguratorDialog.no_account,
)
