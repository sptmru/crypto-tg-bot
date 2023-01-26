import aiogram.utils.markdown as fmt


def access_denied() -> str:
    return (
        "Доступ запрещён! Запрос на доступ отправлен.\n"
        "Пожалуйста, подождите, пока администратор предоставит Вам доступ!"
    )


def access_requested(user_id: int, username: str) -> str:
    user_id = fmt.quote_html(user_id)
    username = fmt.quote_html(username)
    return (
        f'Пользователь <a href="tg://user?id={user_id}">{username}</a> '
        f"с id = {user_id} запрашивает доступ.\n"
        f"Чтобы предоставить доступ, используйте команду:\n"
        f"/access{user_id}\n"
        f"Чтобы отклонить доступ, используйте команду:\n"
        f"/deny{user_id}"
    )


def access_already_requested() -> str:
    return (
        "Вы уже отправляли запрос на получение доступа!\n"
        "Пожалуйста, подождите, пока администратор предоставит Вам доступ!"
    )


def no_access() -> str:
    return "Доступ временно запрещен!"


def db_error_message() -> str:
    return "Неизвестная ошибка!"
