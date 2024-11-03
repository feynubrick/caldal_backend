import json
from urllib import parse

from pytest_bdd import given, parsers, when

from caldal.util.test import get_user_client


@when(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 시간대 "{timezone}"의 "{date_from}"부터 "{date_to}"까지의 스케쥴 목록을 요청합니다.'
    ),
    target_fixture="response",
)
def when_request_to_get_list_of_schedules(
    email: str, timezone: str, date_from: str, date_to: str
):
    encoded_params = parse.urlencode(
        {
            "timezone": timezone,
            "date_from": date_from,
            "date_to": date_to,
        }
    )
    client = get_user_client(email)
    res = client.get(f"/api/v1/schedule/schedules?{encoded_params}")
    return res


@given(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 다음과 같이 일정을 생성했습니다.\n{payload}'
    ),
)
@when(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 다음과 같이 일정 생성을 요청합니다.\n{payload}'
    ),
    target_fixture="response",
)
def request_to_create_schedule(email: str, payload: str):
    request_body = json.loads(payload)
    client = get_user_client(email)
    res = client.post(
        "/api/v1/schedule/schedules", request_body, content_type="application/json"
    )
    return res
