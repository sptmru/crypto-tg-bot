import logging

from aiogram import Bot

from src.crypto_bot.handlers.common import get_commands as get_common_commands

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        *get_common_commands(),
    ]
    await bot.set_my_commands(commands)
    logger.info("Commands set")
