from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def has_user_access(self, user_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def provide_access(self, user_id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def revoke_access(self, user_id: int) -> None:
        raise NotImplementedError()
