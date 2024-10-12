import datetime

from django.utils.translation import gettext_lazy as _
from ninja import Field, FilterSchema, Schema

from caldal.util.schemes import CamelCaseConfig


class ScheduleFilterSchema(FilterSchema):
    date: datetime.date = Field(None, description=_("스케쥴의 날짜입니다"))

    class Config(CamelCaseConfig, Schema.Config):
        pass
