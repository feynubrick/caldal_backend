import pytest
from ninja_jwt.tokens import Token

from caldal.domain.common.auth.auth_token_service import AuthTokenService
from caldal.domain.common.factories.account.user_factory import UserFactory


@pytest.fixture
def user():
    return UserFactory()

@pytest.mark.django_db
class TestAuthTokenService:
    def test_get_both_tokens(self, user):
        tokens = AuthTokenService(user).get_both_tokens()

        # access token payload 확인
        assert isinstance(tokens["access"], Token)
        assert tokens["access"].get("user_id") == user.id

        # refresh token 정상 동작 확인
        refreshed_access_token = tokens["refresh"].access_token
        assert isinstance(refreshed_access_token, Token)
        assert tokens["access"].get("user_id") == user.id
