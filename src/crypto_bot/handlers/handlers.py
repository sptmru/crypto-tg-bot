import logging

from aiogram import Dispatcher

from src.crypto_bot.handlers.common import register_handlers as register_common_handlers

logger = logging.getLogger(__name__)


def register_handlers(dispatcher: Dispatcher) -> None:
    register_common_handlers(dispatcher)
    logger.info("All handlers registered")
