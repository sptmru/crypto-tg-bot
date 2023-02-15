import logging
import os
import asyncio

from aiogram import Bot, Dispatcher, types

token = str(os.environ.get('TELEGRAM_BOT_API_TOKEN'))
logging.basicConfig(level=logging.DEBUG)


bot = Bot(token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Crypto Bot")


@dispatcher.message_handler()
async def unknown(message: types.Message):
    await message.answer("Unknown command or data!")


if __name__ == "__main__":
    asyncio.create_task(dispatcher.start_polling())
