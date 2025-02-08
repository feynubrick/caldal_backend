from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client

from caldal.util.jwt import is_valid_jwt
from caldal.util.string import is_valid_email

User = get_user_model()


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def token_from_app():
    return "valid_token"


@pytest.mark.django_db
class TestAuth:
    @pytest.mark.parametrize("provider", ["google", "apple"])
    @pytest.mark.parametrize("platform", ["IOS", "ANDROID"])
    @patch("google.oauth2.id_token.verify_token")
    @patch(
        "caldal.domain.external.apple.apple_oauth_provider.AppleOAuthProvider._decode_id_token"
    )
    def test_signup(
        self,
        mock_verify_token__apple,
        mock_verify_token__google,
        client,
        token_from_app,
        provider,
        platform,
        id_token_payload,
    ):
        mock_verify_token__google.return_value = id_token_payload
        mock_verify_token__apple.return_value = id_token_payload

        payload = {"token": "fake_token", "platform": platform}
        res = client.post(
            f"/api/v1/account/auth/{provider}",
            payload,
            content_type="application/json",
        )
        res_json = res.json()
        assert res.status_code == 201
        assert is_valid_email(res_json["email"])
        assert is_valid_jwt(res_json["access"])
        assert is_valid_jwt(res_json["refresh"])
        user = User.objects.get(email=res_json["email"])
        assert user.oauth_profiles.filter(provider=provider).count() == 1

    @pytest.mark.parametrize("provider", ["google", "apple"])
    @pytest.mark.parametrize("platform", ["IOS", "ANDROID"])
    @patch("google.oauth2.id_token.verify_token")
    @patch(
        "caldal.domain.external.apple.apple_oauth_provider.AppleOAuthProvider._decode_id_token"
    )
    def test_signin(
        self,
        mock_verify_token__apple,
        mock_verify_token__google,
        client,
        token_from_app,
        provider,
        platform,
        id_token_payload,
    ):
        mock_verify_token__google.return_value = id_token_payload
        mock_verify_token__apple.return_value = id_token_payload

        payload = {"token": "fake_token", "platform": platform}
        res = client.post(
            f"/api/v1/account/auth/{provider}",
            payload,
            content_type="application/json",
        )
        assert res.status_code == 201

        res = client.post(
            f"/api/v1/account/auth/{provider}",
            payload,
            content_type="application/json",
        )
        res_json = res.json()
        assert res.status_code == 200
        assert is_valid_email(res_json["email"])
        assert is_valid_jwt(res_json["access"])
        assert is_valid_jwt(res_json["refresh"])
        user = User.objects.get(email=res_json["email"])
        assert user.oauth_profiles.filter(provider=provider).count() == 1
