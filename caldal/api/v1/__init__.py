from ninja import NinjaAPI, Swagger

from caldal.api.v1.schedule import router as schedule_router
from caldal.config.renderers import OrjsonRenderer

api = NinjaAPI(docs=Swagger(), renderer=OrjsonRenderer())

api.add_router("/schedule", schedule_router)
