from abc import ABC

from caldal.domain.account.const.enums import PlatformEnum
from caldal.domain.account.schemas import IdTokenInfoSchema


class OAuthProvider(ABC):
    def __init__(self, platform: PlatformEnum):
        self.platform = platform

    def verify_oauth_token(self, token: str) -> IdTokenInfoSchema:
        pass
