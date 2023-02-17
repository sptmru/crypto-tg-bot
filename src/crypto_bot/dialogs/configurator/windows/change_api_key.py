import logging

from aiogram import types
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format
from aiogram.dispatcher.handler import ctx_data

import src.crypto_bot.messages.dialogs.configurator.windows as messages
from src.crypto_bot.handlers.bot_utils import send_message
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.dialogs.configurator.windows.common import (
    exception_handler,
    get_back_cancel_keyboard,
)
from src.crypto_bot.services.repository import Repository

logger = logging.getLogger(__name__)


@exception_handler
async def handle_message(
        message: Message, dialog: Dialog, manager: DialogManager
):  # pylint: disable=unused-argument
    user_id = message.from_user.id
    repo: Repository = ctx_data.get().get("repo")
    user_configuration = await repo.get_configuration_repository().get_configuration(user_id)
    logger.debug(user_configuration)
    logger.info("User [id = %d] trying to change their API key", user_id)
    if not bool(user_configuration) or user_configuration.user_id == -1:
        await send_message(
            chat_id=user_id,
            text=messages.no_configuration_available(),
            parse_mode=types.ParseMode.HTML,
        )
        return
    else:
        await manager.dialog().switch_to(ConfiguratorDialog.api_key)


@exception_handler
async def back_click(
        call: CallbackQuery, button: Button, manager: DialogManager
):
    pass


async def get_data(*args, **kwargs):  # pylint: disable=unused-argument
    return {
        "change_api_key": messages.change_api_key(),
    }


change_api_key = Window(
    Format("{change_api_key}"),
    get_back_cancel_keyboard(window_name="change_api_key", show_back=False),
    MessageInput(handle_message),
    state=ConfiguratorDialog.change_api_key,
    getter=get_data,
)
