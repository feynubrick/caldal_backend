import json

from pytest_bdd import given, parsers, scenario, then, when

from caldal.domain.schedule.models import ScheduleGroup
from caldal.util.test import get_user_client


@scenario("create_schedule_group.feature", "사용자는 스케쥴 그룹을 만들 수 있다.")
def test_create_schedule_group_feature(db):
    pass


@scenario(
    "create_schedule_group.feature",
    "스케쥴 그룹이 생성될 때 order_index는 1씩 증가한다.",
)
def test_increment_order_index(db):
    pass


@scenario("create_schedule_group.feature", "잘못된 컬러코드를 보낼 수 없다.")
def test_color_code(db):
    pass


def _request_to_create_schedule_group(email, data):
    client = get_user_client(email)
    res = client.post(
        "/api/v1/schedule/groups",
        data,
        content_type="application/json",
    )
    return res


@given(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 스케쥴 그룹 생성을 요청합니다.\n{payload}'
    ),
)
@when(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 스케쥴 그룹 생성을 요청합니다.\n{payload}'
    ),
    target_fixture="response",
)
def when_request_to_create_schedule_group(email, payload):
    data = json.loads(payload)
    res = _request_to_create_schedule_group(email, data)
    return res


@given(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 {repeat_count_str}번 스케쥴 그룹 생성을 요청합니다.'
    )
)
def given_create_schedule_group_n_times(email, repeat_count_str):
    repeat_count = int(repeat_count_str)

    for i in range(repeat_count):
        data = {
            "name": f"그룹 {i + 1}",
            "color": "#D3BFD9",
        }
        _request_to_create_schedule_group(email, data)


@then(parsers.parse("응답 내용은 다음과 같습니다.\n{payload}"))
def check_response_body(payload, response):
    res_group = response.json()
    group = json.loads(payload)

    assert res_group["name"] == group["name"]
    assert res_group["color"] == group["color"]
    assert res_group["order_index"] == group["order_index"]
    assert res_group["is_default"] == group["is_default"]


@then(
    parsers.parse(
        '이메일이 "{email}"인 사용자가 마지막으로 만든 스케쥴 그룹의 order_index는 {order_index_str}이고, 만들어진 순서대로 1씩 차이가 납니다.'
    )
)
def check_last_schedule_group_order_index(email, order_index_str):
    last_group = (
        ScheduleGroup.objects.filter(owner__email=email).order_by("-id").first()
    )
    assert last_group.order_index == int(order_index_str)

    schedule_groups = ScheduleGroup.objects.filter(owner__email=email).order_by(
        "order_index"
    )
    prev_order_index = schedule_groups[0].order_index
    for schedule_group in schedule_groups[1:]:
        order_index = schedule_group.order_index
        assert order_index - prev_order_index == 1
        prev_order_index = order_index
