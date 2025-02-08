from unittest.mock import patch

import pytest
from faker import Faker

from caldal.domain.account.const.enums import OAuthProviderCodeEnum, PlatformEnum
from caldal.domain.common.auth.oauth_service import OAuthService

fake = Faker()


@pytest.mark.django_db
class TestOAuthService:
    @pytest.mark.parametrize(
        "provider", [OAuthProviderCodeEnum.GOOGLE, OAuthProviderCodeEnum.APPLE]
    )
    @pytest.mark.parametrize("platform", [PlatformEnum.IOS, PlatformEnum.ANDROID])
    @patch("google.oauth2.id_token.verify_token")
    @patch(
        "caldal.domain.external.apple.apple_oauth_provider.AppleOAuthProvider._decode_id_token"
    )
    def test_verify_token_google(
        self,
        mock_verify_token__apple,
        mock_verify_token__google,
        provider,
        platform,
        id_token_payload,
    ):
        mock_verify_token__apple.return_value = id_token_payload
        mock_verify_token__google.return_value = id_token_payload

        token_from_app = "fake_token"
        id_token = OAuthService(provider, platform).verify_token(
            token_from_app
        )
        assert id_token.sub == id_token_payload["sub"]
        assert id_token.email == id_token_payload["email"]
