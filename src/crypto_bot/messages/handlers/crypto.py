def balance_command() -> str:
    return "баланс"


def address_trc20_command() -> str:
    return "адрес TRC20"


def address_erc20_command() -> str:
    return "адрес ERC20"


def help_text() -> str:
    return (
        "/balance - просмотр баланса.\n"
        "/address_trc20 - получение адреса TRC20.\n"
        "/address_erc20 - получение адреса ERC20."
    )
