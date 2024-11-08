from ninja import Field, Schema
from ninja.orm import create_schema

from caldal.domain.schedule.models import ScheduleGroup
from caldal.domain.schedule.schemas.color_validation_mixin import ColorValidationMixin

CreateScheduleGroupInSchema = create_schema(
    ScheduleGroup,
    fields=["name", "color"],
    base_class=ColorValidationMixin,
)


UpdateScheduleGroupInSchema = create_schema(
    ScheduleGroup,
    fields=["name", "color", "order_index"],
    optional_fields=["name", "color", "order_index"],
    base_class=ColorValidationMixin,
)


ScheduleGroupOutSchema = create_schema(
    ScheduleGroup,
    fields=["name", "color", "order_index", "is_default"],
    custom_fields=[("id", int, Field())],
    base_class=Schema,
)
