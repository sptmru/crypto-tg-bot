import logging
import os
import time

import motor.motor_asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_webhook
from aiogram_dialog import DialogRegistry

from src.crypto_bot.commands.commands import set_commands
from src.crypto_bot.dialogs.dialogs import register_dialogs
from src.crypto_bot.filters.filters import bind_filters
from src.crypto_bot.handlers.handlers import register_handlers
from src.crypto_bot.middlewares.middlewares import setup_middlewares
from src.crypto_bot.services.repository import Repository

token = str(os.environ.get('TELEGRAM_BOT_API_TOKEN'))
db_connection_uri = str(os.environ.get("DB_CONNECTION_URI"))
admin_id = int(os.environ.get("BOT_ADMIN_ID"))
webhook_url = str(os.environ.get("WEBHOOK_URL"))
webhook_path = str(os.environ.get("WEBHOOK_PATH"))
server_ip_address = str(os.environ.get("SERVER_IP_ADDRESS"))
webapp_host = str(os.environ.get("WEBAPP_HOST"))
webapp_port = str(os.environ.get("WEBAPP_PORT"))

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot = Bot(token)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
dialog_registry = DialogRegistry(dispatcher)
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(db_connection_uri)


async def init_db():
    repository = Repository(mongo_client)
    await repository.init_db(admin_id)


async def on_startup(_: Dispatcher):
    await bot.set_webhook(webhook_url)
    logger.info("Webhook is set")
    await set_commands(bot)
    logger.info("Commands set")
    await init_db()
    logger.info("DB is initialized")


async def on_shutdown(_: Dispatcher):
    await bot.delete_webhook()
    logger.info("Webhook is deleted")
    mongo_client.close()
    logger.info("DB connection is closed")


def set_utc_time() -> None:
    os.environ["TZ"] = "UTC"
    time.tzset()


def start() -> None:
    set_utc_time()
    setup_middlewares(
        dispatcher=dispatcher,
        admin_id=admin_id,
        server_ip=server_ip_address,
        connector=mongo_client,
    )
    bind_filters(dispatcher)
    register_dialogs(dialog_registry)
    register_handlers(dispatcher)
    dispatcher.stop_polling()
    start_webhook(
        dispatcher=dispatcher,
        webhook_path=webhook_path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=webapp_host,
        port=webapp_port,
    )


def main() -> None:
    try:
        start()
    except:  # pylint: disable=bare-except
        logger.exception("Exception")


if __name__ == "__main__":
    main()
