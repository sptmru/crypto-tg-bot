from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class DataMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, server_ip: str) -> None:
        super().__init__()
        self.server_ip = server_ip

    async def pre_process(self, obj, data, *args) -> None:
        data["server_ip"] = self.server_ip

    async def post_process(self, obj, data, *args) -> None:
        data.pop("server_ip", None)
