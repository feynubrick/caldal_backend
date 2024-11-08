from typing import List

from ninja import Path
from ninja_extra import ControllerBase, api_controller, permissions, route
from ninja_extra.exceptions import PermissionDenied
from ninja_jwt.authentication import JWTAuth

from caldal.domain.account.models import User
from caldal.domain.schedule.model_services import ScheduleGroupModelService
from caldal.domain.schedule.models import ScheduleGroup
from caldal.domain.schedule.path_params.schedule_group_path_param import (
    ScheduleGroupPathParam,
)
from caldal.domain.schedule.schemas.schedule_group_schemas import (
    CreateScheduleGroupInSchema,
    ScheduleGroupOutSchema,
    UpdateScheduleGroupInSchema,
)


@api_controller(
    "schedule/groups",
    tags=["schedule-group"],
    permissions=[permissions.IsAuthenticated],
    auth=[JWTAuth()],
)
class ScheduleGroupController(ControllerBase):
    @route.post("", response={201: ScheduleGroupOutSchema})
    def create_group(
        self,
        request,
        req_body: CreateScheduleGroupInSchema,
    ):
        return ScheduleGroupModelService().create_schedule_group(
            owner=request.user,
            **req_body.dict(),
        )

    @route.get("", response={200: List[ScheduleGroupOutSchema]})
    def get_list_of_groups(
        self,
        request,
    ):
        return ScheduleGroup.objects.filter(owner=request.user)

    @route.get("/{group_id}", response={200: ScheduleGroupOutSchema})
    def get_group_by_id(
        self,
        request,
        group_path_param: Path[ScheduleGroupPathParam],
    ):
        return group_path_param.value()

    @route.patch("/{group_id}", response={200: ScheduleGroupOutSchema})
    def update_group(
        self,
        request,
        group_path_param: Path[ScheduleGroupPathParam],
        req_body: UpdateScheduleGroupInSchema,
    ):
        schedule_group = group_path_param.value()
        self._validate_owner(request.user, schedule_group)
        return ScheduleGroup.objects.filter(id=schedule_group.id).update(
            **req_body.dict()
        )

    @route.delete("/{group_id}", response={204: None})
    def delete_group(
        self,
        request,
        group_path_param: Path[ScheduleGroupPathParam],
    ):
        schedule_group = group_path_param.value()
        self._validate_owner(request.user, schedule_group)
        schedule_group.delete()
        return 204, None

    def _validate_owner(self, user: User, schedule_group: ScheduleGroup):
        if user != schedule_group.owner:
            raise PermissionDenied()
