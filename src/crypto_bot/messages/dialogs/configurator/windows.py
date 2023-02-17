def unknown_error() -> str:
    return "Произошла неизвестная ошибка!"


def cancel_text() -> str:
    return "Отмена"


def back_text() -> str:
    return "Назад"


def api_key() -> str:
    return "Введите API-key:"


def api_passphrase() -> str:
    return "Введите API-passphrase:"


def api_secret() -> str:
    return "Введите API-secret:"


def buy_mode() -> str:
    return "Выберите режим покупки:"


def personal_buy_button() -> str:
    return "Личная покупка"


def company_buy_button() -> str:
    return "Командная покупка"


def crypto_exchange() -> str:
    return "Выберите биржу:"


def no_account_button() -> str:
    return "Нет аккаунта"


def no_account() -> str:
    return "Регистрация аккаунта на бирже"


def continue_button() -> str:
    return "Продолжить"


def period() -> str:
    return "Выберите периодичность покупки:"


def usd() -> str:
    return "Введите сумму покупки:"


def company_buy() -> str:
    return (
        "Если вы хотите делать системные покупки фиксированной "
        "суммой, Вам следует вернуться назад и выбрать режим покупки "
        '"Личная покупка". Если же ваша покупка должна строиться '
        "от показателей KPI, каждый раз запрашивая их "
        'параметры - жмите "Продолжить", и бот предложит '
        "настроить сетку значений."
    )


def start_enter_kpi() -> str:
    return (
        "Покупка от KPI - каждый выбранный период бот будет "
        "задавать вопрос о значении KPI и исходя из этого делать "
        "покупку на необходимую сумму. От 0 до какого-то "
        "значения покупка не производится, поэтому сейчас Вы "
        "должны ввести первое и самое минимальное значение, "
        "начиная с которого осуществляется покупка:"
    )


def enter_kpi() -> str:
    return "Введите значение KPI:"


def enter_usd_value(kpi_value: str = "0.0") -> str:
    return (
        "Введите теперь сумму в долларах, на которую будет "
        f"совершена покупка при значении KPI >= {kpi_value}:"
    )


def company_next_action() -> str:
    return "Выберите следующее действие:"


def add_value_button() -> str:
    return "Добавить значение"


def finish_button() -> str:
    return "Завершить"


def reset_button() -> str:
    return "Начать заново"


def invalid_value() -> str:
    return "Введите корректное числовое значение!"


def get_period_text(days: int) -> str:
    match days:
        case 1:
            text = "Каждый день"
        case 7:
            text = "Каждая неделю"
        case 10:
            text = "Каждая декада"
        case 14:
            text = "Каждые 2 недели"
        case 30:
            text = "Каждые 30 дней"
    return text


def lower_kpi() -> str:
    return "Текущение значение KPI должно быть больше, чем предыдущее"


def server_ip() -> str:
    return "Для лучшей работы при создании ключа можно добавить IP-адрес сервера:"


def change_api_key() -> str:
    return ""


def no_configuration_available() -> str:
    return "Конфигуратор не настроен"
