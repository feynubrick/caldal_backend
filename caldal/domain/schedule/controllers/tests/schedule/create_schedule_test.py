import json

from pytest_bdd import parsers, scenario, then

from caldal.domain.schedule.models import Schedule


@scenario("create_schedule.feature", "사용자는 일정을 생성할 수 있다.")
def test_user_can_create_a_schedule(db):
    pass


@then(
    parsers.parse(
        '다음 조건과 일치하는 이메일이 "{email}"인 사용자의 일정이 하나만 존재합니다.\n{payload}'
    )
)
def check_schedule_uniquely_exists(email: str, payload: str):
    data = json.loads(payload)
    assert Schedule.objects.filter(**data, owner__email=email).count() == 1
