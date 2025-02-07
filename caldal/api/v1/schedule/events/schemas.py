from ninja import Schema
from ninja.orm import create_schema

from caldal.domain.schedule.models import Event, EventGroup

EventGroupModelUuidSchema = create_schema(EventGroup, fields=["uuid"])

_fields = [
    "uuid",
    "type",
    "title",
    "content",
    "start_time",
    "end_time",
    "timezone",
    "created_at",
    "updated_at",
]

EventBaseSchema = create_schema(
    Event,
    fields=_fields,
    custom_fields=[
        ("group", EventGroupModelUuidSchema, None),
    ],
)

EventBaseAllOptionalSchema = create_schema(
    Event,
    fields=_fields,
    optional_fields=_fields[1:],  # uuid는 필수
    custom_fields=[
        ("group", EventGroupModelUuidSchema, None),
    ],
)

EventUuidSchema = create_schema(Event, fields=["uuid"])


class BulkCreateEventsInSchema(Schema):
    events: list[EventBaseSchema]


class BulkUpdateEventsInSchema(Schema):
    events: list[EventBaseAllOptionalSchema]


class BulkDeleteEventsInSchema(Schema):
    events: list[EventUuidSchema]
