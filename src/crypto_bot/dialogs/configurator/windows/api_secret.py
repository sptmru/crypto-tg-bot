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
    await manager.update({"api_secret": message.text})
    dialog_data = manager.current_context().dialog_data
    if dialog_data["crypto_exchange"] == "kucoin":
        await manager.dialog().switch_to(ConfiguratorDialog.api_passphrase)
        return
    else:
        await message.answer(f"Введенные данные: {dialog_data}")
        await manager.done()


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.usd)


api_secret = Window(
    Const("Введите API-secret:"),
    MessageInput(handle_message),
    Row(
        Button(Const("Назад"), id="api_secret_back", on_click=back_click),
        Button(Const("Отмена"), id="api_key_cancel", on_click=cancel),
    ),
    state=ConfiguratorDialog.api_secret,
)
