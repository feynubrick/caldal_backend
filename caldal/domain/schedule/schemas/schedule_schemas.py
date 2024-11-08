from django.utils.translation import gettext_lazy as _
from ninja import Field, Schema
from ninja.orm import create_schema

from caldal.domain.schedule.models import Schedule
from caldal.domain.schedule.schemas.schedule_group_schemas import ScheduleGroupOutSchema

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

_fields.append("group")
ScheduleAllOptionalBaseSchema = create_schema(
    _model,
    fields=_fields,
    optional_fields=_fields,
    base_class=Schema,
)


class CreateScheduleInSchema(ScheduleBaseSchema):
    group_id: int | None = Field(None, description=_("스케쥴 그룹의 ID"))


class UpdateScheduleInSchema(ScheduleAllOptionalBaseSchema):
    pass


class ScheduleOutSchema(ScheduleBaseSchema):
    id: int
    group: ScheduleGroupOutSchema | None = None
