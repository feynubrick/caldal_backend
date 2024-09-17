from typing import List

from django.http import HttpRequest
from ninja import Path, Router

from ..paths import PathParamEvent
from .models import Event
from .schemes.event import CreateEventInSchema, EventOutSchema, UpdateEventInSchema

router = Router()


@router.post(
    "/events",
    by_alias=True,
    response={200: EventOutSchema},
)
def create_event(
    request: HttpRequest,
    req_body: CreateEventInSchema,
):
    return Event.objects.create(**req_body.dict())


@router.get(
    "/events",
    by_alias=True,
    response={200: List[EventOutSchema]},
)
def get_events(request: HttpRequest):
    return Event.objects.all()


@router.patch(
    "/events/{event_id}",
    by_alias=True,
    response={200: EventOutSchema},
)
def update_event(
    request: HttpRequest,
    event_path_param: Path[PathParamEvent],
    req_body: UpdateEventInSchema,
):
    event = event_path_param.value()
    update_data = req_body.dict(exclude_unset=True)
    Event.objects.filter(id=event.id).update(**update_data)
    event.refresh_from_db()
    return event


@router.delete(
    "/events/{event_id}",
    response={204: None},
)
def delete_event(
    request: HttpRequest,
    event_path_param: Path[PathParamEvent],
):
    event = event_path_param.value()
    event.delete()
    return
