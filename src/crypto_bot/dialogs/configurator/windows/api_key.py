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
    await manager.update({"api_key": message.text})
    await manager.dialog().switch_to(ConfiguratorDialog.api_secret)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.usd)


api_key = Window(
    Const("Введите API-key:"),
    MessageInput(handle_message),
    Row(
        Button(Const("Назад"), id="api_key_back", on_click=back_click),
        Button(Const("Отмена"), id="api_key_cancel", on_click=cancel),
    ),
    state=ConfiguratorDialog.api_key,
)
