import logging

from aiogram import Bot, Dispatcher, executor

from src.crypto_bot.config import get_config
from src.crypto_bot.handlers.handlers import register_handlers

logging.basicConfig(level=logging.DEBUG)

config = get_config()
bot = Bot(token=config.telegram_bot_api_token)
dispatcher = Dispatcher(bot)
register_handlers(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
