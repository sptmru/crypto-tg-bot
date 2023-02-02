from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row
from aiogram_dialog.widgets.text import Const

from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import cancel, exception_handler


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.update({"period": call.data})
    await manager.dialog().switch_to(ConfiguratorDialog.usd)


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


period = Window(
    Const("Выберите периодичность покупки:"),
    Group(
        Row(
            Button(Const("Каждый день"), id="1", on_click=next_click),
            Button(Const("Каждая неделя"), id="7", on_click=next_click),
        ),
        Row(
            Button(Const("Каждая декада"), id="10", on_click=next_click),
            Button(Const("Каждые 2 недели"), id="14", on_click=next_click),
        ),
        Button(Const("Каждые 30 дней"), id="30", on_click=next_click),
    ),
    Row(
        Button(Const("Назад"), id="period_back", on_click=back_click),
        Button(Const("Отмена"), id="period_cancel", on_click=cancel),
    ),
    state=ConfiguratorDialog.period,
)
