import logging
from typing import Callable

from aiogram import Dispatcher, types
from aiogram.dispatcher.handler import ctx_data

import src.crypto_bot.messages.handlers.admin.access as messages
from src.crypto_bot.handlers.bot_utils import send_message
from src.crypto_bot.services.exceptions import DBError
from src.crypto_bot.services.repository import Repository

logger = logging.getLogger(__name__)


class InvalidUserID(Exception):
    def __init__(self, invalid_value: str):
        super().__init__()
        self.invalid_value = invalid_value


def exception_handler(func: Callable) -> Callable:
    async def wrapper(*args):
        try:
            message: types.Message = args[0]
            await func(message)
        except InvalidUserID as e:
            logger.exception("Invalid user id value: %s", e.invalid_value)
            await send_message(message.chat.id, messages.invalid_value())
        except DBError:
            logger.exception("DB error occured")
            await send_message(message.chat.id, messages.db_error_message())
        except:  # pylint: disable=bare-except
            logger.exception("Exception")

    return wrapper


@exception_handler
async def access(message: types.Message):
    admin_id = message.from_user.id
    logger.info("Admin [id = %d] pushed /access command", admin_id)
    user_id = get_user_id(message.text[7:])
    is_admin = await handle_admin_user_id(admin_id, user_id)
    if is_admin:
        return
    repo: Repository = ctx_data.get().get("repo")
    user_repo = repo.get_user_repository()
    if not user_repo.has_user_access(user_id):
        user_repo.provide_access(user_id)
        logger.info("User [id = %d] has been provided access", user_id)
        await send_message(admin_id, messages.admin_access_provided(user_id))
        await send_message(user_id, messages.access_provided())
    else:
        await send_message(admin_id, messages.access_already_provided())


@exception_handler
async def noaccess(message: types.Message):
    admin_id = message.from_user.id
    logger.info("Admin [id = %d] pushed /noaccess command", admin_id)
    user_id = get_user_id(message.text[9:])
    is_admin = await handle_admin_user_id(admin_id, user_id)
    if is_admin:
        return
    repo: Repository = ctx_data.get().get("repo")
    user_repo = repo.get_user_repository()
    if user_repo.has_user_access(user_id):
        user_repo.revoke_access(user_id)
        logger.info("User [id = %d] has been revoked access", user_id)
        await send_message(admin_id, messages.admin_access_revoked(user_id))
        await send_message(user_id, messages.access_revoked())
    else:
        await send_message(admin_id, messages.access_not_provided_yet())


def get_user_id(text: str) -> int:
    try:
        user_id = int(text)
    except ValueError as exc:
        raise InvalidUserID(text) from exc
    return user_id


async def handle_admin_user_id(admin_id: int, user_id: int) -> bool:
    if admin_id == user_id:
        await send_message(admin_id, messages.admin_text())
        return True
    return False


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(
        access, lambda message: message.text.startswith("/access"), is_admin=True
    )
    dispatcher.register_message_handler(
        noaccess, lambda message: message.text.startswith("/noaccess"), is_admin=True
    )
    logger.info("Admin access handlers registered")
