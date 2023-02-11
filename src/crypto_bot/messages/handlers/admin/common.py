from src.crypto_bot.messages.handlers.admin.access import help_text as access_help_text
from src.crypto_bot.messages.handlers.crypto import help_text as crypto_help_text


def common_help_text() -> str:
    return "/start - настройка конфигуратора.\n" "/help - помощь."


def help_text() -> str:
    return f"{common_help_text()}\n" f"{access_help_text()}\n" f"{crypto_help_text()}\n"
