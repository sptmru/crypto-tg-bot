import logging
from typing import Dict, List

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

import src.crypto_bot.messages.middlewares.access as messages
from src.crypto_bot.handlers.bot_utils import send_message
from src.crypto_bot.models.role import UserRole

logger = logging.getLogger(__name__)


class AccessMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, admin_id: int, access_ids: List[int]):
        super().__init__()
        self.admin_id = admin_id
        self.access_ids = access_ids

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
        print(self.access_ids)
        if not self._has_user_access(user_id):
            logger.info("Access denied for user [id = %d]", user_id)
            await send_message(message.chat.id, messages.access_denied())
            await send_message(self.admin_id, messages.access_requested(user_id))
            raise CancelHandler()
        else:
            logger.info("Access provided for user [id = %d]", user_id)

    def _has_user_access(self, user_id: int) -> bool:
        return user_id in self.access_ids


class RoleMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, admin_id: int, access_ids: List[int]):
        super().__init__()
        self.admin_id = admin_id
        self.access_ids = access_ids

    async def pre_process(self, obj, data, *args):
        match type(obj):
            case types.Message:
                message: types.Message = obj
                await self._handle_message(message, data)
            case _:
                pass

    async def _handle_message(self, message: types.Message, data: Dict):
        user_id = message.from_user.id
        if user_id == self.admin_id:
            role = UserRole.ADMIN
            data["access_ids"] = self.access_ids
        else:
            role = UserRole.USER
        data["role"] = role
        logger.info("User's [id = %d] role: %s", user_id, role.value)

    async def post_process(self, obj, data, *args):
        data.pop("role", None)
        data.pop("access_ids", None)
