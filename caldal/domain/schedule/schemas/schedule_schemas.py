from ninja import Schema
from ninja.orm import create_schema

from caldal.domain.schedule.models import Schedule

_model = Schedule
_fields = [
    "title",
    "content",
    "start_time",
    "end_time",
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
    pass


class UpdateScheduleInSchema(ScheduleAllOptionalBaseSchema):
    pass


class ScheduleOutSchema(ScheduleBaseSchema):
    pass

    id: int
