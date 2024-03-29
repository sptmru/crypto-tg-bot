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
from src.crypto_bot.services.repository import Repository
from src.crypto_bot.time_utils import get_current_date_utc_timestamp


@exception_handler
async def handle_message(
    message: Message, dialog: Dialog, manager: DialogManager
):  # pylint: disable=unused-argument
    await message.delete()
    configuration: Configuration = manager.current_context().dialog_data[
        "configuration"
    ]
    configuration.api_passphrase = message.text
    await manager.update({"configuration": configuration})
    repo: Repository = ctx_data.get().get("repo")
    await repo.get_configuration_repository().insert_configuration(configuration)
    user = await repo.get_user_repository().get_user(configuration.user_id)
    user.configured_date_ts = get_current_date_utc_timestamp()
    await repo.get_user_repository().update_user(user)
    await message.answer(f"Введенные данные: {configuration}")
    await manager.done()


@exception_handler
async def back_click(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await manager.dialog().switch_to(ConfiguratorDialog.api_secret)


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "api_passphrase": messages.api_passphrase(),
    }


api_passphrase = Window(
    Format("{api_passphrase}"),
    get_back_cancel_keyboard(window_name="api_passphrase", on_back=back_click),
    MessageInput(handle_message),
    state=ConfiguratorDialog.api_passphrase,
    getter=get_data,
)
