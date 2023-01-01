import logging

from aiogram import Dispatcher, types

from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


async def start(message: types.Message):
    await send_message(message.chat.id, "Crypto Bot")


async def unknown(message: types.Message):
    await send_message(message.chat.id, "Unknown command or data!")


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(start, commands="start")
    dispatcher.register_message_handler(unknown)
    logger.info("Common handlers registered")
