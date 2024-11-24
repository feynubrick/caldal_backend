import re
from zoneinfo import available_timezones

from django.utils.translation import gettext_lazy as _
from ninja import Field, Schema
from ninja.orm import create_schema
from pydantic import field_validator

from caldal.domain.schedule.models import Schedule
from caldal.domain.schedule.schemas.schedule_group_schemas import ScheduleGroupOutSchema

_model = Schedule
_fields = [
    "title",
    "content",
    "start_time",
    "end_time",
    "is_all_day",
    "timezone",
]

ScheduleBaseSchema = create_schema(
    _model,
    fields=_fields,
    base_class=Schema,
)

ScheduleAllOptionalBaseSchema = create_schema(
    _model,
    fields=_fields,
    optional_fields=_fields,
    base_class=Schema,
)


class CreateScheduleInSchema(ScheduleBaseSchema):
    group_id: int | None = Field(None, description=_("스케쥴 그룹의 ID"))

    @field_validator("timezone")
    @classmethod
    def check_timezone_format(cls, v: str):
        timezones = available_timezones()
        if v not in timezones:
            raise ValueError("존재하지 않는 시간대입니다.")
        return v


class UpdateScheduleInSchema(ScheduleAllOptionalBaseSchema):
    group_id: int | None = None


class ScheduleOutSchema(ScheduleBaseSchema):
    id: int
    group: ScheduleGroupOutSchema | None = None
