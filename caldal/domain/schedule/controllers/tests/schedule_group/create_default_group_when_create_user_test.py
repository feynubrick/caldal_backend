import json

from pytest_bdd import parsers, scenario, then


@scenario(
    "create_default_group_when_create_user.feature",
    "사용자가 회원 가입할 때 기본 스케쥴 그룹이 생성된다.",
)
def test_create_default_group_when_create_user(db):
    pass


@then(parsers.parse("응답으로 돌아온 스케쥴 그룹 목록은 다음과 같습니다.\n{payload}"))
def check_get_list_of_groups(payload: str, response):
    groups = json.loads(payload)
    res_groups = response.json()

    assert len(groups) == len(res_groups)
    for group, res_group in zip(groups, res_groups):
        assert group["name"] == res_group["name"]
        assert group["color"] == res_group["color"]
        assert group["order_index"] == res_group["order_index"]
        assert group["is_default"] == res_group["is_default"]
