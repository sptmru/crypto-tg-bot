import logging
from typing import List

from aiogram import Dispatcher, types

import src.crypto_bot.messages.handlers.common as messages
from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


async def cmd_start(message: types.Message):
    await send_message(message.chat.id, messages.start())


async def cmd_help(message: types.Message):
    await send_message(message.chat.id, messages.help_text())


async def unknown(message: types.Message):
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
