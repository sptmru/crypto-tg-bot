import logging
from typing import Callable

from aiogram import Dispatcher, types
from aiogram.dispatcher.handler import ctx_data

import src.crypto_bot.messages.handlers.admin.access as messages
from src.crypto_bot.handlers.bot_utils import send_message
from src.crypto_bot.models.user import User
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
            await send_message(
                chat_id=message.chat.id,
                text=messages.invalid_value(value=e.invalid_value),
                parse_mode=types.ParseMode.HTML,
            )
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
    is_admin = await handle_admin_id(admin_id, user_id)
    if is_admin:
        return
    await handle_user_id_access(user_id, admin_id)


@exception_handler
async def noaccess(message: types.Message):
    admin_id = message.from_user.id
    logger.info("Admin [id = %d] pushed /noaccess command", admin_id)
    user_id = get_user_id(message.text[9:])
    is_admin = await handle_admin_id(admin_id, user_id)
    if is_admin:
        return
    await handle_user_id_noaccess(user_id, admin_id)


@exception_handler
async def deny(message: types.Message):
    admin_id = message.from_user.id
    logger.info("Admin [id = %d] pushed /deny command", admin_id)
    user_id = get_user_id(message.text[5:])
    is_admin = await handle_admin_id(admin_id, user_id)
    if is_admin:
        return
    await deny_request(user_id, admin_id)


def get_user_id(text: str) -> int:
    try:
        user_id = int(text)
    except ValueError as exc:
        raise InvalidUserID(text) from exc
    return user_id


async def handle_admin_id(admin_id: int, user_id: int) -> bool:
    if admin_id == user_id:
        await send_message(admin_id, messages.admin_text())
        return True
    return False


async def handle_user_id_access(user_id: int, admin_id: int):
    repo: Repository = ctx_data.get().get("repo")
    user = await repo.get_user_repository().get_user(user_id)
    await insert_user_if_needed(user, user_id)
    if not user.has_access():
        await provide_access(user)
        await send_message(
            chat_id=admin_id,
            text=messages.admin_access_provided(user_id),
            parse_mode=types.ParseMode.HTML,
        )
        await send_message(user_id, messages.access_provided())
    else:
        await send_message(
            chat_id=admin_id,
            text=messages.access_already_provided(user_id),
            parse_mode=types.ParseMode.HTML,
        )


async def handle_user_id_noaccess(user_id: int, admin_id: int):
    repo: Repository = ctx_data.get().get("repo")
    user = await repo.get_user_repository().get_user(user_id)
    if user.has_access():
        await revoke_access(user)
        await send_message(
            chat_id=admin_id,
            text=messages.admin_access_revoked(user_id),
            parse_mode=types.ParseMode.HTML,
        )
        await send_message(user_id, messages.access_revoked())
    else:
        await send_message(
            chat_id=admin_id,
            text=messages.access_not_provided_yet(user_id),
            parse_mode=types.ParseMode.HTML,
        )


async def deny_request(user_id: int, admin_id: int):
    repo: Repository = ctx_data.get().get("repo")
    user = await repo.get_user_repository().get_user(user_id)
    if user.has_sent_request():
        await delete_user(user_id)
        await send_message(
            chat_id=admin_id,
            text=messages.admin_request_denied(user_id),
            parse_mode=types.ParseMode.HTML,
        )
        await send_message(user_id, messages.request_denied())
    else:
        await send_message(
            chat_id=admin_id,
            text=messages.no_request(user_id),
            parse_mode=types.ParseMode.HTML,
        )


async def insert_user_if_needed(user: User, user_id: int):
    repo: Repository = ctx_data.get().get("repo")
    if not user.is_valid():
        user.user_id = user_id
        await repo.get_user_repository().insert_user(user)
        logger.info("User [id = %d] inserted into the DB", user_id)


async def provide_access(user: User):
    user.access = True
    user.sent_request = False
    repo: Repository = ctx_data.get().get("repo")
    await repo.get_user_repository().update_user(user)
    logger.info("User [id = %d] has been provided access", user.user_id)


async def revoke_access(user: User):
    user.access = False
    repo: Repository = ctx_data.get().get("repo")
    await repo.get_user_repository().update_user(user)
    logger.info("User [id = %d] has been revoked access", user.user_id)


async def delete_user(user_id: int):
    repo: Repository = ctx_data.get().get("repo")
    await repo.get_user_repository().delete_user(user_id)
    logger.info("User [id = %d] deleted", user_id)


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(
        access, lambda message: message.text.startswith("/access"), is_admin=True
    )
    dispatcher.register_message_handler(
        noaccess, lambda message: message.text.startswith("/noaccess"), is_admin=True
    )
    dispatcher.register_message_handler(
        deny, lambda message: message.text.startswith("/deny"), is_admin=True
    )
    logger.info("Admin access handlers registered")
