from ninja import Swagger
from ninja_extra import NinjaExtraAPI

from config.renderers import OrjsonRenderer
from domain.account.controllers import AccountController, AuthController
from domain.schedule.controllers.schedule import ScheduleController

api = NinjaExtraAPI(
    renderer=OrjsonRenderer(),
    docs=Swagger(),
)

api.register_controllers(AccountController)
api.register_controllers(AuthController)
api.register_controllers(ScheduleController)
