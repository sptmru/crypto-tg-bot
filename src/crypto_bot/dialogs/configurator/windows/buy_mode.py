from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import cancel, exception_handler


@exception_handler
async def next_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.update({"buy_mode": call.data})
    await manager.dialog().switch_to(ConfiguratorDialog.crypto_exchange)


buy_mode = Window(
    Const("Выберите режим покупки:"),
    Button(Const("Личная покупка"), id="buy_mode_1", on_click=next_click),
    Button(Const("Командная покупка"), id="buy_mode_2", on_click=next_click),
    Button(Const("Отмена"), id="buy_mode_cancel", on_click=cancel),
    state=ConfiguratorDialog.buy_mode,
)
