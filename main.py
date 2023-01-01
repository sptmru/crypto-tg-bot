import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_webhook

from src.crypto_bot.config import get_config
from src.crypto_bot.handlers.handlers import register_handlers

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

config = get_config()
bot = Bot(token=config.telegram_bot.api_token)
dispatcher = Dispatcher(bot)


async def on_startup(_: Dispatcher):
    await bot.set_webhook(config.webhook.url)
    logger.info("Webhook is set")


async def on_shutdown(_: Dispatcher):
    await bot.delete_webhook()
    logger.info("Webhook is deleted")


def start() -> None:
    register_handlers(dispatcher)
    start_webhook(
        dispatcher=dispatcher,
        webhook_path=config.webhook.path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=config.webapp.host,
        port=config.webapp.port,
    )


def main() -> None:
    try:
        start()
    except:  # pylint: disable=bare-except
        logger.exception("Exception")


if __name__ == "__main__":
    main()