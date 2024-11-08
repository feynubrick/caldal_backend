from typing import List

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from ninja import Path, Query
from ninja_extra import ControllerBase, api_controller, permissions, route
from ninja_extra.exceptions import PermissionDenied
from ninja_jwt.authentication import JWTAuth

from caldal.domain.schedule.business_services.create_schedule import (
    CreateScheduleService,
    CreateScheduleServiceInputSchema,
)
from caldal.domain.schedule.filters import ScheduleFilterSchema
from caldal.domain.schedule.models import Schedule
from caldal.domain.schedule.path_params import SchedulePathParam
from caldal.domain.schedule.schemas import (
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
        "",
        response={201: ScheduleOutSchema},
    )
    def create_schedule(self, request: HttpRequest, req_body: CreateScheduleInSchema):
        data = req_body.dict()
        data["owner_id"] = request.user.id
        return CreateScheduleService().run(CreateScheduleServiceInputSchema(**data))

    @route.get(
        "",
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
        response={200: ScheduleOutSchema},
    )
    def update_schedule(
        self,
        request: HttpRequest,
        schedule_path_param: Path[SchedulePathParam],
        req_body: UpdateScheduleInSchema,
    ):
        schedule = schedule_path_param.value()
        self._validate_owner(request.user, schedule)
        update_data = req_body.dict(exclude_unset=True)
        Schedule.objects.filter(id=schedule.id).update(**update_data)
        schedule.refresh_from_db()
        return schedule

    @route.delete(
        "/{schedule_id}",
        response={204: None},
    )
    def delete_schedule(
        self,
        request: HttpRequest,
        schedule_path_param: Path[SchedulePathParam],
    ):
        schedule = schedule_path_param.value()
        self._validate_owner(request.user, schedule)
        schedule.delete()
        return
