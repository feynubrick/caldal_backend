from pytest_bdd import scenario


@scenario("create_schedule.feature", "사용자는 일정을 생성할 수 있다.")
def test_user_can_create_a_schedule(db):
    pass


@scenario("create_schedule.feature", "사용자는 종일 일정을 생성할 수 있다.")
def test_user_can_create_all_day_schedule(db):
    pass


@scenario(
    "create_schedule.feature",
    "사용자는 한국이 아닌 다른 시간대에서도 일정을 생성할 수 있다.",
)
def test_user_can_create_schedule_in_other_timezones(db):
    pass


@scenario(
    "create_schedule.feature",
    "종일 일정 생성을 요청할 때 해당 날의 시작 시간과 다음 날의 시작시간을 보내야 한다.",
)
def test_user_can_create_all_day_schedule_time_condition(db):
    pass


@scenario("create_schedule.feature", "시작 시간은 종료 시간보다 미래일 수 없다.")
def test_end_time_should_be_bigger_than_start_time(db):
    pass
