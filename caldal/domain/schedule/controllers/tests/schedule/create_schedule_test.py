from pytest_bdd import scenario


@scenario("create_schedule.feature", "사용자는 일정을 생성할 수 있다.")
def test_user_can_create_a_schedule(db):
    pass
