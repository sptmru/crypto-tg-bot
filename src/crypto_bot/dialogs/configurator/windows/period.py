from aiogram.dispatcher.handler import ctx_data
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row
from aiogram_dialog.widgets.text import Const, Format

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.models.configuration import BuyMode, Configuration


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    configuration: Configuration = manager.current_context().dialog_data[
        "configuration"
    ]
    configuration.period = int(button.widget_id)
    await manager.update({"configuration": configuration})
    if configuration.buy_mode == BuyMode.PERSONAL:
        await manager.dialog().switch_to(ConfiguratorDialog.usd)
    elif configuration.buy_mode == BuyMode.COMPANY:
        await call.message.answer(messages.server_ip())
        server_ip = ctx_data.get().get("server_ip")
        await call.message.answer(server_ip)
        await manager.dialog().switch_to(ConfiguratorDialog.api_key)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "period": messages.period(),
    }


def get_periods_keyboard() -> Group:
    group = Group(
        Row(
            Button(Const(messages.get_period_text(1)), id="1", on_click=next_click),
            Button(Const(messages.get_period_text(7)), id="7", on_click=next_click),
        ),
        Row(
            Button(Const(messages.get_period_text(10)), id="10", on_click=next_click),
            Button(Const(messages.get_period_text(14)), id="14", on_click=next_click),
        ),
        Button(Const(messages.get_period_text(30)), id="30", on_click=next_click),
    )
    return group


period = Window(
    Format("{period}"),
    get_periods_keyboard(),
    get_back_cancel_keyboard(window_name="period", on_back=back_click),
    state=ConfiguratorDialog.period,
    getter=get_data,
)
