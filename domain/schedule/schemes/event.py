from ninja.orm import create_schema

from domain.schedule.models import Event
from util.schemes import CamelCaseConfig

_model = Event
_fields = [
    "title",
    "content",
    "is_all_day",
    "start_time",
    "end_time",
]

EventBaseSchema = create_schema(_model, fields=_fields)
EventAllOptionalBaseSchema = create_schema(_model, optional_fields=_fields)


class CreateEventInSchema(EventBaseSchema):
    class Config(CamelCaseConfig, EventBaseSchema.Config):
        pass


class UpdateEventInSchema(EventAllOptionalBaseSchema):
    class Config(CamelCaseConfig, EventBaseSchema.Config):
        pass


class EventOutSchema(EventBaseSchema):
    class Config(CamelCaseConfig, EventBaseSchema.Config):
        pass

    id: int
