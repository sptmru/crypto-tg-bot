from decimal import Decimal, InvalidOperation

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import cancel, exception_handler


@exception_handler
async def handle_message(
    message: Message, dialog: Dialog, manager: DialogManager
):  # pylint: disable=unused-argument
    try:
        usd_value = Decimal(message.text)
    except InvalidOperation:
        await message.answer("Введите корректное числовое значение!")
        return
    await manager.update({"usd": usd_value})
    await manager.dialog().switch_to(ConfiguratorDialog.api_key)


@exception_handler
async def back(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.period)


usd = Window(
    Const("Введите сумму покупки:"),
    Row(
        Button(Const("Назад"), id="usd_back", on_click=back),
        Button(Const("Отмена"), id="usd_cancel", on_click=cancel),
    ),
    MessageInput(handle_message),
    state=ConfiguratorDialog.usd,
)
