from typing import List

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from src.crypto_bot.services.repository import Repository


class DBMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, access_ids: List[int]):
        super().__init__()
        self.access_ids = access_ids

    async def pre_process(self, obj, data, *args):
        data["repo"] = Repository(self.access_ids)

    async def post_process(self, obj, data, *args):
        data.pop("repo", None)
