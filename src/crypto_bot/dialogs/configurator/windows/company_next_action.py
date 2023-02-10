from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
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
async def next_click_add(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.enter_kpi)


@exception_handler
async def next_click_finish(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


@exception_handler
async def next_click_reset(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    configuration: Configuration = manager.current_context().dialog_data[
        "configuration"
    ]
    configuration.kpi_usd_values = []
    await manager.update({"configuration": configuration})
    await manager.dialog().switch_to(ConfiguratorDialog.start_enter_kpi)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "company_next_action": messages.company_next_action(),
        "add_value_button": messages.add_value_button(),
        "finish_button": messages.finish_button(),
        "reset_button": messages.reset_button(),
    }


company_next_action = Window(
    Format("{company_next_action}"),
    Button(
        Format("{add_value_button}"),
        id="company_next_action_add_value",
        on_click=next_click_add,
    ),
    Button(
        Format("{finish_button}"),
        id="company_next_action_finish",
        on_click=next_click_finish,
    ),
    Button(
        Format("{reset_button}"),
        id="company_next_action_reset",
        on_click=next_click_reset,
    ),
    get_back_cancel_keyboard(window_name="company_next_action", show_back=False),
    state=ConfiguratorDialog.company_next_action,
    getter=get_data,
)
