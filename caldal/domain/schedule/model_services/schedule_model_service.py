from datetime import datetime

from ninja.errors import HttpError

from caldal.domain.account.models import User
from caldal.domain.schedule.models import Schedule
from caldal.util.consts import DAY_TO_SECONDS
from caldal.util.datetime import compare_timezone_str_to_datetime
from caldal.util.services import ModelService


class ScheduleModelService(ModelService):
    _model = Schedule

    def get_list_of_schedule(self, owner: User):
        return (
            self.get_queryset()
            .filter(owner=owner)
            .order_by("start_time")
            .prefetch_related("group")
        )

    def _validate_time(
        self,
        start_time: datetime,
        end_time: datetime,
        is_all_day: bool,
        timezone_str: str,
    ):
        if start_time > end_time:
            raise HttpError(400, "시작 시간이 종료 시간보다 미래일 수 없습니다.")

        if not start_time.tzinfo or not end_time.tzinfo:
            raise HttpError(400, "시간에는 반드시 타임존 정보가 들어 있어야 합니다.")

        if (
            compare_timezone_str_to_datetime(timezone_str, start_time) is False
            or compare_timezone_str_to_datetime(timezone_str, end_time) is False
            or start_time.tzinfo != end_time.tzinfo
        ):
            raise HttpError(400, "시간대 정보가 일치하지 않습니다.")

        if is_all_day:
            self._validate_all_day_event_time(start_time, end_time, timezone_str)

    def _validate_create(
        self,
        start_time: datetime,
        end_time: datetime,
        is_all_day: bool,
        timezone: str,
        **kwargs
    ):
        self._validate_time(start_time, end_time, is_all_day, timezone)

    def _validate_update(self, **kwargs):
        start_time = kwargs.get("start_time", self._instance.start_time)
        end_time = kwargs.get("end_time", self._instance.end_time)
        is_all_day = kwargs.get("is_all_day", self._instance.is_all_day)
        self._validate_time(start_time, end_time, is_all_day)

    def _validate_all_day_event_time(
        self, start_time: datetime, end_time: datetime, timezone_str: str
    ):

        if (
            not start_time.hour == 0
            or not start_time.minute == 0
            or not start_time.second == 0
            or not start_time.microsecond == 0
        ):
            raise HttpError(400, "종일 이벤트의 경우 날짜 정보만 가지고 있어야 합니다.")

        time_diff = end_time - start_time
        if time_diff.seconds % DAY_TO_SECONDS != 0:
            raise HttpError(
                400,
                "종일 이벤트의 시작시간과 종료시간의 차이는 정확히 하루 단위여야 합니다.",
            )
