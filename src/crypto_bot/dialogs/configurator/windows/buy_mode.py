from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group
from aiogram_dialog.widgets.text import Const, Format

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.models.configuration import BuyMode, Configuration


@exception_handler
async def next_click_personal(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    configuration = Configuration()
    configuration.buy_mode = BuyMode(button.widget_id)
    await manager.update({"configuration": configuration})
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


@exception_handler
async def next_click_company(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    configuration = Configuration()
    configuration.buy_mode = BuyMode(button.widget_id)
    await manager.update({"configuration": configuration})
    await manager.dialog().switch_to(ConfiguratorDialog.company_buy)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "buy_mode": messages.buy_mode(),
    }


def get_buy_modes_keyboard() -> Group:
    group = Group(
        Button(
            Const(messages.personal_buy_button()),
            id=BuyMode.PERSONAL.value,
            on_click=next_click_personal,
        ),
        Button(
            Const(messages.company_buy_button()),
            id=BuyMode.COMPANY.value,
            on_click=next_click_company,
        ),
    )
    return group


buy_mode = Window(
    Format("{buy_mode}"),
    get_buy_modes_keyboard(),
    get_back_cancel_keyboard(window_name="buy_mode", show_back=False),
    state=ConfiguratorDialog.buy_mode,
    getter=get_data,
)
