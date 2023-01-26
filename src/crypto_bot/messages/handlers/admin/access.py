import aiogram.utils.markdown as fmt


def invalid_value(value: str) -> str:
    value = fmt.quote_html(value)
    return (
        f"Введенный Вами id пользователя: <b>{value}</b>.\n"
        "Пожалуйста, введите валидное значение id пользователя!"
    )


def admin_text() -> str:
    return "Используется admin id"


def admin_access_provided(user_id: int) -> str:
    user_id = fmt.quote_html(user_id)
    return (
        "Доступ предоставлен пользователю с "
        f'<a href="tg://user?id={user_id}">id = {user_id}</a>'
    )


def access_provided() -> str:
    return (
        "Вам предоставлен доступ!\nВоспользуйтесь командой /start, чтобы "
        "настроить конфигуратор.\nИли ознакомьтесь со списком команд "
        "при помощи команды /help"
    )


def access_already_provided(user_id: int) -> str:
    user_id = fmt.quote_html(user_id)
    return (
        "Пользователю с "
        f'<a href="tg://user?id={user_id}">id = {user_id}</a>'
        " уже предоставлен доступ"
    )


def admin_access_revoked(user_id: int) -> str:
    user_id = fmt.quote_html(user_id)
    return (
        "Доступ отозван для пользователя с "
        f'<a href="tg://user?id={user_id}">id = {user_id}</a>'
    )


def access_revoked() -> str:
    return "Доступ отозван"


def access_not_provided_yet(user_id: int) -> str:
    user_id = fmt.quote_html(user_id)
    return (
        "Пользователю с "
        f'<a href="tg://user?id={user_id}">id = {user_id}</a>'
        " еще не предоставлялся доступ"
    )


def admin_request_denied(user_id: int) -> str:
    user_id = fmt.quote_html(user_id)
    return (
        "Запрос пользователя с "
        f'<a href="tg://user?id={user_id}">id = {user_id}</a> отклонен'
    )


def request_denied() -> str:
    return "Ваш запрос на доступ отклонён администратором!"


def no_request(user_id: int) -> str:
    user_id = fmt.quote_html(user_id)
    return (
        "Запрос на доступ от пользователя с "
        f'<a href="tg://user?id={user_id}">id = {user_id}</a>'
        " отсутствует"
    )


def db_error_message() -> str:
    return "Неизвестная ошибка!"
