from django.shortcuts import get_object_or_404
from ninja import Schema

from domain.schedule.models import Event


class PathParamEvent(Schema):
    event_id: int

    def value(self) -> Event:
        return get_object_or_404(Event, id=self.event_id)
