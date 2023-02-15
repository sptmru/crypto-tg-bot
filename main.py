import logging
import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook

token = str(os.environ.get('TELEGRAM_BOT_API_TOKEN'))
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token)
dispatcher = Dispatcher(bot)

WEBHOOK_HOST = 'https://cryptobot.sptm.dev'
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8080


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Crypto Bot")


@dispatcher.message_handler()
async def unknown(message: types.Message):
    await message.answer("Unknown command or data!")


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


async def main():
    start_webhook(
        dispatcher=dispatcher,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
    asyncio.create_task(await dispatcher.start_polling())


asyncio.run(main())
