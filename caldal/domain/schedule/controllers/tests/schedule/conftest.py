import json

from pytest_bdd import parsers, then, when

from caldal.domain.schedule.models import Schedule
from caldal.util.test import get_user_client


@when(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 가장 최근에 생성된 일정을 다음과 같이 업데이트하도록 요청했습니다.\n{payload}'
    ),
    target_fixture="response",
)
def when_request_to_update_a_schedule(email: str, payload: str):
    client = get_user_client(email)
    target_schedule = (
        Schedule.objects.filter(owner__email=email).order_by("-id").first()
    )
    data = json.loads(payload)
    res = client.patch(
        f"/api/v1/schedule/schedules/{target_schedule.id}",
        data=data,
        content_type="application/json",
    )
    return res


@then(
    parsers.parse(
        '다음 조건과 일치하는 이메일이 "{email}"인 사용자의 일정이 {count_str}개 존재합니다.\n{payload}'
    )
)
def check_schedule_exists(email: str, count_str: str, payload: str):
    data = json.loads(payload)
    assert Schedule.objects.filter(**data, owner__email=email).count() == int(count_str)
