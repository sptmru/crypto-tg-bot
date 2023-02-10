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


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.start_enter_kpi)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.buy_mode)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "company_buy": messages.company_buy(),
        "continue": messages.continue_button(),
    }


company_buy = Window(
    Format("{company_buy}"),
    Button(Format("{continue}"), id="company_buy_continue", on_click=next_click),
    get_back_cancel_keyboard(window_name="company_buy", on_back=back_click),
    state=ConfiguratorDialog.company_buy,
    getter=get_data,
)
