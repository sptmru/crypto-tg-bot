def balance_command() -> str:
    return "баланс"


def address_trc20_command() -> str:
    return "адрес TRC20"


def address_erc20_command() -> str:
    return "адрес ERC20"


def change_api_key_command() -> str:
    return "сменить API-ключ"


def change_api_key_start() -> str:
    return "Сменить API-ключ:"


def no_configuration_available() -> str:
    return "Конфигуратор не настроен"


def help_text() -> str:
    return (
        "/balance - просмотр баланса.\n"
        "/address_trc20 - получение адреса TRC20.\n"
        "/address_erc20 - получение адреса ERC20.\n"
        "/change_api_key - смена API-ключа"
    )
