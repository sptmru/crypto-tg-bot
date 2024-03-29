import logging
from typing import List

from aiogram import Dispatcher, types
from aiogram_dialog import DialogManager, StartMode

import src.crypto_bot.messages.handlers.common as messages
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog
from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


async def cmd_start(message: types.Message, dialog_manager: DialogManager):
    logger.info("User [id = %d] pushed start command", message.from_user.id)
    await send_message(message.chat.id, messages.start())
    await dialog_manager.start(ConfiguratorDialog.buy_mode, mode=StartMode.RESET_STACK)


async def cmd_help(message: types.Message):
    logger.info("User [id = %d] pushed help command", message.from_user.id)
    await send_message(
        chat_id=message.chat.id,
        text=messages.help_text(),
        parse_mode=types.ParseMode.HTML,
    )


async def unknown(message: types.Message):
    logger.info(
        "User [id = %d] typed the following text: %s",
        message.from_user.id,
        message.text,
    )
    await send_message(message.chat.id, messages.unknown())


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(cmd_start, commands="start")
    dispatcher.register_message_handler(cmd_help, commands="help")
    dispatcher.register_message_handler(unknown)
    logger.info("Common handlers registered")


def get_commands() -> List[types.BotCommand]:
    commands = [
        types.BotCommand(command="/start", description=messages.start_command()),
        types.BotCommand(command="/help", description=messages.help_command()),
    ]
    return commands
