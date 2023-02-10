import logging
from decimal import Decimal, InvalidOperation

from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Format

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.models.configuration import Configuration, KPIUsd

logger = logging.getLogger(__name__)


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
    dialog_data = manager.current_context().dialog_data
    kpi_value = dialog_data["kpi_value"]
    kpi_usd = KPIUsd(kpi=kpi_value, usd=usd_value)
    configuration: Configuration = dialog_data["configuration"]
    configuration.kpi_usd_values.append(kpi_usd)
    await manager.update({"configuration": configuration})
    await manager.dialog().switch_to(ConfiguratorDialog.company_next_action)


# TODO: to catch exception
async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    manager = kwargs["dialog_manager"]
    kpi_value = manager.current_context().dialog_data["kpi_value"]
    return {
        "enter_usd_value": messages.enter_usd_value(kpi_value),
    }


enter_usd_value = Window(
    Format("{enter_usd_value}"),
    get_back_cancel_keyboard(window_name="enter_usd_value", show_back=False),
    MessageInput(handle_message),
    state=ConfiguratorDialog.enter_usd_value,
    getter=get_data,
)
