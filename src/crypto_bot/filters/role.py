from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types.base import TelegramObject

from src.crypto_bot.models.role import UserRole


class AdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin: bool | None = None):
        self.is_admin = is_admin

    async def check(self, obj: TelegramObject):  # pylint: disable=unused-argument
        if self.is_admin is None:
            return True
        data = ctx_data.get()
        is_admin = data.get("role") is UserRole.ADMIN
        return is_admin == self.is_admin
