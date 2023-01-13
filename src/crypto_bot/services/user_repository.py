from typing import List


class UserRepository:
    def __init__(self, access_ids: List[int]):
        self.access_ids = access_ids

    def has_user_access(self, user_id: int) -> bool:
        return user_id in self.access_ids

    def provide_access(self, user_id: int) -> None:
        if not self.has_user_access(user_id):
            self.access_ids.append(user_id)

    def revoke_access(self, user_id: int) -> None:
        if self.has_user_access(user_id):
            self.access_ids.remove(user_id)
