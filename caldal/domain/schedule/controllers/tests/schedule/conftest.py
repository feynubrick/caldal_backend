import json

from pytest_bdd import parsers, then, when

from caldal.domain.schedule.models import Schedule
from caldal.util.test import get_user_client, is_same_time


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


@then(parsers.parse("응답된 일정 데이터는 다음과 같습니다.\n{payload}"))
def check_schedule_response_data(payload: str, response):
    res_schedule = response.json()
    schedule = json.loads(payload)

    assert isinstance(res_schedule["id"], int)
    assert res_schedule["title"] == schedule["title"]
    assert res_schedule["content"] == schedule["content"]
    assert is_same_time(res_schedule["start_time"], schedule["start_time"])
    assert is_same_time(res_schedule["end_time"], schedule["end_time"])
    assert res_schedule["is_all_day"] == schedule["is_all_day"]
    assert res_schedule["timezone"] == schedule["timezone"]
