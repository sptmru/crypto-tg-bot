from decimal import Decimal, InvalidOperation

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


@exception_handler
async def handle_message(
    message: Message, dialog: Dialog, manager: DialogManager
):  # pylint: disable=unused-argument
    try:
        kpi_value = Decimal(message.text)
    except InvalidOperation:
        await message.answer(messages.invalid_value())
        return
    if kpi_value < 0:
        await message.answer(messages.invalid_value())
        return
    await manager.update({"kpi_value": kpi_value})
    await manager.dialog().switch_to(ConfiguratorDialog.enter_usd_value)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.company_buy)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "start_enter_kpi": messages.start_enter_kpi(),
    }


start_enter_kpi = Window(
    Format("{start_enter_kpi}"),
    get_back_cancel_keyboard(window_name="start_enter_kpi", on_back=back_click),
    MessageInput(handle_message),
    state=ConfiguratorDialog.start_enter_kpi,
    getter=get_data,
)
