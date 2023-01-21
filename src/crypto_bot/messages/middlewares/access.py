def access_denied() -> str:
    return "Access denied!"


def access_requested(user_id: int) -> str:
    return f"/access{user_id}"


def db_error_message() -> str:
    return "Unknown error!"
