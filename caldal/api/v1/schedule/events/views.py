from ninja import Router

from caldal.api.v1.schedule.events.schemas import (
    BulkCreateEventsInSchema,
    BulkDeleteEventsInSchema,
    BulkUpdateEventsInSchema,
)
from caldal.domain.schedule.services.logic.event_logic_service import EventLogicService

router = Router(tags=["schedule:events"])


@router.post("/bulk-create", response={204: None})
def bulk_create(request, req_body: BulkCreateEventsInSchema):
    data = req_body.model_dump()
    EventLogicService().bulk_create(request.user, data["events"])
    return 204, None


@router.post("/bulk-update", response={204: None})
def bulk_update(request, req_body: BulkUpdateEventsInSchema):
    data = req_body.model_dump(exclude_none=True)
    EventLogicService().bulk_update(request.user, data["events"])
    return 204, None


@router.post("/bulk-delete", response={204: None})
def bulk_delete(request, req_body: BulkDeleteEventsInSchema):
    data = req_body.model_dump()
    EventLogicService().bulk_delete(request.user, data["events"])
    return 204, None
