from typing import List

from ninja import Path, Query
from ninja_extra import ControllerBase, api_controller, permissions, route

from domain.paths import PathParamSchedule
from domain.schedule.filters import ScheduleFilterSchema
from domain.schedule.models import Schedule
from domain.schedule.schemes.schedule import (
    CreateScheduleInSchema,
    ScheduleOutSchema,
    UpdateScheduleInSchema,
)


@api_controller(
    "schedule/schedules",
    tags=["schedule"],
    permissions=[permissions.IsAuthenticated],
)
class ScheduleController(ControllerBase):
    @route.post(
        "/",
        by_alias=True,
        response={200: ScheduleOutSchema},
    )
    def create_schedule(self, req_body: CreateScheduleInSchema):
        return Schedule.objects.create(**req_body.dict())

    @route.get(
        "/",
        by_alias=True,
        response={200: List[ScheduleOutSchema]},
    )
    def get_schedules(
        self,
        filters: ScheduleFilterSchema = Query(...),
    ):
        return filters.filter(Schedule.objects.all())

    @route.patch(
        "/{schedule_id}",
        by_alias=True,
        response={200: ScheduleOutSchema},
    )
    def update_event(
        self,
        schedule_path_param: Path[PathParamSchedule],
        req_body: UpdateScheduleInSchema,
    ):
        event = schedule_path_param.value()
        update_data = req_body.dict(exclude_unset=True)
        Schedule.objects.filter(id=event.id).update(**update_data)
        event.refresh_from_db()
        return event

    @route.delete(
        "/{schedule_id}",
        response={204: None},
    )
    def delete_event(
        self,
        schedule_path_param: Path[PathParamSchedule],
    ):
        event = schedule_path_param.value()
        event.delete()
        return
