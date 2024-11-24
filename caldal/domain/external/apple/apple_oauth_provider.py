import jwt
import requests
from django.conf import settings
from django.utils import timezone
from jwt.algorithms import RSAAlgorithm

from caldal.domain.account.interfaces.oauth_interface import OAuthProvider
from caldal.domain.account.schemas import IdTokenInfoSchema


class AppleOAuthProvider(OAuthProvider):
    CLIENT_SECRET_MAX_EXPIRATION_DAYS = 180
    VALIDATE_TOKEN_API_ENDPOINT = "https://appleid.apple.com/auth/token"

    def verify_oauth_token(self, token: str) -> IdTokenInfoSchema:
        id_token = self._validate_auth_code(token)
        decoded = self._decode_id_token(id_token)
        return IdTokenInfoSchema(**decoded)

    def _validate_auth_code(self, auth_code: str):
        response = requests.post(
            self.VALIDATE_TOKEN_API_ENDPOINT,
            headers={
                "client_id": settings.APPLE_CLIENT_ID,
                "client_secret": self._create_client_secret(),
                "code": auth_code,
                "grant_type": "authorization_code",
                "redirect_uri": settings.APPLE_OAUTH_REDIRECT_URI,
            },
        )
        response.raise_for_status()
        json_data = response.json()
        id_token = json_data.get("id_token")
        return id_token

    def _decode_id_token(self, id_token: str):
        public_key = self._get_apple_public_key(id_token)
        decoded_token = jwt.decode(
            id_token,
            RSAAlgorithm.from_jwk(public_key),
            algorithms=["RS256"],
            audience=settings.APPLE_CLIENT_ID,
        )
        return decoded_token

    def _get_apple_public_key(self, id_token: str):
        unverified_header = jwt.get_unverified_header(id_token)
        kid = unverified_header["kid"]
        response = requests.get("https://appleid.apple.com/auth/keys")
        keys = response.json()["keys"]

        for key in keys:
            if key["kid"] == kid:
                return key

    def _create_client_secret(self):
        headers = {"kid": settings.SOCIAL_AUTH_APPLE_KEY_ID}

        payload = {
            "iss": settings.APPLE_TEAM_ID,
            "iat": timezone.now(),
            "exp": timezone.now()
            + timezone.timedelta(days=self.CLIENT_SECRET_MAX_EXPIRATION_DAYS),
            "aud": "https://appleid.apple.com",
            "sub": settings.APPLE_CLIENT_ID,
        }

        client_secret = jwt.encode(
            payload,
            settings.APPLE_PRIVATE_KEY,
            algorithm="ES256",
            headers=headers,
        )
        return client_secret