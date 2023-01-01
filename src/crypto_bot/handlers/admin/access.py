import logging

from aiogram import Dispatcher, types

from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


async def access(message: types.Message):
    logger.info("User [id = %d] pushed /access command", message.from_user.id)
    await send_message(message.chat.id, "access")


async def noaccess(message: types.Message):
    logger.info("User [id = %d] pushed /noaccess command", message.from_user.id)
    await send_message(message.chat.id, "noaccess")


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(
        access, lambda message: message.text.startswith("/access"), is_admin=True
    )
    dispatcher.register_message_handler(
        noaccess, lambda message: message.text.startswith("/noaccess"), is_admin=True
    )
    logger.info("Admin access handlers registered")
