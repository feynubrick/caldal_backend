from unittest import mock

from django.test import Client
from pytest_bdd import given, parsers, then, when

from caldal.domain.account.schemas import IdTokenInfoSchema


def _request_to_process_oauth(email: str, provider: str):
    with mock.patch(
        "caldal.domain.account.services.OAuthService.verify_token"
    ) as verify_token_method:
        verify_token_method.return_value = IdTokenInfoSchema(sub=email, email=email)

        client = Client()
        res = client.post(
            f"/api/v1/account/auth/{provider.lower()}",
            data={"id_token": "mock_token"},
            content_type="application/json",
        )
        return res


@given(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 "{provider}" 로그인으로 회원가입했습니다.'
    )
)
def given_user(email: str, provider: str):
    res = _request_to_process_oauth(email, provider)
    res_json = res.json()
    assert res.status_code == 201
    assert res_json["email"] == email


@when(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 "{provider}" 로그인으로 회원가입을 요청합니다.'
    ),
    target_fixture="response",
)
@when(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 "{provider}" 로그인으로 로그인을 요청합니다.'
    ),
    target_fixture="response",
)
def when_user_request_oauth_signup(email: str, provider: str):
    res = _request_to_process_oauth(email, provider)
    return res


@then(parsers.parse("서버의 응답 상태코드는 {status_code}입니다."))
def check_response_status_code(status_code: str, response):
    assert response.status_code == int(status_code)
