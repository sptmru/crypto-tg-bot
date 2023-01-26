import logging

from aiogram import Dispatcher, types

import src.crypto_bot.messages.handlers.admin.common as messages
from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


async def cmd_help(message: types):
    logger.info("User [id = %d] pushed /help command", message.from_user.id)
    await send_message(
        chat_id=message.chat.id,
        text=messages.help_text(),
        parse_mode=types.ParseMode.HTML,
    )


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(cmd_help, commands="help", is_admin=True)
    logger.info("Admin common handlers registered")
