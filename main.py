import logging
import os

from flask import Flask
from aiogram import Bot, Dispatcher, executor, types

token = str(os.environ.get('TELEGRAM_BOT_API_TOKEN'))
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token)
dispatcher = Dispatcher(bot)

flask_app = Flask(__name__)


@flask_app.route("/")
def hello_world():
    return "Hello, World!"


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Crypto Bot")


@dispatcher.message_handler()
async def unknown(message: types.Message):
    await message.answer("Unknown command or data!")


def start_bot():
    executor.start_polling(dispatcher, skip_updates=True)


if __name__ == "__main__":
    start_bot()
    flask_app.run(host="0.0.0.0", port=8080)  # healthcheck
