import logging

from aiogram import Dispatcher

from src.crypto_bot.middlewares.access import AccessMiddleware, RoleMiddleware

logger = logging.getLogger(__name__)


def setup_middlewares(dispatcher: Dispatcher, admin_id: int) -> None:
    dispatcher.setup_middleware(AccessMiddleware(admin_id))
    dispatcher.setup_middleware(RoleMiddleware(admin_id))
    logger.info("Middlewares are configured")
