from ninja import Swagger
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from config.renderers import OrjsonRenderer
from domain.schedule.controllers.schedule import ScheduleController

api = NinjaExtraAPI(
    renderer=OrjsonRenderer(),
    docs=Swagger(),
)

api.register_controllers(NinjaJWTDefaultController)
api.register_controllers(ScheduleController)
