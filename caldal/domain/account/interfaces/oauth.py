from abc import ABC

from caldal.domain.account.schemas import IdTokenInfoSchema


class OAuthProvider(ABC):

    def verify_oauth_token(self, token: str) -> IdTokenInfoSchema:
        pass
