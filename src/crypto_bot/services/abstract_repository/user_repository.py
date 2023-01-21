from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    async def has_user_access(self, user_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def provide_access(self, user_id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def revoke_access(self, user_id: int) -> None:
        raise NotImplementedError()
