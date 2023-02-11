from dataclasses import dataclass


@dataclass
class User:
    user_id: int = -1
    sent_request: bool = False
    access: bool = False
    configured: bool = False

    def is_valid(self) -> bool:
        return self.user_id != -1

    def has_sent_request(self) -> bool:
        return self.is_valid() and self.sent_request

    def has_access(self) -> bool:
        return self.is_valid() and self.access

    def is_configured(self) -> bool:
        return self.is_valid() and self.is_configured()
