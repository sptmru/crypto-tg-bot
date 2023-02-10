from decimal import Decimal, InvalidOperation

from aiogram.dispatcher.handler import ctx_data
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.models.configuration import Configuration


@exception_handler
async def handle_message(
    message: Message, dialog: Dialog, manager: DialogManager
):  # pylint: disable=unused-argument
    try:
        usd_value = Decimal(message.text)
    except InvalidOperation:
        await message.answer(messages.invalid_value())
        return
    if usd_value < 0:
        await message.answer(messages.invalid_value())
        return
    configuration: Configuration = manager.current_context().dialog_data[
        "configuration"
    ]
    configuration.usd = usd_value
    await manager.update({"configuration": configuration})
    await message.answer(messages.server_ip())
    server_ip = ctx_data.get().get("server_ip")
    await message.answer(server_ip)
    await manager.dialog().switch_to(ConfiguratorDialog.api_key)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.period)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "usd": messages.usd(),
    }


usd = Window(
    Format("{usd}"),
    get_back_cancel_keyboard(window_name="usd", on_back=back_click),
    MessageInput(handle_message),
    state=ConfiguratorDialog.usd,
    getter=get_data,
)
