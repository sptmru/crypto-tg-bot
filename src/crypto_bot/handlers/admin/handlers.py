import logging

from aiogram import Dispatcher

from src.crypto_bot.handlers.admin.access import (
    register_handlers as register_access_handlers,
)
from src.crypto_bot.handlers.admin.common import (
    register_handlers as register_common_handlers,
)

logger = logging.getLogger(__name__)


def register_handlers(dispatcher: Dispatcher) -> None:
    register_access_handlers(dispatcher)
    register_common_handlers(dispatcher)
    logger.info("Admin handlers registered")
