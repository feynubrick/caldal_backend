from django.conf import settings
from google.auth.transport.requests import Request
from google.oauth2 import id_token

from caldal.domain.account.interfaces.oauth_interface import OAuthProvider
from caldal.domain.account.schemas.auth_schemas import IdTokenInfoSchema


class GoogleOAuthProvider(OAuthProvider):
    def verify_oauth_token(self, token: str) -> IdTokenInfoSchema:
        parsed_token = id_token.verify_oauth2_token(
            id_token=token,
            request=Request(),
            audience=settings.GOOGLE_OAUTH_CLIENT_ID,
        )

        return IdTokenInfoSchema(**parsed_token)
