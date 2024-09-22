from typing import List

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from ninja import Path, Query
from ninja_extra import ControllerBase, api_controller, permissions, route
from ninja_extra.exceptions import PermissionDenied
from ninja_jwt.authentication import JWTAuth

from domain.paths import PathParamSchedule
from domain.schedule.filters import ScheduleFilterSchema
from domain.schedule.models import Schedule
from domain.schedule.schemes.schedule import (
    CreateScheduleInSchema,
    ScheduleOutSchema,
    UpdateScheduleInSchema,
)

User = get_user_model()


@api_controller(
    "schedule/schedules",
    tags=["schedule"],
    permissions=[permissions.IsAuthenticated],
    auth=[JWTAuth()],
)
class ScheduleController(ControllerBase):
    def _validate_owner(self, user: User, schedule: Schedule):
        if user != schedule.owner:
            raise PermissionDenied()

    @route.post(
        "/",
        by_alias=True,
        response={200: ScheduleOutSchema},
    )
    def create_schedule(self, request: HttpRequest, req_body: CreateScheduleInSchema):
        return Schedule.objects.create(owner=request.user, **req_body.dict())

    @route.get(
        "/",
        by_alias=True,
        response={200: List[ScheduleOutSchema]},
    )
    def get_schedules(
        self,
        request: HttpRequest,
        filters: ScheduleFilterSchema = Query(...),
    ):
        return filters.filter(Schedule.objects.filter(owner=request.user))

    @route.patch(
        "/{schedule_id}",
        by_alias=True,
        response={200: ScheduleOutSchema},
    )
    def update_event(
        self,
        request: HttpRequest,
        schedule_path_param: Path[PathParamSchedule],
        req_body: UpdateScheduleInSchema,
    ):
        event = schedule_path_param.value()
        self._validate_owner(request.user, event)
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
        request: HttpRequest,
        schedule_path_param: Path[PathParamSchedule],
    ):
        event = schedule_path_param.value()
        self._validate_owner(request.user, event)
        event.delete()
        return
