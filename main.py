import logging
import os
from aiogram import Bot, Dispatcher, executor, types

TELEGRAM_BOT_API_TOKEN = str(os.getenv('TG_API_KEY'))

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TELEGRAM_BOT_API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Crypto Bot")


@dispatcher.message_handler()
async def unknown(message: types.Message):
    await message.answer("Unknown command or data!")


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
