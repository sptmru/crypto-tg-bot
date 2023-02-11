import logging

from aiogram import Dispatcher

from src.crypto_bot.handlers.admin.handlers import (
    register_handlers as register_admin_handlers,
)
from src.crypto_bot.handlers.common import register_handlers as register_common_handlers
from src.crypto_bot.handlers.crypto.crypto import (
    register_handlers as register_crypto_handlers,
)

logger = logging.getLogger(__name__)


def register_handlers(dispatcher: Dispatcher) -> None:
    register_admin_handlers(dispatcher)
    register_crypto_handlers(dispatcher)
    register_common_handlers(dispatcher)
    logger.info("All handlers registered")
