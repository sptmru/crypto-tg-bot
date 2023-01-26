import logging
from typing import Dict

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler, ctx_data
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

import src.crypto_bot.messages.middlewares.access as messages
from src.crypto_bot.handlers.bot_utils import send_message
from src.crypto_bot.models.role import UserRole
from src.crypto_bot.models.user import User
from src.crypto_bot.services.exceptions import DBError
from src.crypto_bot.services.repository import Repository

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
                try:
                    await self._handle_message(message)
                except DBError:
                    logger.exception("DB error occured")
                    await send_message(message.chat.id, messages.db_error_message())
                    raise CancelHandler()  # pylint: disable=raise-missing-from
            case _:
                pass

    async def post_process(self, obj, data, *args):
        pass

    async def _handle_message(self, message: types.Message):
        user_id = message.from_user.id
        logger.info("User [id = %d] is trying to get access", user_id)
        repo: Repository = ctx_data.get().get("repo")
        user = await repo.get_user_repository().get_user(user_id)
        if not user.is_valid():
            logger.info("Access denied for user [id = %d]", user_id)
            user.user_id = user_id
            user.sent_request = True
            await insert_user(user)
            username = get_username_from_message(message)
            await send_message(message.chat.id, messages.access_denied())
            await send_message(
                chat_id=self.admin_id,
                text=messages.access_requested(user_id, username),
                parse_mode=types.ParseMode.HTML,
            )
            raise CancelHandler()
        elif user.has_sent_request():
            logger.info("Access denied for user [id = %d]", user_id)
            await send_message(message.chat.id, messages.access_already_requested())
            raise CancelHandler()
        elif not user.has_access():
            logger.info("Access denied for user [id = %d]", user_id)
            await send_message(message.chat.id, messages.no_access())
            raise CancelHandler()
        logger.info("Access provided for user [id = %d]", user_id)


async def insert_user(user: User):
    repo: Repository = ctx_data.get().get("repo")
    await repo.get_user_repository().insert_user(user)
    logger.info("User [id = %d] inserted into the DB", user.user_id)


def get_username_from_message(message: types.Message) -> str:
    return message.from_user.username or message.from_user.full_name


class RoleMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, admin_id: int):
        super().__init__()
        self.admin_id = admin_id

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
        else:
            role = UserRole.USER
        data["role"] = role
        logger.info("User's [id = %d] role: %s", user_id, role.value)

    async def post_process(self, obj, data, *args):
        data.pop("role", None)
