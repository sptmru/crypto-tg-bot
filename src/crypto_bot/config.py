import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

logger = logging.getLogger(__name__)


@dataclass
class TelegramBot:
    api_token: str
    admin_id: int


@dataclass
class Webhook:
    host: str
    path: str
    url: str


@dataclass
class WebApp:
    host: str
    port: int


@dataclass
class DBConfig:
    connection_uri: str


@dataclass
class Config:
    telegram_bot: TelegramBot
    webhook: Webhook
    webapp: WebApp
    db: DBConfig


ROOT_DIR = Path(__file__).parent.parent.parent.absolute()


def get_config() -> Config:
    _load_dotenv()
    return Config(
        telegram_bot=_get_telegram_bot(),
        webhook=_get_webhook(),
        webapp=_get_webapp(),
        db=_get_db_config(),
    )


def _load_dotenv() -> None:
    dotenv_path = Path(ROOT_DIR, ".env")
    if not dotenv_path.exists():
        logger.error(".env not found: %s", dotenv_path)
        sys.exit(1)
    load_dotenv()


def _get_telegram_bot() -> TelegramBot:
    api_token = os.getenv("TELEGRAM_BOT_API_TOKEN")
    if api_token is None:
        logger.error("TELEGRAM_BOT_API_TOKEN is not provided")
        sys.exit(1)
    admin_id = os.getenv("TELEGRAM_ADMIN_ID")
    if admin_id is None:
        logger.error("TELEGRAM_ADMIN_ID is not provided")
        sys.exit(1)
    return TelegramBot(api_token, int(admin_id))


def _get_webhook() -> Webhook:
    host = os.getenv("WEBHOOK_HOST")
    if host is None:
        logger.error("WEBHOOK_HOST is not provided")
        sys.exit(1)
    path = os.getenv("WEBHOOK_PATH")
    if path is None:
        logger.error("WEBHOOK_PATH is not provided")
        sys.exit(1)
    url = os.getenv("WEBHOOK_URL")
    if url is None:
        logger.error("WEBHOOK_URL is not provided")
        sys.exit(1)
    return Webhook(host, path, url)


def _get_webapp() -> WebApp:
    host = os.getenv("WEBAPP_HOST")
    if host is None:
        logger.error("WEBAPP_HOST is not provided")
        sys.exit(1)
    port = os.getenv("WEBAPP_PORT")
    if port is None:
        logger.error("WEBAPP_PORT is not provided")
        sys.exit(1)
    return WebApp(host, int(port))


def _get_db_config() -> DBConfig:
    db_uri = os.getenv("DB_URI")
    if db_uri is None:
        logger.error("DB_URI is not provided")
        sys.exit(1)
    return DBConfig(connection_uri=db_uri)
