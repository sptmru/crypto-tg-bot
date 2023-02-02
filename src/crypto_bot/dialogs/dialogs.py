import logging

from aiogram_dialog import DialogRegistry

from src.crypto_bot.dialogs.configurator.dialogs import (
    register_dialogs as register_configurator_dialogs,
)

logger = logging.getLogger(__name__)


def register_dialogs(dialog_registry: DialogRegistry) -> None:
    register_configurator_dialogs(dialog_registry)
    logger.info("All dialogs registered")
