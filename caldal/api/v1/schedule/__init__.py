from ninja import Router

from caldal.api.v1.schedule.event_groups import router as event_groups_router
from caldal.api.v1.schedule.events import router as events_router

router = Router()

router.add_router("/events", events_router)
router.add_router("/event-groups", event_groups_router)
