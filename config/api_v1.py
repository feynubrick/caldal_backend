from ninja import NinjaAPI, Swagger

from config.renderers import OrjsonRenderer
from domain.schedule.api import router as schedule_router

api = NinjaAPI(renderer=OrjsonRenderer(), docs=Swagger())

api.add_router("schedule", schedule_router)
