from django.shortcuts import get_object_or_404
from ninja import Schema

from domain.schedule.models import Schedule


class PathParamEvent(Schema):
    event_id: int

    def value(self) -> Schedule:
        return get_object_or_404(Schedule, id=self.event_id)
