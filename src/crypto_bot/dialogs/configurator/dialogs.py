import logging

from aiogram_dialog import Dialog, DialogRegistry

from src.crypto_bot.dialogs.configurator.windows.windows import get_windows

logger = logging.getLogger(__name__)

configurator_dialog = Dialog(
    *get_windows(),
)


def register_dialogs(dialog_registry: DialogRegistry) -> None:
    dialog_registry.register(configurator_dialog)
    logger.info("Configurator dialogs registered")
