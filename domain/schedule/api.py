from typing import List

from django.http import HttpRequest
from ninja import Path, Query, Router

from ..paths import PathParamSchedule
from .filters import ScheduleFilterSchema
from .models import Schedule
from .schemes.schedule import (
    CreateScheduleInSchema,
    ScheduleOutSchema,
    UpdateScheduleInSchema,
)

router = Router()


@router.post(
    "/schedules",
    by_alias=True,
    response={200: ScheduleOutSchema},
)
def create_event(
    request: HttpRequest,
    req_body: CreateScheduleInSchema,
):
    return Schedule.objects.create(**req_body.dict())


@router.get(
    "/schedules",
    by_alias=True,
    response={200: List[ScheduleOutSchema]},
)
def get_events(
    request: HttpRequest,
    filters: ScheduleFilterSchema = Query(...),
):
    return filters.filter(Schedule.objects.all())


@router.patch(
    "/schedules/{schedule_id}",
    by_alias=True,
    response={200: ScheduleOutSchema},
)
def update_event(
    request: HttpRequest,
    schedule_path_param: Path[PathParamSchedule],
    req_body: UpdateScheduleInSchema,
):
    event = schedule_path_param.value()
    update_data = req_body.dict(exclude_unset=True)
    Schedule.objects.filter(id=event.id).update(**update_data)
    event.refresh_from_db()
    return event


@router.delete(
    "/schedules/{schedule_id}",
    response={204: None},
)
def delete_event(
    request: HttpRequest,
    schedule_path_param: Path[PathParamSchedule],
):
    event = schedule_path_param.value()
    event.delete()
    return
