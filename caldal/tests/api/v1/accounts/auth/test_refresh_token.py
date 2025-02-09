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
@patch("google.oauth2.id_token.verify_token")
@patch(
    "caldal.domain.external.apple.apple_oauth_provider.AppleOAuthProvider._decode_id_token"
)
def tokens(
    mock_verify_token__apple,
    mock_verify_token__google,
    request,
    id_token_payload,
    client,
):
    provider, platform  = request.param
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
    return res_json


@pytest.mark.django_db
class TestOAuthAuthenticate:
    @pytest.mark.parametrize(
        "tokens",
        [
            ("google", "IOS"),
            ("google", "ANDROID"),
            ("apple", "IOS"),
            ("apple", "ANDROID"),
        ],
        indirect=True,
    )
    def test_refresh_token(
        self,
        client,
        tokens,
    ):
        payload = {"refresh": tokens["refresh"]}
        res = client.post(
            f"/api/v1/account/auth/refresh",
            payload,
            content_type="application/json",
        )
        res_json = res.json()
        assert res.status_code == 200
        assert is_valid_jwt(res_json["access"])
        assert is_valid_jwt(res_json["refresh"])
        assert tokens["refresh"] == res_json["refresh"]
