from ninja import Router

from caldal.api.v1.schedule.event_groups.schemas import (
    BulkCreateEventGroupsInSchema,
    BulkDeleteEventGroupsInSchema,
    BulkUpdateEventGroupsInSchema,
)
from caldal.domain.schedule.controllers.event_group_controller import (
    EventGroupController,
)

router = Router(tags=["schedule:event-groups"])


@router.post("/bulk-create", response={204: None})
def bulk_create(request, req_body: BulkCreateEventGroupsInSchema):
    data = req_body.model_dump()
    EventGroupController().bulk_create(request.user, data["groups"])
    return 204, None


@router.post("/bulk-update", response={204: None})
def bulk_update(request, req_body: BulkUpdateEventGroupsInSchema):
    data = req_body.model_dump(exclude_none=True)
    EventGroupController().bulk_update(request.user, data["groups"])
    return 204, None


@router.post("/bulk-delete", response={204: None})
def bulk_delete(request, req_body: BulkDeleteEventGroupsInSchema):
    data = req_body.model_dump()
    EventGroupController().bulk_delete(request.user, data["groups"])
    return 204, None
