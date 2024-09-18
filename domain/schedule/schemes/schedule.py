from ninja.orm import create_schema

from domain.schedule.models import Schedule
from util.schemes import CamelCaseConfig

_model = Schedule
_fields = [
    "content",
    "date",
    "start_time",
    "end_time",
]

ScheduleBaseSchema = create_schema(_model, fields=_fields)
ScheduleAllOptionalBaseSchema = create_schema(_model, optional_fields=_fields)


class CreateScheduleInSchema(ScheduleBaseSchema):
    class Config(CamelCaseConfig, ScheduleBaseSchema.Config):
        pass


class UpdateScheduleInSchema(ScheduleAllOptionalBaseSchema):
    class Config(CamelCaseConfig, ScheduleBaseSchema.Config):
        pass


class ScheduleOutSchema(ScheduleBaseSchema):
    class Config(CamelCaseConfig, ScheduleBaseSchema.Config):
        pass

    id: int
