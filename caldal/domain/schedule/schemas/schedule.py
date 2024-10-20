from ninja.orm import create_schema

from caldal.domain.schedule.models import Schedule
from caldal.util.schemas import CamelCaseSchema

_model = Schedule
_fields = [
    "content",
    "date",
    "start_time",
    "end_time",
]

ScheduleBaseSchema = create_schema(
    _model,
    fields=_fields,
    base_class=CamelCaseSchema,
)
ScheduleAllOptionalBaseSchema = create_schema(
    _model,
    fields=_fields,
    optional_fields=_fields,
    base_class=CamelCaseSchema,
)


class CreateScheduleInSchema(ScheduleBaseSchema):
    pass


class UpdateScheduleInSchema(ScheduleAllOptionalBaseSchema):
    pass


class ScheduleOutSchema(ScheduleBaseSchema):
    pass

    id: int
