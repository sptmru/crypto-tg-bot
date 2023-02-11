import logging
from typing import List

from aiogram import Dispatcher, types

import src.crypto_bot.messages.handlers.crypto as messages
from src.crypto_bot.handlers.bot_utils import send_message

logger = logging.getLogger(__name__)


async def balance(message: types.Message):
    logger.info("User [id = %d] pushed start command", message.from_user.id)
    await send_message(message.chat.id, "balance")


async def address(message: types.Message):
    logger.info("User [id = %d] pushed help command", message.from_user.id)
    await send_message(message.chat.id, "address")


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(balance, commands=["balance"])
    dispatcher.register_message_handler(
        address, commands=["address_trc20", "address_erc20"]
    )
    logger.info("Crypto handlers registered")


def get_commands() -> List[types.BotCommand]:
    commands = [
        types.BotCommand(command="/balance", description=messages.balance_command()),
        types.BotCommand(
            command="/address_trc20", description=messages.address_trc20_command()
        ),
        types.BotCommand(
            command="/address_erc20", description=messages.address_erc20_command()
        ),
    ]
    return commands
