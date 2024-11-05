from ninja_jwt.tokens import RefreshToken

from caldal.domain.account.models import User


class AuthTokenService:
    def __init__(self, user: User):
        self.user = user
        self.refresh_token = self._create_refresh_token()

    def _create_refresh_token(self):
        return RefreshToken.for_user(user=self.user)

    def get_refresh_token(self) -> str:
        return str(self.refresh_token)

    def get_access_token(self) -> str:
        return str(self.refresh_token.access_token)
