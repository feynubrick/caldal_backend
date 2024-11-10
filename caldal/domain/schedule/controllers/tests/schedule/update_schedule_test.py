from pytest_bdd import scenario


@scenario(
    "update_schedule.feature",
    "사용자는 등록한 스케쥴의 전체 데이터를 한번에 업데이트할 수 있다.",
)
def test_complete_update_schedule_feature(db):
    pass


@scenario(
    "update_schedule.feature",
    "사용자는 등록한 스케쥴의 일부 데이터만 부분적으로 업데이트할 수 있다.",
)
def test_partial_update_schedule_feature(db):
    pass
