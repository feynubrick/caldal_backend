import datetime
from zoneinfo import ZoneInfo

from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from ninja import Field, FilterSchema

from caldal.util.filters import handle_filter_empty_value
from caldal.util.schemas import CamelCaseSchemaMixin


class ScheduleFilterSchema(CamelCaseSchemaMixin, FilterSchema):
    date: datetime.date = Field(None, description=_("스케쥴의 날짜입니다"))
    date_from: datetime.date = Field(None, description=_("가져오려는 일정의 시작 일자"))
    date_to: datetime.date = Field(None, description=_("가져오려는 일정의 끝 일자"))
    timezone: str = Field("Asia/Seoul", description=_("시간대"))

    def custom_expression(self) -> Q:
        tz = ZoneInfo(self.timezone)
        filter_date = self._filter_date(self.date, tz)
        filter_date_from = self._filter_date_from(self.date_from, tz)
        filter_date_to = self._filter_date_to(self.date_to, tz)
        return filter_date & filter_date_from & filter_date_to

    @handle_filter_empty_value
    def _filter_date(self, value: datetime.date, tz: ZoneInfo) -> Q:
        start_of_day = datetime.datetime.combine(value, datetime.time.min, tzinfo=tz)
        end_of_day = datetime.datetime.combine(value, datetime.time.max, tzinfo=tz)

        return (
            Q(start_time__range=(start_of_day, end_of_day))
            | Q(end_time__range=(start_of_day, end_of_day))
            | Q(start_time__lt=start_of_day, end_time__gt=end_of_day)
        )

    @handle_filter_empty_value
    def _filter_date_from(self, value: datetime.date, tz: ZoneInfo) -> Q:
        time_from = datetime.datetime.combine(value, datetime.time.min, tzinfo=tz)
        return Q(start_time__gte=time_from)

    @handle_filter_empty_value
    def _filter_date_to(self, value: datetime.date, tz: ZoneInfo) -> Q:
        time_to = datetime.datetime.combine(value, datetime.time.max, tzinfo=tz)
        return Q(end_time__lte=time_to)
