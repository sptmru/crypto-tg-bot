import logging
import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv

logger = logging.getLogger(__name__)


@dataclass
class Config:
    telegram_bot_api_token: str


def get_config() -> Config:
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_API_TOKEN")
    if token is None:
        logger.error("TELEGRAM_BOT_API_TOKEN is not provided")
        sys.exit(1)
    return Config(telegram_bot_api_token=token)
