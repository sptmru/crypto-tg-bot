from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from src.crypto_bot.services.repository import Repository


class DBMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, connector):
        super().__init__()
        self.connector = connector

    async def pre_process(self, obj, data, *args):
        data["repo"] = Repository(self.connector)

    async def post_process(self, obj, data, *args):
        data.pop("repo", None)
