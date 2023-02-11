from src.crypto_bot.messages.handlers.crypto import help_text as crypto_help_text


def start() -> str:
    return (
        "Привет!\nПеред началом работы с любой биржей помните: то, что "
        "касается вывода средств, должно происходить с максимальным "
        "количеством ваших подтверждений, позаботьтесь об этом в первую "
        "очередь!\n\nЭто xAurumBot! Он позволяет покупать BTC автоматически и "
        "с заданным периодом, следуя стратегии долларового усреднения для "
        "достижения максимальной отдачи на дистанции лет. Для работы с вашей "
        "биржей ему потребуется API-ключ со всеми разрешениями, помимо вывода "
        "средств. Итак, приступим"
    )


def unknown() -> str:
    return "Неизвестная команда или данные!"


# Commands


def start_command() -> str:
    return "настройка конфигуратора"


def help_command() -> str:
    return "помощь"


# Help message


def common_help_text() -> str:
    return "/start - настройка конфигуратора.\n" "/help - помощь."


def help_text() -> str:
    return f"{common_help_text()}\n" f"{crypto_help_text()}"
