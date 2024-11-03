import json

from pytest_bdd import parsers, scenario, then

from caldal.util.test import is_same_time


@scenario("list_schedules.feature", "생성한 스케쥴이 없을 경우")
def test_when_no_schedule(db):
    pass


@scenario(
    "list_schedules.feature",
    "스케쥴을 생성했고, 스케쥴이 생성된 시간을 포함하는 시간 필터를 요청한 경우",
)
def test_when_schedule_created_and_with_right_filter_schedule(db):
    pass


@then(parsers.parse("응답 결과는 다음과 같습니다.\n{payload}"))
def check_response_body(payload: str, response):
    res_schedule_list = response.json()
    schedule_list = json.loads(payload)
    for schedule, res_schedule in zip(schedule_list, res_schedule_list):
        assert schedule["title"] == res_schedule["title"]
        assert schedule["content"] == res_schedule["content"]
        assert is_same_time(schedule["start_time"], res_schedule["start_time"])
        assert is_same_time(schedule["end_time"], res_schedule["end_time"])
