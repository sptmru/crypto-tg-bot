def invalid_value() -> str:
    return "Invalid value"


def admin_text() -> str:
    return "Admin id is used"


def access_provided() -> str:
    return "Access provided"


def admin_access_provided(user_id: int) -> str:
    return f"Access provided for user [id = {user_id}]"


def access_already_provided() -> str:
    return "User has already got access"


def admin_access_revoked(user_id: int) -> str:
    return f"Access revoked for user [id = {user_id}]"


def access_revoked() -> str:
    return "Access revoked"


def access_not_provided_yet() -> str:
    return "User has not got access yet"
