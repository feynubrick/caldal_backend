import datetime

from django.utils.translation import gettext_lazy as _
from ninja import Field, FilterSchema, Schema

from caldal.util.schemas import CamelCaseConfig


class ScheduleFilterSchema(FilterSchema):
    date: datetime.date = Field(None, description=_("스케쥴의 날짜입니다"))
    date_from: datetime.date = Field(
        None, description=_("가져오려는 일정의 시작 일자"), q="date__gte"
    )
    date_to: datetime.date = Field(
        None, description=_("가져오려는 일정의 끝 일자 (포함 X)"), q="date__lt"
    )

    class Config(CamelCaseConfig, Schema.Config):
        pass
