import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

import src.crypto_bot.messages.middlewares.access as messages
from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


class AccessMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, admin_id: int):
        super().__init__()
        self.admin_id = admin_id

    async def pre_process(self, obj, data, *args):
        match type(obj):
            case types.Message:
                message: types.Message = obj
                await self._handle_message(message)
            case _:
                pass

    async def post_process(self, obj, data, *args):
        pass

    async def _handle_message(self, message: types.Message):
        user_id = message.from_user.id
        logger.info("User [id = %d] is trying to get access", user_id)
        if not self._is_admin(user_id):
            logger.info("Access denied for user [id = %d]", user_id)
            await send_message(message.chat.id, messages.access_denied())
            raise CancelHandler()
        else:
            logger.info("Access provided for user [id = %d]", user_id)

    def _is_admin(self, user_id: int) -> bool:
        return user_id == self.admin_id
