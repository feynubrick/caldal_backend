from ninja import Schema
from ninja.orm import create_schema

from caldal.domain.schedule.models import EventGroup

_fields = [
    "uuid",
    "owner",
    "name",
    "color",
    "order_index",
    "created_at",
    "updated_at",
]

EventGroupUuidSchema = create_schema(EventGroup, fields=["uuid"])

EventGroupBaseSchema = create_schema(
    EventGroup,
    fields=_fields,
)

EventGroupAllOptionalBaseSchema = create_schema(
    EventGroup,
    fields=_fields,
    optional_fields=_fields,
)


class BulkCreateEventGroupsInSchema(Schema):
    groups: list[EventGroupBaseSchema]


class BulkUpdateEventGroupsInSchema(Schema):
    groups: list[EventGroupAllOptionalBaseSchema]


class BulkDeleteEventGroupsInSchema(Schema):
    groups: list[EventGroupUuidSchema]
