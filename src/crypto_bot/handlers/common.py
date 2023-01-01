import logging

from aiogram import Dispatcher, types

logger = logging.getLogger(__name__)


async def start(message: types.Message):
    await message.answer("Crypto Bot")


async def unknown(message: types.Message):
    await message.answer("Unknown command or data!")


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(start, commands="start")
    dispatcher.register_message_handler(unknown)
    logger.info("Common handlers registered")
