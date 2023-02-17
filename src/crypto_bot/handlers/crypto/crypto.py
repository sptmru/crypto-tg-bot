import logging
from typing import List

from aiogram import Dispatcher, types
from aiogram_dialog import DialogManager, StartMode

import src.crypto_bot.messages.handlers.crypto as messages
from src.crypto_bot.handlers.bot_utils import send_message
from src.crypto_bot.dialogs.configurator.states import ConfiguratorDialog

logger = logging.getLogger(__name__)


async def balance(message: types.Message):
    logger.info("User [id = %d] pushed start command", message.from_user.id)
    await send_message(message.chat.id, "balance")


async def address(message: types.Message):
    logger.info("User [id = %d] pushed help command", message.from_user.id)
    await send_message(message.chat.id, "address")


async def change_api_key(message: types.Message, dialog_manager: DialogManager):
    logger.info("User [id = %d] pushed change_api_key command", message.from_user.id)
    await send_message(message.chat.id, messages.change_api_key_start())
    await dialog_manager.start(ConfiguratorDialog.change_api_key, mode=StartMode.RESET_STACK)


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(balance, commands=["balance"])
    dispatcher.register_message_handler(
        address, commands=["address_trc20", "address_erc20"]
    )
    dispatcher.register_message_handler(
        change_api_key, commands=['change_api_key']
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
        types.BotCommand(
            command="/change_api_key", description=messages.change_api_key_command()
        )
    ]
    return commands
