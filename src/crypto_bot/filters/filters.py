import logging

from aiogram import Dispatcher

from src.crypto_bot.filters.role import AdminFilter

logger = logging.getLogger(__name__)


def bind_filters(dispatcher: Dispatcher) -> None:
    dispatcher.bind_filter(AdminFilter)
    logger.info("Filters binded")
