from datetime import datetime, timedelta

from ninja.errors import HttpError

from caldal.domain.account.models import User
from caldal.domain.schedule.models import Schedule
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
        self, start_time: datetime, end_time: datetime, is_all_day: bool
    ):
        if start_time > end_time:
            raise HttpError(400, "시작 시간이 종료 시간보다 미래일 수 없습니다.")

        if is_all_day and end_time - start_time != timedelta(hours=24):
            raise HttpError(
                400,
                "종일 이벤트의 시작과 끝 시간은 하루의 시작과 다음날의 시작 시간이어야 합니다.",
            )

    def _validate_create(
        self, start_time: datetime, end_time: datetime, is_all_day: bool, **kwargs
    ):
        self._validate_time(start_time, end_time, is_all_day)

    def _validate_update(self, **kwargs):
        start_time = kwargs.get("start_time", self._instance.start_time)
        end_time = kwargs.get("end_time", self._instance.end_time)
        is_all_day = kwargs.get("is_all_day", self._instance.is_all_day)
        self._validate_time(start_time, end_time, is_all_day)
