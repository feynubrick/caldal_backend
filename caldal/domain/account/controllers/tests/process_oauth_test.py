import json

from pytest_bdd import given, parsers, scenario, then

from caldal.domain.account.models import User


@scenario("process_oauth.feature", "사용자는 소셜 로그인으로 회원가입할 수 있다.")
def test_user_can_sign_up_by_oauth(db):
    pass


@scenario(
    "process_oauth.feature", "회원가입한 사용자는 소셜 로그인으로 로그인할 수 있다."
)
def test_user_can_sign_in_by_oauth(db):
    pass


@given(parsers.parse('이메일이 "{email}"인 사용자는 존재하지 않습니다.'))
def given_no_user(email: str):
    assert User.objects.filter(email=email).exists() is False


@then(parsers.parse("다음 정보로 사용자를 한명 찾을 수 있습니다.\n{payload}"))
def check_unique_user(payload: str):
    data = json.loads(payload)
    user = User.objects.get(email=data["email"])

    assert (
        user.oauth_profiles.filter(
            provider=data["provider"],
            identifier__isnull=False,
        ).count()
        == 1
    )
