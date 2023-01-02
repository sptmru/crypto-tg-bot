import logging
from typing import List

from aiogram import Dispatcher

from src.crypto_bot.middlewares.access import AccessMiddleware, RoleMiddleware

logger = logging.getLogger(__name__)


def setup_middlewares(
    dispatcher: Dispatcher, admin_id: int, access_ids: List[int]
) -> None:
    dispatcher.setup_middleware(AccessMiddleware(admin_id, access_ids))
    dispatcher.setup_middleware(RoleMiddleware(admin_id, access_ids))
    logger.info("Middlewares are configured")
