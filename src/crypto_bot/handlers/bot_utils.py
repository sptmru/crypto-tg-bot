import logging
from typing import Callable

from aiogram.dispatcher.webhook import SendMessage

logger = logging.getLogger(__name__)


def exception_handler(func: Callable) -> Callable:
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except:  # pylint: disable=bare-except
            logger.exception("Exception")

    return wrapper


@exception_handler
async def send_message(chat_id: int, text: str, parse_mode: str | None = None):
    await SendMessage(chat_id, text, parse_mode)()
