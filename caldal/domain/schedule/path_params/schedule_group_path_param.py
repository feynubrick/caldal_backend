from django.shortcuts import get_object_or_404
from ninja import Schema

from caldal.domain.schedule.models import ScheduleGroup


class ScheduleGroupPathParam(Schema):
    group_id: int

    def value(self) -> ScheduleGroup:
        return get_object_or_404(ScheduleGroup, id=self.group_id)
